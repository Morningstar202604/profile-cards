#!/usr/bin/env python3
"""Build the Profile Verse showcase images (walls + README hero).

Reads the per-card PNG renders (produced by scripts/shot.sh from the SVG
previews) and lays them out in a balanced two-column masonry on a themed
backdrop with a brand header strip.

Usage:
    SHOTS_DIR=<dir with <card>_<theme>.png> python3 scripts/build_showcase.py

Outputs:
    assets/showcase/wall-dark.png   — 10 cards · dark theme
    assets/showcase/wall-light.png  — 10 cards · light theme
    assets/hero-home.png            — banner + typing + 4 hero cards (dark)
"""

import os
from PIL import Image, ImageDraw, ImageFilter
import math

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
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

PALETTES = {
    "dark": {
        "bg_top": (7, 11, 30), "bg_bottom": (20, 28, 54),
        "text": (228, 200, 127), "sub": (148, 156, 176),
        "line": (42, 58, 107), "gold": (201, 168, 106),
        "star": (190, 200, 224),
    },
    "light": {
        "bg_top": (244, 241, 234), "bg_bottom": (255, 255, 255),
        "text": (176, 141, 62), "sub": (120, 124, 136),
        "line": (212, 202, 176), "gold": (176, 141, 62),
        "star": (140, 132, 120),
    },
}


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


def build_hero(out):
    theme = "dark"
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
    build_wall("dark", os.path.join(ROOT, "assets/showcase/wall-dark.png"))
    build_wall("light", os.path.join(ROOT, "assets/showcase/wall-light.png"))
    build_hero(os.path.join(ROOT, "assets/hero-home.png"))


if __name__ == "__main__":
    main()
