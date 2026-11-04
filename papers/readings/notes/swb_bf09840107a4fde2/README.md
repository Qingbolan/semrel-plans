# Lim et al. — PANORAMA: A Dataset and Benchmarks Capturing Decision Trails and Rationales in Patent Examination

本文发布 PANORAMA：8,143 份美国专利审查记录（2015–2024），保留原始申请、审查员引用的现有技术、首次非最终驳回（Non-Final Rejection）、最终权利要求和授权通知，并用 GPT-4o 把驳回书解析为逐条权利要求的结构化理由。

基于此构造三个按审查流程排列的权利要求级基准：现有技术检索（PAR4PC）、段落定位（PI4PC）和新颖性/非显而易见性判定（NOC4PC）。12 个 LLM 在前两项上明显好于随机，但在 NOC4PC 上多数接近随机基线 32.33。

已读正文 §1–§5 与附录 A–C 中数据统计、清洗、专家验证、任务构造与评测部分；未逐项核对附录全部分领域结果表。

[原文](https://papers.neurips.cc/paper_files/paper/2025/file/4aab82c8d6b77c0b6b010145c1bfcdd3-Paper-Datasets_and_Benchmarks_Track.pdf)

版本：NeurIPS 2025 Datasets and Benchmarks Track 会议版（含附录），52 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头，PDF pp.1–2、5–6 |
| 方法（数据采集、解析、专家验证、任务构造） | §2、附录 A.5、B.1–B.4、C.2.2、C.3.2、C.4.2，PDF pp.3–5、25–27、32–35、37、40–41、44 |
| 评测 | §3.1–3.5、Tables 2–3、附录 C.2.3、C.3.3、C.4.3、Table 17，PDF pp.6–8、37、41、43、45 |
| 局限 | §4、附录 D.2，PDF p.9、52 |
