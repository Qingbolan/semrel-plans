# Biester, Abdelaal, Del Gaudio — LLMClean: Context-Aware Tabular Data Cleaning via LLM-Generated OFDs

LLMClean 用 LLM 从脏表格的列名和内容自动生成上下文模型（RDF 形式），从中抽取本体函数依赖（OFD），再用这些规则做错误检测，并把检测结果交给 Baran 或插补方法修复。在 IoT（1,000 行）、Hospital（1,000 行）和 CONTEXT（约 99,300 行）三个注入错误的数据集上，作者报告其检测 F1 高于 HoloClean、ED2、Raha 等基线；另在 LM-KBC 上评估提示集成，14 个关系的平均 F1 为 62.53%。已阅读全部正文并渲染 PDF p.10 的 Figures 8–10 核对柱状图；论文仍是 ACM 模板占位的预印稿。

[原文](https://arxiv.org/abs/2404.18681)

版本：arXiv 2404.18681v1（2024-04-29），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2（OFD 类型与数据集分类），PDF pp.1–3 |
| 方法 | §3–5、Figures 1–4、Algorithms 1–2，PDF pp.2–6 |
| 评测 | §6.1–6.2、Table 2、Figures 5–10，PDF pp.6–10；Figures 8–10 已渲染核对 |
| 局限 | §6.3 Discussion、§8，PDF pp.11、13 |
