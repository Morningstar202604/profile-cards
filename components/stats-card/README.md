# Profile Stats Card（Profile Verse 组件）

差异化统计卡：关注者 / 公开仓库 / 已合并 PR 三个大数字，像行星一样排在金色星轨上，背景是星空。一眼特征：**数字骑在星轨上**，不是普通统计条。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Stats Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/stats-card/preview/stats-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate stats card
  uses: Morningstar202604/profile-cards/components/stats-card@v1
  with:
    user: your-github-username
    output: stats-card.svg
```

```markdown
![Stats](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/stats-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | GitHub 用户名 |
| `output` | 否 | `stats-card.svg` | 输出路径 |
| `token` | 否 | `github.token` | 一般不用改 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

数据真实来自 GitHub API（关注者 / 公开仓库 / 已合并 PR），每日自动刷新。

## License

MIT © Morningstar202604
