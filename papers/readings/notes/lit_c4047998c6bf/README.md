# Song et al. — QUITE: A Query Rewrite System Beyond Rules via LLM Agents

QUITE 是一个免训练的 SQL 查询改写系统：由有限状态机编排多个 LLM 智能体（DeepSeek-R1 负责推理，Claude-3.7-Sonnet 负责改写、验证和决策），借助数据库反馈迭代改写，配套知识库、混合等价校验器和 pg_hint_plan 提示注入。

在 PostgreSQL 14 上的 TPC-H、DSB、Calcite 和 LLM 生成的 StackOverflow 负载中，平均延迟低于 LearnedRewrite、LLM-R2、R-Bot 和单智能体基线（如 TPC-H 平均延迟从原查询 69.84 s 降到 25.60 s，DSB 从 32.62 s 降到 5.85 s，Table 4）。已阅读全文；摘要、引言和正文中的“最高提升”数字口径不一致，详见评测栏目。

[原文](https://arxiv.org/abs/2506.07675)

版本：arXiv:2506.07675v3（2026-01-02），14 页（含参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–4 |
| 方法 | §3–6、Table 1–3、Algorithm 1，PDF pp.4–8 |
| 评测 | §7、Table 4–8、Fig. 6–10，PDF pp.9–12 |
| 局限 | 无独立章节；§1、§5.2、§7.1、Table 8，PDF pp.2–3、7、9、12 |
