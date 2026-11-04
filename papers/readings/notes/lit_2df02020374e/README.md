# Sun et al. — R-Bot: An LLM-based Query Rewrite System

R-Bot 用 LLM 为 SQL 选择并排序 Apache Calcite 的改写规则，而不是让 LLM 直接改写 SQL，从而保证改写等价且可执行。它离线从文档、规则代码和 Stack Overflow 问答中整理改写证据，在线按结构加语义检索证据、生成“recipe”，再分步选规则并依据代价反思迭代。在 TPC-H、DSB、Calcite 上，查询延迟优于 LearnedRewrite 和直接使用 GPT-4/3.5；华为部署在 ICBC 的 20 条慢查询上把总延迟从 9.23 小时降到 4.37 小时。已读正文及 Tables 4–9（p.10–11 已渲染核对）；未复现实验。

[原文](https://arxiv.org/abs/2412.01661)

版本：arXiv:2412.01661v2（2025-07-22），PVLDB 模板，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2、Tables 1–3，PDF pp.1–3 |
| 方法 | §3–§6、Figures 2–4，PDF pp.3–9 |
| 评测 | §7、Tables 4–9、Figures 5–10，PDF pp.9–12；p.10–11 已渲染核对 |
| 局限 | §7.3（top-k、反思开销）、§8，PDF pp.11–12；论文无独立局限章节 |
