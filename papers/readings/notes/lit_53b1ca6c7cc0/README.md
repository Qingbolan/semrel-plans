# Li et al. — Harnessing Generalist Agents for Contextualized Time Series

本文提出 TimeClaw：一个包在冻结 LLM 策略外面的“时间序列原生”agent harness，由可执行时序工具（MCP 工作区，全精度数值）、经验驱动的能力演化（把重复的子过程蒸馏成新工具）和多模态情节记忆（文本嵌入 + 20 维序列指纹两阶段检索）组成。在 CiK、TSRBench（20% 分层子集）和 TSAIA 金融多选题上，以 GPT-5-nano 为骨干报告了优于各类基线的结果，并在 TSRBench 上使用最少 token。已阅读正文 §1–6 与附录 A–C、E、F（部分）、H；未逐项核对全部附录表格与 prompt 模板。

[原文](https://arxiv.org/abs/2606.05404)

版本：arXiv 2606.05404v1（2026-06-03），38 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2（式 1–6），PDF pp.1–3；附录 A |
| method | §3.1–3.4（式 7–12），PDF pp.3–5；附录 B–C（指纹与两阶段检索），pp.15–22 |
| evaluation | §4、Tables 1–3、Figures 3–5，PDF pp.5–8；附录 E.1–E.4、Tables 7–11，pp.23–27；附录 H.2–H.3 |
| limitations | 正文无独立 Limitations 节；§2.2 与附录 A 讨论的是“直接用 LLM”的局限。本笔记的局限为阅读者整理 |
