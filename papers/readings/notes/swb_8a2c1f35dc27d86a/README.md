# Stab & Gurevych — Parsing Argumentation Structures in Persuasive Essays

本文提出议论文论证结构的标注方案、402 篇标注语料和端到端解析器：CRF 识别论证成分，SVM 分类成分与关系，再用整数线性规划联合求出段内树结构。ILP 联合模型在成分分类上显著优于基分类器和启发式基线（macro F1 0.826），关系识别 0.751，并在 microtext 语料上复验。已阅读引言、标注方案、语料构建、解析器、评测、误差分析、讨论与附录 A；附录 C 的特征消融只作了浏览。

[原文](https://aclanthology.org/J17-3005)

版本：Computational Linguistics 43(3):619–660，2017，doi:10.1162/COLI_a_00295；ACL Anthology PDF，42 页（第 42 页为出版方附加的被引列表）。PDF 页码 = 期刊页码 − 618。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.2，PDF pp.1–3、9–11 |
| method | §4（语料构建）、§5.1–5.4，PDF pp.12–27 |
| evaluation | §4.2、§4.5、§5.5，Tables 2–3、6、8、12–13，PDF pp.12–16、20、27–29 |
| limitations | §5.6、§6，PDF pp.29–31；附录 A Table A.1，PDF p.32 |
