#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contribution Grid Card (3D) — Profile Verse component
------------------------------------------------------
A fully self-built replacement for third-party contribution animations:
your GitHub contribution calendar rendered as a 3D isometric field of gold
columns, rising with daily activity. Signature look: isometric 3D columns
(one glance = different from every flat green grid), starfield + gold.

Real data: GitHub contribution calendar via GraphQL (full year).
Pure stdlib SVG — zero server, zero JS, no third-party action needed.

Env: GH_TOKEN (required) · USER (default Morningstar202604) · OUTPUT
     (default contrib-grid-card.svg) · THEME (dark|light)

Part of Profile Verse: https://github.com/Morningstar202604/profile-verse
"""

import math
import os
import sys
from datetime import date, datetime, timedelta, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _ROOT)

from core import github as gh  # noqa: E402
from core import theme as th  # noqa: E402

OUTPUT = os.environ.get("OUTPUT", "contrib-grid-card.svg")
USER = os.environ.get("USER", "Morningstar202604")
THEME = os.environ.get("THEME", "dark")

W = 640
S = 8.0          # isometric cell size
H_UNIT = 5.0     # bar height per activity level
MAX_LEVEL = 4

DX = S * math.cos(math.radians(30))
DY = S * math.sin(math.radians(30))

# gold ramp per theme: level -> (top face, right face, left face)
def _mix(c1, c2, t):
    """Blend two #RRGGBB colors by t in [0,1]."""
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join("%02X" % round(x + (y - x) * t) for x, y in zip(a, b))


def ramp_of(pal):
    """Derive a 4-level 3D column ramp from the palette's accent color —
    theme-agnostic, so new themes (aurora/sunset/mint/…) adapt automatically."""
    b, g = pal["gold_bright"], pal["gold"]
    d = _mix(g, "#000000", 0.30)
    dd = _mix(d, "#000000", 0.35)
    levels = [
        (d, _mix(d, "#000000", 0.30), _mix(d, "#000000", 0.50)),
        (g, _mix(g, "#000000", 0.22), _mix(g, "#000000", 0.42)),
        (_mix(b, g, 0.40), _mix(b, g, 0.60), _mix(b, g, 0.75)),
        (b, _mix(b, "#FFFFFF", 0.25), _mix(b, "#FFFFFF", 0.45)),
    ]
    return {i + 1: levels[i] for i in range(4)}
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def build_weeks(days):
    """Group flat calendar days into Sunday-start weeks (list of 7-count lists)."""
    by_date = {}
    for d in days:
        by_date[d["date"]] = d["count"]
    if not by_date:
        return []
    dates = sorted(by_date)
    first = date.fromisoformat(dates[0])
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    last = date.fromisoformat(dates[-1])
    weeks = []
    ws = start
    while ws <= last:
        weeks.append([by_date.get((ws + timedelta(days=i)).isoformat(), 0) for i in range(7)])
        ws += timedelta(days=7)
    return weeks


def level_of(count):
    if count <= 0:
        return 0
    if count == 1:
        return 1
    if count <= 3:
        return 2
    if count <= 6:
        return 3
    return 4


def cell(x0, y0, level, pal):
    """One isometric cell: floor diamond + up to 3 prism faces."""
    base_fill = pal["gold"]
    base_op = 0.14 if th.is_light(THEME) else 0.07
    out = (
        '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" '
        'fill="%s" fill-opacity="%s"/>'
        % (x0, y0 - DY, x0 + DX, y0, x0, y0 + DY, x0 - DX, y0, base_fill, base_op)
    )
    if level:
        top, right, left = ramp_of(pal)[level]
        h = level * H_UNIT
        t = (x0, y0 - DY - h)
        r = (x0 + DX, y0 - h)
        b = (x0, y0 + DY - h)
        l = (x0 - DX, y0 - h)
        out += (
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            % (
                l[0], l[1], x0, y0, x0, y0 + DY, b[0], b[1], left,
                x0, y0, r[0], r[1], b[0], b[1], x0, y0 + DY, right,
                t[0], t[1], r[0], r[1], b[0], b[1], l[0], l[1], top,
            )
        )
    return out


def legend(pal, y):
    """Five swatches: 0 / 1 / 2-3 / 4-6 / 7+ per day."""
    items = ["0", "1", "2-3", "4-6", "7+"]
    ramp = ramp_of(pal)
    cols = [base_color(pal), ramp[1][0], ramp[2][0], ramp[3][0], ramp[4][0]]
    out = ['<text x="310" y="%d" font-family="%s" font-size="10.5" fill="%s">每日贡献</text>' % (y + 11, th.FONT, pal["muted"])]
    x = 392
    for name, c in zip(items, cols):
        out.append(
            '<rect x="%d" y="%d" width="12" height="12" rx="2.5" fill="%s"/>'
            '<text x="%d" y="%d" font-family="%s" font-size="10" fill="%s">%s</text>'
            % (x, y, c, x + 15, y + 11, th.FONT, pal["muted"], name)
        )
        x += 48
    return "".join(out)


def base_color(pal):
    return pal["gold"]


