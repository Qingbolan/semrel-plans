# Unstructured Data Analysis using LLMs: A Comprehensive Benchmark

本文提出 UDA-Bench，用来评测基于 LLM 的非结构化数据分析（UDA）系统。基准包含 5 个数据集，共 10 万余篇文档，跨艺术、体育、法律、金融、医疗五个领域。30 名研究生花了约 10,000 小时，为 147 个属性人工标注出关系表作为 gold。在此基础上，作者用 SQL/代码模板生成 240 条查询。

作者在统一的 GPT-4.1-mini 下比较了 7 个系统（Evaporate、Palimpzest、LOTUS、DocETL、ZenDB、QUEST、UQE），并逐项拆解逻辑优化与物理优化策略。短文档数据集上，多数系统的抽取 F1 约 0.85；长文档数据集上，最好的系统也只有约 0.5–0.66。按文档分块能节省 token，但可能漏掉证据；DocETL 在 Finance 上每篇文档每条查询约消耗 818K token（Table 3）。

[原文](https://arxiv.org/abs/2510.27119v1)

版本：arXiv 2510.27119v1（2025-10-31，cs.DB），共 13 页。已通读 §1–6、Tables 1–4 和 Figures 1–14，并对照 p.10 的渲染页核对了 Table 3–4。正文多处提到的附录不在这个版本里，本文不声称读过附录。
