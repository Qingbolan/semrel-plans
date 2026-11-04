# Ouyang et al. — nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow

nvAgent 是一个面向自然语言到可视化（NL2VIS）的三智能体流程：processor 做数据库描述与模式过滤，composer 用“草图—填充”生成中间表示 VQL，validator 把 VQL 翻译成 Matplotlib 代码并按执行错误回送修正。在 VisEval 上，以 GPT-4o 为骨干时单表/多表通过率为 85.63%/81.07%，比最好基线高 7.88/9.23 个百分点。已阅读正文 §1–§4、局限与附录 A–C；未逐条核对附录 E 的提示词全文，未复现实验。

[原文](https://arxiv.org/abs/2502.05036)

版本：arXiv:2502.05036v1（2025-02-07），33 页（正文 8 页，其余为参考文献与附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2，PDF pp.1–2 |
| method | §3（Figure 2），PDF pp.2–4 |
| evaluation | §4、Tables 1–5、Figure 5，PDF pp.4–7；附录 A–C、Tables 6–9，PDF pp.13–15 |
| limitations | Limitations，PDF p.9；§4.6 错误分析，PDF p.7 |
