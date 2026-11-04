# Islamaj et al. — NLM-Chem, a new resource for chemical entity recognition in PubMed full text literature

本文是 Scientific Data 的数据描述论文，发布 NLM-Chem：150 篇 PMC 开放获取全文论文，由 10 位 NLM 资深 MeSH 标引员双人标注化学实体提及，并归一化到 MeSH 标识符。共 38,342 个提及、4,867 个不同化学名、2,064 个 MeSH ID。作者同时给出 BlueBERT + MTCR 识别与归一化工具：在 NLM-Chem 测试集上，加入 NLM-Chem 训练数据后，提及识别 F1 从 0.610 提升到 0.757，MeSH ID 识别 F1 从 0.682 提升到 0.772。

已通读全文，包括选文、标注流程、数据记录、一致性、语料特征与基线实验。

[原文](https://www.nature.com/articles/s41597-021-00875-1)

版本：Scientific Data 8:91（2021），12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、Background & Summary，PDF pp.1–2 |
| 方法 | Methods（选文、指南、标注流程、工具、MTCR），PDF pp.2–6 |
| 评测 | Data Records、Technical Validation、Usage Notes、Tables 2–7，PDF pp.6–10 |
| 局限 | 原文无独立局限章节；相关讨论散见于 Technical Validation 与 Table 5 分析，PDF pp.7–9 |
