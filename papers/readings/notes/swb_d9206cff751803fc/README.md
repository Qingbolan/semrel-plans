# Thompson et al. — Annotation and detection of drug effects in text for pharmacovigilance

本文发布 PHAEDRA 语料：597 篇 MEDLINE 摘要，标注了三类实体、四类事件（不良反应、潜在治疗效果、联合用药、药物相互作用）、事件属性、两类关系和共指，并用 HYPHEN 自动把药物和疾病实体规范化到 MeSH / SNOMED-CT。双人一致性在宽松匹配下实体 92.6% F、事件识别 78.4% F；用 NERSuite 和 EventMine 训练的基线在测试集上分别得到 79.5% 宽松 F 和 47.2% F（事件及主要参与者）。已阅读 33 页正文全部（参考文献除外）。

[原文](https://link.springer.com/article/10.1186/s13321-018-0290-y)

版本：Journal of Cheminformatics 10:37（2018），PMC6089860 出版社 PDF（PMC 开放数据 S3 副本），33 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、Background，pp.1–5，Table 1 |
| 方法 | Methods（文档选择、五层标注、规范化），pp.5–12，Tables 2–6 |
| 评测 | Results and discussion：IAA、规范化、语料统计、NERSuite/EventMine，pp.12–29，Tables 7–25 |
| 局限 | 跨句信息分析 pp.22–25（Table 21）；Conclusions 与未来工作 p.29 |
