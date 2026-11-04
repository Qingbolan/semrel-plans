# Jacobs & Hoste — Extracting Fine-Grained Economic Events from Business News

本文是在 SENTiVENT 数据集（288 篇英文公司新闻、18 个经济事件主类型、48 种论元角色）上做有监督细粒度经济事件抽取的试点研究：用当时 ACE 上的先进模型 DYGIE++ 识别并分类事件触发词和论元。最佳配置（BERT-Large+LSTM，含 NER 子任务）的触发词识别 F1 为 52.71、论元分类 F1 为 38.01，远低于同一模型在 ACE05 上的 76.22 和 56.33；作者认为主因是多词触发词被强制压缩成单 token，导致类别歧义。已阅读全文 §1–7 及 Tables 1–5。

[原文](https://aclanthology.org/2020.fnp-1.36)

版本：Proceedings of the 1st Joint Workshop on FNP-FNS（COLING 2020 workshop），pp.235–245（ACL Anthology 2020.fnp-1.36），11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–2 |
| 方法 | §3 数据集、§4 实验设置，PDF pp.2–6 |
| 评测 | §5、Tables 2–5，PDF pp.6–8 |
| 局限 | §5 误差分析、§7，PDF pp.6–8 |
