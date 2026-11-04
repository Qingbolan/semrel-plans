# Huang et al. — E2ETune: End-to-End Knob Tuning via Fine-tuned Generative Language Model

E2ETune 把数据库参数（knob）调优表述为序列到序列生成：输入工作负载统计、查询计划文本和内部指标，微调后的 Mistral-7B 直接输出 45 个 PostgreSQL knob 的分桶取值，无需逐次回放工作负载的迭代搜索。训练数据由 GPT-4-Turbo 生成的 OLAP 查询、随机加权的 OLTP 事务，以及"HEBO + 代价模型"搜出的标签组成，共 2,953 条。

在 10 个标准基准和 3 个真实基准上，它的调优时间最短（TPC-H 上 19.8 分钟，HEBO 为 1,381.7 分钟），性能提升在多数基准上处于最优或次优。已阅读正文 §1–10，并渲染核对 p.7 的 Table 1。

[原文](https://arxiv.org/abs/2404.11581)

版本：arXiv:2404.11581v3（2025-03-19），对应 PVLDB 18(5):1466–1480，15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 定义 1–2，PDF pp.1–2、4 |
| 方法 | §4–7、Figure 2，PDF pp.4–7 |
| 评测 | §8、Figures 3–5、Tables 1–3，PDF pp.7–12；Table 1 已渲染核对 |
| 局限 | §9 Discussion，PDF p.13；§8.2.3 真实基准结果 |
