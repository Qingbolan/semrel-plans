# Lee et al. — Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems

这是一篇 8 页的愿景论文：把数据库完整性约束推广为"语义完整性约束（SIC）"，用声明式 `ASSERT` 语句约束语义算子的 LLM 输出，并讨论其在逻辑/物理优化、可观测性和企业级约束管理中的位置。论文没有实现评测、数据集或实验数字，以 Rhode Island Hospital 合作中提炼的电子病历（EHR）查询作贯穿示例。已通读全文 §1–§8。

[原文](https://www.vldb.org/pvldb/vol18/p4073-lee.pdf)

版本：PVLDB Vol.18 No.11，pp.4073–4080（2025），doi:10.14778/3749646.3749677，8 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、Table 1，pp.4073–4074 |
| 方法 | §2–§4（架构、接口、约束类别、执行策略），pp.4074–4077；§5–§6，pp.4077–4078 |
| 评测 | 无实验；仅 Table 1 的设计目标/成功标准，p.4074 |
| 局限 | 各节"open challenge"段落，§3、§4.2、§6，pp.4074–4078 |
