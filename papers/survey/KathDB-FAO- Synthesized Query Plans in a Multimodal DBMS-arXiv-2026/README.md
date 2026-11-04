# KathDB-FAO: Synthesized Query Plans in a Multimodal DBMS

多模态 DBMS 中，自然语言查询没有标准的算子分解，且模型推理是最贵的操作。KathDB-FAO（Xiao、Brown、Borycki、Balazinska，华盛顿大学 / Teradata）把查询计划的每个节点做成执行时合成代码的函数（Function-as-Operator，FAO）：先把查询拆成细粒度原子动作，在样本上执行原子计划，推导上下游契约，再选择哪些动作融合进同一函数，从而表达“找到第五件合格商品即停止”这类跨算子提前终止；合成的函数可跨查询复用。

在 SemBench 的 Movie、E-Com、MMQA 及作者新增的 Additional 场景上，执行成本比次优系统平均降低 58.8%，质量相当或更好（§6.1，Table 2）。

[原文](https://arxiv.org/abs/2609.28761v1)

版本：arXiv 2609.28761v1（2026-09-23，cs.DB），15 页；首页 PVLDB 卷期、2020 年与 DOI 为模板占位，按 arXiv-2026 归档。已通读 §1–8，数字已对照全文复核（2026-11）；未复现实验。
