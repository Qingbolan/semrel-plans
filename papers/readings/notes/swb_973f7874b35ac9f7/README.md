# Deksne et al. — Retrieval-Augmented Generation for Procurement Validation

本文把 RAG 用于拉脱维亚语公共采购文件的合规核查：按检查清单逐题判断采购文件是否满足要求，回答 yes/no/n/a。作者逐一比较文本抽取库、切分大小、嵌入模型、重排序和提示形式；最佳配置（微调 bge-m3 + gpt-4o）在公开采购核查数据集上总体准确率 70.73%。这是一篇 8 页的应用型会议论文，已通读正文与附录提示。

[原文](https://www.scitepress.org/Papers/2026/142494/142494.pdf)

版本：ICAART 2026 第 5 卷，pp.4048–4055，DOI 10.5220/0014249400004052，8 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–3 |
| 方法 | §3–4、Figure 1、附录 1–4，PDF pp.2–6、8 |
| 评测 | §4、Tables 1–4，PDF pp.3–6 |
| 局限 | §4.2、§4.4、§5，PDF pp.4–7 |
