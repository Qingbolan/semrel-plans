# Zhang et al. — TAIJI: MCP-based Multi-Modal Data Analytics on Data Lakes

这是一篇愿景/系统设想论文：提出基于 Model Context Protocol（MCP）的多模态数据湖分析系统 TAIJI，由宿主 LLM 智能体把自然语言查询翻译为分层语义算子（NL2Operator），再分派给各模态专用的 MCP 服务器执行，并以深度研究式数据增强与机器遗忘刷新知识。初步实验只在 Craigslist 家具数据集的 3 条查询上与纯 GPT-4.1 比较，报告平均延迟降低 43%。已通读全文 §1–§6。

[原文](https://arxiv.org/abs/2505.11270)

版本：arXiv 2505.11270v1（2025-05-16），13 页（正文 11 页 + 参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1，pp.1–4 |
| 方法 | §3（客户端管理器、服务器管理器、增强器），pp.4–9 |
| 评测 | §4、Table 1、Fig.6–8，pp.9–11 |
| 局限 | §5 挑战与机会、§6 结论，p.11 |
