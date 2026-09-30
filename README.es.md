<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/showcase/hero-home.png">
    <img src="assets/showcase/hero-light.png" alt="Profile Verse — tarjetas de perfil de GitHub de código abierto" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · Tarjetas de perfil de GitHub de código abierto</h1>

<p align="center"><sub>**Profile Verse** es la marca &middot; este repositorio se llama <code>profile-cards</code> — el mismo proyecto, una sola familia.</sub></p>

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

> ⭐ **¿Te gusta el proyecto? Dale una estrella** — un clic y las tarjetas seguirán siendo gratis para siempre.

**Profile Verse** convierte un perfil de GitHub normal en una **vitrina estelar basada en datos**: 10 **tarjetas SVG** de código abierto — encabezado mecanografiado, estadísticas, racha, cuadrícula 3D de contribuciones, pila tecnológica, insignias doradas, proyectos, impacto open source, resumen anual, banner — generadas gratis por **GitHub Actions**, **actualizadas a diario** con **datos reales de la API de GitHub**, en **7 temas de color** (modo oscuro y claro). Un archivo de workflow, copiar y pegar, sin servidores, sin coste. [Demo en vivo](https://github.com/Morningstar202604/Morningstar202604) — las tarjetas funcionan hoy en una página real.

## ✨ Features

- **10 tarjetas, un lenguaje de diseño** — mecanografía · estadísticas · racha · contribuciones · pila tecnológica · insignias · proyectos · impacto · resumen anual · banner
- **7 temas característicos** — `dark` `light` `rose` `ocean` `aurora` `sunset` `mint`; cada tarjeta en todos los temas
- **100% datos reales** — API REST de GitHub + calendario de contribuciones; cada tarjeta indica fuente y hora de actualización
- **$0 para siempre** — SVG puro generado por GitHub Actions gratis; sin servidor, sin base de datos, sin tarjeta de crédito
- **Actualización diaria automática** — los números nunca quedan obsoletos; ejecuta de nuevo en cualquier momento con `workflow_dispatch` y elige tema
- **Instalación con un archivo** — copia un workflow en tu repositorio de perfil y aparecen las 10 tarjetas
- **Cambio oscuro/claro automático** — los bloques `<picture>` siguen el tema del sistema del visitante
- **Fork y listo** — `${{ github.repository_owner }}` hace que los forks muestren *tus* datos automáticamente

## ✨ Why


| | Profile Verse | Soluciones habituales |
|---|---|---|
| **Aspecto** | Un lenguaje de diseño (noche estrellada × oro), cada tarjeta con forma propia | Barras planas idénticas a las de todos |
| **Temas** | 7 temas | Solo oscuro, o roto en claro |
| **Datos** | Datos reales de la API de GitHub con fuente y hora | Instantáneas estáticas o números falsos |
| **Coste** | $0 para siempre (SVG con Actions gratis) | APIs de pago, servidores propios |

## 🚀 クイックスタート / Quick start

Añade este único workflow a tu repositorio de perfil (`.github/workflows/profile-verse.yml`) y las 10 tarjetas aparecerán en tu página — actualizadas a diario.

### 🎨 Temas

| Theme | Style | Vibe |
|---|---|---|
| `dark` | Azul medianoche × oro | noche estrellada, por defecto |
| `light` | Papel marfil × oro antiguo | limpio y clásico |
| `rose` | Marfil rosado × oro rosa | suave y romántico |
| `ocean` | Verde azulado profundo × plata lunar | frío y profundo |
| `aurora` | Violeta brillante × violeta eléctrico | soñador y brillante |
| `sunset` | Crema cálida × naranja coral | enérgico y cálido |
| `mint` | Jade fresco × verde azulado | nítido y fresco |

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

## 🗂 Catálogo de tarjetas — 10 tarjetas × 2 temas

Cada tarjeta tiene versión **oscura** (noche estrellada) y **clara** (papel).

| Card | Description | Previews |
|---|---|---|
| [`impact-card`](components/impact-card/) | Tus PRs fusionados valorados por los niveles de estrellas de los repos — el «contenido de oro» de tu perfil | ![preview](components/impact-card/preview/impact-card.svg) · ![light](components/impact-card/preview/impact-card-light.svg) |
| [`stats-card`](components/stats-card/) | Estadísticas mínimas: seguidores / repos públicos / PRs fusionados en una órbita dorada | ![preview](components/stats-card/preview/stats-card.svg) · ![light](components/stats-card/preview/stats-card-light.svg) |
| [`streak-card`](components/streak-card/) | Tu racha actual como estrella brillante en el centro de un dial de 60 marcas | ![preview](components/streak-card/preview/streak-card.svg) · ![light](components/streak-card/preview/streak-card-light.svg) |
| [`typing-card`](components/typing-card/) | Tu eslogan se escribe solo bajo las estrellas con cursor dorado parpadeante (SVG puro + SMIL) | ![preview](components/typing-card/preview/typing-card.svg) · ![light](components/typing-card/preview/typing-card-light.svg) |
| [`contrib-grid-card`](components/contrib-grid-card/) | Cuadrícula isométrica dorada de contribuciones (53 semanas, cinco niveles de oro) | ![preview](components/contrib-grid-card/preview/contrib-grid-card.svg) · ![light](components/contrib-grid-card/preview/contrib-grid-card-light.svg) |
| [`tech-stack-card`](components/tech-stack-card/) | Tu lenguaje principal es la estrella central; los demás orbitan y forman una constelación | ![preview](components/tech-stack-card/preview/tech-stack-card.svg) · ![light](components/tech-stack-card/preview/tech-stack-card-light.svg) |
| [`banner-card`](components/banner-card/) | Nombre brillante, texto degradado, estelas de cometa (puramente visual) | ![preview](components/banner-card/preview/banner-card.svg) · ![light](components/banner-card/preview/banner-card-light.svg) |
| [`badge-card`](components/badge-card/) | Una fila de medallas doradas en lugar de shields planos (datos reales o totalmente personalizable) | ![preview](components/badge-card/preview/badge-card.svg) · ![light](components/badge-card/preview/badge-card-light.svg) |
| [`year-review-card`](components/year-review-card/) | Doce meses orbitan un anillo dorado — balance anual + cuatro medallas estrella | ![preview](components/year-review-card/preview/year-review-card.svg) · ![light](components/year-review-card/preview/year-review-card-light.svg) |
| [`projects-card`](components/projects-card/) | Tus repos no-fork con más estrellas en una cuadrícula 2×2 | ![preview](components/projects-card/preview/projects-card.svg) · ![light](components/projects-card/preview/projects-card-light.svg) |

## 🔄 Showcase

El escaparate familiar (`assets/showcase/wall-*.png` y `assets/hero-*.png`) se reconstruye a diario a las 01:00 UTC con **GitHub Actions** — todos los números son datos reales de la API de GitHub.

---

Detalles (galería de las 10 tarjetas, personalización, sistema de diseño) en el **[English README](README.md)**.

⭐ **¡Dale una estrella al proyecto!**

## 📜 License

MIT © Morningstar202604
