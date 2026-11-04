# Xu, Mao et al. — DAgent: A Relational Database-Driven Data Analysis Report Generation Agent

DAgent 是一个面向"查询关系数据库后生成分析报告"（RDB-DA）的 LLM agent，由规划、工具（问题分解、向量/Text-to-SQL 混合检索、SQL 改写、报告生成）和记忆三模块组成；作者同时构建了由 HangSeng 金融数据集与 BIRD 改造而来的 DA-Dataset（正文写共 735 条）。在 DeepSeek-V2.5 打分的 0–10 分制下，DAgent 报告质量平均分在 DA-CCKS/DA-BIRD 上为 6.62/6.72，表/列检索 F1 也高于各基线。已阅读全文正文（§1–7）；论文无附录，未复现实验。

[原文](https://arxiv.org/abs/2503.13269)

版本：arXiv:2503.13269v2（2025-04-01），VLDB 模板排版（页眉卷期号为模板占位），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–3 |
| method | §4.1–4.4、Figure 1，PDF pp.4–7 |
| evaluation | §5（数据集构建）、§6、Tables 1–3、Figure 4–5，PDF pp.7–12 |
| limitations | §7 结论中的未来工作，p.12；论文无独立局限章节 |
