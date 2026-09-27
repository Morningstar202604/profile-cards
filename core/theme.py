# -*- coding: utf-8 -*-
"""Profile Verse — shared design tokens for every card.

Two full palettes: "dark" (deep-blue + gold brand, default) and "light"
(paper-white + deep gold, for profiles on light themes). Every component
reads `theme` input -> THEME env -> th.palette(THEME).

Premium finish layer (anti-AI-flat):
  - 3-stop sky gradient (deep space, not one flat wash)
  - gold nebula (top-right) + blue nebula (bottom-left) radial glows
  - micro-grain dots (film texture instead of sterile vector flatness)
  - a few 4-ray sparkles among the starfield
  - thin gold corner ticks framing the card
  - gradient number fills for hero figures
"""

import random
import xml.sax.saxutils as sax

FONT = "'Segoe UI',Helvetica,Arial,'PingFang SC','Microsoft YaHei',sans-serif"
FONT_CN = "'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif"

# Semantic version of the design system & component suite.
# Release flow: bump here -> bump the "· vX.Y.Z" footer literal in every
# component generator -> regenerate all previews -> tag vX.Y.Z + move vX.
VERSION = "1.4.1"

# --------------------------------------------------------------------------
# brand palettes
# --------------------------------------------------------------------------
PALETTES = {
    "dark": {
        "bg_top": "#070B1E",
        "bg_mid": "#0B1026",
        "bg_bottom": "#141C36",
        "line": "#2A3A6B",
        "line_soft": "#1D2A52",
        "text": "#F5F0E6",
        "muted": "#9AA3B5",
        "dim": "#6E7893",
        "gold": "#C9A86A",
        "gold_bright": "#E4C87F",
        "sub": "#7C87A3",
        "star": "#F5F0E6",
        "star_op": 0.35,
        "row_sub": "#D5DAE4",
        "panel": "#0E1530",
        "panel_top": "#16204A",
        "nebula": "#2B4B9E",
        "neb_op_g": 0.16,
        "neb_op_b": 0.22,
        "glow_op": 0.10,
        "grain": "#FFFFFF",
        "fil_op": 0.05,
        "edge_op": 0.20,
    },
    "light": {
        "bg_top": "#FFFFFF",
        "bg_mid": "#FBF9F4",
        "bg_bottom": "#F4F1EA",
        "line": "#E5DFD2",
        "line_soft": "#EDE7DA",
        "text": "#16213E",
        "muted": "#5F6B7F",
        "dim": "#8A93A6",
        "gold": "#B08D3E",
        "gold_bright": "#8F6F2C",
        "sub": "#8A93A6",
        "star": "#C9A86A",
        "star_op": 0.16,
        "row_sub": "#3C4858",
        "panel": "#FFFFFF",
        "panel_top": "#FDFCF8",
        "nebula": "#DCCBA8",
        "neb_op_g": 0.14,
        "neb_op_b": 0.20,
        "glow_op": 0.06,
        "grain": "#8F6F2C",
        "fil_op": 0.035,
        "edge_op": 0.20,
    },
    "rose": {
        # Rose Gold — warm ivory paper, rosy gilding
        "bg_top": "#FFF9F6",
        "bg_mid": "#FDF2EC",
        "bg_bottom": "#F6E7DE",
        "line": "#EBD3C6",
        "line_soft": "#F3E2D8",
        "text": "#4A2C33",
        "muted": "#8A6A6F",
        "dim": "#B2959A",
        "gold": "#C98A7A",
        "gold_bright": "#E0A992",
        "sub": "#A0807F",
        "star": "#C98A7A",
        "star_op": 0.18,
        "row_sub": "#5C3D42",
        "panel": "#FFFCFA",
        "panel_top": "#FCEFE8",
        "nebula": "#E8B8A6",
        "neb_op_g": 0.16,
        "neb_op_b": 0.18,
        "glow_op": 0.08,
        "grain": "#C98A7A",
        "fil_op": 0.045,
        "edge_op": 0.20,
    },
    "ocean": {
        # Deep Sea — cold navy-teal, moonlight silver-blue gilding
        "bg_top": "#04101C",
        "bg_mid": "#071828",
        "bg_bottom": "#0E2B3E",
        "line": "#1E4457",
        "line_soft": "#143244",
        "text": "#EAF4F7",
        "muted": "#93AFBB",
        "dim": "#6E8B97",
        "gold": "#7FB6C9",
        "gold_bright": "#C4E3EE",
        "sub": "#7C97A3",
        "star": "#EAF4F7",
        "star_op": 0.35,
        "row_sub": "#CFE3EA",
        "panel": "#0A2030",
        "panel_top": "#12354A",
        "nebula": "#3E7E96",
        "neb_op_g": 0.20,
        "neb_op_b": 0.18,
        "glow_op": 0.12,
        "grain": "#FFFFFF",
        "fil_op": 0.05,
        "edge_op": 0.22,
    },
}

