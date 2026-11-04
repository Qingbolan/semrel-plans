# Lin et al. — Sema-SQL: Extending Relational Queries with Large Language Models

本文提出 Sema-SQL：把自然语言问题自动翻译成“混合关系代数”（HRA，关系算子中嵌入 LLM UDF）查询，再做代价优化（LLM UDF 位置的动态规划 + SMT 等价验证、UDF 改写为 SQL）和执行优化（语义连接 smart-batching）。在 120 题的 TAG+ 上，Claude Sonnet 4.5 下执行准确率 89.2%，与需要专家手写管道的 LOTUS/Palimpzest 相当；优化使 33 个被改写查询的平均时延降 28%、token 降 21%。已阅读全文正文（无附录），核对了 Table 3–5 与 §6.3 的数字。

[原文](https://arxiv.org/abs/2604.23477)

版本：arXiv:2604.23477v2（2026-05-14），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

注意：批次标题为 “SEMA-SQL: Beyond Traditional Relational Querying with Large Language Models”，而 v2 PDF 标题为 “Sema-SQL: Extending Relational Queries with Large Language Models”，作者与 arXiv 编号一致，视为同一论文的不同版本标题（v1 未下载核对）。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Figure 1–2，PDF pp.1–2；Problem 3.1，p.4 |
| method | §2 HRA（Def. 2.1、Table 1），pp.3–4；§3 查询生成，pp.4–6；§4 代价优化（Alg. 1、Fig. 6–7），pp.6–7；§5 执行与 smart-batching（Alg. 2–3），pp.7–8 |
| evaluation | §6、Table 2–5、Fig. 8–11，PDF pp.8–12 |
| limitations | 无独立局限章节；散见于脚注 2 与 SMT 超时回退（p.7）、§4 末“留作未来工作”（p.7）、§6.2.2 错误分析（p.10）、§6.3.1 剩余语义错误（p.11） |
