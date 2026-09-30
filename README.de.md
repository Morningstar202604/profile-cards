<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/showcase/hero-home.png">
    <img src="assets/showcase/hero-light.png" alt="Profile Verse — Open-Source-GitHub-Profilkarten" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · Open-Source-GitHub-Profilkarten</h1>

<p align="center"><sub>**Profile Verse** ist die Marke &middot; dieses Repo heißt <code>profile-cards</code> — dasselbe Projekt, eine Familie.</sub></p>

<div align="center">

[English](README.md) &middot; [中文](README.zh.md) &middot; [日本語](README.ja.md) &middot; [Deutsch](README.de.md) &middot; [Español](README.es.md) &middot; [Français](README.fr.md) &middot; [한국어](README.ko.md)

</div>

<p align="center">
  <a href="https://github.com/Morningstar202604/profile-cards/stargazers"><img src="https://img.shields.io/github/stars/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=stars" alt="GitHub stars" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/forks"><img src="https://img.shields.io/github/forks/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=forks" alt="GitHub forks" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/actions"><img src="https://img.shields.io/github/actions/workflow/status/Morningstar202604/profile-cards/update.yml?style=flat&color=%23C9A86A&label=previews" alt="daily preview refresh" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Morningstar202604/profile-cards?style=flat&color=%23C9A86A" alt="MIT license" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/releases"><img src="https://img.shields.io/github/v/release/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=version" alt="v1.6.0" /></a>
  <img src="https://img.shields.io/badge/SVG-100%25-C9A86A?style=flat" alt="pure SVG, zero server" />
</p>

> ⭐ **Dir gefällt das Projekt? Gib einen Star** — ein Klick, und die Karten bleiben für immer kostenlos.

