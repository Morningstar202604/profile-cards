# Contribution Grid Card (3D)

![Contribution Grid Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/contrib-grid-card/preview/contrib-grid-card.svg)

把你的 GitHub 贡献日历，画成一片**3D 等距金色贡献柱**：柱子高度 = 当天贡献量，
像一片金色城市从星空里长出来。

**一眼特征：等距 3D 立体柱。** 主页的 3D 统计图为什么好看？因为它把"平面绿格子"
换成了"立体柱状"——形态一变，一眼可辨。本卡就是这一思路的自研实现：等距投影 +
三面着色（顶面亮、右面中、左面暗），金色分级（1 / 2-3 / 4-6 / 7+ 天贡献五档），
完全替换第三方 3D 贡献 Action，零服务器、零第三方依赖、纯 Python 标准库生成 SVG。

数据真实：GitHub 贡献日历（GraphQL），每日自动刷新，月份刻度、图例、数据来源全部标注。

## 在 workflow 里使用

```yaml
- uses: actions/checkout@v4
- name: Generate contribution grid
  uses: Morningstar202604/profile-cards/components/contrib-grid-card@v1
  with:
    user: your-github-username
    output: contrib-grid.svg
```

## 在 README 里引用

```markdown
![Contributions](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/contrib-grid.svg)
```

## 输入参数

| 参数 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | GitHub 用户名 |
| `output` | 否 | `contrib-grid-card.svg` | 生成的 SVG 路径 |
| `token` | 否 | `${{ github.token }}` | GitHub token（默认用 workflow 自带） |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

> 浅色主题示例：`theme: light`。

## 本地运行

```bash
GH_TOKEN=xxx USER=your-name python3 generate_contrib_grid_card.py
```

## 数据与刷新

- 数据：GitHub 贡献日历 API（GraphQL），全年真实数据
- 刷新：GitHub Actions 定时任务自动重跑并提交新 SVG，零服务器

Part of **Profile Verse** · [仓库](https://github.com/Morningstar202604/profile-cards) · MIT
