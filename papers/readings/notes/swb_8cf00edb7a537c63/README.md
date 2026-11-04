# Wang, Qian et al. — FinTagging: Benchmarking LLMs for Extracting and Structuring Financial Information

FinTagging 把 XBRL 标注改写为两阶段"抽取–对齐"任务：FinNI 从句子或表格中抽取数值事实及其 5 种类型，FinCL 把每个事实链接到含 17,688 个概念的完整 US-GAAP 分类体系（先向量检索 top-200 候选，再由 LLM 重排）。数据来自 142 份 10-K 的 iXBRL 自动标注，并抽审 1,949 个实例。零样本下 DeepSeek-V3 的 FinNI F1 最高（0.6932），但 FinCL 准确率全都低于 0.19。已通读正文与附录 A–I。

[原文](https://arxiv.org/abs/2505.20650)

版本：arXiv:2505.20650v5（2026-05-17），17 页（ACM 模板，会议信息仍为占位符）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3.1，PDF pp.1–3 |
| 方法 | §3.2–3.6、Algorithms 1–2，PDF pp.3–5；附录 C–G，pp.10–13 |
| 评测 | §4、Tables 5–8，PDF pp.5–7；附录 A、H–I（Tables 13–14），pp.8、14 |
| 局限 | §4.2–4.4、§5（无独立局限节），PDF pp.6–7 |
