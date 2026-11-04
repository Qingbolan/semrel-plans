# Gan et al. — Enhancing LLM Medical Coding with Structured External Knowledge

本文提出 RAG-Coding，一种免训练的四步智能体式 ICD-10-CM 编码方法：先由 LLM 生成候选码，再用基于 ICD 表格列表构建的知识图谱审核，然后检索编码指南并生成按码摘要，最后依据摘要复核。同时发布 MDACE-2025，即依照 2025 年指南对 MDACE 测试集的专家重标注，补充了编码顺序和理由说明。在 MDACE 上，RAG-Coding 比最佳 LLM 基线的 micro-F1 高 3–13 个百分点，与监督模型 PLM-ICD 大致持平；在 MDACE-2025 上，GPT-5 骨干比 PLM-ICD 的 micro-F1 高 8 个百分点。已阅读正文 §1–8、Limitations 及附录 B–H。

[原文](https://arxiv.org/abs/2605.27377)

版本：arXiv 2605.27377v2（2026-05-28），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3、§5.1，PDF pp.1–4 |
| 方法 | §4（MDACE-2025）、§5.2–5.5、Fig.1–2，PDF pp.3–5 |
| 评测 | §6–7、Tables 1–4，附录 C、F–H（Tables 5–12），PDF pp.5–8、12–16 |
| 局限 | Limitations，PDF p.9；§7.3 及附录 H 错误分析 |
