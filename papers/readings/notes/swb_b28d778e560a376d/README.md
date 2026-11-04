# Lao, Zimmerer, Ovcharenko, … , Kipf, Trummer — SemBench: A Benchmark for Semantic Query Processing Engines

SemBench 是面向“语义查询处理引擎”（SQPE，用 LLM 求值的语义 SQL 算子）的基准：5 个场景、55 条查询，覆盖文本、图像、音频与表格，含语义过滤、连接、映射、排序、分类算子；同时度量成本、质量、延迟、内存与扩展性。作者用 gemini-2.5-flash 统一评测 LOTUS、Palimpzest、ThalamusDB 和 BigQuery，发现没有系统支持全部查询，语义连接是成本与质量的主要分歧点。已阅读正文 §1–§6，并渲染核对 Table 2–3（PDF p.7）。

[原文](https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf)

版本：PVLDB 19(8): 1754–1767, 2026，doi:10.14778/3811243.3811249，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.4，PDF pp.1–3 |
| method | §3（Table 1）、§4.1–4.6（Table 2），PDF pp.3–7 |
| evaluation | §5.1–5.5、Tables 3–5、Figure 1，PDF pp.6–12；Table 2–3 已渲染核对 |
| limitations | §4.6、§5.3–5.5、§6，PDF pp.7–12 |
