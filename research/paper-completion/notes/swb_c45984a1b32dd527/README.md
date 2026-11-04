# Lei, Yan, Momo & Cohen — Learning Reusable Agent Subroutines from Experience

本文提出 ARISE：从 ReAct 智能体的成功轨迹中归纳反复出现的推理步骤，合成为一个小型“智能体子程序”库。每个子程序是带固定签名的自然语言规格，由一次独立 LLM 调用执行。在 MuSR 三个任务、RuleArena NBA 和 Natural Plan 会议安排上，DeepSeek-V3 与 Gemini 2.5 Flash 的五任务平均为 67.4% 和 77.7%，高于 CoT、PoT、ReAct、AWM、ACE、ASI。同一段归纳文本作为子程序执行，比作为检索技能或改写成 Python 工具更好。批次标题 “Inducing Reasoning Primitives from Agent Traces” 是 v1 标题；本笔记读的是 v2。已读正文 §1–6 和附录 A–L。

[原文](https://arxiv.org/abs/2606.02994)

版本：arXiv:2606.02994v2（2026-10-14），27 页；v1（2026-06-02）题为 “Inducing Reasoning Primitives from Agent Traces”，v2 改为现标题。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–4 |
| 方法 | §3.2–3.3、附录 C，PDF pp.4–5、16–17 |
| 评测 | §4–5、Tables 1–5、附录 D–K（Tables 6–18），PDF pp.5–9、17–26 |
| 局限 | §3.2 末段、附录 L，PDF pp.5、27 |
