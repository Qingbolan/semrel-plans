# 工作负载

**文献筛选**（p.6）：从 2013–2018 年主要期刊在 PubMed 中约 10 万篇文章，缩小到约 6,500 篇 IPF 相关文章，再选出 500 篇临床前研究（含吡非尼酮、尼达尼布等药物或不含药物）；人工优先排序取 top 300 做 MetaMap Lite 自动预标注；从中随机取 120 篇由标注者 1 人工标注，另从剩余中选 30 篇 GGPs 较多的摘要用于 IAA，共 150 篇。

**规模**：

| 项目 | 数量 | 每篇均值 |
|---|---|---|
| 实体（含 3 类提示词） | 9,297 | 61.98 |
| 其中 GGPs / Disorder / Subject | 2,925 / 2,090 / 1,048 | 19.50 / 13.93 / 6.99 |
| 事件 | 4,899 | 32.66 |
| 其中 Positive_regulation / Biological_process | 1,265 / 740 | 8.43 / 4.93 |
| 关系 | 1,681 | 11.21 |

（Tables 1–3，pp.3–6）Binding 仅 8 例，Dissociation 为 0；金标 Negated 事件仅 93 例（Table 2，p.4；p.15）。

**划分**：没有固定的 train/dev/test 划分，评估采用十折交叉验证（p.7、p.10）。IAA 数据为 30 篇的双人标注（p.6）。

**高频内容**：Disorder 中 IPF（C1800706）出现 929 次；GGPs 中 Interleukin-8 155 次；Pharmacological_substance 中 Bleomycin 59 次（Table 4，pp.8–9）。

依据：Annotation process、Tables 1–4，PDF pp.3–9、15。
