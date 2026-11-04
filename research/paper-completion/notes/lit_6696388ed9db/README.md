# Islam et al. — DataNarrative: Automated Data-Driven Storytelling with Visualizations and Texts

本文提出"数据故事生成"任务：给定数据表、标题和用户意图，生成多段文字与可视化规格交替的故事；并发布含 1,449 个故事（Pew、Tableau、GapMinder）的基准。方法为 Generator/Critic 两个 LLM 智能体，依次执行反思、提纲、叙述三步，每步生成-审查-修订，共 9 次调用。以 GPT-4o 为底座时，Gemini-1.5-pro 评审的成对胜率 78.17%（直接提示 20.05%），人评平均胜率 71.2%。已阅读正文 §1–6、Limitations、Ethics 与附录 A.3–A.5、Table 8 与错误示例。

[原文](https://aclanthology.org/2024.emnlp-main.1073/)

版本：EMNLP 2024 主会论文，Proceedings pp.19253–19286，34 页（ACL Anthology PDF 2024.emnlp-main.1073）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§4.1 任务定义，PDF pp.1–2、5 |
| 方法 | §3 基准构建、§4 框架、Figure 2，PDF pp.3–6；附录 A.3–A.4，p.14 |
| 评测 | §5、Tables 4–7，PDF pp.6–8；附录 Table 8，p.18 |
| 局限 | §5.5 错误分析、Limitations，PDF pp.8–9 |
