# SemBench: A Benchmark for Semantic Query Processing Engines

SemBench 是一个系统级基准，评测对象是“语义查询处理引擎”（SQPE）：这类系统在 SQL 中加入由 LLM 求值的 filter、join、map、rank、classify 等语义算子。基准含 5 个场景、55 条查询，覆盖文本、图像和音频。gold 的做法是用源数据集（主要来自 Kaggle）的人工标签替换语义谓词后执行 SQL 得到。

作者让 LOTUS、Palimpzest、ThalamusDB 和 BigQuery 统一使用 gemini-2.5-flash，同时比较费用、质量和延迟。核心发现是实现方式会带来数量级的成本差异。Movie 场景中，各系统对 LIMIT 的处理不同，使 Q1/Q5/Q6 的费用相差 100× 以上。语义 join 上，ThalamusDB 平均 $0.14、质量 0.487，Palimpzest 为 $3.29、0.703（Table 5）。

[原文](https://arxiv.org/abs/2511.01716v2)

版本：arXiv 2511.01716v2（2026-03-16，cs.DB），共 14 页，PVLDB 模板中的卷期和 DOI 仍是占位。已通读 §1–6、Tables 1–5 和 Figure 1（PDF pp.1–12），表中数值已按本地 PDF 全文核对，未复现实验。
