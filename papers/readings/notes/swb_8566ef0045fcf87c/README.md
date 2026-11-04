# Begimher et al. — SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents

AWS 团队提出 SIR-Bench：由 129 个匿名真实事件模式，经 OUAT 框架在受控 AWS 环境中重放并做 LLM 辅助变体，生成 794 个安全事件响应测试用例（475 TP / 319 FP）。指标包括分诊准确率 M1、新证据发现 M2 和工具使用 M3。作者自己的 SIR 智能体达到 97.1% TP 检出率、73.4% FP 排除率，平均每例发现 5.67 个新关键发现。全文仅 12 页，已完整阅读；数据集与 OUAT 尚未发布（§6），且只评测了一个智能体。

[原文](https://arxiv.org/abs/2604.12040)

版本：arXiv:2604.12040v1（2026-04-13，cs.CR），12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–3 |
| 方法 | §3，PDF pp.3–6 |
| 评测 | §4、Tables 3–6，PDF pp.6–11 |
| 局限 | §4.2.1、§6，PDF pp.10–11 |
