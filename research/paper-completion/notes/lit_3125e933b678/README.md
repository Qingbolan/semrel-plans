# Qiang, Wang, Taylor — Agent-OM: Leveraging LLM Agents for Ontology Matching

本文提出 Agent-OM：用一对共享记忆的 LLM 智能体（检索智能体、匹配智能体）加一组本体匹配工具完成两个本体间类/属性的等价对齐。在 OAEI Conference、Anatomy、MSE 三个赛道上，作者报告其在简单任务上接近长期最优、在复杂和少样本任务上明显更好，但主要结果以图呈现，正文给出的多为排名而非数值（如 Conference 总体 F1 在 2022 年排 3/13，MSE TC2 的 P/R/F1 均最高）。在 CMT-ConfOf 消融中，Agent-OM 消耗约 2.7×10^5 token，LLM-Only 为 6.4×10^5（Figure 9）。

已阅读 PVLDB 正文 §1–§10；附录中的海报、复现说明和 OAEI 2025 参赛报告只浏览，未据其写结论。

[原文](https://arxiv.org/abs/2312.00326)

版本：arXiv:2312.00326v30（2026-10-19），正文为 PVLDB 18(3):516–529，PDF 共 35 页（正文 pp.1–14，其后为海报、复现说明及 OAEI 2025 结果报告）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2，pp.1–3 |
| 方法 | §3、§4（Figure 1、Tables 1–3），pp.3–7 |
| 评测 | §5–§6（Figures 3–12），pp.7–11；Figure 9 已渲染核对 |
| 局限 | §7–§9，pp.11–12 |
