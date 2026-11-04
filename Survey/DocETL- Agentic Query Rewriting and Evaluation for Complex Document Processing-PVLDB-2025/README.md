# DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing

已有的 LLM 声明式数据处理系统（LOTUS、Palimpzest 等）把用户写的算子当作固定的，只优化代价；但在长文档、复杂任务上，单次 LLM 调用的输出质量本身就不够。DocETL 提供基于 YAML 的声明式管道（含新算子 resolve、gather、split），并用 LLM 智能体按 13 条重写指令把易错的算子分解为更简单、更准确的子管道，再由验证智能体在样本上评分与两两比较选出计划。

在四个任务（CUAD 合同条款抽取、Steam 评论时间排序、Black Vault 解密文档地点汇总、BioDEX 药物反应分类）上，优化后的计划比基线准确 21–80%，例如 CUAD 上 F1 0.477，比 LOTUS（0.393）高 21.4%；代价是执行成本上升，如 CUAD 由 0.08 美元增至 1.46 美元，外加 1.58 美元的一次性优化成本。

[原文](https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf)

版本：PVLDB 18(9):3035–3048（2025），doi:10.14778/3746405.3746426。2026-10-14 全文核读，2026-11 复核 §1–7、Tables 1–6、Figures 1–5 的数字；未复现实验。
