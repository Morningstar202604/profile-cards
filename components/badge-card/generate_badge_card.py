#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Badge Card — Profile Verse component
------------------------------------
A row of gold medal-style badges that replace the flat shields.io strip:
each badge is a pill with a golden gradient border and a star icon.
Signature look: golden medals, not flat pills.

Data: by default auto-computed from GitHub (merged PRs / yearly contributions /
public repos / followers); or pass your own via `badges` ("label=value;...").
Without GH_TOKEN, auto mode falls back to the three public REST metrics
(merged PRs / repos / followers) and omits the GraphQL-only yearly total.

Env: GH_TOKEN (optional) · USER (default Morningstar202604) ·
     BADGES (optional custom badges) · OUTPUT (default badge-card.svg) ·
     THEME (dark|light)

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

OUTPUT = os.environ.get("OUTPUT", "badge-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
BADGES_RAW = os.environ.get("BADGES", "")
THEME = os.environ.get("THEME", "dark")

W, H = 640, 172
BADGE_W, BADGE_H = 136, 74
GAP = 12


def star_icon(cx, cy, r=7, fill="#C9A86A"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append("%.1f,%.1f" % (cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return '<polygon points="%s" fill="%s"/>' % (" ".join(pts), fill)


def badge(x, value, label, pal):
    return (
        '<defs>'
        '<linearGradient id="ge%d" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
        '</linearGradient></defs>'
        '<rect x="%d" y="64" width="%d" height="%d" rx="20" fill="url(#pb)" stroke="url(#ge%d)" stroke-width="1.6"/>'
        '<line x1="%d" y1="65" x2="%d" y2="65" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
        '<circle cx="%d" cy="96" r="11" fill="%s" opacity="0.16"/>'
        '<circle cx="%d" cy="96" r="6" fill="none" stroke="%s" stroke-opacity="0.5" stroke-width="0.8"/>'
        '%s'
        '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="25" font-weight="700" fill="url(#gtb)">%s</text>'
        '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="11" letter-spacing="2" fill="%s">%s</text>'
        '<circle cx="%d" cy="118" r="1.6" fill="%s" opacity="0.8"/>'
        '<circle cx="%d" cy="118" r="1.6" fill="%s" opacity="0.8"/>'
        % (x, pal["gold"], pal["gold_bright"],
           x, BADGE_W, BADGE_H, x,
           x + 14, x + BADGE_W - 14, pal["gold_bright"],
           x + 20, pal["gold_bright"], x + 20, pal["gold_bright"],
           star_icon(x + 20, 96, 8, pal["gold_bright"]),
           x + BADGE_W // 2 + 12, 100, th.FONT, th.esc(value),
           x + BADGE_W // 2 + 12, 123, th.FONT, pal["muted"], th.esc(label),
           x + 24, pal["gold"], x + BADGE_W - 24, pal["gold"])
    )


def main():
    pal = th.palette(THEME)
    try:
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        if BADGES_RAW.strip():
            items = []
            for seg in BADGES_RAW.split(";"):
                seg = seg.strip()
                if not seg:
                    continue
                if "=" in seg:
                    label, value = seg.split("=", 1)
                    items.append((value.strip(), label.strip()))
                else:
                    items.append((seg.strip(), seg.strip()))
        else:
            prof = gh.fetch_user(USER)
            prs = len(gh.fetch_merged_prs(USER))
            items = [
                ("%d" % prs, "已合并 PR"),
                ("%d" % prof.get("public_repos", 0), "公开仓库"),
                ("%d" % prof.get("followers", 0), "关注者"),
            ]
            if gh.token():
                total, _ = gh.fetch_contribution_calendar(USER)
                items.insert(1, ("%d" % total, "全年贡献"))

        badges = []
        n = len(items[:5])
        total_w = n * BADGE_W + (n - 1) * GAP
        x0 = (W - total_w) // 2
        for i, (value, label) in enumerate(items[:5]):
            badges.append(badge(x0 + i * (BADGE_W + GAP), value, label, pal))

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Badges — %s">'
            '%s'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">BADGES</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<line x1="40" y1="56" x2="600" y2="56" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="55" x2="354" y2="55" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 52 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '<defs><linearGradient id="pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>%s</defs>'
            '%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">badge-card · v1.5.0</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                pal["gold"],
                th.FONT, pal["gold_bright"],
                th.FONT, pal["sub"], date,
                pal["line"],
                pal["gold"], pal["gold"],
                pal["panel_top"], pal["panel"], th.num_gradient(pal, "b"),
                "".join(badges),
                H - 16, th.FONT, pal["dim"],
                th.esc("数据来源 GitHub API · 每日自动刷新 · 零服务器" if not BADGES_RAW.strip() else "自定义徽章 · 由输入参数生成 · 零服务器"),
                H - 16, th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %d badges)" % (OUTPUT, len(svg), len(items)))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
