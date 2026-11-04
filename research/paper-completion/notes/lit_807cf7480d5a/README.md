# Luo et al. — nvBench 2.0: Resolving Ambiguity in Text-to-Visualization through Stepwise Reasoning

nvBench 2.0 是面向“含歧义自然语言查询生成可视化”的基准：一条查询对应多个合理图表（1→n），并附有逐步消歧推理路径。数据集含 7,878 条查询、24,076 个可视化，来自 153 个领域的 780 张表；作者同时提出在该数据上用 SFT + Step-DPO 训练的 Step-Text2Vis（Qwen2.5-7B），F1@3 达 81.50%，比直接提示 GPT-4o 高 22.54 个百分点。已阅读正文 §1–§6 与附录 B、D、E、F；未逐项核对附录 C 的全部统计图和全部提示模板。

[原文](https://arxiv.org/abs/2503.12880)

版本：arXiv:2503.12880v3（2026-01-04，标注 NeurIPS 2025 Datasets and Benchmarks Track），38 页（正文 10 页）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Table 1，PDF pp.1–3 |
| method | §2.1（数据合成）、§3（Step-Text2Vis），PDF pp.3–6；附录 B，PDF pp.24–29 |
| evaluation | §4、Table 3、Figures 4–5，PDF pp.6–10；附录 D–E，PDF pp.32–33 |
| limitations | 附录 F，PDF p.34 |
