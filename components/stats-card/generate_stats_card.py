#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Profile Stats Card — Profile Verse component
---------------------------------------------
A differentiated "stats" card: three hero numbers (followers / public repos /
merged PRs) sitting on golden orbit arcs over a starfield. Signature look:
planets-on-orbits, not a plain grid.

Env: GH_TOKEN (optional — public data works anonymously, token raises the
     rate limit) · USER (default Morningstar202604) · OUTPUT
     (default stats-card.svg) · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import os
import sys
from datetime import datetime, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "stats-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
THEME = os.environ.get("THEME", "dark")

W, H = 640, 300


def orbit(x, y, rx, ry, rot, pal):
    return '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="none" stroke="%s" stroke-opacity="0.35" transform="rotate(%d %d %d)"/>' % (
        x, y, rx, ry, pal["gold"], rot, x, y)


def orbit_ticks(x, y, rx, ry, rot, pal, n=6):
    """Small gold studs along an orbit — rhythm along the arcs."""
    import math
    out = []
    for i in range(n):
        a = math.radians(175 + i * (160.0 / max(n - 1, 1)))
        px = x + rx * math.cos(a)
        py = y + ry * math.sin(a)
        out.append('<circle cx="%.1f" cy="%.1f" r="1.5" fill="%s" opacity="0.55" transform="rotate(%d %d %d)"/>'
                   % (px, py, pal["gold"], rot, x, y))
    return "".join(out)


def main():
    pal = th.palette(THEME)
    try:
        prof = gh.fetch_user(USER)
        followers = int(prof.get("followers", 0))
        repos = int(prof.get("public_repos", 0))
        prs = len(gh.fetch_merged_prs(USER))
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        blocks = [
            (120, str(followers), "关注者"),
            (320, str(repos), "公开仓库"),
            (520, str(prs), "已合并 PR"),
        ]
        nums = "".join(
            '<text x="%d" y="186" text-anchor="middle" font-family="%s" font-size="44" font-weight="700" fill="url(#gtst)">%s</text>'
            '<text x="%d" y="212" text-anchor="middle" font-family="%s" font-size="12.5" letter-spacing="3" fill="%s">%s</text>'
            '<line x1="%d" y1="224" x2="%d" y2="224" stroke="%s" stroke-width="1.6" opacity="0.8"/>'
            '<circle cx="%d" cy="232" r="2.4" fill="%s"/>'
            % (x, th.FONT, th.esc(v), x, th.FONT, pal["muted"], th.esc(label),
               x - 34, x + 34, pal["gold"], x, pal["gold"])
            for x, v, label in blocks
        )
        planets = "".join(
            '<circle cx="%d" cy="%d" r="3.4" fill="%s" opacity="0.95"/>'
            '<circle cx="%d" cy="%d" r="6.5" fill="%s" opacity="0.22"/>'
            % (px, py, pal["gold_bright"], px, py, pal["gold_bright"])
            for px, py in [(160, 138), (470, 128), (252, 222)]
        )

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Profile Stats — %s">'
            '%s'
            '<defs>%s</defs>'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">PROFILE STATS</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
            '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 公开数据</text>'
            '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="83" x2="354" y2="83" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '%s'
            '%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub API · 每日自动刷新 · 零服务器</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">stats-card · v1.4.1</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                th.num_gradient(pal, "st"),
                pal["gold"],
                th.FONT, pal["gold_bright"],
                th.FONT, pal["sub"], date,
                th.FONT, pal["text"], th.esc(USER),
                th.FONT, pal["sub"],
                pal["line"], pal["gold"], pal["gold"],
                orbit(320, 170, 300, 70, -6, pal) + orbit_ticks(320, 170, 300, 70, -6, pal)
                + orbit(320, 170, 300, 70, 6, pal) + orbit_ticks(320, 170, 300, 70, 6, pal)
                + orbit(320, 170, 300, 52, 0, pal) + orbit_ticks(320, 170, 300, 52, 0, pal, 8) + planets,
                nums,
                276, th.FONT, pal["dim"],
                276, th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s: followers=%d repos=%d prs=%d)" % (OUTPUT, len(svg), USER, followers, repos, prs))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
