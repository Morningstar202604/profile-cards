# Badge Card（Profile Verse 组件）

一排**金色奖章徽章**，替代千篇一律的 shields.io 平铺条：每枚徽章都是渐变金边 + 星形图标的圆角奖章。一眼特征：**金色奖章质感**。

默认自动模式：从 GitHub API 取真实数据（已合并 PR / 全年贡献 / 公开仓库 / 关注者）；也可以传 `badges` 完全自定义。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Badge Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/badge-card/preview/badge-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate badge card
  uses: Morningstar202604/profile-cards/components/badge-card@v1
  with:
    user: your-github-username
    output: badge-card.svg
```

```markdown
![Badges](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/badge-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | GitHub 用户名（自动模式用） |
| `badges` | 否 | 空 | 自定义徽章：`标签=值;标签=值;...`（最多 5 个）；留空 = 自动模式 |
| `output` | 否 | `badge-card.svg` | 输出路径 |
| `token` | 否 | `github.token` | 自动模式需要 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

## License

MIT © Morningstar202604
