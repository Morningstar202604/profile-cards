# -*- coding: utf-8 -*-
"""Profile Verse — shared GitHub API layer used by every component."""

import json
import os
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"


def token():
    return os.environ.get("GH_TOKEN", "").strip()


def api(path, params=None):
    """GET an API path. Public endpoints work without a token; when a token is
    present it is sent as a Bearer header. An *empty* Bearer header is never
    sent — GitHub rejects it with 401."""
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-verse",
    }
    tok = token()
    if tok:
        headers["Authorization"] = "Bearer " + tok
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_merged_prs(user, max_pr=300):
    """Merged PRs of `user` as a list of dicts: repo, number, merged_at, url."""
    prs = []
    query = "is:pr author:%s is:merged" % user
    page = 1
    try:
        while True:
            data = api(
                "/search/issues",
                {"q": query, "per_page": 100, "page": page, "sort": "updated", "order": "desc"},
            )
            for it in data.get("items", []):
                merged_at = (it.get("pull_request") or {}).get("merged_at")
                if not merged_at:
                    continue
                full_name = it.get("repository_url", "").replace(API + "/repos/", "")
                if not full_name:
                    continue
                prs.append({
                    "repo": full_name,
                    "number": it.get("number"),
                    "merged_at": merged_at,
                    "url": it.get("html_url", ""),
                })
            total = data.get("total_count", 0)
            if not data.get("items") or page * 100 >= total or len(prs) >= max_pr:
                break
            page += 1
    except urllib.error.HTTPError as e:
        if e.code == 422:  # `is:merged` unsupported in this environment
            return fetch_merged_prs_closed(user, max_pr)
        raise
    return prs[:max_pr]


def fetch_merged_prs_closed(user, max_pr=300):
    """Fallback: search closed PRs and keep only merged ones."""
    prs = []
    query = "is:pr author:%s is:closed" % user
    page = 1
    while True:
        data = api(
            "/search/issues",
            {"q": query, "per_page": 100, "page": page, "sort": "updated", "order": "desc"},
        )
        for it in data.get("items", []):
            merged_at = (it.get("pull_request") or {}).get("merged_at")
            if not merged_at:
                continue
            full_name = it.get("repository_url", "").replace(API + "/repos/", "")
            if not full_name:
                continue
            prs.append({
                "repo": full_name,
                "number": it.get("number"),
                "merged_at": merged_at,
                "url": it.get("html_url", ""),
            })
        total = data.get("total_count", 0)
        if not data.get("items") or page * 100 >= total or len(prs) >= max_pr:
            break
        page += 1
    return prs[:max_pr]


def get_stars(repo):
    """stargazers_count of a repository."""
    return int(api("/repos/" + repo).get("stargazers_count", 0))


def fmt_stars(n):
    """1000 -> 1k, 189900 -> 189.9k."""
    if n >= 1000:
        v = n / 1000.0
        s = ("%.1f" % v).rstrip("0").rstrip(".")
        return s + "k"
    return str(n)


def fetch_user(user):
    """Public profile of `user` (followers, public_repos, ...)."""
    return api("/users/" + user)


def fetch_total_stars(user):
    """Sum of stargazers_count across all public repos of `user`."""
    total, page = 0, 1
    while True:
        data = api("/users/%s/repos" % user, {"per_page": 100, "page": page, "sort": "created"})
        if not data:
            break
        total += sum(r.get("stargazers_count", 0) for r in data)
        if len(data) < 100:
            break
        page += 1
    return total


def fetch_repos(user):
    """All public repos of `user` as [{name, language, stars}]. Paginated."""
    repos, page = [], 1
    while True:
        data = api("/users/%s/repos" % user, {"per_page": 100, "page": page, "sort": "created"})
        if not data:
            break
        for r in data:
            repos.append({
                "name": r.get("name", ""),
                "language": (r.get("language") or "Other").strip() or "Other",
                "stars": int(r.get("stargazers_count", 0)),
            })
        if len(data) < 100:
            break
        page += 1
    return repos


def fetch_contribution_calendar(user):
    """Full-year contribution calendar via GraphQL.

    Returns (total, days) where days is a list of {"date": "YYYY-MM-DD", "count": int}
    oldest first. Requires GH_TOKEN.
    """
    q = (
        "query($login: String!){user(login:$login){contributionsCollection{"
        "contributionCalendar{totalContributions weeks{contributionDays{"
        "date contributionCount}}}}}}"
    )
    payload = json.dumps({"query": q, "variables": {"login": user}}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "profile-verse",
    }
    tok = token()
    if tok:
        headers["Authorization"] = "Bearer " + tok
    req = urllib.request.Request(API + "/graphql", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    try:
        cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    except (KeyError, TypeError):
        raise RuntimeError("GraphQL error: %s" % json.dumps(data.get("errors") or data)[:300])
    days = []
    for week in cal.get("weeks", []):
        for d in week.get("contributionDays", []):
            days.append({"date": d["date"], "count": d["contributionCount"]})
    return int(cal.get("totalContributions", 0)), days


def compute_streaks(days):
    """Given days (oldest first), return (current_streak, longest_streak)."""
    by_date = {}
    for d in days:
        by_date[d["date"]] = d["count"]
    dates = sorted(by_date)
    if not dates:
        return 0, 0
    from datetime import date as _date

    # current streak: walk back from today (skip future), count consecutive days with count>0,
    # but allow today to be 0 (streak measured up to yesterday).
    def prev_day(s):
        d = _date.fromisoformat(s)
        return (d - __import__("datetime").timedelta(days=1)).isoformat()

    today = _date.today().isoformat()
    cur = 0
    day = today
    # skip today if no contribution yet
    if by_date.get(day, 0) == 0:
        day = prev_day(day)
    while day in by_date and by_date[day] > 0:
        cur += 1
        day = prev_day(day)

    # longest
    longest = run = 0
    for d in dates:
        if by_date[d] > 0:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    return cur, longest
