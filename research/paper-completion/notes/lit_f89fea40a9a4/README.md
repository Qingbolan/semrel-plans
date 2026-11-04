# Wang & Li — AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries

AOP 是一个面向数据湖复杂自然语言查询的 LLM 流水线自动编排系统。系统预定义 22 个语义算子（Retrieve、Scan、Filter、Aggregate、Validate 等）；收到查询后，由 LLM 生成多条链式流水线，改写为 DAG 并合并，再逐层交互执行，根据中间结果调整，并配合代价模型、预取、并行和上下文管理。在 CRAG 的五类复杂问题上，AOP 以 Llama 3.1-8B 为模型，例如 Comparison 类达到 54.1%，直接问 LLM 为 9.30%，最强的 RecurRAG 为 38.1%。已阅读全文。

[原文](https://www.vldb.org/cidrdb/papers/2025/p32-wang.pdf)

版本：CIDR 2025（p32），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Fig. 2，PDF pp.1–3 |
| method | §2–6、Table 1、Figs. 3–6，PDF pp.3–10 |
| evaluation | §7、Figs. 7–9，PDF pp.10–11 |
| limitations | §6、§8–9；局限主要为阅读者归纳，PDF pp.9–12 |
