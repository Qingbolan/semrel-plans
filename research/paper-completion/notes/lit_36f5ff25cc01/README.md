# Bendinelli, Dox & Holz — Exploring LLM Agents for Cleaning Tabular Machine Learning Datasets

本文是 ICLR 2025 “Foundation Models in the Wild” 研讨会论文：作者固定预处理和训练流水线，只允许 LLM 通过 IPython 修改被人为注入系统性错误的训练集，并用一个评估工具返回在干净测试集上的分数。

四个模型（gpt-4o、o3-mini、claude-3-5-sonnet、gemini-2.0-flash-exp）在三个 Kaggle 数据集上都未达到干净数据的性能；它们能修正单值或单行层面的错误，但难以发现跨多行的分布偏移、趋势和偏差。Hotel Bookings 上所有模型提升都不足 1%；gemini-2.0-flash-exp 在 200k token 预算下 Titanic 提升 3.69%，放宽到 2M token 后为 8.88%（Fig. 2、Table 2）。已阅读正文 §1–5 与附录 A（错误注入、提示词）。

[原文](https://arxiv.org/abs/2503.06664)

版本：arXiv:2503.06664v1（2025-03-09，ICLR 2025 Workshop on Foundation Models in the Wild），14 页（正文 9 页 + 参考文献 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，pp.1–2 |
| method | §3（数据集构造、清洗智能体）、附录 A.1–A.2，pp.2–4、12–14 |
| evaluation | §4、Fig. 2–4、Tables 1–4，pp.4–8 |
| limitations | §5.2，p.9 |
