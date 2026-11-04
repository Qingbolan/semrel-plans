# Chen, Ren, Ma, Shi — Large Language Models for Predictive Analysis: How Far Are They?

本文提出 PredictiQ 基准，用 44 个公开表格数据集、8 个领域、1,130 条专家编写的预测分析问题，评测 12 个 LLM 在"给定问题与整表 CSV，输出文字分析 + 代码"时的表现。评分覆盖文本、代码、文本-代码对齐三域七项（每项 0–4 分，满分 28），主评审为 GPT4Turbo（与专家对齐率 90.5%）；最高的 GPT4O3Mini 总分 24.11，但仍有 51% 代码缺少预处理。已阅读正文 §1–8 与附录 A–E；未逐格核对附录 Table 12–14 的全部数值。

[原文](https://arxiv.org/abs/2505.17149)

版本：arXiv:2505.17149v1（2025-05-22），18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2（式 1），PDF pp.1–3 |
| method | §3.1–3.4、Table 1，附录 A–C、Table 7–9，PDF pp.3–4、12–15 |
| evaluation | §4.1–4.6、Table 2–6、Figure 2–4，PDF pp.4–8；附录 D、Table 10–16，PDF pp.14–17 |
| limitations | §7 Limitations、§8 Ethics Statement，PDF pp.8–9；§4.6，p.8 |
