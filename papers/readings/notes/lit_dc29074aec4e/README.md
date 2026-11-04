# Li, Fang et al. — AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark

本文提出 AutoDCWorkflow：给定一张脏表和一个数据分析目的，由 LLM 迭代地选择目标列、检查列质量、生成 OpenRefine 操作及参数，最终输出可复用的清洗工作流和清洗后的表。作者同时构建了一个基准：6 个数据集、96 张表、142 个目的，从答案、列值、工作流三个维度评测。在合并结果中，Gemma 2-27B 的答案 F1 从原始表的 0.2201 提高到 0.6256。已阅读正文 §1–§9，以及附录 A.4–A.6 和 Table 8 的分数据集结果。

[原文](https://arxiv.org/abs/2412.06724)

版本：arXiv:2412.06724v3（2025-08-23），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–4 |
| 方法 | §4、Figure 2、Table 3，PDF pp.3–5 |
| 评测 | §5–§7、Tables 4–7，PDF pp.5–9；附录 Table 8，pp.15 |
| 局限 | §9（Limitation I–V），PDF pp.9–10 |
