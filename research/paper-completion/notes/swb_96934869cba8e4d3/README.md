# Huang, Ma et al. — Modeling Insider Filing Delays in Financial Markets with an Interpretable XGBoost Framework

本文构建 IFD（Insider Filing Delay）数据集——2002–2025 年美国 SEC Form 4 内部人公开市场交易约 405 万条，按"是否超过两个工作日申报期限"标注违规——并提出 MaBoost（Mamba 序列编码器 + XGBoost 分类器）。在三种输入配置下 MaBoost 的 F1 为 94.79 / 99.47 / 96.76，高于 28 个统计、深度序列和编码器基线及多种 LLM 用法。正文对数据规模、标签构造和指标的描述存在多处自相矛盾，且标签由申报延迟直接计算，延迟相关字段又在特征中，见各栏分析。已通读全文（正文 13 页，无附录），未复现实验。

[原文](https://arxiv.org/abs/2507.20162)

版本：arXiv:2507.20162v3（2025-09-27），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Introduction、Related Work，PDF pp.1–2 |
| 方法 | Methodology、Table 1，PDF pp.2–3 |
| 评测 | Dataset and Implementation、Experimental Result、Tables 2–8、Figures 1–3，PDF pp.3–9 |
| 局限 | Discussion、Future Work，PDF pp.9–10 |
