#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projects Card — Profile Verse component
----------------------------------------
A 2×2 grid of project cards (name · description · language · stars) that
replaces the flat text list. Signature look: four postcard panels on the
starfield, gold titles, one star per panel.

Data: live from the GitHub REST API — the user's non-fork repos, sorted by
stars (ties by most recently pushed), top 4. Public data, no token needed.

Env: GH_TOKEN (optional) · USER (default Morningstar202604) ·
     COUNT (default 4, max 8) · OUTPUT (default projects-card.svg) ·
     THEME (dark|light|rose|ocean|aurora|sunset|mint)

Part of Profile Verse: https://github.com/Morningstar202604/profile-cards
"""

import html
import os
import sys
from datetime import datetime, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "projects-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
COUNT = min(int(os.environ.get("COUNT", "4")), 8)
THEME = os.environ.get("THEME", "dark")

W, H = 640, 300
GX0, GY0, GW, GH_ = 40, 96, 270, 74
GAPX, GAPY = 20, 12

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178C6", "JavaScript": "#F1E05A",
    "Go": "#00ADD8", "Rust": "#DEA584", "Java": "#B07219", "Kotlin": "#A97BFF",
    "Dart": "#00B4AB", "Swift": "#F05138", "C++": "#F34B7D", "C": "#555555",
    "C#": "#178600", "Shell": "#89E051", "HTML": "#E34C26", "CSS": "#663399",
    "Vue": "#41B883", "Markdown": "#083FA1", "Dockerfile": "#384D54",
    "Ruby": "#701516", "PHP": "#4F5D95", "Lua": "#000080", "Zig": "#EC915C",
}


def lang_color(lang, pal):
    if not lang:
        return pal["gold"]
    return LANG_COLORS.get(lang, pal["gold"])


def clip_desc(desc, limit=34):
    if not desc:
        return "No description"
    desc = desc.strip()
    if len(desc) <= limit:
        return desc
    return desc[: limit - 1].rstrip() + "…"


def clip_name(name, limit=24):
    return name[: limit - 1].rstrip() + "…" if len(name) > limit else name


def panel(x, y, repo, pal, idx):
    name = th.esc(clip_name(repo["name"]))
    desc = th.esc(clip_desc(repo.get("description") or ""))
    lang = repo.get("language") or ""
    stars = repo.get("stargazers_count", 0)
    lc = lang_color(lang, pal)
    lang_txt = th.esc(lang if lang else "repo")
    return (
        '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="1.2"/>'
        '<path d="M%d %d l8 2 l-8 2 z" fill="%s" opacity="0.85"/>'
        '<text x="%d" y="%d" font-family="%s" font-size="13.5" font-weight="700" fill="%s">%s</text>'
        '<text x="%d" y="%d" font-family="%s" font-size="10" fill="%s">%s</text>'
        '<circle cx="%d" cy="%d" r="3.2" fill="%s"/>'
        '<text x="%d" y="%d" font-family="%s" font-size="9.5" letter-spacing="1" fill="%s">%s</text>'
        '<text x="%d" y="%d" text-anchor="end" font-family="%s" font-size="11" fill="%s">★ %s</text>'
        % (
            x, y, GW, GH_, pal["panel"], pal["line"],
            x + 14, y + 18, pal["gold"],
            x + 26, y + 22, th.FONT, pal["gold_bright"], name,
            x + 16, y + 42, th.FONT, pal["muted"], desc,
            x + 18, y + 60, lc,
            x + 28, y + 63.5, th.FONT, pal["sub"], lang_txt,
            x + GW - 14, y + 22, th.FONT, pal["gold"], stars,
        )
    )


def main():
    pal = th.palette(THEME)
    repos = []
    try:
        data = gh.api("/users/%s/repos" % USER, {"per_page": 100, "page": 1, "sort": "pushed"})
        repos = [r for r in data if not r.get("fork")]
        repos.sort(key=lambda r: (r.get("stargazers_count", 0), r.get("pushed_at", "")), reverse=True)
    except Exception as err:  # noqa: BLE001
        print(f"warn: repos fetch failed ({err}); rendering empty grid")
    repos = repos[:COUNT]
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    panels = "".join(
        panel(GX0 + (i % 2) * (GW + GAPX), GY0 + (i // 2) * (GH_ + GAPY), r, pal, i)
        for i, r in enumerate(repos)
    )
    empties = "".join(
        '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="1" stroke-dasharray="4 4" opacity="0.55"/>'
        % (GX0 + (i % 2) * (GW + GAPX), GY0 + (i // 2) * (GH_ + GAPY), GW, GH_, pal["panel"], pal["line"])
        for i in range(len(repos), 4)
    )

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Projects — %s">'
        '%s'
        '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
        '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">PROJECTS</text>'
        '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
        '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
        '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 公开数据</text>'
        '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
        '%s%s'
        '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub API · 每小时自动刷新 · 零服务器</text>'
        '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">projects-card · v1.6.0</text>'
        '</svg>'
        % (
            W, H, W, H, th.esc(USER),
            th.card_bg(pal, W, H),
            pal["gold"],
            th.FONT, pal["gold_bright"],
            th.FONT, pal["sub"], date,
            th.FONT, pal["text"], th.esc(USER),
            th.FONT, pal["sub"],
            pal["line"],
            panels, empties,
            H - 16, th.FONT, pal["dim"],
            H - 16, th.FONT, pal["dim"],
        )
    )
    os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("OK: wrote %s (%d bytes, %s, %d projects)" % (OUTPUT, len(svg), USER, len(repos)))


if __name__ == "__main__":
    main()
