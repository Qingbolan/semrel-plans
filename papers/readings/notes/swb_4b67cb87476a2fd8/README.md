# Choi, Breck & Cardie — Joint Extraction of Entities and Relations for Opinion Recognition

本文在 MPQA 新闻语料上同时抽取观点表达、观点来源（持有者）以及二者之间的“来源表达观点”链接关系。方法是先分别训练 CRF 实体标注器和最大熵链接分类器，再用整数线性规划（ILP）做全局一致推断，并加入语义角色标注（SRL）特征。重叠匹配下最终链接 F1 为 68.9，来源抽取 F1 从 73.9 提升到 78.1。已阅读全文 9 页。

[原文](https://aclanthology.org/W06-1651)

版本：EMNLP 2006 会议论文（pp.431–439），9 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–3 |
| 方法 | §3–5、Table 1，PDF pp.3–6 |
| 评测 | §6–8、Tables 2–5，PDF pp.6–9 |
| 局限 | §8 Implicit links、脚注 17，PDF pp.7、9（无单独局限性章节） |
