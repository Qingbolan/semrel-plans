# Wei et al. — RACOON: An LLM-based Framework for Retrieval-Augmented Column Type Annotation with a Knowledge Graph

RACOON 是列类型标注（CTA）的检索增强框架：先把列中单元格链接到 Wikidata 实体，取实体标签或 `instance_of` 三元组，按列汇总计数后写入提示，再让 GPT-3.5 从 255 个 Freebase 类型中选择。在 WikiTables-TURL-CTA 全部 13,025 列测试集上，相对不加 KG 的同一 LLM 提示，micro-F1 最高提升约 0.21（单标签设置，使用真值实体链接）。全文含附录均已阅读，Table 1 已渲染核对；未复现实验。

[原文](https://arxiv.org/abs/2409.14556)

版本：arXiv:2409.14556v2（2024-11-01），NeurIPS 2024 格式短文，8 页（正文 4 页）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1、Figure 1，PDF pp.1–2 |
| 方法 | §2、Figures 2–3，PDF pp.2–4 |
| 评测 | §3、Table 1，PDF pp.3–4（已渲染核对）；附录 A 提示，PDF p.8 |
| 局限 | §2（未做单元格选择、链接失败回退）、§3 链接器分析，PDF pp.2–4；无独立局限章节 |

阅读者分析：脚注标为 NeurIPS 2024，但 4 页正文的篇幅更像研讨会短文；原文未写明具体 track。
