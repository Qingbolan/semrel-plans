# Nagano et al. — A novel corpus of molecular to higher-order events that facilitates the understanding of the pathogenic mechanisms of idiopathic pulmonary fibrosis

本文发布特发性肺纤维化（IPF）领域的生物医学文本标注语料：150 篇 PubMed 摘要，标注 9,297 个实体（含 3 类提示词）、4,899 个事件、1,681 个关系，实体和事件触发词归一化到 UMLS ID，并新增 `disorder` 事件论元以区分与疾病相关的事件。作者用 BENNERD 和 DeepEventMine 做十折交叉验证：实体 NER F1 87.43，而事件抽取 F1 仅 45.08、关系抽取 49.64。已阅读正文全部章节、Tables 1–3 与 8–11；对 Tables 4–7 的高频 UMLS ID 只做抽查。

[原文](https://www.nature.com/articles/s41598-023-32915-8)

版本：Scientific Reports 13:5986（2023），doi:10.1038/s41598-023-32915-8，出版社 PDF，24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 引言，PDF pp.1–2 |
| 方法 | Methods and materials（实体/事件/关系定义、归一化、标注流程、评估），PDF pp.2–7；Tables 1–3 |
| 评测 | Results and discussion，PDF pp.7–15；Tables 8–10，pp.19–21 |
| 局限 | PDF pp.10–15 关于稀有类型、单人标注、IAA 的讨论；p.19 关于未复用已有语料 |
