# Year Review Card（Profile Verse 组件）

一年 12 个月绕成一枚**金色年轮**：每个月的贡献是一颗星，星越大越亮代表贡献越多；最活跃的月份带光晕。轮心是近一年贡献总数（金色渐变），右侧四枚「年度星章」：最活跃月 / 最长连续 / 合并 PR / 主力语言。

属于 [Profile Verse](https://github.com/Morningstar202604/profile-cards) 全家桶的第 9 个组件。

![Year Review dark](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/year-review-card/preview/year-review-card.svg)

![Year Review light](https://cdn.jsdelivr.net/gh/Morningstar202604/profile-cards@main/components/year-review-card/preview/year-review-card-light.svg)

## 特性

- **金色年轮**：12 个月星绕环排布（星径与亮度按当月贡献量），最活跃月带光晕
- 轮心：近一年贡献总数（金色渐变）
- 四枚星章：最活跃月 · 最长连续 · 合并 PR · 主力语言（真实数据）
- 数据来源：GitHub 贡献日历（近 365 天）+ 已合并 PR + 仓库主语言
- 双主题：`dark`（星夜）/ `light`（纸面）

## 怎么用

```yaml
- uses: Morningstar202604/profile-cards/components/year-review-card@v1
  with:
    user: your-github-username
    output: year-review-card.svg
    theme: dark        # 或 light
```

## 与其它卡的关系

`streak-card` 讲「连续」，`contrib-grid-card` 讲「逐日分布」，`year-review-card` 讲「一年总览」——三张卡可以一起用，各讲一个角度。