def main():
    if not gh.token():
        sys.stderr.write("error: GH_TOKEN is required — the contribution calendar is fetched via GitHub GraphQL, which always requires authentication.\n")
        return 1
    pal = th.palette(THEME)
    try:
        total, days = gh.fetch_contribution_calendar(USER)
        weeks = build_weeks(days)
        date_s = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        if not weeks:
            svg = (
                '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="200" viewBox="0 0 %d 200" role="img" aria-label="Contribution Grid — %s">'
                '%s'
                '<text x="30" y="40" font-family="%s" font-size="15" font-weight="700" letter-spacing="2.5" fill="%s">CONTRIBUTION GRID</text>'
                '<text x="320" y="120" text-anchor="middle" font-family="%s" font-size="14" fill="%s">%s</text>'
                '</svg>'
                % (W, W, th.esc(USER), th.card_bg(pal, W, 200), th.FONT, pal["gold_bright"], th.FONT, pal["muted"], th.esc("今年还没有贡献数据"))
            )
            with open(OUTPUT, "w", encoding="utf-8") as f:
                f.write(svg)
            return 0

        wn = len(weeks)
        min_bx = -6 * DX
        max_bx = (wn - 1) * DX
        span_x = max_bx - min_bx
        x0 = (W - span_x) / 2 + DX
        y0 = 150 + MAX_LEVEL * H_UNIT
        max_by = (wn - 1 + 6) * DY
        H = int(max_by + y0 + DY) + 72

        # painter's order: back (small w+d) to front (large w+d)
        cells = []
        prev_month = None
        month_labels = []
        for w in range(wn):
            wd0 = week_of(weeks, w, days)
            m = wd0.month
            if m != prev_month:
                bx = (w - 0) * DX + x0 - DX
                by = (w + 0) * DY + y0 - DY - 11
                if bx > 20 and bx < W - 40:
                    month_labels.append(
                        '<text x="%.1f" y="%.1f" font-family="%s" font-size="9.5" font-weight="600" fill="%s">%s</text>'
                        % (bx, by, th.FONT, pal["muted"], MONTHS[m - 1])
                    )
                prev_month = m
            for d in range(7):
                count = weeks[w][d]
                bx = (w - d) * DX + x0
                by = (w + d) * DY + y0
                cells.append((w + d, cell(bx, by, level_of(count), pal)))

        cells.sort(key=lambda t: t[0])
        body = "".join(month_labels) + "".join(c for _, c in cells)

        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="Contribution Grid — %s">'
            '%s'
            '<defs><radialGradient id="lightsweep" cx="0.78" cy="0.22" r="0.55"><stop offset="0" stop-color="%s" stop-opacity="0.12"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient></defs>'
            '<path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="%s" opacity="0.95"/>'
            '<text x="40" y="44" font-family="%s" font-size="14.5" font-weight="700" letter-spacing="3" fill="%s">CONTRIBUTION GRID</text>'
            '<text x="610" y="44" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1" fill="%s">更新于 %s</text>'
            '<text x="40" y="70" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>'
            '<text x="610" y="70" text-anchor="end" font-family="%s" font-size="11" letter-spacing="1" fill="%s">GitHub · 全年贡献 %d 次</text>'
            '<line x1="40" y1="84" x2="600" y2="84" stroke="%s" stroke-width="1"/>'
            '<line x1="286" y1="83" x2="354" y2="83" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
            '<path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="%s" opacity="0.9"/>'
            '%s'
            '%s'
            '%s'
            '<text x="30" y="%d" font-family="%s" font-size="10.5" fill="%s">数据来源 GitHub 贡献日历 · 每日自动刷新</text>'
            '<text x="610" y="%d" text-anchor="end" font-family="%s" font-size="10.5" letter-spacing="1.5" fill="%s">contrib-grid-card · v1.5.0</text>'
            '</svg>'
            % (
                W, H, W, H, th.esc(USER),
                th.card_bg(pal, W, H),
                pal["gold_bright"], pal["bg_top"],
                pal["gold"],
                th.FONT, pal["gold_bright"],
                th.FONT, pal["sub"], date_s,
                th.FONT, pal["text"], th.esc(USER),
                th.FONT, pal["sub"], total,
                pal["line"], pal["gold"], pal["gold"],
                body,
                '<rect width="%d" height="%d" fill="url(#lightsweep)"/>' % (W, H - 20),
                legend(pal, H - 26),
                H - 16, th.FONT, pal["dim"],
                H - 16, th.FONT, pal["dim"],
            )
        )
        os.makedirs(os.path.dirname(os.path.abspath(OUTPUT)) or ".", exist_ok=True)
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(svg)
        print("OK: wrote %s (%d bytes, %s: total=%d weeks=%d)" % (OUTPUT, len(svg), USER, total, wn))
        return 0
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("error: %s\n" % e)
        return 1


def week_of(weeks, w, days):
    """First day of week w (for month labels)."""
    by_date = {}
    for d in days:
        by_date[d["date"]] = d["count"]
    dates = sorted(by_date)
    first = date.fromisoformat(dates[0])
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    return start + timedelta(days=7 * w)


if __name__ == "__main__":
    sys.exit(main())
