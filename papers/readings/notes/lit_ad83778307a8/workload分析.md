# 工作负载

论文没有数据集、基准或查询集合。唯一的输入示例是 Figure 2 中"四家 IT 公司的真实股价数据"（§2.2 末、§3，pp.2–3）。原文未说明是哪四家公司、时间范围、行数或数据来源。

系统使用的封闭候选集合（附录 A，pp.7–8）可以视为任务空间的定义：

| 类别 | 候选 |
|---|---|
| 洞察类型（13 种） | Change Over Time、Characterize Distribution、Cluster、Comparison、Correlate、Determine Range、Deviation、Find Anomalies、Find Extremum、Magnitude、Part to Whole、Sort、Trend |
| 图表类型 | bar、scatter、pie、line |
| 入场动画 | Axes-fade-in、Bar-grow-in、Line-wipe-in、Pie-wheel-in、Scatter-fade-in、Fade-in、Float-in、Fly-in、Zoom-in 等 12 种 |
| 强调动画 | Bar-bounce、Zoom-in-then-zoom-out、Shine-in-a-short-duration、Highlight-one-and-fade-others |
| 退出动画 | Fade-out |
| 注释类型 | mark label、circle、text、rule、trend line、arrow |

底座模型为 GPT-4（§2.1，p.2）。原文未报告运行次数、耗时、成本或失败率。

阅读者分析：若要用于评测，只能把上述候选集合视为输出约束，需要另行构建数据表集合与人工评分标准。
