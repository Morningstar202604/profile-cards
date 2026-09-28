# Streak Card（Profile Verse 组件）

差异化连续贡献卡：当前连续天数是一颗**星轨环中央的亮星**，环外环绕十二颗星点（星座感），下方两枚星章显示最长连续与全年贡献。一眼特征：**星轨环 + 中心亮星**。

数据真实：来自 GitHub 贡献日历（GraphQL，全年数据），非估算。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Streak Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/streak-card/preview/streak-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate streak card
  uses: Morningstar202604/profile-cards/components/streak-card@v1
  with:
    user: your-github-username
    output: streak-card.svg
```

```markdown
![Streak](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/streak-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | GitHub 用户名 |
| `output` | 否 | `streak-card.svg` | 输出路径 |
| `token` | 否 | `github.token` | 一般不用改 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

口径：当前连续 = 从今天往前数连续有贡献的天数（今天还没贡献则从昨天起算）；最长连续 = 全年最大连续段；全年贡献 = 贡献日历总数。

## License

MIT © Morningstar202604
