<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-home.png">
    <img src="assets/hero-light.png" alt="Profile Verse — 把 GitHub 主页的每个部位换成一张好卡" width="100%" />
  </picture>
</p>

<h1 align="center">Profile Verse · 主页宇宙</h1>

<p align="center">
  <b>把 GitHub 主页的每一个部位，都换成一张更好看的卡。</b><br/>
  零服务器 · 零成本 · 数据真实 · 深浅双主题 · 一个仓库逛完全部组件。
</p>

<p align="center">
  <a href="https://github.com/Morningstar202604/profile-cards/stargazers"><img src="https://img.shields.io/github/stars/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=stars" alt="GitHub stars" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/forks"><img src="https://img.shields.io/github/forks/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=forks" alt="GitHub forks" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/actions"><img src="https://img.shields.io/github/actions/workflow/status/Morningstar202604/profile-cards/update.yml?style=flat&color=%23C9A86A&label=previews" alt="预览自动刷新" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Morningstar202604/profile-cards?style=flat&color=%23C9A86A" alt="MIT license" /></a>
  <a href="https://github.com/Morningstar202604/profile-cards/releases"><img src="https://img.shields.io/github/v/release/Morningstar202604/profile-cards?style=flat&color=%23C9A86A&label=version" alt="v1.6.0" /></a>
  <a href="README.md"><img src="https://img.shields.io/badge/readme-English-8FB4F5?style=flat" alt="English" /></a>
</p>

**Profile Verse** 把 GitHub 主页的每个区块都替换成一张有辨识度的卡：星空打字机、3D 贡献柱、金色影响力奖牌、技术栈星座……全部共享同一套设计语言——**星夜 × 鎏金**，每张卡都带真实的 **深色 / 浅色** 双主题。

不需要服务器、不需要数据库、不需要绑卡。卡片是纯 SVG，由 GitHub Actions（免费）生成并每日自动刷新；数据全部来自 GitHub API 的**真实数据**，每张卡都标注数据来源与更新时间。

