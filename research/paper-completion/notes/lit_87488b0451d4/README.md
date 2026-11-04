# Wang et al. — FDABench: A Benchmark for Data Agents on Analytical Queries over Heterogeneous Data

FDABench 是评测“数据智能体”在异构数据（关系库、文档、网页、图像、视频、音频）上回答分析型查询的基准，含 2,007 个任务（单选、多选、报告），由 LLM 驱动的 PUDDING 框架加专家审核从 4,127 个候选中构造（接受率 48.6%）。

作者评测了 6 个通用分析智能体、3 个语义算子框架（LOTUS、Palimpzest、DocETL）、4 个 RAG 方法，以及 12 个 LLM × 4 种工作流模式；主要结论是性能更多取决于分析流水线拓扑与工具编排质量，强“思考”模型叠加复杂工作流可能适得其反。已阅读正文 §1–7 与附录 A–D；评分细则与难度标注细节在外部技术报告中，未阅读。

[原文](https://arxiv.org/abs/2509.02473)

版本：arXiv:2509.02473v3（2026-08-15，KDD ’26 版本），12 页。早期 v1/v2 的任务数与实验可能不同，本文笔记只依据 v3。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1–3.2、Table 1，pp.1–3 |
| method | §4 数据集构造与 PUDDING、§4.3 评测框架、附录 B–C，pp.4–6、11–12 |
| evaluation | §5、Tables 3–10、Fig. 4–6，pp.6–9 |
| limitations | §5.1 复现说明、§5.2–5.5、§6，pp.6–9；无单独局限章节 |