# aliases for backward-compatible reads inside generators that still use
# module-level tokens (each generator should switch to pal[...] eventually)
BG = PALETTES["dark"]["bg_top"]
CARD = PALETTES["dark"]["bg_bottom"]
LINE = PALETTES["dark"]["line"]
TEXT = PALETTES["dark"]["text"]
MUTED = PALETTES["dark"]["muted"]
DIM = PALETTES["dark"]["dim"]
GOLD = PALETTES["dark"]["gold"]
GOLD_BRIGHT = PALETTES["dark"]["gold_bright"]


def palette(name):
    """Return the palette dict for a theme name; unknown -> dark."""
    key = (name or "").strip().lower()
    return PALETTES.get(key, PALETTES["dark"])


def esc(s):
    """XML-escape a string for safe embedding in SVG."""
    return sax.escape(s, {'"': "&quot;"})


# --------------------------------------------------------------------------
# starfield & card background
# --------------------------------------------------------------------------
STARS = [
    (24, 30, 1.4), (47, 74, 1.1), (72, 28, 1.5), (95, 58, 1.2), (121, 88, 1.0),
    (148, 42, 1.3), (172, 70, 1.1), (196, 32, 1.5), (221, 64, 1.2), (247, 24, 1.0),
    (269, 82, 1.4), (294, 46, 1.1), (318, 26, 1.5), (343, 76, 1.2), (369, 52, 1.0),
    (394, 34, 1.4), (419, 72, 1.1), (445, 28, 1.5), (471, 60, 1.2), (495, 40, 1.0),
    (522, 78, 1.4), (546, 30, 1.1), (572, 64, 1.5), (597, 44, 1.2), (622, 34, 1.0),
    (34, 116, 1.0), (88, 108, 1.3), (141, 122, 1.1), (197, 106, 1.4), (252, 118, 1.0),
    (307, 108, 1.3), (364, 124, 1.1), (421, 104, 1.4), (478, 120, 1.0), (536, 110, 1.3),
    (596, 122, 1.1), (26, 164, 1.2), (79, 150, 1.0), (131, 174, 1.3), (186, 158, 1.1),
    (240, 170, 1.2), (296, 152, 1.0), (351, 176, 1.3), (406, 162, 1.1), (462, 172, 1.2),
    (518, 156, 1.0), (574, 168, 1.3), (622, 150, 1.1), (31, 210, 1.1), (83, 224, 1.4),
    (138, 206, 1.0), (193, 222, 1.2), (248, 210, 1.1), (303, 226, 1.4), (358, 208, 1.0),
    (413, 224, 1.2), (468, 212, 1.1), (524, 228, 1.4), (578, 214, 1.0), (631, 220, 1.2),
    (28, 262, 1.3), (82, 278, 1.1), (136, 260, 1.2), (191, 276, 1.0), (246, 264, 1.3),
    (301, 280, 1.1), (356, 262, 1.2), (411, 278, 1.0), (466, 266, 1.3), (521, 282, 1.1),
    (576, 264, 1.2), (631, 278, 1.0), (35, 316, 1.0), (89, 330, 1.2), (144, 318, 1.1),
    (199, 332, 1.3), (254, 320, 1.0), (309, 334, 1.2), (364, 322, 1.1), (419, 336, 1.3),
    (474, 324, 1.0), (529, 338, 1.2), (584, 326, 1.1), (37, 372, 1.2), (92, 388, 1.0),
    (147, 376, 1.3), (202, 390, 1.1), (257, 378, 1.2), (312, 392, 1.0), (367, 380, 1.3),
    (422, 394, 1.1), (477, 382, 1.2), (532, 396, 1.0), (587, 384, 1.3),
]

