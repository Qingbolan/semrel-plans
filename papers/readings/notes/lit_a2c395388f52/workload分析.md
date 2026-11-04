# workload

评测共 44 条语义 SQL：(1) 作者自建 30 条混合查询，覆盖四个 schema——BookReview（3 表，平均 682 行）、Yelp（3 表，1,594 行）、GoogleLocal（2 表，1,040 行）取自 DataAgentBench，TPC-H（SF=0.005，8 表，平均 10,851 行）（Table 1）。DataAgentBench 的原始问题是自然语言或基础 SQL，作者把其中的意图人工翻译为 SP/SF/SJ 语义算子；TPC-H 查询则在文本列上加了语义谓词。Q1–Q3 使用 SP，Q4–Q30 使用 SF，Q16–Q17、Q25、Q27–Q30 还使用 SJ；最复杂的查询有 9 个连接和 4 个 SF（Figure 5）。(2) SemBench E-Commerce 子集 14 条，有人工标注，但查询通常少于 3 个关系算子。作者认为 SemBench 中多数查询的算子数 ≤3，计划级优化的空间有限，这是自建基准的理由。

与图谱查询的关系（阅读者分析）：本项目从上游仓库固定提交中照搬了 plop/agent-bench 的 Q1–Q30 共 30 条，数量与论文的 30 条混合查询一致；但逐条是否与论文版本完全相同，需另行比对。

依据：[arXiv:2604.09944v2（2026-04-24），13 页](https://arxiv.org/abs/2604.09944)，§1、§6.1，Table 1、Figure 5，PDF pp.2、7–8。
