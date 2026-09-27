# Changelog

All notable changes to Profile Verse are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/lang/zh-CN/).

## [1.6.0] - 2026-09-28

### Added
- **projects-card** — new component: a 2×2 grid of project cards
  (name · description · language · stars) replacing the flat text list.
  Live from the GitHub REST API (top non-fork repos by stars), all seven
  themes, `count` input up to 8.

## [1.5.0] - 2026-09-28

### Added
- **Three new bright themes**: `aurora` (electric violet), `sunset` (coral orange),
  `mint` (fresh jade) — seven themes in total, every card renders every theme.
- Contribution-grid column ramp now derives from the palette accent, so new
  themes adapt automatically (zero config).
- README theme cheat-sheet & the brand name **ProfileVerse · 星卡**.

### Changed
- **Repo renamed to `profile-cards`** on all platforms (GitCode / GitHub ×2 /
  Gitee), synced to the same commit; old links 301-redirect.
- Design polish pass: unified 10.5px footer scale, larger hero numbers,
  orbit studs on stats, banner glow & type scale-up, streak copy fix,
  tech-stack constellation raised to avoid footer collision.
- Edge-marks watermark opacity lowered 30% (whisper, not noise).

### Fixed
- **Core**: no empty `Authorization: Bearer` header when no token — GitHub
  rejects an empty Bearer with 401, which broke every data card without a token.
- **README / example workflow**: banner-card quick-start used `name:` instead
  of the required `user:` input — the first step of the copy-paste workflow.
- **token guard**: REST cards (stats / impact / tech-stack) run anonymously;
  badge auto-mode degrades to 3 REST metrics without a token; GraphQL cards
  now explain why a token is required.
- **year-review-card**: unified core import (no double module), removed the
  embedded `actions/checkout` that reset the workspace mid-workflow, `python`
  → `python3`.
- update.yml now passes `token: ${{ github.token }}` explicitly to API cards.

## [1.4.1] - 2026-09-25

### Fixed
- **impact-card**: the "贡献分档 · 按仓库 star" heading no longer sits on the
  tier-box top edge — heading and diamond stud moved up 16px so the tiers read
  cleanly (visual polish pass caught by eyeball review).
- **year-review-card**: medal panel labels were touching the panel bottom
  edge; panels are 6px taller now, labels rest comfortably inside.
- **contrib-grid-card**: the footer line was long enough to collide with the
  "每日贡献" legend on the same row; shortened it so both sit apart.

## [1.4.0] - 2026-09-25

### Changed
- **One repo, one entry**: the standalone `contrib-grid-card` repository has
  been merged back into this monorepo. All nine cards now ship from
  `profile-verse` only — single `@v1`, single workflow. The old standalone
  repo is archived and its README redirects here.

## [1.3.1] - 2026-09-25

### Fixed
- **Postcard edges refined**: marquee repeat counts now use measured glyph
  widths so textLength only ever letter-spaces gently (no more squeezed
  overlapping glyphs); vertical monograms keep natural spacing, are vertically
  centered, and are skipped on cards too short to fit even one repeat.
- **banner-card** was missing the edge texture (own background builder) — the
  letterpress marquees + monograms are now applied there too.
- Light/Rose edge opacity raised (0.16/0.17 → 0.20) for a visible-but-subtle
  signature on paper.

## [1.3.0] - 2026-09-24

### Added
- **Two new themes**: `rose` (Rose Gold — warm ivory × rosy gilding) and
  `ocean` (Deep Sea — navy-teal × moonlight silver-blue), alongside `dark`
  (Midnight) and `light` (Ivory). One `theme:` input on every card.
- **Postcard letterpress edges**: every card now carries hairline edge
  marquees (top/bottom) and vertical monograms (left/right) —
  `PROFILE VERSE ✦ ZERO SERVER ✦ …` — like printed stationery.
- All 9 component action.yml `theme` descriptions updated to the four themes.

## [Unreleased]

### Added
- **Stargazer Wall** (`.github/workflows/star-wall.yml`) — a weekly issue that
  thanks every new star; stateless, API-driven, idempotent.
- **Standalone split** — `contrib-grid-card` extracted via `git subtree split`
  into [Morningstar202604/contrib-grid-card](https://github.com/Morningstar202604/contrib-grid-card)
  (own history, `@v1` refs, own topics). Pattern documented in README.

## [1.2.0] - 2026-09-24

### Added
- **year-review-card** — the 9th component: a golden annual ring (12 month-stars
  sized/brightened by real monthly contributions, halo on the peak month), the
  year's total glowing at the center, and four star-medals (peak month / longest
  streak / merged PRs / top language). Data from the 365-day contribution
  calendar + merged PRs + repo languages.
- Showcase walls rebuilt to 9 cards (dark + light).
- update.yml now refreshes **all 18 previews** (9 cards × dark/light) daily.

## [1.1.0] - 2026-09-24

### Added
- **Gold brocade texture layer** (`filigree()` in `core/theme.py`) — fine diamond lattice under the starfield, low opacity, on every card in both themes.
- **Inner hairline frame** (double-border framing) on all cards.
- **Corner diamond studs** inside the four gold L-shaped corner marks.
- **Semantic version footer** on every card (`banner-card · v1.1.0` … `impact-card · v1.1.0`).
- `core/theme.py` exports `VERSION` as the single design-system version source.
- `VERSIONING.md` — official release & reference rules (`@v1`, `@v1.1.0`, `@main`).
- `examples/profile-verse.yml` — copy-paste whole-homepage workflow.
- `assets/showcase/wall-dark.png` / `wall-light.png` — dual-theme showcase walls.
- CI workflow `.github/workflows/ci.yml` — regenerates all 16 previews + XML validation on every push/PR.

### Changed
- README rewritten (English primary) + README.zh.md, hero image, comparison table, badges.
- Repo metadata: description, homepage (live demo), 8 search topics.

## [1.0.0] - 2026-09-24

First stable release of the monorepo suite.

### Added
- 8 components: `impact-card`, `stats-card`, `streak-card`, `typing-card`,
  `contrib-grid-card`, `tech-stack-card`, `banner-card`, `badge-card`.
- Shared design system `core/`: GitHub API layer, contribution calendar,
  star tiers, dual-theme palettes (dark / light).
- 3-stop sky gradient, gold/blue nebulas, film grain, 4-ray sparkles,
  gradient numbers, gold corner ticks.
- GitHub Actions `action.yml` per component — zero-server generation.
- Daily auto-refresh workflow `update.yml` for the 16 previews.
- `git subtree split`-ready monorepo layout ("先合后拆").
- Live demo on [Morningstar202604 homepage](https://github.com/Morningstar202604/Morningstar202604).

[1.3.0]: https://github.com/Morningstar202604/profile-cards/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/Morningstar202604/profile-cards/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Morningstar202604/profile-cards/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Morningstar202604/profile-cards/releases/tag/v1.0.0

[1.5.0]: https://github.com/Morningstar202604/profile-cards/compare/v1.4.1...v1.5.0

[1.6.0]: https://github.com/Morningstar202604/profile-cards/compare/v1.5.0...v1.6.0
