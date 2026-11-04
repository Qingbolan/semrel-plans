# Abaskohi, Ramesh et al. — AgentAda: Skill-Adaptive Data Analytics for Tailored Insight Discovery

AgentAda 是一个面向单表数据分析的 LLM 智能体：按用户目标与 persona 生成问题，用混合 RAG 从 74 项分析技能库中检索技能，再据技能文档生成可执行 Python 代码、读图作答并汇总洞见。论文同时发布由 700 个 Kaggle notebook 构建的 KaggleBench 和经 TextGrad 提示优化的 LLM 评审器 SCORER。人评中带技能版本在 Depth of Analysis 上胜率 48.78%（无技能版 27.67%）；KaggleBench QA 精确匹配准确率 90.6%（Table 5）。

已读正文 §1–7 及附录 A–H、K、L 与 Tables 6–16；未逐条审读提示词（附录 I/J）和任务级明细表。

[原文](https://arxiv.org/abs/2504.07421)

版本：arXiv:2504.07421v3（2025-10-13），41 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–3 |
| method | §3（KaggleBench）、§4（AgentAda 流程）、§5（SCORER），Fig.2–3，PDF pp.3–6；附录 A–B、Table 6–7，pp.14–16 |
| evaluation | §6.1–6.5、Tables 2–5，PDF pp.6–10；附录 D–H、K–L、Tables 8–16，pp.17–21、27–29、35–36 |
| limitations | §7 结论与未来工作、Ethics Statement，PDF p.10；无独立 Limitations 节 |
