# Tan, Zhao, Li, Yu, Piao, Cheng, Meng, Zhao, Rong — Can Large Language Models Be Query Optimizer for Relational Databases?

本文提出 LLM-QO：把关系查询优化表述为序列生成任务，微调 LLaMA3-8B 直接输出带物理连接算子的执行计划，而不做显式计划枚举。

训练数据由 QInstruct 配方构造（SQL、列统计、单例示范、从 PostgreSQL/Oracle 等多个优化器中按实际执行时间选出的最佳计划），分两阶段训练：指令微调 Qit 与偏好优化 Qdpo。在 PostgreSQL 执行引擎上，Qdpo 版本平均执行时间为 PostgreSQL 的 91.4%（IMDB）、94.4%（JOB-light）、31.3%（DSB）。已读全文；Tables 1–2 已渲染核对。

[原文](https://doi.org/10.1145/3769771)

版本：arXiv:2502.05562v1 预印本，15 页（ACM 正式版 HTTP 403 未获取，正式版可能有修订）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–4 |
| method | §4–6，PDF pp.4–7 |
| evaluation | §7、Tables 1–4、Figs.5–9，PDF pp.7–12；p.9 已渲染核对 |
| limitations | §3、§7.3、§7.7、§8，PDF pp.4、9、11–12 |
