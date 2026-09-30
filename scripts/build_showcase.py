#!/usr/bin/env python3
"""Build the Profile Verse showcase images (walls + README hero).

Reads the per-card PNG renders (produced by scripts/shot.sh from the SVG
previews) and lays them out in a balanced two-column masonry on a themed
backdrop with a brand header strip.

Usage:
    SHOTS_DIR=<dir with <card>_<theme>.png> python3 scripts/build_showcase.py
    THEME=all    python3 scripts/build_showcase.py   # all seven themes
    THEME=rose   python3 scripts/build_showcase.py   # single theme

Themes (from core/theme.py): dark · light · rose · ocean · aurora · sunset · mint.
Default when THEME is unset: dark + light (the classic pair).

Outputs (per selected theme T):
    assets/showcase/wall-T.png      — 10 cards · theme T
    assets/showcase/hero-T.png      — banner + typing + hero cards · theme T
    assets/showcase/hero-home.png   — alias of the dark hero (README header)
"""

import os
import sys
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from PIL import Image, ImageDraw, ImageFilter  # noqa: E402
from core.theme import PALETTES as THEME_PALETTES  # noqa: E402
import math  # noqa: E402

SHOTS = os.environ.get("SHOTS_DIR", "/tmp/fin")

CARD_W = 520          # readable gallery width
GAP = 30              # base inter-card gap
PAD = 44              # wall padding
HEADER_H = 118        # brand strip height

CARDS = [
    "impact-card", "year-review-card", "stats-card", "banner-card",
    "contrib-grid-card", "tech-stack-card", "streak-card", "badge-card",
    "typing-card", "projects-card",
]

# Two balanced columns (heights at CARD_W: 884/552/487/390/244 vs 777/585/585/280/195)
COL1 = ["impact-card", "year-review-card", "stats-card", "banner-card", "projects-card"]
COL2 = ["contrib-grid-card", "tech-stack-card", "streak-card", "badge-card", "typing-card"]

# Palettes come straight from core/theme.py so every theme (dark/light/rose/
# ocean/aurora/sunset/mint) gets a matching wall & hero backdrop automatically.
_NEEDED = ("bg_top", "bg_bottom", "text", "sub", "line", "gold", "star")


def _rgb(hexv):
    hexv = hexv.lstrip("#")
    return tuple(int(hexv[i:i + 2], 16) for i in (0, 2, 4))


PALETTES = {
    name: {k: _rgb(pal[k]) for k in _NEEDED}
    for name, pal in THEME_PALETTES.items()
}
THEMES = list(PALETTES.keys())


def wanted_themes():
    raw = (os.environ.get("THEME") or (sys.argv[1] if len(sys.argv) > 1 else "") or "").strip().lower()
    if not raw:
        return ["dark", "light"]
    if raw == "all":
        return THEMES
    out = []
    for t in raw.replace(",", " ").split():
        if t in PALETTES and t not in out:
            out.append(t)
    return out


def load_card(name, theme, w):
    im = Image.open(os.path.join(SHOTS, "%s_%s.png" % (name, theme))).convert("RGB")
    ow, oh = im.size
    h = int(round(oh * w / ow))
    return im.resize((w, h), Image.LANCZOS)


def backdrop(w, h, pal):
    img = Image.new("RGB", (w, h), pal["bg_top"])
    grad = Image.new("L", (1, h))
    for y in range(h):
        t = y / max(h - 1, 1)
        grad.putpixel((0, y), int(255 * (0.65 + 0.35 * t)))
    img = Image.composite(Image.new("RGB", (w, h), pal["bg_bottom"]), img, grad.resize((w, h)))
    # soft vignette — only edges get a gentle darkening, centre untouched
    vig = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(vig)
    d.ellipse((-w * 0.30, -h * 0.30, w * 1.30, h * 1.30), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(180))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    img = Image.composite(dark, img, vig.point(lambda p: int((255 - p) * 0.5)))
    # faint starfield
    import random
    rnd = random.Random(7)
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(ov)
    for _ in range(int(w * h / 2200)):
        x, y = rnd.randint(0, w - 1), rnd.randint(0, h - 1)
        r = rnd.choice([1, 1, 1, 2])
        a = rnd.randint(12, 34)
        d2.ellipse((x - r, y - r, x + r, y + r), fill=pal["star"] + (a,))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    return img


