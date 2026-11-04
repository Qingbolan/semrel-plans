# Yang, Luo et al. — Data Imputation with Limited Data Redundancy Using Data Lakes

本文提出 LakeFill：当表内冗余不足以填补缺失值时，在数据湖中做**元组级**检索增强填补，采用"检索（对比学习的元组编码器）→ 重排（清单式 LLM 标注训练的 BERT 重排器）→ 推理（两阶段置信度感知的 LLM 填补）"框架，并发布 mvBench（9,009 个不完整元组、约 339 万个数据湖元组）。在六个数据集上，LakeFill + GPT-4o 的精确匹配准确率为 0.907–0.978，明显高于无检索与 BM25 检索。已阅读正文全部章节（§1–8）；论文无附录，未复现实验。

[原文](https://www.vldb.org/pvldb/vol18/p3354-tang.pdf)

版本：PVLDB Vol.18 No.10，pp.3354–3367（2025），doi:10.14778/3748191.3748200，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2、Figure 1，PDF pp.1–2（页码 3354–3355） |
| method | §3–5、Figures 2–4、Table 1、Theorem 4.1，PDF pp.3–7 |
| evaluation | §6.1–6.6、Tables 2–10、Figure 5，PDF pp.7–12 |
| limitations | 正文无局限章节；边界散见 §6.1（标注范围）、§6.3 Exp-2、§6.6，pp.7、9、12 |
