# Wang, Li, Feng — iDataLake: An LLM-Powered Analytics System on Data Lakes

这是一篇系统设计综述性质的短文，介绍面向多模态数据湖的 LLM 分析系统 iDataLake。设计包括：21 个语义算子（7 类）；通过对比学习把表格行与文本对齐到同一嵌入空间，再用 Louvain 社区发现把数据分块；用“粗匹配 + LLM 精排”迭代选算子，组成 DAG 执行计划；执行过程中按中间结果调整或重新规划。全文没有实验、数据集或量化结果，摘要中“高准确、低成本”的说法在本文内没有证据支持。已读全文。

[原文](http://sites.computer.org/debull/A25mar/p57.pdf)

版本：IEEE Data Engineering Bulletin，2025 年 3 月期，印刷页 pp.57–69，PDF 13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，印刷页 pp.57–59 |
| method | §2、Table 1、Figs.1–4，印刷页 pp.59–67 |
| evaluation | 无实验章节；§3 评测挑战，印刷页 p.67 |
| limitations | §3，印刷页 pp.67–68 |