# a few 4-ray sparkles scattered among the dots
SPARKLES = [
    (86, 46, 5), (238, 150, 4), (404, 62, 6), (556, 196, 4), (120, 300, 5),
    (492, 330, 4), (316, 52, 4), (66, 240, 4),
]


def sparkle(cx, cy, r, color, op=0.55):
    """4-ray twinkle (two crossed lines, round caps) + centre dot."""
    return (
        '<path d="M%.1f %.1f H%.1f M%.1f %.1f V%.1f" stroke="%s" stroke-width="1" '
        'stroke-linecap="round" opacity="%s"/>'
        '<circle cx="%.1f" cy="%.1f" r="1.1" fill="%s" opacity="%s"/>'
        % (cx - r, cy, cx + r, cx, cy - r, cy + r, color, op, cx, cy, color, op)
    )


def microdots(w, h, pal):
    """Film-grain dots: ~72 sub-pixel specks, very low opacity."""
    rnd = random.Random(20260924)
    out = []
    for _ in range(72):
        x = rnd.uniform(6, w - 6)
        y = rnd.uniform(6, h - 6)
        r = rnd.choice([0.4, 0.5, 0.6])
        op = rnd.uniform(0.035, 0.085)
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.3f"/>' % (x, y, r, pal["grain"], op))
    return "".join(out)


def filigree(pal, uid="1"):
    """Diamond brocade lattice — fine gold filigree at very low opacity.
    A quiet 'woven metal' texture under the starfield, so cards never feel
    flat or empty while numbers stay the loudest element."""
    cell = 26.0
    h2 = cell / 2.0
    op = pal.get("fil_op", 0.045)
    g = pal["gold"]
    return (
        '<pattern id="fil%s" width="%.1f" height="%.1f" patternUnits="userSpaceOnUse">'
        '<path d="M%.1f 0 L%.1f %.1f L%.1f %.1f L0 %.1f Z" fill="none" stroke="%s" stroke-width="0.5" opacity="%s"/>'
        '<circle cx="%.1f" cy="%.1f" r="0.55" fill="%s" opacity="%s"/>'
        '<circle cx="0" cy="0" r="0.35" fill="%s" opacity="%s"/>'
        '</pattern>'
        % (uid, cell, h2, h2, cell, h2, h2, cell, h2, g, op, h2, h2, g, op * 1.6, g, op)
    )


def edge_marks(w, h, pal):
    """Postcard letterpress edges — hairline marquee bands along the top and
    bottom, plus vertical monograms on the sides when the card is tall enough.

    Natural glyph widths are measured (chromium) once: ~179px per horizontal
    repeat, ~63px per vertical repeat at font-size 5.5. Repeat counts are
    derived from the band length so textLength only ever *gently* letter-spaces
    (never squeezes glyphs into overlapping blobs); vertical columns keep
    natural spacing, are vertically centered, and are skipped on cards too
    short to fit even one repeat.
    """
    g = pal["gold"]
    op = pal.get("edge_op", 0.18) * 0.7  # keep it a whisper, not noise
    top = "P R O F I L E   V E R S E   \u2726   \u661f\u591c\u9381\u91d1   \u2726   ZERO SERVER   \u2726   GITHUB API   \u2726"
    bot = "R E A L   D A T A   \u2726   MIT LICENSE   \u2726   \u6bcf\u65e5\u81ea\u52a8\u5237\u65b0   \u2726   \u96f6\u670d\u52a1\u5668   \u2726"
    mon = "P R O F I L E   V E R S E   \u2726   "
    nat_h = 179.0
    nat_v = 63.0
    bw = w - 52
    nh = max(1, int(bw / nat_h))
    out = (
        '<text x="26" y="9" font-family="%s" font-size="5.5" fill="%s" opacity="%s" textLength="%d">%s</text>'
        '<text x="26" y="%d" font-family="%s" font-size="5.5" fill="%s" opacity="%s" textLength="%d">%s</text>'
        % (FONT, g, op, bw, top * nh, h - 10, FONT, g, op, bw, bot * nh)
    )
    bh = h - 52
    nv = max(0, int(bh / nat_v))
    if nv >= 1:
        span = nv * nat_v
        y0 = int(h - 26 - (bh - span) / 2)      # vertically center the column
        text = mon * nv
        for x in (8, w - 12):
            out += (
                '<text x="%d" y="%d" font-family="%s" font-size="5.5" fill="%s" opacity="%s" '
                'transform="rotate(-90 %d %d)">%s</text>'
                % (x, y0, FONT, g, op, x, y0, text)
            )
    return out


