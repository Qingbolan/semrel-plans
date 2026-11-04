# Legrand et al. — PGxCorpus, a manually annotated corpus for pharmacogenomics

本文是 Scientific Data 的数据描述论文，发布药物基因组学（PGx）关系抽取语料 PGxCorpus。语料包含来自 911 篇 PubMed 摘要的 945 个句子，人工标注了 6,761 个实体（10 类，层级组织，含嵌套与不连续实体）和约 2,871 个关系（7 类，带模态）。作者用 CNN/多通道 CNN 做 10 折交叉验证基线：NER 宏平均 F1 为 49.15–71.93，关系抽取宏平均 F1 为 45.67–49.56，只区分"是否为 PGx 关系"时为 54.04。已通读全文，包括构建流程、一致性、预标注修正与基线；补充材料未读。

[原文](https://www.nature.com/articles/s41597-019-0342-9)

版本：Scientific Data 7:3（2020），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、Background & Summary、与已有语料比较、Table 1，PDF pp.1–3 |
| 方法 | Methods（检索、预标注、PHARE 扩展、人工标注）、Tables 4–5、Figs. 3–5，PDF pp.4–7 |
| 评测 | Data Records、Technical Validation、Tables 8–12，PDF pp.7–11 |
| 局限 | Baseline performances 中的模型限制讨论，PDF pp.10–11 |
