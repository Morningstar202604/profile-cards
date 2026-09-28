# Banner Card（Profile Verse 组件）

主页顶部的**星空全景头图**：你的名字金色发光（SVG 辉光），一条流星划过夜空，整片星野为背景。一眼特征：**发光名字 + 流星轨迹**。

纯视觉组件，不需要 GitHub API，任何用户都能直接用；填上自己的名字和标语即可。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Banner Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/banner-card/preview/banner-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate banner card
  uses: Morningstar202604/profile-cards/components/banner-card@v1
  with:
    user: your-github-username
    text: "你的标语"
    output: banner-card.svg
```

```markdown
![Banner](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/banner-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `user` | 是 | — | 显示在横幅上的名字 |
| `text` | 否 | `Code under the stars, ship with the dawn` | 名字下方的标语 |
| `output` | 否 | `banner-card.svg` | 输出路径 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

## License

MIT © Morningstar202604
