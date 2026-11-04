# Wadhwa et al. — Learning from Natural Language Explanations for Generalizable Entity Matching

本文把实体匹配（EM）从二分类改写为条件生成，用 Mistral-7B-Instruct / Alpaca 为训练对生成链式思维式解释，再用"标签+解释"微调 FlanT5-base，以提升跨领域、跨 schema、跨来源分布的泛化。Table 2 中加入解释后平均 F1 在跨 schema 设置提升 22.32、跨领域 14.47、跨分布 13.67；消融显示把解释换成乱码会明显掉分。已阅读正文、Limitations 与附录 A–F，未复现实验。

[原文](https://aclanthology.org/2024.emnlp-main.352)

版本：EMNLP 2024 主会，pp.6114–6129（ACL Anthology 2024.emnlp-main.352），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1，PDF pp.1–2 |
| 方法 | §2–§2.3、附录 A/C，PDF pp.2–5、13–14 |
| 评测 | Tables 1–5、§3 消融 A–E 与 H1/H2、附录 B/D/E/F，PDF pp.2–8、13–16 |
| 局限 | Limitations、Ethical Considerations，PDF p.9 |
