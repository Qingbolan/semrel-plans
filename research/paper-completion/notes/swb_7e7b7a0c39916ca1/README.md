# Chalkidis et al. — LexGLUE: A Benchmark Dataset for Legal Language Understanding in English

LexGLUE 把 7 个已有英文法律 NLP 数据集（ECtHR A/B、SCOTUS、EUR-LEX、LEDGAR、UNFAIR-ToS、CaseHOLD）统一为标准化基准，并对 TF-IDF+SVM 与 7 个 base 规模 Transformer 做基线评测。法律领域预训练模型（Legal-BERT、CaseLaw-BERT）总体最好，尤其在 macro-F1 上；Legal-BERT 跨任务算术均值 µ-F1/m-F1 为 79.8/72.0（BERT 77.8/69.5，Table 4）；但没有一个模型在所有任务上最优，SCOTUS 上线性 SVM 反而最好。已阅读正文及附录 B–G，未复现实验。

[原文](https://aclanthology.org/2022.acl-long.297)

版本：ACL 2022 长文，pp.4310–4330（ACL Anthology 2022.acl-long.297），21 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–§2，PDF pp.1–3 |
| 方法 | §3 数据集与简化、§4 模型与微调，PDF pp.3–7 |
| 评测 | §5、Tables 3–4，附录 B–E，PDF pp.7–8、17–18 |
| 局限 | §6 Vision、§7 Limitations，附录 F，PDF pp.8–9、19 |
