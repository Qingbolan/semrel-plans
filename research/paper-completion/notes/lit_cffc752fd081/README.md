# Salemi et al. — LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science

本文提出一种受经典黑板架构启发的 LLM 多智能体系统：主智能体把请求贴到共享黑板，各自负责数据湖一个文件簇的 file agent 与一个 web search agent 自主决定是否响应，主智能体最终生成可执行 Python 程序回答数据科学问题。在 KramaBench 及作者改造的 DSBench、DA-Code（加入"先找文件"环节）上，相对最佳基线端到端成功率提升 13%–57%（相对值），文件发现 F1 最高相对提升约 9%。

已阅读正文全部及附录 A、D、F 的数据与补充实验；未逐一审阅附录 C 的提示词全文和 G 的样本 ID 列表。

[原文](https://arxiv.org/abs/2510.01285)

版本：arXiv 2510.01285v2（2026-01-31），44 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，pp.1–3 |
| method | §3（含 3.1–3.2），pp.4–6；附录 D，p.29 |
| evaluation | §4、Tables 1–2、Figure 2，pp.6–10；附录 A Table 3，p.19；附录 F 与 Table 4、Figures 18–23，pp.31–41 |
| limitations | §6 结论与未来工作，pp.11–12（原文无独立局限性章节） |
