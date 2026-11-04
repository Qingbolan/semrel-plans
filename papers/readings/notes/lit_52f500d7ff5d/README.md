# Sahu et al. — InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation

InsightBench 是面向“端到端业务数据分析智能体”的基准：100 个基于 ServiceNow 表结构合成的表格数据集（每个 500 行），由标注者预先植入趋势/异常（共 475 条 insight），要求智能体从一个高层目标出发自行提问、写代码、解读结果并给出总结与行动建议。作者同时提出基线智能体 AgentPoirot，在 gpt-4o 上的 insight 级 LLaMA-3-Eval 为 0.60，高于 Pandas Agent 的 0.54。已阅读正文 §1–7 与附录 A、B.1–B.3、C；未逐条审读附录 D 的全部提示词与附录 B.5 的流程图细节。

[原文](https://arxiv.org/abs/2407.06423)

版本：arXiv 2407.06423v4（2025-02-27，ICLR 2025 会议版），33 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、Figure 1，PDF pp.1–3 |
| 方法 | §2.1–2.4、§3.1、附录 B.1–B.3，PDF pp.3–7、14–19 |
| 评测 | §2.2、§3.2、§4、Table 1、Figure 4、附录 C Table 4、Figure 8，PDF pp.5、7–9、20 |
| 局限 | §7、附录 A，PDF pp.10、14 |
