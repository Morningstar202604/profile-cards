#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banner Card — Profile Verse component
-------------------------------------
A wide hero banner for the top of your profile: your name glowing in gold over
a starfield, with a comet trail crossing the sky. Signature look: glowing name
+ comet trail. No API needed — pure visual.

Env: USER (default Morningstar202604) · TEXT (subtitle, default below) ·
     OUTPUT (default banner-card.svg) · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import os
import random
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "banner-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
TEXT = os.environ.get("TEXT", "Code under the stars, ship with the dawn")
THEME = os.environ.get("THEME", "dark")

W, H = 960, 240


def stars(pal, n=120, seed=11):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x = rnd.uniform(8, W - 8)
        y = rnd.uniform(8, H - 8)
        r = rnd.choice([0.7, 1.0, 1.3, 1.7])
        op = rnd.uniform(0.12, 0.5)
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.2f"/>' % (x, y, r, pal["star"], op))
    # a few bright twinkles
    for _ in range(6):
        x = rnd.uniform(60, W - 60)
        y = rnd.uniform(30, H - 40)
        out.append(th.sparkle(x, y, rnd.choice([4, 5, 6]), pal["gold_bright"], 0.6))
    return "".join(out)


def comet(pal):
    """A comet trail arcing across the banner."""
    return (
        '<path d="M -60 208 Q 300 26 640 118 T 1030 52" fill="none" stroke="%s" stroke-width="1.6" stroke-opacity="0.55" stroke-dasharray="1 9" stroke-linecap="round"/>'
        '<path d="M 640 118 Q 700 132 762 108" fill="none" stroke="%s" stroke-width="2.2" stroke-opacity="0.85" stroke-linecap="round"/>'
        '<circle cx="762" cy="108" r="3.2" fill="%s"/>'
        '<circle cx="762" cy="108" r="8" fill="%s" opacity="0.25"/>'
        '<path d="M 900 40 Q 934 62 962 56" fill="none" stroke="%s" stroke-width="1.2" stroke-opacity="0.45" stroke-linecap="round"/>'
        '<circle cx="962" cy="56" r="1.8" fill="%s" opacity="0.7"/>'
        % (pal["gold"], pal["gold_bright"], pal["gold_bright"], pal["gold_bright"],
           pal["gold"], pal["gold_bright"])
    )


def main():
    pal = th.palette(THEME)
    try:
        name = USER if len(USER) <= 24 else USER[:23] + "\u2026"
        defs = (
            '<defs>'
            '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="%s"/><stop offset="0.5" stop-color="%s"/>'
            '<stop offset="1" stop-color="%s"/></linearGradient>'
            '<radialGradient id="nebG" cx="0.22" cy="0.10" r="0.62">'
            '<stop offset="0" stop-color="%s" stop-opacity="0.22"/>'
            '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="nebB" cx="0.92" cy="0.88" r="0.6">'
            '<stop offset="0" stop-color="%s" stop-opacity="0.24"/>'
            '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="glow" cx="0.5" cy="0.5" r="0.62">'
            '<stop offset="0" stop-color="%s" stop-opacity="0.18"/>'
            '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
            '<linearGradient id="gtext" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="%s"/><stop offset="0.5" stop-color="%s"/>'
            '<stop offset="1" stop-color="%s"/></linearGradient>'
            '<filter id="blur1" x="-40%%" y="-40%%" width="180%%" height="180%%">'
            '<feGaussianBlur stdDeviation="8"/></filter>'
            '<filter id="blur2" x="-30%%" y="-30%%" width="160%%" height="160%%">'
            '<feGaussianBlur stdDeviation="3.4"/></filter>'
            '</defs>'
            '<rect width="%d" height="%d" fill="url(#bg)"/>'
            '<rect width="%d" height="%d" fill="url(#nebG)"/>'
            '<rect width="%d" height="%d" fill="url(#nebB)"/>'
            '<rect width="%d" height="%d" fill="url(#glow)"/>'
            '%s'
            '%s'
            '<rect x="0.5" y="0.5" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1"/>'
            '%s'
            '%s'
            % (
                pal["bg_top"], pal.get("bg_mid", pal["bg_top"]), pal["bg_bottom"],
                pal["gold"], pal["bg_top"],
                pal.get("nebula", "#2B4B9E"), pal["bg_top"],
                pal["gold"], pal["bg_top"],
                pal["gold_bright"], pal["gold"], pal["gold_bright"],
                W, H, W, H, W, H, W, H,
                stars(pal),
                th.microdots(W, H, pal),
                W - 1, H - 1, pal["line"],
                th.edge_marks(W, H, pal),
                th.corner_marks(W, H, pal),
            )
        )
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="%s">'
            '%s'
            '%s'
            '<text x="480" y="126" text-anchor="middle" font-family="%s" font-size="54" font-weight="800" fill="%s" filter="url(#blur1)">%s</text>'
            '<text x="480" y="126" text-anchor="middle" font-family="%s" font-size="54" font-weight="800" fill="%s" filter="url(#blur2)">%s</text>'
            '<text x="480" y="126" text-anchor="middle" font-family="%s" font-size="54" font-weight="800" fill="url(#gtext)">%s</text>'
            '<line x1="430" y1="150" x2="530" y2="150" stroke="%s" stroke-width="1.3" opacity="0.85"/>'
            '<path d="M480 145 l4.5 4.5 l-4.5 4.5 l-4.5 -4.5 z" fill="%s" opacity="0.95"/>'
            '<text x="480" y="180" text-anchor="middle" font-family="%s" font-size="14.5" letter-spacing="3" fill="%s">%s</text>'
            '<text x="28" y="224" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">PROFILE VERSE</text>'
            '<text x="932" y="224" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">banner-card · v1.4.1</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                defs,
                comet(pal),
                th.FONT, pal["gold_bright"], th.esc(name),
                th.FONT, pal["gold"], th.esc(name),
                th.FONT, th.esc(name),
                pal["gold"],
                pal["gold"],
                th.FONT, pal["muted"], th.esc(TEXT),
                th.FONT, pal["dim"],
                th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s)" % (OUTPUT, len(svg), USER))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
