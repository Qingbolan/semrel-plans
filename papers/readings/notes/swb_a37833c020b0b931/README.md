# Friedrich, Palmer & Pinkal — Situation entity types: automatic classification of clause-level aspect

本文给出首个较稳健的子句级“情境实体”（SE）类型自动标注系统，并发布约 40,000 个子句、覆盖 13 个体裁（MASC 12 个书面体裁 + Wikipedia）的 SE 标注语料。系统用线性链 CRF 联合预测文档内子句标签序列，结合 Brown 聚类与面向主动词、主指称、子句的句法语义特征；开发集 10 折交叉验证准确率 76.4%，人类上界 79.6%，留出测试集 74.7%。已通读全文。

[原文](https://aclanthology.org/P16-1166)

版本：ACL 2016（第 54 届年会，Berlin）长文，pp.1757–1768，ACL Anthology P16-1166 PDF，12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，pp.1757–1758 |
| 方法 | §4 数据、§5 特征与 CRF、Table 3，pp.1759–1761 |
| 评测 | §6.1–6.6、Table 5–11、Figure 3，pp.1761–1764 |
| 局限 | §7 抽象实体、§8，pp.1764–1765 |
