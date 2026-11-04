# Wei, Liu, Tay et al. — CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage

CORTEX 是面向安全运营中心（SOC）告警分诊的多智能体 LLM 架构：编排、行为分析（路由到工作流）、证据获取（调用 SIEM、身份、资产等类型化工具）和推理协调四类角色共同产生可审计的分诊报告。在作者自建的生产环境 SOC 调查轨迹数据集上，与使用相同工具的单智能体 ReAct 基线相比，可行动类 F1 从 0.66 升到 0.78，误报率从 24.9% 降到 14.2%，但中位延迟从 44.6 秒增至 152.4 秒。本文为 7 页短文加 10 页工作流提示附录，已全部阅读。

[原文](https://arxiv.org/abs/2510.00311)

版本：arXiv:2510.00311v1（2025-09-30，预印本），17 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2，PDF pp.1–3 |
| 方法 | §3.1–3.2、Tables 1–3、Figure 1，PDF pp.3–5；附录 A.1–A.10，pp.9–17 |
| 评测 | §4.1–4.3、Tables 4–5，PDF pp.5–6 |
| 局限 | §5 Limitations and Future Work，PDF p.7 |
