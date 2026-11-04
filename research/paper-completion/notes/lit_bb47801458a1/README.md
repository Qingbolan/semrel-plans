# Qi et al. — Sema: A High-performance System for LLM-based Semantic Query Processing

Sema 是在 DuckDB 内部实现语义算子的查询引擎：用户用 SemaSQL 在 SELECT/WHERE/JOIN ON 中嵌入自然语言表达式，优化器用辅助 LLM 压缩表达式并把可推导部分改写为关系谓词，执行器对连续 SemFilter 做自适应执行（重排、融合、批量 prompt）。作者在自建的 20 条查询（基于 BIRD 的 9 个数据库）上报告相对 Lotus 2–4×、相对 Palimpzest 2–10× 的加速，质量与 Lotus/Palimpzest 相当，明显优于 FlockMTL。已读正文全部章节和附录中的数据集表与部分查询文本，未逐条核对附录 32 张查询图。

[原文](https://arxiv.org/abs/2603.11622)

版本：arXiv:2603.11622v1（2026-03-12），27 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–2，PDF pp.1–3 |
| method | §3–6、Tables 1–2、Algorithm 1，pp.3–8；附录 A–B，pp.16–17 |
| evaluation | §7、Tables 3–6、Figs.4–7，pp.8–12；附录 C Tables 7–8，pp.17–18 |
| limitations | §2.2 末段、§5.1/§5.2 末段，pp.3、6–7 |
