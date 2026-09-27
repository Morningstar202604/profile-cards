# -*- coding: utf-8 -*-
"""year-review-card — a golden annual ring: 12 months orbit the ring, the
year's total glows in the center, and four 'star medals' summarise the year.

Signature shape: the annual ring (year of stars). Real data from the GitHub
contribution calendar (last 365 days) + merged PRs + repo languages.

Env:  GH_TOKEN (required) · USER (default Morningstar202604) · THEME (dark|light)
      OUTPUT (default year-review-card.svg)
"""

import math
import os
import sys
from datetime import date as _date

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

USER = os.environ.get("USER", "Morningstar202604")
THEME = os.environ.get("THEME", "dark")
OUTPUT = os.environ.get("OUTPUT", "year-review-card.svg")
FONT = th.FONT

W, H = 640, 340
CX, CY = 150, 198
RING_R = 80
MONTHS = "JFMAMJJASOND"
MONTH_NAMES_CN = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]


def month_ring(months, pal):
    """12 month-stars on a golden ring; size/brightness follow contributions."""
    out = []
    mx = max(months) or 1
    peak = max(range(12), key=lambda i: months[i])
    for i, c in enumerate(months):
        ang = math.radians(i * 30.0 - 90.0)
        x = CX + RING_R * math.cos(ang)
        y = CY + RING_R * math.sin(ang)
        if i == peak and c > 0:
            out.append('<circle cx="%.1f" cy="%.1f" r="6.5" fill="%s" opacity="0.16"/>' % (x, y, pal["gold"]))
        if c > 0:
            r = 1.3 + 2.2 * math.sqrt(c / mx)
            op = 0.5 + 0.5 * math.sqrt(c / mx)
            out.append('<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s" opacity="%.2f"/>' % (x, y, r, pal["gold"], op))
        else:
            out.append('<circle cx="%.1f" cy="%.1f" r="1" fill="%s" opacity="0.32"/>' % (x, y, pal["dim"]))
        lx = CX + (RING_R + 16) * math.cos(ang)
        ly = CY + (RING_R + 16) * math.sin(ang)
        out.append(
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="8.5" fill="%s">%s</text>'
            % (lx, ly + 3, FONT, pal["muted"], MONTHS[i])
        )
    return "".join(out)


def metric(x, y, w, h, value, label, pal):
    """One 'star medal' — gradient panel, top gold hairline, diamond stud."""
    return (
        '<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="url(#pp)" stroke="%s" stroke-opacity="0.35"/>'
        '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2" opacity="0.8"/>'
        '<path d="M%d %d l3 -3 l3 3 l-3 3 z" fill="%s"/>'
        '<text x="%d" y="%d" font-family="%s" font-size="18" font-weight="700" fill="url(#yr)">%s</text>'
        '<text x="%d" y="%d" font-family="%s" font-size="9.5" letter-spacing="1.5" fill="%s">%s</text>'
        % (x, y, w, h, pal["line"],
           x, y + 18, x + w, y + 18, pal["gold"],
           x + 14, y + 14, pal["gold"],
           x + 14, y + 46, FONT, th.esc(value),
           x + 14, y + 60, FONT, pal["muted"], th.esc(label))
    )


def main():
    if not gh.token():
        sys.stderr.write("error: GH_TOKEN is required — the contribution calendar is fetched via GitHub GraphQL, which always requires authentication.\n")
        return 1
    try:
        pal = th.palette(THEME)
        light = THEME.strip().lower() == "light"
        total, days = gh.fetch_contribution_calendar(USER)
        cur, longest = gh.compute_streaks(days)
        months = [0] * 12
        for d in days:
            dt = _date.fromisoformat(d["date"])
            months[dt.month - 1] += d["count"]
        year_total = sum(months)
        peak = max(range(12), key=lambda i: months[i]) if any(months) else 0
        peak_count = months[peak]
        peak_name = MONTH_NAMES_CN[peak]

        try:
            prs = len(gh.fetch_merged_prs(USER, max_pr=50))
        except Exception:  # noqa: BLE001
            prs = 0
        try:
            repos = gh.fetch_repos(USER)
            lang_counts = {}
            for r in repos:
                l = (r.get("language") or "Other").strip() or "Other"
                lang_counts[l] = lang_counts.get(l, 0) + 1
            top_lang = max(lang_counts, key=lang_counts.get) if lang_counts else "—"
        except Exception:  # noqa: BLE001
            top_lang = "—"

        date = _date.today().isoformat()
        ring = month_ring(months, pal)
        m1 = metric(320, 120, 132, 70, "%s · %d" % (peak_name, peak_count), "最活跃月", pal)
        m2 = metric(468, 120, 132, 70, "%d 天" % longest, "最长连续", pal)
        m3 = metric(320, 198, 132, 70, "%d" % prs, "合并 PR", pal)
        m4 = metric(468, 198, 132, 70, top_lang, "主力语言", pal)

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Year in Review — %s">'
            '%s'
            '<defs>'
            '<linearGradient id="pp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
            '<linearGradient id="yr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
            '</defs>'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">YEAR IN REVIEW</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
            '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 近一年回顾</text>'
            '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="83" x2="354" y2="83" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1" opacity="0.4"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="0.6" stroke-dasharray="3 5" opacity="0.5"/>'
            '%s'
            '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="30" font-weight="600" fill="url(#yr)">%d</text>'
            '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="10" letter-spacing="2.5" fill="%s">贡献 · 近一年</text>'
            '%s%s%s%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub API · 每日自动刷新 · 零服务器</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10" letter-spacing="1.5" fill="%s">year-review-card · v1.5.0</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                pal["panel_top"], pal["panel"],
                pal["gold_bright"], pal["gold"],
                pal["gold"],
                FONT, pal["gold_bright"],
                FONT, pal["sub"], date,
                FONT, pal["text"], th.esc(USER),
                FONT, pal["sub"],
                pal["line"], pal["gold"], pal["gold"],
                CX, CY, RING_R, pal["gold"],
                CX, CY, RING_R - 20, pal["gold"],
                ring,
                CX, CY - 10, FONT, year_total,
                CX, CY + 20, FONT, pal["muted"],
                m1, m2, m3, m4,
                H - 24, FONT, pal["dim"],
                H - 24, FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s: year_total=%d peak=%s(%d) longest=%d prs=%d lang=%s)" % (
            OUTPUT, len(svg), USER, year_total, peak_name, peak_count, longest, prs, top_lang))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