> 🚀 **正在使用**：[Morningstar202604 主页](https://github.com/Morningstar202604/Morningstar202604) 已用 Profile Verse 卡片。

---

## ✨ 为什么选它

| | Profile Verse | 常见方案 |
|---|---|---|
| **外观** | 统一星夜鎏金设计语言，每张卡一个「一眼特征」 | 千篇一律的统计条 |
| **主题** | 每张卡都有 **深色 + 浅色**，跟随系统自动切换 | 只有深色，浅色主页没法用 |
| **数据** | GitHub API 真实数据，卡上标注来源与更新时间 | 静态快照或假数字 |
| **成本** | 永久免费——SVG 由免费 Actions 生成 | 付费 API、自建服务器 |
| **上手** | 一个 workflow 文件，复制即用 | 要配一堆服务 |
| **贪吃蛇？** | 不做蛇，不撞脸 | 🐍 满大街都是 |

## 🚀 快速开始（全家桶）

把下面这一个 workflow 放进你的主页仓库（`.github/workflows/profile-verse.yml`），10 张卡就全部出现在主页上，每日自动刷新。把 `theme:` 设成 `dark` 或 `light`（也可以手动触发时选择）。

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
          name: 你的用户名
          output: assets/profile-verse/banner-card.svg
          theme: ${{ inputs.theme }}

      - name: Typing
        uses: Morningstar202604/profile-cards/components/typing-card@v1
        with:
          phrases: "写代码，赏星光;与其更好，不如不同"
          output: assets/profile-verse/typing-card.svg
          theme: ${{ inputs.theme }}

      - name: Stats
        uses: Morningstar202604/profile-cards/components/stats-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/stats-card.svg
          theme: ${{ inputs.theme }}

      - name: Streak
        uses: Morningstar202604/profile-cards/components/streak-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/streak-card.svg
          theme: ${{ inputs.theme }}

      - name: Contribution grid (3D)
        uses: Morningstar202604/profile-cards/components/contrib-grid-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/contrib-grid-card.svg
          theme: ${{ inputs.theme }}

      - name: Tech stack
        uses: Morningstar202604/profile-cards/components/tech-stack-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/tech-stack-card.svg
          theme: ${{ inputs.theme }}

      - name: Badges
        uses: Morningstar202604/profile-cards/components/badge-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/badge-card.svg
          theme: ${{ inputs.theme }}

      - name: Projects (2×2 项目网格)
        uses: Morningstar202604/profile-cards/components/projects-card@v1
        with:
          user: 你的用户名
          output: assets/profile-verse/projects-card.svg
          theme: ${{ inputs.theme }}

      - name: Impact (按仓库 star 分档的已合并 PR)
        uses: Morningstar202604/profile-cards/components/impact-card@v1
        with:
          users: 你的用户名                 # 多账号聚合：a,b
          output: assets/profile-verse/impact-card.svg
          theme: ${{ inputs.theme }}

      - name: Year review (年度回顾星轮)
        uses: Morningstar202604/profile-cards/components/year-review-card@v1
        with:
          user: 你的用户名
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

在 `README.md` 里用 `<picture>` 引用——卡片会**跟随访客的系统深浅色自动切换**：

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-verse/impact-card.svg">
  <img src="./assets/profile-verse/impact-card-light.svg" alt="开源影响力" width="100%" />
</picture>
```

搞定。没有服务器、没有成本、每天自动刷新。

## 🗂 组件展示厅 · 10 卡 × 双主题

每张卡都有 **`dark`（星夜）与 `light`（纸面）** 两个主题。

### 1 · impact-card — 开源影响力卡
你的已合并 PR 到底有多值钱？按贡献仓库的 star 分档金色徽章（S≥50k★ 到 D<100★），加 TOP 仓库榜单。主页的「含金量」担当。

![Impact dark](components/impact-card/preview/impact-card.svg)
![Impact light](components/impact-card/preview/impact-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/impact-card@v1
  with:
    users: 你的用户名            # 多账号聚合：a,b
    output: impact-card.svg
```

### 2 · stats-card — 极简统计卡
关注 / 公开仓库 / 已合并 PR 三个数字骑着金色星轨。大数字 + 少文字，拒绝密密麻麻。

![Stats dark](components/stats-card/preview/stats-card.svg)
![Stats light](components/stats-card/preview/stats-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/stats-card@v1
  with:
    user: 你的用户名
    output: stats-card.svg
```

### 3 · streak-card — 连续打卡星环
当前连续天数 = 60 刻度表盘中央的亮星。真实贡献日历数据。

![Streak dark](components/streak-card/preview/streak-card.svg)
![Streak light](components/streak-card/preview/streak-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/streak-card@v1
  with:
    user: 你的用户名
    output: streak-card.svg
```

### 4 · typing-card — 星空打字机
一句话在星空里自己打出来，金色闪烁光标。纯 SVG + SMIL，不需要外部服务。

![Typing dark](components/typing-card/preview/typing-card.svg)
![Typing light](components/typing-card/preview/typing-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/typing-card@v1
  with:
    phrases: "第一句话;第二句话;第三句话"   # 最多 3 条
    output: typing-card.svg
```

### 5 · contrib-grid-card — 3D 贡献柱
等距投影的立体金色柱子（顶面亮 / 右面中 / 左面暗三面着色），五档金色分级，53 周全年日历。主页上「一眼差异」的那张卡。

![Contrib dark](components/contrib-grid-card/preview/contrib-grid-card.svg)
![Contrib light](components/contrib-grid-card/preview/contrib-grid-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/contrib-grid-card@v1
  with:
    user: 你的用户名
    output: contrib-grid-card.svg
```

> ✅ **单一入口**：原独立仓库已合并回本仓库 —— 这张卡只在全家桶里，一个仓库、一个 `@v1`。

### 6 · tech-stack-card — 技术栈星座
主语言是中央亮星，其余语言沿金色椭圆环绕、虚线连成星座。来自真实仓库主语言统计。

![Tech dark](components/tech-stack-card/preview/tech-stack-card.svg)
![Tech light](components/tech-stack-card/preview/tech-stack-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/tech-stack-card@v1
  with:
    user: 你的用户名
    output: tech-stack-card.svg
```

### 7 · banner-card — 星空全景头图
发光名字 + 渐变字 + 双流星。纯视觉，不需要 API。

![Banner dark](components/banner-card/preview/banner-card.svg)
![Banner light](components/banner-card/preview/banner-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/banner-card@v1
  with:
    name: 你的名字
    output: banner-card.svg
```

### 8 · badge-card — 金色奖章
一排金色奖章徽章（渐变金边 + 星形图标），替代 shields 平铺条。默认自动取真实数据，也可以完全自定义。

![Badge dark](components/badge-card/preview/badge-card.svg)
![Badge light](components/badge-card/preview/badge-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/badge-card@v1
  with:
    user: 你的用户名
    output: badge-card.svg
    # badges: "PRs=12;Stars=256.9k;Repos=19"   # 可选：完全自定义
```

### 9 · year-review-card — 年度回顾星轮
一年 12 个月绕成一枚金色年轮：星越大越亮代表当月贡献越多，最活跃月带光晕；轮心是近一年贡献总数，右侧四枚年度星章（最活跃月 / 最长连续 / 合并 PR / 主力语言）。数据来自真实贡献日历。

![Year dark](components/year-review-card/preview/year-review-card.svg)
![Year light](components/year-review-card/preview/year-review-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/year-review-card@v1
  with:
    user: 你的用户名
    output: year-review-card.svg
```

### 10 · projects-card — 项目网格卡
按 star 数取你排名靠前的非 fork 仓库，排成 2×2 网格——名称 · 简介 · 语言 · star，替换主页上干巴巴的文本列表。数据来自 GitHub REST API，`count` 最多 8 个。

![Projects dark](components/projects-card/preview/projects-card.svg)
![Projects light](components/projects-card/preview/projects-card-light.svg)

```yaml
- uses: Morningstar202604/profile-cards/components/projects-card@v1
  with:
    user: 你的用户名
    output: projects-card.svg
```

## 🔄 全家桶图：自动刷新 & 换肤

全家桶展示图（`assets/showcase/wall-*.png` 与 `assets/hero-*.png`）由
[`update.yml`](.github/workflows/update.yml) 流水线**每天 01:00 UTC 自动重建**——
每张卡的数字全部来自真实 GitHub API，卡上自带更新时间戳，图里的内容永远不会过期。

- **手动刷新 / 换肤**：进入 **Actions → Refresh Preview Cards → Run workflow**，
  在 `theme` 里填 `dark`、`light`、`rose`、`ocean`、`aurora`、`sunset`、`mint`，
  或填 `all` 一次生成全部主题。流水线会用最新数据按所选主题重建墙图与头图并推回仓库。
- **产物**：`assets/showcase/wall-<主题>.png`（全部 10 张卡）与
  `assets/showcase/hero-<主题>.png`（横幅 + 打字机 + 主页精选行）；深色头图同时保留为 `hero-home.png`。
- **深浅色自动切换**：本 README 头图用了 `<picture>`，访客深色模式看到深色头图、浅色模式看到浅色头图。
- **显示你自己的数字**：把 `update.yml` 里的 `user` / `users` 改成你的 GitHub 用户名，
  下一次运行后所有卡（含全家桶图）都会换成你的真实数据。

## 🎨 设计规范（差异化 + 不拥挤）

- **一眼特征**：每张卡一个独特形态（星轨 / 表盘 / 打字机 / 3D 等距柱 / 星座 / 流星横幅 / 奖章），不做撞脸方案，不做贪吃蛇
- **星夜 × 鎏金**：深蓝渐变夜空 + 金色只用在数据（数字、锚点、奖牌），正文保持低饱和灰蓝——发光的是数字，不是装饰
- **七主题一键切换**：全部色板集中在 `core/theme.py` —— `dark`（午夜·默认）、`light`（纸面）、`rose`（玫瑰金）、`ocean`（深海）、`aurora`（电光紫）、`sunset`（珊瑚橙）、`mint`（薄荷青）。

| 主题 | 名称 | 气质 |
| --- | --- | --- |
| `dark` | 午夜 | 星夜深蓝 × 鎏金（默认） |
| `light` | 纸面 | 象牙白 × 压印金 |
| `rose` | 玫瑰金 | 暖白 × 蔷薇金 |
| `ocean` | 深海 | 冷蓝绿 × 月光银青 |
| `aurora` | 电光紫 | 亮紫纸面 × 电光紫鎏金 |
| `sunset` | 珊瑚橙 | 暖奶油 × 珊瑚橙鎏金 |
| `mint` | 薄荷青 | 清新翡翠 × 青碧 |

- **明信片装帧**：每张卡四边带一层压印暗记 —— 顶/底细字带、左右竖排文字（`PROFILE VERSE ✦ 零服务器 ✦ …`），像印刷信笺的边注。
- **数据真实**：统一走 `core/github.py`——GitHub API / 贡献日历 / star 分档，每日刷新，卡上标注来源与更新时间
- **留白优先**：640 宽横版，大数字 + 少文字

## 🧱 目录结构

```
profile-cards/
├── core/                     共享核心：GitHub API · 贡献日历 · star 分档 · 七主题
├── components/
│   ├── impact-card/          组件 = 生成脚本 + 模板 + action.yml + README + preview
│   ├── stats-card/
│   ├── streak-card/
│   ├── typing-card/
│   ├── contrib-grid-card/
│   ├── tech-stack-card/
│   ├── year-review-card/
│   ├── banner-card/
│   ├── badge-card/
│   └── projects-card/
├── examples/                 复制即用的 workflow
├── .github/workflows/        本仓库预览每日自刷新
└── README.md                 组件目录页
```

## 🌱 一个仓库 · 一个入口

全部十张卡都从这个单一仓库发货 —— 一个 `@v1`、一个 workflow、零服务器。
（`contrib-grid-card` 曾短暂拆出过独立仓，现已合并回来；旧链接会自动指向本仓库。）

每周自动更新的 **⭐ Stargazer Wall 感谢墙**（`.github/workflows/star-wall.yml`）会
在 Issues 里感谢每一位新 star，见 [Issues](https://github.com/Morningstar202604/profile-cards/issues)。

## 🤝 贡献

新卡创意、主题打磨、Bug 反馈都欢迎。见 [CONTRIBUTING](CONTRIBUTING.md)，并请遵守 [行为准则](CODE_OF_CONDUCT.md)。

## 📜 License

MIT © Morningstar202604  ·  [VERSIONING](VERSIONING.md)  ·  [CHANGELOG](CHANGELOG.md)
