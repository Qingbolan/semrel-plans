# Zhang et al. — ScienceBenchmark: A Complex Real-World Benchmark for Evaluating Natural Language to SQL Systems

本文构建面向三个真实科学数据库（CORDIS 科研政策、SDSS 天体物理、OncoMX 癌症研究）的 NL-to-SQL 基准。每个库由专家写 100 条 Seed 和 100 条 Dev NL/SQL 对，并用 GPT-3 回译管道生成 1,065–2,061 条合成训练对。在 Spider 上表现很好的系统，在 Dev 集上的执行准确率仅 0–60%。已读正文全部章节；表格数字取自 `pdftotext -layout` 文本。

[原文](https://arxiv.org/abs/2306.04743)

版本：arXiv:2306.04743v2（2023-12-05），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–3 |
| 方法 | §3.1–3.4、Algorithm 1、Tables 1–2，PDF pp.3–8 |
| 评测 | §4–5、Tables 3–5，PDF pp.8–11 |
| 局限 | 无独立局限章节；§3.4 合成数据复杂度、§4.2 银标准不过滤、§5.4 讨论，PDF pp.7–11 |
