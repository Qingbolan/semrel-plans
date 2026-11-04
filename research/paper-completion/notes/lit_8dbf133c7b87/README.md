# Dharwada et al. — Query Rewriting via LLMs (LITHE)

本文提出 LITHE，一个供 DBA 使用的 LLM 查询改写助手（SQL 到 SQL）。它组合四类手段：基本提示集成、数据库感知的规则提示（R1–R6）、基于 token 概率的 MCTS 解码，以及“抽样结果比对 + 逻辑证明”的等价检查和回退检测。

在 PostgreSQL v16 + GPT-4o、TPC-DS 100 GB 中 88 条慢查询（>10 s）上，LITHE 得到 26 个代价有效改写（CPR，优化器估计加速 ≥1.5 倍），代价加速几何平均 CSGM 为 11.5，实测运行时间加速几何平均 TSGM 为 13.2；SOTA 集成为 13 个、6.1 和 4.9。已阅读正文和附录 A–B，附录 C–D 只看了与方法相关的部分。

[原文](https://arxiv.org/abs/2502.12918)

版本：arXiv:2502.12918v4（2025-09-02），38 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–5 |
| 方法 | §3–6，Table 1–4、Algorithm 1，PDF pp.5–15 |
| 评测 | §7、Table 5–8、Fig. 8–9，PDF pp.15–21；附录 A–B，pp.29–31 |
| 局限 | §8，PDF pp.21–23 |
