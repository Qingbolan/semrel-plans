# Multi-Objective Agentic Rewrites for Unstructured Data Processing

DocETL 的原优化器只优化准确率，不考虑成本；而且语义算子之间相互影响，局部最优的子计划拼起来不一定全局最优。MOAR（Wei、Shankar 等，UW / UC Berkeley / Google）为 DocETL 新增 18 条改写指令（总数超过 30，含代码合成、算子融合与重排），把“整条流水线”作为搜索节点，用改编自树上 UCB 的多臂老虎机算法在有限评估预算内挑选下一个要改写的流水线，返回准确率—成本 Pareto 前沿。

在六个文档处理工作负载上，MOAR 的最高准确率平均比次优优化器 Abacus 高 27%，并能以其 55% 的成本达到 Abacus 的最高准确率（§5.2，Tables 4–5）。

[原文](https://arxiv.org/abs/2512.02289v4)

版本：arXiv 2512.02289v4（2026-04-01，cs.DB），24 页。已通读 §1–5、结论及附录相关表，数字已对照全文复核（2026-11）；未复现实验。
