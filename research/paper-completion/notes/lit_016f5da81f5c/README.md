# Li et al. — The Dawn of Natural Language to SQL: Are We Fully Ready?

本文是 NL2SQL 实验研究（PVLDB 17(11)）。作者构建多角度评测平台 NL2SQL360，在 Spider 与 BIRD 开发集上，按 SQL 复杂度、SQL 特征、数据库领域、问句变体、成本与效率等 15 种设置比较 13 个 LLM 方法与 7 个 PLM 方法，得出"没有单一赢家"及 12 条发现。随后用遗传算法在模块化设计空间中搜索出 SuperSQL，在 Spider 测试集取得 87.0% EX、BIRD 测试集取得 62.66% EX。已阅读全文 §1–7 及 Tables 1–7；Figures 5–9、11–12 的逐柱数值未逐项核对。

[原文](https://arxiv.org/abs/2406.01265)

版本：arXiv:2406.01265v3（PVLDB 17(11): 3318–3331, 2024），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1（Q1–Q3、Example 1、Figure 3）、§2，PDF pp.1–4 |
| 方法 | §3 NL2SQL360（Figure 4、QVT 公式）、§5.1–5.3 设计空间与 AAS，PDF pp.4–5、10–12 |
| 评测 | §4 Exp-1–Exp-9、Tables 2–7、Figures 5–12；§5.3 SuperSQL，PDF pp.5–12 |
| 局限 | §2.3 现有实验局限、§6 研究机会，PDF pp.4、12 |
