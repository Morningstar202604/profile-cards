# Tech Stack Card（Profile Verse 组件）

把你的技术栈画成一片**星座**：主语言是中央的亮星，其他语言像星星一样环绕它，星点之间用虚线连成星座。一眼特征：**技术栈星座图**，不是平铺的技能条/徽章排。

数据真实：来自 GitHub API 每个公开仓库的主语言，按仓库数统计，中央星 = 使用最多的语言。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Tech Stack Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/tech-stack-card/preview/tech-stack-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate tech stack card
  uses: Morningstar202604/profile-cards/components/tech-stack-card@v1
  with:
    user: your-github-username
    output: tech-stack-card.svg
```

```markdown
![Tech Stack](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/tech-stack-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | GitHub 用户名 |
| `output` | 否 | `tech-stack-card.svg` | 输出路径 |
| `token` | 否 | `github.token` | 一般不用改 |
| `max_nodes` | 否 | `6` | 环绕中央星的语言节点数 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

## License

MIT © Morningstar202604
