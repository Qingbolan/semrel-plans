# Yu, Xu et al. — Visual Document Understanding and Reasoning: A Multi-Agent Collaboration Framework with Agent-Wise Adaptive Test-Time Scaling

本文提出 MACT：把视觉文档问答拆成规划、执行、判断、作答四个经训练的智能体，判断智能体只负责发现错误并退回，测试时对不同智能体采用不同的扩展方式。三个约 24–28B 总参数的变体在 15 个基准上的平均分为 74.8–77.2，相对基模型高 9.9–11.5 点，也高于 Gemini-2.0-Pro 与 70B 级开源模型。所读 v2 共 10 页，不含正文引用的附录，训练数据与提示细节因此无法核对。

[原文](https://arxiv.org/abs/2508.03404)

版本：arXiv:2508.03404v2（2025-11-14），10 页；该版本正文引用的附录 7–8 与 Tab. 8 未随 PDF 提供（v1 为 15 页含附录，未作为本次证据）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1，pp.1–2 |
| method | §2.1–2.3、Algorithm 1、Figures 2–3，pp.2–5 |
| evaluation | §3–4、Tables 1–5、Figure 4，pp.5–8 |
| limitations | 无独立局限节；§4.2 修正次数讨论，p.8 |
