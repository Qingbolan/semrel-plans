# Kang et al. — Distilling LLM Agent into Small Models with Retrieval and Code Tools

本文提出 Agent Distillation：把 LLM 智能体（CodeAct 形式）的“思考—行动—观察”轨迹蒸馏到 0.5B–7B 小模型，使其学会调用检索与代码工具，而非只模仿静态思维链。另提出两项改进：教师侧的 first-thought prefix（ftp）与学生推理时的 self-consistent action generation（sag）。在 4 个事实推理和 4 个数学推理基准上，蒸馏后的 0.5B/1.5B/3B/7B 智能体平均分接近或超过大一档的 CoT 蒸馏模型；例如 7B 学生 +ftp+sag 的 8 任务平均为 42.68，高于同规模 CoT 蒸馏的 33.54（Table 2）。已阅读正文 §1–8 与结论/局限；Table 2 以 170 dpi 渲染核对；附录仅粗读。

[原文](https://arxiv.org/abs/2505.17612)

版本：arXiv:2505.17612v2（2025-11-05，NeurIPS 2025），38 页（含附录与清单）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、Figure 2，PDF pp.2–3 |
| 方法 | §3–4、Figure 3，PDF pp.4–5 |
| 评测 | §5–7、Tables 1–4、Figures 4–8，PDF pp.5–10（Table 2 已渲染） |
| 局限 | §8 结论后 “Limitations & Future Works”，PDF p.10；§6 数学结果讨论，PDF pp.7–8 |
