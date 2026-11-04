# Louis & Spanakis — A Statutory Article Retrieval Dataset in French

本文发布 BSARD（Belgian Statutory Article Retrieval Dataset）：1,108 个比利时公民提出的法语原生法律问题，由法律援助机构 Droits Quotidiens 的执业法律专家标注相关法条，检索语料为 32 部比利时法典中的 22,633 条法条。作者比较了 TF-IDF、BM25、零样本与微调双编码器，最好的是在 BSARD 上训练的 two-tower CamemBERT，测试集 R@100=74.78%。已读正文全部、附录 A–C（法典清单、指标定义、数据说明书）；Table 2 与 Table 3 数值从提取文本逐列核对。

[原文](https://aclanthology.org/2022.acl-long.468)

版本：ACL 2022 Long Papers，pp.6789–6803（2022.acl-long.468），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2，PDF pp.1–3 |
| 方法 | §3.1 数据构建、§4 检索模型，PDF pp.3–6 |
| 评测 | §5、Table 2，PDF pp.7–8；附录 B 指标定义，p.12 |
| 局限 | §6.1，PDF p.8；附录 C 数据说明书，pp.12–14 |
