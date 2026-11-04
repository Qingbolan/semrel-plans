# Liu & Mozafari — GenRewrite: Query Rewriting via Large Language Models

GenRewrite 用 LLM 做 SQL 到 SQL 的查询改写，不局限于既有改写规则：LLM 在改写时总结“自然语言改写规则”（NLR2），系统按瓶颈相似度把有效规则当作提示复用，并用反例驱动的语义修正和基于 `EXPLAIN` 的语法修正修复错误改写。在 TPC-DS、JOB 及 SQLStorm 生成的两组变体上，它在各加速阈值下优化的查询数都最多（TPC-DS ≥2x 为 25/99）。已阅读正文 §1–8；附录 A/B 的改写样例仅浏览，未逐一核对。

[原文](https://arxiv.org/abs/2403.09060)

版本：arXiv:2403.09060v3（2025-12-02），19 页（ACM 模板，会议信息仍为占位符）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3，PDF pp.1–4 |
| 方法 | §4（Algorithm 1、Figures 4–6、Tables 1–2），PDF pp.4–7 |
| 评测 | §5（Tables 3–9），PDF pp.7–13 |
| 局限 | §1 Target workloads、§4.1 单一主导规则假设、§6 Discussion，PDF pp.2、6、12–13 |