**Profile Verse** verwandelt ein schlichtes GitHub-Profil in eine **sternklare, datengetriebene Showcase-Seite**: 10 Open-Source-**SVG-Karten** — Typing-Header, Statistiken, Streak, 3D-Beitragsdiagramm, Tech-Stack, goldene Badges, Projekte, Open-Source-Impact, Jahresrückblick, Banner — kostenlos erzeugt von **GitHub Actions**, **täglich aktualisiert** mit **echten GitHub-API-Daten**, in **7 Farbthemen** (dunkel & hell). Eine Workflow-Datei, Copy & Paste, keine Server, null Kosten. [Live-Demo](https://github.com/Morningstar202604/Morningstar202604) — die Karten laufen heute auf einer echten Homepage.

## ✨ Features

- **10 Karten, eine Designsprache** — Typing · Statistiken · Streak · Beiträge · Tech-Stack · Badges · Projekte · Impact · Jahresrückblick · Banner
- **7 Signatur-Themes** — `dark` `light` `rose` `ocean` `aurora` `sunset` `mint`; jede Karte in jedem Theme
- **100% echte Daten** — GitHub-REST-API + Contribution-Kalender; jede Karte nennt Quelle & Aktualisierungszeit
- **$0 für immer** — reines SVG, generiert von kostenloser GitHub Actions; kein Server, keine Datenbank, keine Kreditkarte
- **Täglich automatisch aktualisiert** — Zahlen werden nie alt; jederzeit manuell via `workflow_dispatch` mit Theme-Auswahl
- **Setup mit einer Datei** — eine Workflow-Datei ins Profil-Repo kopieren, fertig
- **Dunkel/Hell automatisch** — `<picture>` folgt dem System-Theme des Besuchers
- **Fork & fertig** — `${{ github.repository_owner }}` zeigt in Forks automatisch *deine* Daten

## ✨ Why


| | Profile Verse | Übliche Lösungen |
|---|---|---|
| **Look** | Eine Designsprache (Sternennacht × Gold), jede Karte mit eigenem Charakter | Einheitsbalken wie überall |
| **Themes** | 7 Themes | Nur dunkel, oder hell kaputt |
| **Daten** | Echte GitHub-API-Daten mit Quelle & Zeitstempel | Statische Schnappschüsse / Fake-Zahlen |
| **Kosten** | Für immer $0 (SVG via kostenloser Actions) | Bezahl-APIs, eigene Server |

## 🚀 クイックスタート / Quick start

Füge diese eine Workflow-Datei zu deinem Profil-Repo hinzu (`.github/workflows/profile-verse.yml`) — alle 10 Karten erscheinen auf deiner Homepage und aktualisieren sich täglich.

### 🎨 Themes

| Theme | Style | Vibe |
|---|---|---|
| `dark` | Mitternachtsblau × Gold | Sternennacht, Standard |
| `light` | Elfenbeinpapier × Antikgold | clean & klassisch |
| `rose` | Rosé-Ivory × Roségold | weich & romantisch |
| `ocean` | Tiefseegrün × Mondlichtsilber | kühl & tief |
| `aurora` | Leuchtviolett × Elektroviolett | träumerisch & hell |
| `sunset` | Warmcreme × Korallenorange | energisch & warm |
| `mint` | Frisches Jade × Teal | frisch & klar |

```yaml
name: Profile Verse Cards

on:
  schedule:
    - cron: "10 1 * * *"
  workflow_dispatch:
    inputs:
      theme:
        description: dark or light
        default: dark

permissions:
  contents: write

concurrency:
  group: profile-verse
  cancel-in-progress: true

jobs:
  cards:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4

      - name: Banner
        uses: Morningstar202604/profile-cards/components/banner-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/banner-card.svg
          theme: ${{ inputs.theme }}

      - name: Typing
        uses: Morningstar202604/profile-cards/components/typing-card@v1
        with:
          phrases: "Hello, I am a developer;Code under the stars"
          output: assets/profile-verse/typing-card.svg
          theme: ${{ inputs.theme }}

      - name: Stats
        uses: Morningstar202604/profile-cards/components/stats-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/stats-card.svg
          theme: ${{ inputs.theme }}

      - name: Streak
        uses: Morningstar202604/profile-cards/components/streak-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/streak-card.svg
          theme: ${{ inputs.theme }}

      - name: Contribution grid (3D)
        uses: Morningstar202604/profile-cards/components/contrib-grid-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/contrib-grid-card.svg
          theme: ${{ inputs.theme }}

      - name: Tech stack
        uses: Morningstar202604/profile-cards/components/tech-stack-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/tech-stack-card.svg
          theme: ${{ inputs.theme }}

      - name: Badges
        uses: Morningstar202604/profile-cards/components/badge-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/badge-card.svg
          theme: ${{ inputs.theme }}

      - name: Projects (2×2 grid)
        uses: Morningstar202604/profile-cards/components/projects-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/projects-card.svg
          theme: ${{ inputs.theme }}

      - name: Impact (merged PRs by repo star tiers)
        uses: Morningstar202604/profile-cards/components/impact-card@v1
        with:
          users: your-github-username        # multi-account: a,b
          output: assets/profile-verse/impact-card.svg
          theme: ${{ inputs.theme }}

      - name: Year review (annual ring)
        uses: Morningstar202604/profile-cards/components/year-review-card@v1
        with:
          user: your-github-username
          output: assets/profile-verse/year-review-card.svg
          theme: ${{ inputs.theme }}

      - name: Commit & push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/profile-verse
          if git diff --cached --quiet; then echo "no changes"; else
            git commit -m "chore: refresh profile-verse cards [skip ci]"
            git pull --rebase origin main || git rebase --abort
            git push
          fi
```

## 🗂 Kartenübersicht — 10 Karten × 2 Themes

Jede Karte gibt es in **dunkel** (Sternennacht) und **hell** (Papier).

| Card | Description | Previews |
|---|---|---|
| [`impact-card`](components/impact-card/) | Gemergte PRs, bewertet nach den Star-Tiers der Repos — der «Goldgehalt» deines Profils | ![preview](components/impact-card/preview/impact-card.svg) · ![light](components/impact-card/preview/impact-card-light.svg) |
| [`stats-card`](components/stats-card/) | Minimale Statistiken: Follower / öffentliche Repos / gemergte PRs auf goldener Umlaufbahn | ![preview](components/stats-card/preview/stats-card.svg) · ![light](components/stats-card/preview/stats-card-light.svg) |
| [`streak-card`](components/streak-card/) | Dein aktueller Streak als heller Stern im Zentrum einer 60-Takt-Skala | ![preview](components/streak-card/preview/streak-card.svg) · ![light](components/streak-card/preview/streak-card-light.svg) |
| [`typing-card`](components/typing-card/) | Deine Tagline tippt sich unter Sternen mit blinkendem Gold-Cursor (reines SVG + SMIL) | ![preview](components/typing-card/preview/typing-card.svg) · ![light](components/typing-card/preview/typing-card-light.svg) |
| [`contrib-grid-card`](components/contrib-grid-card/) | Isometrisches goldenes Beitragsdiagramm (53 Wochen, fünf Gold-Tiers) | ![preview](components/contrib-grid-card/preview/contrib-grid-card.svg) · ![light](components/contrib-grid-card/preview/contrib-grid-card-light.svg) |
| [`tech-stack-card`](components/tech-stack-card/) | Deine Hauptsprache als Zentralstern, andere kreisen auf goldenen Ellipsen | ![preview](components/tech-stack-card/preview/tech-stack-card.svg) · ![light](components/tech-stack-card/preview/tech-stack-card-light.svg) |
| [`banner-card`](components/banner-card/) | Leuchtender Name, Gradient-Text, Kometenspuren (rein visuell) | ![preview](components/banner-card/preview/banner-card.svg) · ![light](components/banner-card/preview/banner-card-light.svg) |
| [`badge-card`](components/badge-card/) | Eine Reihe goldener Medaillen statt flacher shields (echte Daten oder frei anpassbar) | ![preview](components/badge-card/preview/badge-card.svg) · ![light](components/badge-card/preview/badge-card-light.svg) |
| [`year-review-card`](components/year-review-card/) | 12 Monate umkreisen einen goldenen Ring — Jahresbilanz + vier Sternmedaillen | ![preview](components/year-review-card/preview/year-review-card.svg) · ![light](components/year-review-card/preview/year-review-card-light.svg) |
| [`projects-card`](components/projects-card/) | Deine Top-Nicht-Fork-Repos nach Stars in einem 2×2-Raster | ![preview](components/projects-card/preview/projects-card.svg) · ![light](components/projects-card/preview/projects-card-light.svg) |

## 🔄 Showcase

Die Familien-Showcase (`assets/showcase/wall-*.png` & `assets/hero-*.png`) wird täglich um 01:00 UTC von **GitHub Actions** neu gebaut — alle Zahlen sind echte GitHub-API-Daten.

---

Details (Galerie aller 10 Karten, Anpassung, Design-System) im **[English README](README.md)**.

⭐ **Gib dem Projekt einen Star!**

## 📜 License

MIT © Morningstar202604
