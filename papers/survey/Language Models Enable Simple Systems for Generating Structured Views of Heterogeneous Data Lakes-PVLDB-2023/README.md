# Language Models Enable Simple Systems for Generating Structured Views of Heterogeneous Data Lakes

目标是在不做领域训练的前提下，把异构文档（网页、邮件、PDF）自动变成可查询的表。本文提出 Evaporate，比较两种实现：让 LLM 逐文档直接抽取（Evaporate-Direct），或让 LLM 从少量样例生成抽取函数再批量运行（Evaporate-Code）。后者便宜但质量差；Evaporate-Code+ 生成多个候选函数，并用适配后的弱监督聚合。

在 16 个真实设置上，Evaporate-Code+ 平均 OpenIE Pair F1 66.7，比 Direct 高 10.1 分（18%），LLM 处理的 token 平均少 110 倍；在 SWDE 上也超过需要领域训练的 DOM-LM 等基线（Tables 2–3）。

[原文](https://arxiv.org/abs/2304.09433v3)

版本：arXiv 2304.09433v3（2025-03-07）；正式发表于 PVLDB 17(2):92–105（2023），DOI 10.14778/3626292.3626294，目录按正式发表信息归档。已核读 §1–4、Figures 1–5、Tables 1–5 及附录相关部分，数字已对照全文核对，未复现实验。
