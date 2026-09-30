<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/showcase/hero-home.png">
    <img src="assets/showcase/hero-light.png" alt="Profile Verse — オープンソース GitHub プロフィールカード" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · オープンソース GitHub プロフィールカード</h1>

<p align="center"><sub>**Profile Verse** がブランド名 &middot; このリポジトリは <code>profile-cards</code> — 同じプロジェクト、同じ家族。</sub></p>

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

> ⭐ **気に入ったら Star をお願いします** — クリックひとつで、カードは永久に無料のままです。

**Profile Verse** は、ありふれた GitHub プロフィールを**星降るデータのショーケース**に変えます：オープンソースの **SVG カード** 10 枚 — タイピングヘッダー、統計、連続コミット、3D コントリビューション、技術スタック、金色バッジ、プロジェクト、OSS インパクト、年間レビュー、バナー。**GitHub Actions** が無料で生成し、**毎日自動更新**。データは **GitHub API の実データ**、**7 テーマ**（ダーク＆ライト）対応。workflow 1 ファイルをコピーするだけで完了、サーバー不要・コストゼロ。[ライブデモ](https://github.com/Morningstar202604/Morningstar202604) は実際のホームページで稼働中。

## ✨ Features

- **10 カード、1 つのデザイン言語** — タイピング・統計・連続コミット・コントリビューション・技術スタック・バッジ・プロジェクト・インパクト・年間レビュー・バナー
- **7 つのシグネチャテーマ** — `dark` `light` `rose` `ocean` `aurora` `sunset` `mint`、全カード全テーマ対応
- **100% 実データ** — GitHub REST API + コントリビューションカレンダー；各カードに出典と更新時刻を表記
- **永久無料** — 無料の GitHub Actions が生成する純 SVG；サーバー・DB・カード登録不要
- **毎日自動更新** — 数字は古くなりません；`workflow_dispatch` でいつでも手動更新＆テーマ変更
- **1 ファイルでセットアップ完了** — プロフィールリポジトリに workflow をコピーするだけ
- **ダーク/ライト自動切替** — `<picture>` が訪問者のシステムテーマに追従
- **fork すれば自動対応** — `${{ github.repository_owner }}` で fork は**自分の**データを表示

## ✨ Why


| | Profile Verse | 一般的な解決策 |
|---|---|---|
| **見た目** | 統一された星夜×金のデザイン言語、カードごとに特徴的な形状 | ありふれたバーの羅列 |
| **テーマ** | 7 テーマ対応 | ダークのみ、またはライト崩れ |
| **データ** | GitHub API の実データ、出典と時刻を表記 | 静的スナップショットや偽の数値 |
| **コスト** | 永久無料（無料 Actions で SVG 生成） | 有料 API・自前サーバー |

## 🚀 クイックスタート / Quick start

この workflow をプロフィールリポジトリ（`.github/workflows/profile-verse.yml`）に追加するだけで、10 枚のカードがホームページに並び、毎日自動更新されます。

### 🎨 テーマ

| Theme | Style | Vibe |
|---|---|---|
| `dark` | ミッドナイト・ネイビー × 金色 | 星夜、デフォルト |
| `light` | アイボリー紙 × アンティーク金 | クリーン＆クラシック |
| `rose` | ブラッシュ・アイボリー × ローズゴールド | ソフト＆ロマンティック |
| `ocean` | 深海ティール × 月光シルバー | クール＆ディープ |
| `aurora` | ブライト・バイオレット × エレクトリックバイオレット | ドリーミー＆ブライト |
| `sunset` | ウォームクリーム × コーラルオレンジ | エナジェティック＆ウォーム |
| `mint` | フレッシュジェイド × ティール | クリア＆フレッシュ |

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

## 🗂 カード一覧 — 10 枚 × 2 テーマ

すべてのカードに**ダーク**（星夜）と**ライト**（紙）の 2 バージョンがあります。

| Card | Description | Previews |
|---|---|---|
| [`impact-card`](components/impact-card/) | マージ済み PR をリポジトリのスター層で評価 — プロフィールの「金含有量」 | ![preview](components/impact-card/preview/impact-card.svg) · ![light](components/impact-card/preview/impact-card-light.svg) |
| [`stats-card`](components/stats-card/) | フォロワー / 公開リポジトリ / マージ PR が金色の軌道に乗る最小統計 | ![preview](components/stats-card/preview/stats-card.svg) · ![light](components/stats-card/preview/stats-card-light.svg) |
| [`streak-card`](components/streak-card/) | 現在の連続コミットが 60 目盛りダイヤルの中心に輝く | ![preview](components/streak-card/preview/streak-card.svg) · ![light](components/streak-card/preview/streak-card-light.svg) |
| [`typing-card`](components/typing-card/) | 星空の下でタグラインがタイプされ、金色カーソルが点滅（純 SVG + SMIL） | ![preview](components/typing-card/preview/typing-card.svg) · ![light](components/typing-card/preview/typing-card-light.svg) |
| [`contrib-grid-card`](components/contrib-grid-card/) | 等角投影の金色コントリビューショングリッド（53 週・5 段階の金） | ![preview](components/contrib-grid-card/preview/contrib-grid-card.svg) · ![light](components/contrib-grid-card/preview/contrib-grid-card-light.svg) |
| [`tech-stack-card`](components/tech-stack-card/) | メイン言語が中央の星、他が楕円軌道で星座に結ばれる | ![preview](components/tech-stack-card/preview/tech-stack-card.svg) · ![light](components/tech-stack-card/preview/tech-stack-card-light.svg) |
| [`banner-card`](components/banner-card/) | 光る名前、グラデーション文字、彗星の軌跡（純ビジュアル） | ![preview](components/banner-card/preview/banner-card.svg) · ![light](components/banner-card/preview/banner-card-light.svg) |
| [`badge-card`](components/badge-card/) | フラットな shields の代わりに金色メダルの列（実データ / カスタム可） | ![preview](components/badge-card/preview/badge-card.svg) · ![light](components/badge-card/preview/badge-card-light.svg) |
| [`year-review-card`](components/year-review-card/) | 12 ヶ月が金色リングを公転 — 年間実績と 4 つの星メダル | ![preview](components/year-review-card/preview/year-review-card.svg) · ![light](components/year-review-card/preview/year-review-card-light.svg) |
| [`projects-card`](components/projects-card/) | スター上位の非 fork リポジトリを 2×2 グリッドで表示 | ![preview](components/projects-card/preview/projects-card.svg) · ![light](components/projects-card/preview/projects-card-light.svg) |

## 🔄 Showcase

ファミリーショーケース（`assets/showcase/wall-*.png`・`assets/hero-*.png`）は毎日 01:00 UTC に **GitHub Actions** が再構築します — すべての数字は GitHub API の実データです。

---

詳細（10 カードのギャラリー、カスタマイズ、設計システム）は **[English README](README.md)** を参照してください。

⭐ **気に入ったら Star をお願いします！**

## 📜 License

MIT © Morningstar202604
