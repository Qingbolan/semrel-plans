# Sun et al. — AgenticDataBench: A Comprehensive Benchmark for Data Agents

AgenticDataBench 是面向 LLM 数据智能体的端到端数据科学基准：从 6,510 个 Stack Overflow 解答中经 LLM 分解与层次聚类得到 433 个“数据科学技能”，再按技能覆盖从蚂蚁集团真实业务中选出 102 个任务、在 58 个公开数据集上生成并人工修订 242 个任务，共 344 个任务、15 个领域、27.3GB 数据。对 4 种 harness × 3 个 LLM 的 12 个组合评测，最高总分为 CodeX（Kimi-K2.5）48.8%，最低为 CodeX（Claude Sonnet 4.6）31.6%。已阅读全文正文（§1–§7）；该版本无附录，433 个技能的完整清单与各任务评测函数细节正文未列出。

[原文](https://arxiv.org/abs/2607.01647)

版本：arXiv:2607.01647v1（cs.DB，2026-07-02），14 页（含参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、Table 1，PDF pp.1–2 |
| method | §2–§5（技能定义、基准流水线、层次技能抽取、任务选择与生成），PDF pp.2–7 |
| evaluation | §6、Tables 2–5、Figs 5–9，PDF pp.7–12 |
| limitations | §6.2–6.4 中的失败分析与消融、§7，PDF pp.9–12（原文无独立 limitations 节） |
