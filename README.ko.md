<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/showcase/hero-home.png">
    <img src="assets/showcase/hero-light.png" alt="Profile Verse — 오픈소스 GitHub 프로필 카드" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · 오픈소스 GitHub 프로필 카드</h1>

<p align="center"><sub>**Profile Verse**는 브랜드명 &middot; 이 저장소는 <code>profile-cards</code> — 같은 프로젝트, 하나의 패밀리입니다.</sub></p>

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

> ⭐ **마음에 드시나요? Star를 눌러주세요** — 한 번의 클릭으로 카드는 영원히 무료로 유지됩니다.

**Profile Verse**는 평범한 GitHub 프로필을 **별빛 가득한 데이터 쇼케이스**로 바꿔줍니다: 오픈소스 **SVG 카드** 10장 — 타이핑 헤더, 통계, 연속 커밋, 3D 기여도, 기술 스택, 금색 배지, 프로젝트, 오픈소스 영향력, 연간 리뷰, 배너 — **GitHub Actions**로 무료 생성, **매일 자동 업데이트**, 데이터는 **GitHub API 실데이터**, **7가지 테마**(다크/라이트). workflow 파일 하나를 복사하면 끝, 서버 없음·비용 없음. [라이브 데모](https://github.com/Morningstar202604/Morningstar202604)가 실제 홈페이지에서 운영 중입니다.

## ✨ Features

- **카드 10장, 하나의 디자인 언어** — 타이핑 · 통계 · 연속 커밋 · 기여도 · 기술 스택 · 배지 · 프로젝트 · 영향력 · 연간 리뷰 · 배너
- **7가지 시그니처 테마** — `dark` `light` `rose` `ocean` `aurora` `sunset` `mint`, 모든 카드가 모든 테마 지원
- **100% 실데이터** — GitHub REST API + 기여 캘린더; 각 카드에 출처와 업데이트 시각 표기
- **영원히 무료** — 무료 GitHub Actions가 생성하는 순수 SVG; 서버·DB·카드 등록 불필요
- **매일 자동 업데이트** — 숫자는 절대 낡지 않습니다; `workflow_dispatch`로 언제든 수동 실행·테마 변경
- **파일 하나로 셋업 완료** — 프로필 저장소에 workflow를 복사하면 카드 10장이 모두 등장
- **다크/라이트 자동 전환** — `<picture>`가 방문자의 시스템 테마를 따라갑니다
- **fork하면 자동 적용** — `${{ github.repository_owner }}`로 fork에서 *내* 데이터가 자동 표시

## ✨ Why


| | Profile Verse | 흔한 해결책 |
|---|---|---|
| **비주얼** | 통일된 별밤×금색 디자인 언어, 카드마다 특징적인 형태 | 어디서나 똑같은 평면 바 |
| **테마** | 7가지 테마 | 다크만, 또는 라이트에서 깨짐 |
| **데이터** | GitHub API 실데이터, 출처·시각 표기 | 정적 스냅샷이나 가짜 숫자 |
| **비용** | 영원히 $0 (무료 Actions로 SVG 생성) | 유료 API, 자체 서버 |

## 🚀 クイックスタート / Quick start

이 workflow 파일 하나를 프로필 저장소(`.github/workflows/profile-verse.yml`)에 추가하면 카드 10장이 홈페이지에 나타나고 매일 자동 업데이트됩니다.

### 🎨 테마

| Theme | Style | Vibe |
|---|---|---|
| `dark` | 미드나잇 네이비 × 금색 | 별밤, 기본값 |
| `light` | 아이보리 종이 × 앤틱 골드 | 클린 & 클래식 |
| `rose` | 블러시 아이보리 × 로즈 골드 | 소프트 & 로맨틱 |
| `ocean` | 딥씨 틸 × 문라이트 실버 | 쿨 & 딥 |
| `aurora` | 브라이트 바이올렛 × 일렉트릭 바이올렛 | 드리미 & 브라이트 |
| `sunset` | 웜 크림 × 코랄 오렌지 | 에너제틱 & 웜 |
| `mint` | 프레시 제이드 × 틸 | 크리스프 & 프레시 |

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

## 🗂 카드 목록 — 10장 × 2테마

모든 카드에 **다크**(별밤)와 **라이트**(종이) 버전이 있습니다.

| Card | Description | Previews |
|---|---|---|
| [`impact-card`](components/impact-card/) | 리포지토리 스타 등급으로 평가한 병합 PR — 프로필의 '금 함량' | ![preview](components/impact-card/preview/impact-card.svg) · ![light](components/impact-card/preview/impact-card-light.svg) |
| [`stats-card`](components/stats-card/) | 팔로워 / 공개 저장소 / 병합 PR이 금색 궤도를 도는 미니멀 통계 | ![preview](components/stats-card/preview/stats-card.svg) · ![light](components/stats-card/preview/stats-card-light.svg) |
| [`streak-card`](components/streak-card/) | 현재 연속 커밋이 60눈금 다이얼 중앙에서 빛나는 카드 | ![preview](components/streak-card/preview/streak-card.svg) · ![light](components/streak-card/preview/streak-card-light.svg) |
| [`typing-card`](components/typing-card/) | 별빛 아래 태그라인이 타이핑되고 금색 커서가 깜빡임(순수 SVG + SMIL) | ![preview](components/typing-card/preview/typing-card.svg) · ![light](components/typing-card/preview/typing-card-light.svg) |
| [`contrib-grid-card`](components/contrib-grid-card/) | 등각 투영 금색 기여 그리드(53주, 5단계 골드) | ![preview](components/contrib-grid-card/preview/contrib-grid-card.svg) · ![light](components/contrib-grid-card/preview/contrib-grid-card-light.svg) |
| [`tech-stack-card`](components/tech-stack-card/) | 주 언어가 중심 별, 나머지는 타원 궤도로 별자리를 이룸 | ![preview](components/tech-stack-card/preview/tech-stack-card.svg) · ![light](components/tech-stack-card/preview/tech-stack-card-light.svg) |
| [`banner-card`](components/banner-card/) | 빛나는 이름, 그라데이션 텍스트, 혜성 궤적(순수 비주얼) | ![preview](components/banner-card/preview/banner-card.svg) · ![light](components/banner-card/preview/banner-card-light.svg) |
| [`badge-card`](components/badge-card/) | 평면 shields 대신 금색 메달 줄(실데이터 또는 완전 커스텀) | ![preview](components/badge-card/preview/badge-card.svg) · ![light](components/badge-card/preview/badge-card-light.svg) |
| [`year-review-card`](components/year-review-card/) | 12개월이 금색 링을 공전 — 연간 성과와 별 메달 4개 | ![preview](components/year-review-card/preview/year-review-card.svg) · ![light](components/year-review-card/preview/year-review-card-light.svg) |
| [`projects-card`](components/projects-card/) | 스타 상위 non-fork 저장소를 2×2 그리드로 표시 | ![preview](components/projects-card/preview/projects-card.svg) · ![light](components/projects-card/preview/projects-card-light.svg) |

## 🔄 Showcase

패밀리 쇼케이스(`assets/showcase/wall-*.png`·`assets/hero-*.png`)는 매일 01:00 UTC에 **GitHub Actions**가 재구성합니다 — 모든 숫자는 GitHub API 실데이터입니다.

---

자세한 내용(카드 10장 갤러리, 커스터마이징, 디자인 시스템)은 **[English README](README.md)** 를 참고하세요.

⭐ **프로젝트에 Star를 눌러주세요!**

## 📜 License

MIT © Morningstar202604
