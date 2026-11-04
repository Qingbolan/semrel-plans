# Deng et al. — ReFoRCE: A Text-to-SQL Agent with Self-Refinement, Consensus Enforcement, and Column Exploration

ReFoRCE 是 UCSD 与 Snowflake AI Research 的企业级 Text-to-SQL 智能体：先按表名模式分组并做表级 LLM 模式链接以压缩超长模式，再生成多个经执行自修正的候选 SQL，用结果多数投票选出高置信答案，平票时才触发“列探索”（用逐步复杂的探查 SQL 了解嵌套列和取值）。用 o3 时在 Spider 2.0-Snow / Lite 上 EX 为 35.83 / 36.56，论文称当时位列排行榜第一。已阅读正文 §1–5 与附录 A–C（模式链接召回、成本统计、列探索算法），附录 D 的长案例轨迹只浏览；p.7 Tables 1–2 已渲染核对。

[原文](https://arxiv.org/abs/2502.00675)

版本：arXiv 2502.00675v5（2025-06-03），33 页（正文 11 页 + 附录 A–D 与排行榜截图）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–4 |
| 方法 | §3.2.1–3.2.3、Eq.(1)–(7)、Fig. 1–2；附录 A、C，PDF pp.3–6、13–17 |
| 评测 | §4.1–4.3、Tables 1–4；附录 B Tables 5–7，PDF pp.6–9、13–14；p.7 已渲染核对 |
| 局限 | §5.1，PDF p.9 |
