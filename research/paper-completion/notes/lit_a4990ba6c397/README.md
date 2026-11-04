# Saparina & Lapata — AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries

AMBROSIA 是一个歧义 text-to-SQL 基准，覆盖三类歧义：范围歧义、附着歧义和模糊性。它包含 16 个领域、846 个由 LLM 受控生成的多表数据库；每个歧义问题配有人工写的无歧义解读和对应 SQL，问题、解读与 SQL 合计 4,242 条。在零样本条件下，最好的 Llama3-70B（Prompt）在歧义问题上的召回只有 30.7%，在无歧义问题上为 64.5%；同时给出全部解读（AllFound）的比例不超过 1.9%。已阅读正文 §1–§6 以及附录 B、E、F、G 和数据说明书中的划分说明。

[原文](https://arxiv.org/abs/2406.19073)

版本：arXiv:2406.19073v2（2024-10-31），NeurIPS 2024 Datasets and Benchmarks Track，29 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1–3.2，PDF pp.1–4 |
| 方法 | §3.3–3.5、Table 1，PDF pp.5–7；附录 B、E，pp.15、19 |
| 评测 | §4、Tables 2–5，PDF pp.7–10；附录 F–G，pp.19、23 |
| 局限 | §5，PDF p.10；数据说明书，p.26 |
