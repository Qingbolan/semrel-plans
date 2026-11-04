# Dobbins et al. — The Leaf Clinical Trials Corpus: a new resource for query generation from clinical trial eligibility criteria

本文是 Scientific Data 的数据描述论文，发布 LCT 语料：1,006 份 ClinicalTrials.gov 入排标准文本，按 50 类实体、51 类关系做细粒度标注，目的是为"把自然语言入排标准转成数据库查询"的多步 NLP 流程提供训练与评测数据。基线中，SciBERT 实体识别的微平均 F1 为 81.3%，R-BERT+SciBERT 关系抽取为 85.2%。语料本身不包含查询，无法直接评测查询生成。已通读全文，包括标注方案、标注过程、质量验证、基线、用法说明与局限。

[原文](https://www.nature.com/articles/s41597-022-01521-0)

版本：Scientific Data 9:490（2022），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、Background & Summary、Table 1，PDF pp.1–2 |
| 方法 | Methods（标注方案、与 Chia 比较、标注过程），PDF pp.2–9 |
| 评测 | Technical Validation、Tables 4–7，PDF pp.9–12 |
| 局限 | Limitations、Future work，PDF pp.12–13 |
