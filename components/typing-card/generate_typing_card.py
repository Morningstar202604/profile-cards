#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Typing Card — Profile Verse component
--------------------------------------
A differentiated slogan banner: text types itself letter by letter over a
starfield with a gold cursor, looping through your phrases. Pure SVG + SMIL
animation, so it animates anywhere an <img> renders — no server, no JS.

Env: PHRASES (semicolon-separated, default below) · OUTPUT (default typing-card.svg)
     · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "typing-card.svg")
THEME = os.environ.get("THEME", "dark")
PHRASES = [p.strip() for p in os.environ.get("PHRASES", "夜观星象，以代码作舟;Code under the stars, ship with the dawn;Full-stack AI engineer").split(";") if p.strip()][:3]

W, H = 640, 120
FS = 17
SPEED = 0.12   # s per typed char
DELETE = 0.045  # s per deleted char
HOLD = 1.8     # s a completed phrase stays on screen
EPS = 0.0005


def char_w(ch):
    if "\u4e00" <= ch <= "\u9fff" or ch in "\uff0c\u3002\u3001\uff01\uff1a\uff1b\u2026":
        return 1.0
    if ch == " ":
        return 0.32
    return 0.6


def widths(text):
    return [char_w(c) for c in text]


def total_w(text):
    return sum(widths(text)) * FS


def build_timeline(phrases):
    """Return (T, events) where events[i] = (type_start, type_len, del_start).
    Letter windows are derived from these. phrase 0 is fully visible at t=0."""
    lens = [len(p) for p in phrases]
    starts = []
    t = HOLD + lens[0] * DELETE
    for i in range(1, len(phrases)):
        starts.append(t)
        t += lens[i] * SPEED + HOLD + lens[i] * DELETE
    t0s = t
    T = t0s + lens[0] * SPEED + HOLD
    return T, [None] + starts + [t0s]


def letter_anim(phrase_idx, k, lens, starts, T):
    eps = EPS / T
    if phrase_idx == 0:
        a = (HOLD + (k + 1) * DELETE) / T
        b = (starts[-1] + (k + 1) * SPEED) / T
        vals = "visible;visible;hidden;hidden;visible;visible"
        keys = "0;%.4f;%.4f;%.4f;%.4f;1" % (a, min(a + eps, 1), b, min(b + eps, 1))
    else:
        s = (starts[phrase_idx] + (k + 1) * SPEED) / T
        e = (starts[phrase_idx] + lens[phrase_idx] * SPEED + HOLD + (k + 1) * DELETE) / T
        vals = "hidden;hidden;visible;visible;hidden;hidden"
        keys = "0;%.4f;%.4f;%.4f;%.4f;1" % (s, min(s + eps, 1), e, min(e + eps, 1))
    return (
        '<animate attributeName="visibility" dur="%.2fs" repeatCount="indefinite" '
        'values="%s" keyTimes="%s"/>' % (T, vals, keys)
    )


def main():
    pal = th.palette(THEME)
    try:
        lens = [len(p) for p in PHRASES]
        T, starts = build_timeline(PHRASES)

        texts = []
        for i, phrase in enumerate(PHRASES):
            wsum = total_w(phrase)
            tspans = []
            x = 0
            for k, ch in enumerate(phrase):
                dx = "" if k == 0 else ' dx="%.1f"' % (widths(phrase)[k] * FS)
                vis = "" if i == 0 else ' visibility="hidden"'
                tspans.append(
                    '<tspan%s%s>%s%s</tspan>'
                    % (dx, vis, th.esc(ch), letter_anim(i, k, lens, starts, T))
                )
            texts.append(
                '<text x="320" y="66" text-anchor="middle" font-family="%s" font-size="%d" '
                'font-weight="600" fill="%s" letter-spacing="1">%s</text>'
                % (th.FONT, FS, pal["gold_bright"], "".join(tspans))
            )

        max_w = max(total_w(p) for p in PHRASES)
        cursor_x = 320 + max_w / 2 + 6
        cursor = (
            '<rect x="%.1f" y="46" width="3.5" height="22" rx="1.5" fill="%s">'
            '<animate attributeName="opacity" values="1;0.1;1" dur="0.9s" repeatCount="indefinite"/>'
            '</rect>' % (cursor_x, pal["gold"])
        )

        decor = (
            '<circle cx="320" cy="62" r="52" fill="none" stroke="%s" stroke-opacity="0.10" stroke-width="1"/>'
            '<circle cx="320" cy="62" r="66" fill="none" stroke="%s" stroke-opacity="0.06" stroke-width="1" stroke-dasharray="1 6"/>'
            '%s'
            '<line x1="40" y1="92" x2="600" y2="92" stroke="%s" stroke-width="0.8" opacity="0.7"/>'
            '<line x1="286" y1="91" x2="354" y2="91" stroke="%s" stroke-width="1.2" opacity="0.8"/>'
            '<path d="M320 88 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            % (pal["gold"], pal["gold"],
               th.sparkle(584, 34, 6, pal["gold_bright"], 0.7),
               pal["line"], pal["gold"], pal["gold"])
        )
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="%s">'
            '%s'
            '%s'
            '%s%s'
            '<text x="30" y="106" font-family="%s" font-size="9.5" letter-spacing="1" fill="%s">PROFILE VERSE</text>'
            '<text x="610" y="106" text-anchor="end" font-family="%s" font-size="9.5" letter-spacing="1.5" fill="%s">typing-card · v1.5.0</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(PHRASES[0]),
                th.card_bg(pal, W, H),
                decor,
                "".join(texts), cursor,
                th.FONT, pal["dim"],
                th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %d phrases, cycle %.1fs)" % (OUTPUT, len(svg), len(PHRASES), T))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