def corner_marks(w, h, pal, ln=11):
    """Four thin gold L-shaped corner ticks + inner diamond studs — the
    'framed print' detail."""
    g = pal["gold"]
    return (
        '<path d="M%.1f %.1f h%d M%.1f %.1f v%d" fill="none" stroke="%s" stroke-width="1" opacity="0.6"/>'
        '<path d="M%.1f %.1f h%d M%.1f %.1f v%d" fill="none" stroke="%s" stroke-width="1" opacity="0.6"/>'
        '<path d="M%.1f %.1f h%d M%.1f %.1f v%d" fill="none" stroke="%s" stroke-width="1" opacity="0.6"/>'
        '<path d="M%.1f %.1f h%d M%.1f %.1f v%d" fill="none" stroke="%s" stroke-width="1" opacity="0.6"/>'
        '<path d="M%.1f %.1f l2.4 -2.4 l2.4 2.4 l-2.4 2.4 z" fill="none" stroke="%s" stroke-width="0.7" opacity="0.5"/>'
        '<path d="M%.1f %.1f l2.4 -2.4 l2.4 2.4 l-2.4 2.4 z" fill="none" stroke="%s" stroke-width="0.7" opacity="0.5"/>'
        '<path d="M%.1f %.1f l2.4 -2.4 l2.4 2.4 l-2.4 2.4 z" fill="none" stroke="%s" stroke-width="0.7" opacity="0.5"/>'
        '<path d="M%.1f %.1f l2.4 -2.4 l2.4 2.4 l-2.4 2.4 z" fill="none" stroke="%s" stroke-width="0.7" opacity="0.5"/>'
        % (
            10.5, 10.5, ln, 10.5, 10.5, ln, g,
            w - 10.5 - ln, 10.5, ln, w - 10.5, 10.5, ln, g,
            10.5, h - 10.5 - ln, ln, 10.5, h - 10.5, ln, g,
            w - 10.5 - ln, h - 10.5 - ln, ln, w - 10.5, h - 10.5, ln, g,
            22.5, 22.5, g,
            w - 22.5, 22.5, g,
            22.5, h - 22.5, g,
            w - 22.5, h - 22.5, g,
        )
    )


def starfield(pal, w, h):
    """Star-dot field + a few sparkles, sized to (w, h)."""
    dots = []
    for x, y, r in STARS:
        if x < w - 4 and y < h - 4:
            dots.append('<circle cx="%d" cy="%d" r="%g" fill="%s" opacity="%s"/>' % (x, y, r, pal["star"], pal["star_op"]))
    for x, y, r in SPARKLES:
        if x < w - 6 and y < h - 6:
            dots.append(sparkle(x, y, r, pal["star"], 0.5))
    return "".join(dots)


def num_gradient(pal, uid="1"):
    """Gold gradient for hero numbers / titles."""
    return (
        '<linearGradient id="gt%s" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
        '</linearGradient>' % (uid, pal["gold_bright"], pal["gold"])
    )


