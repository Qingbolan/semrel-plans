# Schrader et al. — MuLMS: A Multi-Layer Annotated Text Corpus for Information Extraction in the Materials Science Domain

MuLMS 是一个资源论文：50 篇 CC BY 开放获取材料科学论文（7 个子领域），由领域专家对全文逐句穷尽标注命名实体、关系和"测量（Measurement）"框架。作者定义测量句识别、嵌套 NER、关系抽取三类任务，并给出基于 BERT/SciBERT/MatSciBERT 的基线；MatSciBERT 在 NER 上测试 micro-F1 79.6，基于金标实体的关系抽取测试 micro-F1 67.6，而用预测实体时降到 36.5。已阅读正文 §1–6、Limitations；附录仅按需查阅，未复现实验。

[原文](https://aclanthology.org/2023.wiesp-1.11)

版本：Proceedings of the 2nd Workshop on Information Extraction from Scientific Publications（WIESP 2023），pp.84–100，ACL Anthology 2023.wiesp-1.11，17 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–2 |
| 方法 | §3 语料与标注方案、§4 任务与模型，PDF pp.2–6 |
| 评测 | §3.4 IAA、§5、Tables 5–12，PDF pp.4–8 |
| 局限 | §6 Conclusion、Limitations，PDF pp.8–9 |
