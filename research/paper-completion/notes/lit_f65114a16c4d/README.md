# Cecchi & Babkin — ReportGPT: Human-in-the-loop Verifiable Table-to-Text Generation

ReportGPT 是 J.P. Morgan AI Research 的工业短文：先生成一段只含 12 个算子的 Lisp 风格 DSL 程序，再由 Python 解释器在表上执行，最后让 GPT-4 把（程序、结果）写成一句评论；用户对照程序与表格高亮逐句接受或拒绝，接受的样本又作为少样本示例反馈给生成模块。在 HiTab 表格上的小规模用户研究中，PCFG 生成程序的接受率最高（如 3-shot 95.0%、加人工标题 98.0%），但洞察力排名最低，链式 LLM 排名最好（平均名次 1.71）。已阅读全文与附录提示模板说明，pp.3、6 已渲染核对；论文无单独局限性章节。

[原文](https://aclanthology.org/2024.emnlp-industry.39/)

版本：EMNLP 2024 Industry Track，pp.529–537，ACL Anthology 2024.emnlp-industry.39，9 页（含参考文献与附录 A）。批次元数据写作 2025 年，但原文为 2024 年 11 月会议论文。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，PDF pp.1–2 |
| 方法 | §3.1–3.7、Figures 1–2，PDF pp.2–4；附录 A Figures 3–5，PDF p.8–9 |
| 评测 | §4.1–4.4、§5、Tables 1–2，PDF pp.4–6；Table 1/2 已渲染核对 |
| 局限 | 无专门章节；§5 的权衡讨论与阅读者从 §4 设置推断的边界，PDF pp.5–6 |
