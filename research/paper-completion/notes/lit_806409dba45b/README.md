# Dong & Wang — From Interpretation to Compilation: Compilation-Based Execution of Semantic Operators [Vision]

这是一篇 PVLDB 格式的 vision 论文：主张语义算子系统把 LLM 当作“语义编译器”而非运行时解释器——对 sem_filter / sem_map / sem_join 只调用一次 LLM 生成确定性 Python 函数，再本地执行。初步实验包括独立单算子（各 100 个谓词）、Palimpzest 内单算子（30/36/29 条查询）与 SemBench movie Q1–Q10；LLM 调用减少一到两个数量级，SemBench 总时间 711.3s→290.1s。全文 7 页均已阅读。它是同作者完整系统论文 SemBaker（arXiv:2608.06677）的前序工作。

[原文](https://arxiv.org/abs/2607.13407)

版本：arXiv:2607.13407v1（2026-07-15），7 页（PVLDB 模板，卷期为占位符）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Table 1、Figure 1，PDF pp.1–3 |
| method | §3–4、Figure 2，PDF pp.3–4 |
| evaluation | §5.1–5.4、Tables 2–5，PDF pp.4–6 |
| limitations | §5.5，p.5；§6 研究机会，pp.5–6 |
