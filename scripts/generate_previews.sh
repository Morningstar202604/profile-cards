#!/usr/bin/env bash
# Generate all 10 card preview SVGs in one theme and render them to PNGs
# (inputs for scripts/build_showcase.py). Used by update.yml when a manual
# run asks for a non-dark/light theme.
#
# Usage:
#   THEME=rose [USER=<github name>] [GH_TOKEN=<token>] bash scripts/generate_previews.sh
#   THEME=all   bash scripts/generate_previews.sh        # all seven themes
#
# Outputs (temp dirs, never committed):
#   /tmp/previews-<theme>/<card>.svg     — generated preview SVGs
#   $SHOTS_DIR/<card>_<theme>.png        — rendered PNGs (default /tmp/shots)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
THEME="${THEME:-dark}"
USERNAME="${USER:-Morningstar202604}"
SHOTS="${SHOTS_DIR:-/tmp/shots}"
CARDS="impact-card stats-card streak-card typing-card contrib-grid-card tech-stack-card banner-card badge-card year-review-card projects-card"

export GH_TOKEN="${GH_TOKEN:-}"

render_png() { # $1 svg  $2 out
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

gen_one() { # $1 theme
  local t="$1"
  local dir="/tmp/previews-$t"
  mkdir -p "$dir" "$SHOTS"
  export THEME="$t"
  for card in $CARDS; do
    local script="generate_$(echo "$card" | tr '-' '_').py"
    export OUTPUT="$dir/$card.svg"
    export USER="$USERNAME"
    case "$card" in
      impact-card) export USERS="${USERS:-$USERNAME}" ;;
      typing-card) export PHRASES="${PHRASES:-Hello, I am a developer;Code under the stars}" ;;
      banner-card) export TEXT="${TEXT:-$USERNAME}" ;;
      *) ;;
    esac
    python3 "$ROOT/components/$card/$script"
  done
  for card in $CARDS; do
    render_png "$dir/$card.svg" "$SHOTS/${card}_$t.png"
  done
  echo "previews + PNGs ready for theme $t"
}

if [ "$THEME" = "all" ]; then
  for t in dark light rose ocean aurora sunset mint; do gen_one "$t"; done
else
  gen_one "$THEME"
fi
