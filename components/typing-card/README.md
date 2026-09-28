# Typing Card（Profile Verse 组件）

差异化标语横幅：文字在星空背景上一字一字"打出来"，金色光标闪烁，循环播放你的标语。纯 SVG + SMIL 动画，任何能渲染 `<img>` 的地方都会动——**不用服务器、不用 JS**。

一眼特征：**星空打字机 + 金色光标**。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards)。

![Typing Card](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/typing-card/preview/typing-card.svg)

## 用法

```yaml
- uses: actions/checkout@v4
- name: Generate typing card
  uses: Morningstar202604/profile-cards/components/typing-card@v1
  with:
    phrases: "你的标语一;Your slogan two;第三条"
    output: typing-card.svg
```

```markdown
![Typing](https://cdn.jsdelivr.net/gh/你的用户名/你的仓库@main/typing-card.svg)
```

## 输入参数

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `phrases` | 否 | 默认三条示例标语 | 分号分隔，最多 3 条 |
| `output` | 否 | `typing-card.svg` | 输出路径 |
| `theme` | 否 | `dark` | 颜色主题：`dark`（深蓝星空）或 `light`（米白纸面） |

## License

MIT © Morningstar202604
