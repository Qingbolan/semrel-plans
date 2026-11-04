# Ma, Shankar et al. — Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents

本文提出 Data Agent Benchmark（DAB）：104 条自然语言查询、17 个数据集、4 种 DBMS（PostgreSQL、MongoDB、SQLite、DuckDB）。代理要跨库集成、对齐格式不一致的连接键、从自由文本中抽取值，并用到领域知识；每题由专门的验证脚本确定性判定。主实验中最好的代理 GPT-5.5（Codex）pass@1 为 57%，patents 数据集无任何代理解出。已读正文 §1–7 及附录 A.4、C–E 中与数据构造和实验相关的部分；未逐条核对 Table 6 中全部 104 条查询。

[原文](https://arxiv.org/abs/2603.20576)

版本：arXiv:2603.20576v3（2026-10-07），27 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–4 |
| method | §3.2–3.3、Figure 2、Table 2，PDF pp.4–6；附录 A.4，p.20 |
| evaluation | §4、Tables 3–5，PDF pp.6–9；附录 C–E，pp.22–26 |
| limitations | §6–7，PDF p.10 |
