#!/usr/bin/env bash
# Render every card preview SVG to a PNG (inputs for scripts/build_showcase.py).
#
# Uses rsvg-convert (librsvg2-bin) when available, falls back to ImageMagick.
# Output naming matches build_showcase.py: <card>_dark.png / <card>_light.png.
#
# Usage:
#   SHOTS_DIR=<dir> bash scripts/shot.sh          # default: /tmp/shots
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${SHOTS_DIR:-/tmp/shots}"
CARDS="badge-card banner-card contrib-grid-card impact-card projects-card stats-card streak-card tech-stack-card typing-card year-review-card"

mkdir -p "$OUT"

render() {
  local svg="$1" out="$2"
  local w h
  w="$(grep -oE '<svg[^>]*width="[0-9]+' "$svg" | head -1 | grep -oE '[0-9]+' || echo 640)"
  h="$(grep -oE '<svg[^>]*height="[0-9]+' "$svg" | head -1 | grep -oE '[0-9]+' || echo 480)"
  if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert -w "$w" -h "$h" "$svg" -o "$out"
  elif command -v convert >/dev/null 2>&1; then
    convert -background none "$svg" -resize "${w}x${h}!" "$out"
  else
    echo "error: no SVG renderer found (install librsvg2-bin or ImageMagick)" >&2
    exit 1
  fi
}

count=0
if [ -n "${PREVIEW_DIR:-}" ] && [ -n "${THEME:-}" ]; then
  # theme mode: a flat dir of <card>.svg files (from scripts/generate_previews.sh)
  for card in $CARDS; do
    render "$PREVIEW_DIR/$card.svg" "$OUT/${card}_${THEME}.png"
    count=$((count + 1))
  done
else
  # default mode: the committed dark/light previews in components/*/preview
  for card in $CARDS; do
    render "$ROOT/components/$card/preview/$card.svg" "$OUT/${card}_dark.png"
    render "$ROOT/components/$card/preview/$card-light.svg" "$OUT/${card}_light.png"
    count=$((count + 2))
  done
fi
echo "rendered $count PNGs -> $OUT"
