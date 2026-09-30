<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/showcase/hero-home.png">
    <img src="assets/showcase/hero-light.png" alt="Profile Verse — cartes de profil GitHub open source" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · Cartes de profil GitHub open source</h1>

<p align="center"><sub>**Profile Verse** est la marque &middot; ce dépôt s'appelle <code>profile-cards</code> — le même projet, une seule famille.</sub></p>

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

> ⭐ **Le projet vous plaît ? Laissez une étoile** — un clic, et les cartes restent gratuites pour toujours.

**Profile Verse** transforme un profil GitHub ordinaire en une **vitrine étoilée pilotée par les données** : 10 **cartes SVG** open source — en-tête machine à écrire, statistiques, série, grille 3D de contributions, stack technique, badges dorés, projets, impact open source, bilan annuel, bannière — générées gratuitement par **GitHub Actions**, **actualisées chaque jour** avec de **vraies données de l'API GitHub**, en **7 thèmes de couleur** (mode sombre & clair). Un fichier de workflow, copier-coller, zéro serveur, zéro coût. [Démo en direct](https://github.com/Morningstar202604/Morningstar202604) — les cartes tournent aujourd'hui sur une vraie page d'accueil.

## ✨ Features

- **10 cartes, un langage de design** — machine à écrire · stats · série · contributions · stack · badges · projets · impact · bilan annuel · bannière
- **7 thèmes signature** — `dark` `light` `rose` `ocean` `aurora` `sunset` `mint` ; chaque carte rend chaque thème
- **100% de données réelles** — API REST GitHub + calendrier de contributions ; chaque carte indique sa source et son horodatage
- **$0 pour toujours** — SVG pur généré par GitHub Actions gratuit ; pas de serveur, pas de base de données, pas de carte bancaire
- **Actualisation automatique quotidienne** — les chiffres ne vieillissent jamais ; relancez à tout moment via `workflow_dispatch` et choisissez un thème
- **Installation en un fichier** — copiez un workflow dans votre dépôt de profil et les 10 cartes apparaissent
- **Bascule sombre/clair automatique** — les blocs `<picture>` suivent le thème système du visiteur
- **Fork & c'est tout** — `${{ github.repository_owner }}` affiche automatiquement *vos* données dans les forks

## ✨ Why


| | Profile Verse | Solutions courantes |
|---|---|---|
| **Rendu** | Un langage de design (nuit étoilée × or), chaque carte avec une forme propre | Barres plates identiques partout |
| **Thèmes** | 7 thèmes | Sombre uniquement, ou cassé en clair |
| **Données** | Vraies données d'API GitHub, source et horodatage | Captures statiques ou faux chiffres |
| **Coût** | $0 pour toujours (SVG via Actions gratuites) | API payantes, serveurs auto-hébergés |

## 🚀 クイックスタート / Quick start

Ajoutez ce seul workflow à votre dépôt de profil (`.github/workflows/profile-verse.yml`) et les 10 cartes apparaissent sur votre page — actualisées chaque jour.

### 🎨 Thèmes

| Theme | Style | Vibe |
|---|---|---|
| `dark` | Bleu nuit × or | nuit étoilée, défaut |
| `light` | Papier ivoire × or ancien | propre et classique |
| `rose` | Ivoire rosé × or rose | doux et romantique |
| `ocean` | Vert sarcelle profond × argent lunaire | froid et profond |
| `aurora` | Violet éclatant × violet électrique | rêveur et lumineux |
| `sunset` | Crème chaleureuse × orange corail | énergique et chaleureux |
| `mint` | Jade frais × sarcelle | net et frais |

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

## 🗂 Galerie de cartes — 10 cartes × 2 thèmes

Chaque carte existe en **sombre** (nuit étoilée) et **claire** (papier).

| Card | Description | Previews |
|---|---|---|
| [`impact-card`](components/impact-card/) | Vos PR fusionnés valorisés par les paliers d'étoiles des dépôts — la « teneur en or » de votre profil | ![preview](components/impact-card/preview/impact-card.svg) · ![light](components/impact-card/preview/impact-card-light.svg) |
| [`stats-card`](components/stats-card/) | Stats minimales : followers / repos publics / PR fusionnés sur une orbite dorée | ![preview](components/stats-card/preview/stats-card.svg) · ![light](components/stats-card/preview/stats-card-light.svg) |
| [`streak-card`](components/streak-card/) | Votre série actuelle brille au centre d'un cadran à 60 graduations | ![preview](components/streak-card/preview/streak-card.svg) · ![light](components/streak-card/preview/streak-card-light.svg) |
| [`typing-card`](components/typing-card/) | Votre slogan se tape sous les étoiles avec un curseur doré clignotant (SVG pur + SMIL) | ![preview](components/typing-card/preview/typing-card.svg) · ![light](components/typing-card/preview/typing-card-light.svg) |
| [`contrib-grid-card`](components/contrib-grid-card/) | Grille isométrique dorée des contributions (53 semaines, cinq paliers d'or) | ![preview](components/contrib-grid-card/preview/contrib-grid-card.svg) · ![light](components/contrib-grid-card/preview/contrib-grid-card-light.svg) |
| [`tech-stack-card`](components/tech-stack-card/) | Votre langage principal est l'étoile centrale ; les autres orbitent en constellation | ![preview](components/tech-stack-card/preview/tech-stack-card.svg) · ![light](components/tech-stack-card/preview/tech-stack-card-light.svg) |
| [`banner-card`](components/banner-card/) | Nom lumineux, texte dégradé, traînées de comète (purement visuel) | ![preview](components/banner-card/preview/banner-card.svg) · ![light](components/banner-card/preview/banner-card-light.svg) |
| [`badge-card`](components/badge-card/) | Une rangée de médailles dorées au lieu des shields plats (données réelles ou entièrement personnalisables) | ![preview](components/badge-card/preview/badge-card.svg) · ![light](components/badge-card/preview/badge-card-light.svg) |
| [`year-review-card`](components/year-review-card/) | Douze mois orbitent un anneau doré — bilan annuel + quatre médailles étoiles | ![preview](components/year-review-card/preview/year-review-card.svg) · ![light](components/year-review-card/preview/year-review-card-light.svg) |
| [`projects-card`](components/projects-card/) | Vos repos non-fork les plus étoilés dans une grille 2×2 | ![preview](components/projects-card/preview/projects-card.svg) · ![light](components/projects-card/preview/projects-card-light.svg) |

## 🔄 Showcase

La vitrine de la famille (`assets/showcase/wall-*.png` et `assets/hero-*.png`) est reconstruite chaque jour à 01:00 UTC par **GitHub Actions** — tous les chiffres sont de vraies données de l'API GitHub.

---

Détails (galerie des 10 cartes, personnalisation, système de design) dans le **[English README](README.md)**.

⭐ **Laissez une étoile au projet !**

## 📜 License

MIT © Morningstar202604
