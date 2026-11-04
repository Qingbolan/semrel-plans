# Ai, Tang, Wang — NLI4VolVis: Natural Language Interaction for Volume Visualization via LLM Multi-Agents and Editable 3D Gaussian Splatting

本文是一个面向科学体数据可视化的自然语言交互系统。它先对多视角渲染图做语义分割，再为每个语义部件训练可编辑的 3D 高斯模型，并用 CLIP 支持开放词汇查询，最后由分层的多智能体 LLM 通过函数调用和声明式命令来编辑场景。评估包括 8 个数据集的案例研究和 8 人用户研究，没有定量对比基线。已读正文与附录 §1–4。

[原文](https://arxiv.org/abs/2507.12621)

版本：arXiv:2507.12621v1（2025-07-16，IEEE TVCG 模板预印本，含附录），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2、Table 1，PDF pp.1–3 |
| 方法 | §3.1–3.5、Figure 2，PDF pp.3–6 |
| 评测 | §4、Table 2–3、Figures 5–10，PDF pp.6–9；附录 §1–4，PDF pp.9–11 |
| 局限 | §5，PDF p.9；附录 §2–3，PDF pp.10–11 |
