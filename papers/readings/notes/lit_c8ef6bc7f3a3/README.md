# Cai, Sheen & Doan — Columbo: Expanding Abbreviated Column Names for Tabular Data Using Large Language Models

本文研究把缩写列名（如 "eSal"）扩展为英文短语（"employee salary"）。贡献有三：在 NameGuess 公开合成数据外新增四个含真实人工缩写的企业/科学数据集；提出同义词感知的 EM/F1 指标；提出 Columbo（Summarizer 聚类摘要 + Generator 规则与 token 级 CoT + Reviser 跨列一致性修正）。

在五个数据集上同义词感知 EM 比 NameGuess 高 4–29 个百分点（如 University 92.2% vs 63.2%）。已阅读正文、Limitations 与附录 A.2，并渲染核对 Tables 1–5。

[原文](https://arxiv.org/abs/2508.09403)

版本：arXiv:2508.09403v3（2025-09-23），19 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，pp.1–3 |
| method | §3–§5，pp.3–6；附录 A.2–A.5 |
| evaluation | §6，pp.6–8，Tables 1–5（已渲染） |
| limitations | §6 末、§8、Limitations，pp.8–10 |
