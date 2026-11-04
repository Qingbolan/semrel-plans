# Xie et al. — OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment

本文提出阿里云的 Text-to-SQL 多智能体框架 OpenSearch-SQL，分为预处理、抽取、生成、精修四个阶段，并在各阶段之间加入"一致性对齐"智能体，以减少上游幻觉向下游传递。另有两项设计：由 LLM 自动补写思维链的 Query-CoT-SQL 动态少样本，以及忽略 JOIN 等语法细节的中间语言 SQL-Like。不做任何微调，基于 GPT-4o 在 BIRD 上取得开发集 EX 69.3%、测试集 EX 72.28%、R-VES 69.36%，作者称提交时三项均排名第一。全文已读。

[原文](https://arxiv.org/abs/2502.14913)

版本：arXiv:2502.14913v1（2025-02-19，ACM 模板会议信息未填写），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.2–2.3，PDF pp.1–3 |
| 方法 | §3.1–3.7、Algorithm 1，PDF pp.4–8 |
| 评测 | §4、Tables 1–7，PDF pp.8–12 |
| 局限 | §3.8、§4.6，PDF pp.7–8、12（无独立局限章节） |
