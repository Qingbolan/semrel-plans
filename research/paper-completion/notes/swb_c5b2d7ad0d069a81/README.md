# Habernal & Gurevych — Exploiting Debate Portals for Semi-Supervised Argumentation Mining in User-Generated Web Discourse

本文把网络用户文本中的论证成分识别（claim、premise、backing 等，BIO 编码）作为句级序列标注问题，用 SVMhmm 求解，并提出"论证空间"特征：用词向量把辩论网站上的无标注帖子和句子投影到潜在空间并聚类，再以目标句到各聚类中心的余弦相似度为特征。在 340 篇教育争议文档上，该特征在交叉验证、跨领域、跨语域三种设置中都优于基线特征组合，但最好结果仍只有人工一致性的约一半：交叉验证中最佳组合（FS2+3+4）平均 token 级 F1 为 0.348，人工为 0.707（Table 1）。已阅读全文正文 §1–6 及 Tables 1–4。

[原文](https://aclanthology.org/D15-1255)

版本：EMNLP 2015，pp.2127–2137（ACL Anthology D15-1255），11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–3 |
| 方法 | §4–4.2，PDF pp.3–5 |
| 评测 | §5、§5.1、Tables 1–4，PDF pp.5–8 |
| 局限 | §5（rebuttal/refutation 不报告）、§5.1、§6，PDF pp.5–8 |