def card_bg(pal, w, h):
    """Full background: 3-stop sky + gold/blue nebulas + gold brocade + starfield
    + grain + double hairline frame + gold corner ticks.  id="bg"/"glow" stay
    stable so existing components that reference url(#glow) keep working."""
    return (
        '<defs>'
        '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset="0.5" stop-color="%s"/>'
        '<stop offset="1" stop-color="%s"/>'
        '</linearGradient>'
        '<radialGradient id="nebG" cx="0.84" cy="0.10" r="0.62">'
        '<stop offset="0" stop-color="%s" stop-opacity="%s"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/>'
        '</radialGradient>'
        '<radialGradient id="nebB" cx="0.10" cy="0.92" r="0.60">'
        '<stop offset="0" stop-color="%s" stop-opacity="%s"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/>'
        '</radialGradient>'
        '<radialGradient id="glow" cx="0.5" cy="0.42" r="0.72">'
        '<stop offset="0" stop-color="%s" stop-opacity="%s"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/>'
        '</radialGradient>'
        '%s'
        '</defs>'
        '<rect width="%d" height="%d" fill="url(#bg)"/>'
        '<rect width="%d" height="%d" fill="url(#nebG)"/>'
        '<rect width="%d" height="%d" fill="url(#nebB)"/>'
        '<rect width="%d" height="%d" fill="url(#glow)"/>'
        '<rect width="%d" height="%d" fill="url(#fil1)"/>'
        '%s'
        '%s'
        '<rect x="0.5" y="0.5" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1"/>'
        '<rect x="2.5" y="2.5" width="%d" height="%d" fill="none" stroke="%s" stroke-width="0.6" opacity="0.55"/>'
        '%s'
        '%s'
        % (
            pal["bg_top"], pal.get("bg_mid", pal["bg_top"]), pal["bg_bottom"],
            pal["gold"], pal.get("neb_op_g", 0.16), pal["bg_top"],
            pal.get("nebula", "#2B4B9E"), pal.get("neb_op_b", 0.22), pal["bg_top"],
            pal["gold"], pal.get("glow_op", 0.10), pal["bg_top"],
            filigree(pal),
            w, h, w, h, w, h, w, h, w, h,
            starfield(pal, w, h),
            microdots(w, h, pal),
            w - 1, h - 1, pal["line"],
            w - 5, h - 5, pal.get("line_soft", pal["line"]),
            edge_marks(w, h, pal),
            corner_marks(w, h, pal),
        )
    )


# --------------------------------------------------------------------------
# star tiering for impact-card (same across themes)
# --------------------------------------------------------------------------
TIERS = [
    ("S", 50000, "\u226550k\u2605", "#C9A86A", "#E4C87F"),
    ("A", 10000, "\u226510k\u2605", "#5B8DEF", "#8FB4F5"),
    ("B", 1000, "\u22651k\u2605", "#4EC9A0", "#7ED9B8"),
    ("C", 100, "\u2265100\u2605", "#B48AE8", "#C3A6EF"),
    ("D", 0, "<100\u2605", "#6E7893", "#B9C0CE"),
]

# GitHub-style language colors for tech-stack-card
LANGUAGE_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178C6", "JavaScript": "#F1E05A",
    "HTML": "#E34C26", "CSS": "#563D7C", "SCSS": "#C6538C", "Vue": "#41B883",
    "Java": "#B07219", "C": "#555555", "C++": "#F34B7D", "C#": "#178600",
    "Go": "#00ADD8", "Rust": "#DEA584", "Shell": "#89E051", "Markdown": "#083FA1",
    "Jupyter Notebook": "#DA5B0B", "PHP": "#4F5D95", "Ruby": "#701516",
    "Swift": "#F05138", "Kotlin": "#A97BFF", "Dart": "#00B4AB",
    "Dockerfile": "#384D54", "Makefile": "#427819", "Other": "#8B949E",
}


def lang_color(lang):
    return LANGUAGE_COLORS.get(lang, LANGUAGE_COLORS["Other"])
