# Dorbani, Yasser, Lin, Mhedhbi — Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB

本文是 FlockMTL 的演示论文：一个 DuckDB 扩展，把 LLM 调用做成 SQL 标量/聚合函数（llm_filter、llm_complete、llm_reduce、llm_rerank 等），并把 MODEL 与 PROMPT 作为与 TABLE 并列的 DDL 模式对象。唯一的量化结果是在 Kaggle Bank Review 数据上，批处理使对话补全类映射函数最多 7× 加速、嵌入类函数最多 48× 加速。全文 4 页均已阅读；论文没有质量评测、基线系统对比或局限性章节。

[原文](https://arxiv.org/abs/2504.01157)

版本：arXiv:2504.01157v1（PVLDB 演示论文预印本），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，PDF p.1 |
| method | §2.1–2.3、Table 1、Queries 1–3、Fig.1，PDF pp.2–4 |
| evaluation | §2.3 Batching 段，PDF p.4；§3 演示，PDF p.4 |
| limitations | 无独立章节；阅读者据 §2.3、§3 推断 |
