# Wen et al. — When should I search more: Adaptive Complex Query Optimization with Reinforcement Learning

本文是 RAG 检索前的“查询优化”（query rewriting/decomposition）方法，不是数据库意义上的查询优化。ACQO 用 Qwen2.5-3B 通过强化学习自适应决定是否把用户问题拆为多个子查询，用 Rank-Score Fusion（RSF）合并多路检索结果，并用两阶段课程强化学习稳定训练。论文报告在 HotpotQA 上 BM25/ANCE 两种检索器所有指标最好，在 TopiOCQA 上召回最好但 MRR/NDCG 不及 ConvSearch-R1，推理延迟约为后者的 1/9。已读正文与附录 A、B。

[原文](https://arxiv.org/abs/2601.21208)

版本：arXiv:2601.21208v1（2026-01-29），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2、§3.1，PDF pp.1–5 |
| method | §3.2–3.4、附录 A，PDF pp.5–7、11–12 |
| evaluation | §4、Tables 2–5、附录 B（Tables 6–10），PDF pp.7–9、12–16 |
| limitations | 无独立章节；由阅读者从实验表格归纳 |
