#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tech Stack Card — Profile Verse component
-----------------------------------------
Your languages drawn as a constellation: the primary language is the bright
star at the centre, other languages orbit it as stars linked by constellation
lines. Signature look: star-map constellation, not a badge strip.

Real data: language of every public repo via GitHub API (repo count per
language, top 6).

Env: GH_TOKEN (optional — public data works anonymously, token raises the
     rate limit) · USER (default Morningstar202604) · OUTPUT
     (default tech-stack-card.svg) · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import math
import os
import sys
from collections import Counter
from datetime import datetime, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "tech-stack-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
THEME = os.environ.get("THEME", "dark")
MAX_NODES = int(os.environ.get("MAX_NODES", "6"))

W, H = 640, 360
CX, CY = 320, 196
RX, RY = 196, 88


def node(x, y, color, label, count, pal, out_pos):
    """One constellation node: glow + dot + label + count chip."""
    ox, oy = out_pos
    return (
        '<circle cx="%.1f" cy="%.1f" r="11" fill="%s" opacity="0.16"/>'
        '<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>'
        '<circle cx="%.1f" cy="%.1f" r="7.5" fill="none" stroke="%s" stroke-opacity="0.55" stroke-width="0.8"/>'
        '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="13" font-weight="600" fill="%s">%s</text>'
        '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="10" letter-spacing="1.5" fill="%s">%d 个仓库</text>'
        % (x, y, color, x, y, color, x, y, color,
           x + ox, y + oy, th.FONT, pal["text"], th.esc(label),
           x + ox, y + oy + 15, th.FONT, pal["muted"], count)
    )


def star5(cx, cy, r, fill, opacity=""):
    """5-point star polygon."""
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append("%.1f,%.1f" % (cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    op = ' opacity="%s"' % opacity if opacity else ""
    return '<polygon points="%s" fill="%s"%s/>' % (" ".join(pts), fill, op)


def main():
    pal = th.palette(THEME)
    try:
        repos = gh.fetch_repos(USER)
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        lang_counts = Counter(r["language"] for r in repos)
        top = lang_counts.most_common(MAX_NODES + 1)

        if not repos:
            svg = (
                '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Tech Stack — %s">'
                '%s<text x="30" y="40" font-family="%s" font-size="15" font-weight="700" letter-spacing="2.5" fill="%s">TECH STACK</text>'
                '<text x="320" y="180" text-anchor="middle" font-family="%s" font-size="14" fill="%s">暂无公开仓库</text></svg>'
                % (W, H, W, H, th.esc(USER), th.card_bg(pal, W, H), th.FONT, pal["gold_bright"], th.FONT, pal["muted"])
            )
            with open(OUTPUT, "w", encoding="utf-8") as f:
                f.write(svg)
            return 0

        primary = top[0][0]
        others = top[1:1 + MAX_NODES]

        # constellation lines: spokes centre->node + edges between neighbours
        lines = []
        n = len(others)
        for i, (lang, cnt) in enumerate(others):
            a = -math.pi / 2 + i * 2 * math.pi / n
            x = CX + RX * math.cos(a)
            y = CY + RY * math.sin(a)
            lines.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="0.30" stroke-width="1"/>' % (CX, CY, x, y, pal["gold"]))
            lines.append('<circle cx="%.1f" cy="%.1f" r="1.4" fill="%s" opacity="0.8"/>' % (x, y, pal["gold"]))
        for i in range(n):
            a1 = -math.pi / 2 + i * 2 * math.pi / n
            a2 = -math.pi / 2 + ((i + 1) % n) * 2 * math.pi / n
            lines.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="0.13" stroke-width="1" stroke-dasharray="3 4"/>' % (
                CX + RX * math.cos(a1), CY + RY * math.sin(a1),
                CX + RX * math.cos(a2), CY + RY * math.sin(a2), pal["gold"]))

        nodes = []
        for i, (lang, cnt) in enumerate(others):
            a = -math.pi / 2 + i * 2 * math.pi / n
            x = CX + RX * math.cos(a)
            y = CY + RY * math.sin(a)
            ox = math.cos(a) * 30
            oy = math.sin(a) * 22
            nodes.append(node(x, y, th.lang_color(lang), lang, cnt, pal, (ox, oy)))

        center = (
            '<ellipse cx="%d" cy="%d" rx="38" ry="15" fill="none" stroke="%s" stroke-opacity="0.35" stroke-width="1" stroke-dasharray="2 5"/>'
            '<circle cx="%d" cy="%d" r="2.2" fill="%s" opacity="0.9"/>'
            '<circle cx="%d" cy="%d" r="18" fill="%s" opacity="0.18"/>'
            '<circle cx="%d" cy="%d" r="10" fill="%s" opacity="0.28"/>'
            '%s'
            '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="13" font-weight="700" letter-spacing="1" fill="%s">%s</text>'
            '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="9" letter-spacing="2" fill="%s">主语言</text>'
            % (CX, CY, pal["gold"], CX + 34, CY - 4, pal["gold_bright"],
               CX, CY, pal["gold"], CX, CY, pal["gold"], star5(CX, CY, 13, pal["gold_bright"]),
               CX, CY + 40, th.FONT, pal["text"], th.esc(primary),
               CX, CY + 53, th.FONT, pal["muted"])
        )

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Tech Stack — %s">'
            '%s'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">TECH STACK</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
            '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 仓库主语言</text>'
            '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="83" x2="354" y2="83" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '%s%s%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub API · 按仓库主语言统计 · 每日自动刷新 · 零服务器</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10" letter-spacing="1.5" fill="%s">tech-stack-card · v1.4.1</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                pal["gold"],
                th.FONT, pal["gold_bright"],
                th.FONT, pal["sub"], date,
                th.FONT, pal["text"], th.esc(USER),
                th.FONT, pal["sub"],
                pal["line"], pal["gold"], pal["gold"],
                "".join(lines), center, "".join(nodes),
                H - 18, th.FONT, pal["dim"],
                H - 18, th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s: %d repos, top: %s)" % (OUTPUT, len(svg), USER, len(repos), ", ".join("%s=%d" % (l, c) for l, c in top[:4])))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