def draw_header(img, theme):
    w, h = img.size
    pal = PALETTES[theme]
    d = ImageDraw.Draw(img, "RGBA")
    # wordmark
    word = "P R O F I L E   V E R S E"
    tw = 0
    font = None
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font = ImageFont.load_default()
    # measure roughly with default if dejavu missing
    if font is not None:
        try:
            tw = d.textlength(word, font=font)
        except Exception:
            tw = len(word) * 15
    d.text(((w - tw) / 2, HEADER_H / 2 - 22), word, font=font, fill=pal["text"] + (255,))
    sub = "10 C A R D S  ·  R E A L   D A T A  ·  D A I L Y   R E F R E S H  ·  Z E R O   S E R V E R"
    try:
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except Exception:
        f2 = ImageFont.load_default()
    sw = d.textlength(sub, font=f2)
    d.text(((w - sw) / 2, HEADER_H / 2 + 10), sub, font=f2, fill=pal["sub"] + (220,))
    # divider
    d.line((PAD, HEADER_H - 8, w - PAD, HEADER_H - 8), fill=pal["line"] + (160,), width=1)
    # gold tick at divider centre
    d.line(((w - 120) / 2, HEADER_H - 11, (w + 120) / 2, HEADER_H - 11), fill=pal["gold"] + (220,), width=2)


def build_wall(theme, out):
    pal = PALETTES[theme]
    col1 = [(c, load_card(c, theme, CARD_W)) for c in COL1]
    col2 = [(c, load_card(c, theme, CARD_W)) for c in COL2]
    h1 = sum(im.height for _, im in col1) + GAP * (len(col1) - 1)
    h2 = sum(im.height for _, im in col2) + GAP * (len(col2) - 1)
    H = max(h1, h2)
    total_w = PAD * 2 + CARD_W * 2 + GAP
    total_h = HEADER_H + PAD * 2 + H
    img = backdrop(total_w, total_h, pal)
    draw_header(img, theme)
    y_base = HEADER_H + PAD
    for col, colh in ((col1, h1), (col2, h2)):
        gap = GAP + (H - colh) / (len(col) - 1) if len(col) > 1 else GAP
        y = y_base
        for _, im in col:
            x = PAD if col is col1 else PAD + CARD_W + GAP
            img.paste(im, (int(x), int(y)))
            y += im.height + gap
    img.save(out)
    print(out, img.size, "cols h:", h1, h2, "delta:", abs(h1 - h2))


def build_hero(out, theme):
    pal = PALETTES[theme]
    w = 1160
    banner = load_card("banner-card", theme, w)
    typing = load_card("typing-card", theme, w)
    h1 = [(c, load_card(c, theme, 560)) for c in ["impact-card", "streak-card", "stats-card"]]
    h2 = [(c, load_card(c, theme, 560)) for c in ["contrib-grid-card", "tech-stack-card", "year-review-card"]]
    col_h = lambda col: sum(im.height for _, im in col) + GAP * (len(col) - 1)
    H = max(col_h(h1), col_h(h2))
    total_h = HEADER_H + PAD + banner.height + 22 + typing.height + 26 + H + PAD
    img = backdrop(w, total_h, pal)
    draw_header(img, theme)
    y = HEADER_H + PAD
    img.paste(banner, (0, y)); y += banner.height + 22
    img.paste(typing, (0, y)); y += typing.height + 26
    for col in (h1, h2):
        gap = GAP + (H - col_h(col)) / (len(col) - 1)
        yy = y
        for _, im in col:
            x = PAD if col is h1 else PAD + 560 + GAP
            img.paste(im, (int(x), int(yy)))
            yy += im.height + gap
    img.save(out)
    print(out, img.size)


def main():
    themes = wanted_themes()
    if not themes:
        print("no valid themes; use THEME=dark|light|rose|ocean|aurora|sunset|mint|all")
        return 1
    for t in themes:
        build_wall(t, os.path.join(ROOT, "assets/showcase/wall-%s.png" % t))
        hero = os.path.join(ROOT, "assets/showcase/hero-%s.png" % t)
        build_hero(hero, t)
        if t == "dark":
            shutil.copy(hero, os.path.join(ROOT, "assets/showcase/hero-home.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
