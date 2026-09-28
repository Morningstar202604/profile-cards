# Impact Card（Profile Verse 组件）

生成一张展示"已合并 PR × 仓库 star"的贡献影响力卡片（SVG），自动标注你在多大体量的开源项目里被合并过 PR。零服务器、零成本：GitHub Actions 定时生成、提交到仓库、任何人一行 `<img>` 引用。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards) 全家桶的第一个组件。

![Impact Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/impact-card/preview/impact-card.svg)

## 特性

- 大数字：合并 PR 总数 · 贡献仓库数 · 影响力分（Σ 贡献过仓库的 star）
- 贡献分档：S ≥50k★ / A ≥10k★ / B ≥1k★ / C ≥100★ / D <100★
- TOP 贡献仓库榜：仓库名 + star + 合并 PR 数（≥10k★ 金色高亮）
- 最近合并 PR + 更新时间，每日自动刷新
- 支持多账号聚合：`users: a,b`

## 怎么用（别人一键接入）

在你自己的仓库里加一个 workflow（公开仓库 Actions 免费，0 元）：

```yaml
name: Refresh Impact Card

on:
  schedule:
    - cron: "0 1 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  card:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate impact card
        uses: Morningstar202604/profile-cards/components/impact-card@v1
        with:
          users: your-github-username
          output: impact-card.svg

      - name: Commit & push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add impact-card.svg
          if git diff --cached --quiet; then exit 0; fi
          git commit -m "chore: refresh impact card [skip ci]"
          git push
```

然后任意 README / 网页里一行引用（国内推荐 jsDelivr，自带缓存与国内节点）：

```markdown
![Impact Card](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/impact-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `users` | 是 | — | GitHub 用户名，多账号用逗号分隔，如 `a,b` |
| `output` | 否 | `impact-card.svg` | 生成的 SVG 路径 |
| `token` | 否 | `github.token` | 一般不用改；私有数据场景可传带权限的 token |
| `max_prs` | 否 | `300` | 每个用户最多扫描的已合并 PR 数 |
| `max_top` | 否 | `5` | 卡片上展示的 TOP 仓库数 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

## 工作原理

1. GitHub Search API 拉取 `is:pr author:<用户> is:merged` 的全部已合并 PR
2. 按仓库去重后读取每个仓库的 star 数
3. 按 star 分档（S/A/B/C/D）统计，取 TOP 仓库与最近合并
4. Python 直接生成 SVG（共享 `core/`，无第三方依赖）

> 说明：star 是"项目影响力"的代理指标，不等于代码质量；按分档展示比单一总分更直观、更难被刷。

## License

MIT © Morningstar202604
