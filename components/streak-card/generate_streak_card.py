#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Streak Card — Profile Verse component
--------------------------------------
A differentiated streak card: the current streak is the star at the centre of
a golden orbital ring (a "star orbit"), with longest streak and yearly total
contributions as two constellation chips. Signature look: star-orbit ring.

Data is real, from the GitHub contribution calendar (GraphQL, full year).

Env: GH_TOKEN (required) · USER (default Morningstar202604) · OUTPUT
     (default streak-card.svg) · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import math
import os
import sys
from datetime import datetime, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "streak-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
THEME = os.environ.get("THEME", "dark")

W, H = 640, 360
CX, CY, R = 320, 195, 84


def ring_dots(pal, n=12, r=R + 14):
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n
        out.append('<circle cx="%.1f" cy="%.1f" r="1.6" fill="%s" opacity="0.8"/>' % (CX + r * math.cos(a), CY + r * math.sin(a), pal["gold"]))
    for i in range(60):
        a = 2 * math.pi * i / 60
        x1, y1 = CX + (R + 8) * math.cos(a), CY + (R + 8) * math.sin(a)
        x2, y2 = CX + (R + 12) * math.cos(a), CY + (R + 12) * math.sin(a)
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" opacity="0.28"/>' % (x1, y1, x2, y2, pal["gold"]))
    return "".join(out)


def chip(x, w, value, label, pal):
    return (
        '<rect x="%d" y="294" width="%d" height="42" rx="21" fill="url(#ppanel)" stroke="%s" stroke-opacity="0.6"/>'
        '<path d="M%d 303 l2 -2.5 l2 2.5 l-2 2.5 z" fill="%s" opacity="0.9"/>'
        '<text x="%d" y="313" text-anchor="middle" font-family="%s" font-size="16" font-weight="700" fill="url(#gtsk)">%s</text>'
        '<text x="%d" y="328" text-anchor="middle" font-family="%s" font-size="11" letter-spacing="1.5" fill="%s">%s</text>'
        % (x, w, pal["line"], x + w // 2 - 2, pal["gold"], x + w // 2, th.FONT, th.esc(value), x + w // 2, th.FONT, pal["muted"], th.esc(label))
    )


def main():
    if not gh.token():
        sys.stderr.write("error: GH_TOKEN is required — the contribution calendar is fetched via GitHub GraphQL, which always requires authentication.\n")
        return 1
    pal = th.palette(THEME)
    try:
        total, days = gh.fetch_contribution_calendar(USER)
        cur, longest = gh.compute_streaks(days)
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        light = THEME != "dark"

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Streak — %s">'
            '%s'
            '<defs>%s</defs>'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">STREAK</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
            '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 贡献日历</text>'
            '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="83" x2="354" y2="83" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="url(#glow)"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="url(#grk)" stroke-opacity="%s" stroke-width="1.8"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-opacity="%s" stroke-dasharray="2 6"/>'
            '%s'
            '<circle cx="%d" cy="%d" r="4" fill="%s"/>'
            '<circle cx="%d" cy="%d" r="7" fill="%s" opacity="0.25"/>'
            '<text x="%d" y="203" text-anchor="middle" font-family="%s" font-size="50" font-weight="700" fill="url(#gtsk)">%d</text>'
            '<text x="%d" y="229" text-anchor="middle" font-family="%s" font-size="12" letter-spacing="2" fill="%s">当前连续天数</text>'
            '%s'
            '%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub 贡献日历 · 每日自动刷新 · 零服务器</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">streak-card · v1.4.1</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                th.num_gradient(pal, "sk") + '<linearGradient id="grk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="0.5" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>' % (pal["gold"], pal["gold_bright"], pal["gold"]) + '<linearGradient id="ppanel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>' % (pal["panel_top"], pal["panel"]),
                pal["gold"],
                th.FONT, pal["gold_bright"],
                th.FONT, pal["sub"], date,
                th.FONT, pal["text"], th.esc(USER),
                th.FONT, pal["sub"],
                pal["line"], pal["gold"], pal["gold"],
                CX, CY, R + 26,
                CX, CY, R,
                0.9 if light else 0.55,
                CX, CY, R + 14, pal["gold"], 0.4 if light else 0.18,
                ring_dots(pal),
                CX, CY - R - 14, pal["gold_bright"],
                CX, CY - R - 14, pal["gold"],
                CX, th.FONT, cur,
                CX, th.FONT, pal["muted"],
                chip(100, 170, "%d 天" % longest, "最长连续", pal),
                chip(370, 170, "%d 次" % total, "全年贡献", pal),
                340, th.FONT, pal["dim"],
                340, th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s: current=%d longest=%d total=%d)" % (OUTPUT, len(svg), USER, cur, longest, total))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
