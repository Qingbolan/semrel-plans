# Zeighami, Shankar & Parameswaran — Featurized-Decomposition Join: Low-Cost Semantic Joins with Guarantees

本文提出 FDJ，用于降低语义连接（对两表每对元组用 LLM 判断自然语言谓词）的成本：先用 LLM 自动生成“特征抽取 + 廉价距离比较”的谓词，组合成合取范式（CNF）的“特征化分解”来剪掉非匹配对，再用 LLM 复核候选对，并通过高维阈值的统计分析保证召回目标。在 6 个真实数据集上，FDJ 的成本平均约为 BARGAIN 的一半，最多降低约 10 倍（Movies），最多比理想级联低约 8 倍。已阅读正文 §1–10 及附录 E、I；未逐行核对附录 H 的证明。

[原文](https://arxiv.org/abs/2512.05399)

版本：arXiv:2512.05399v1（2025-12-05，cs.DB），21 页（正文 12 页 + 参考文献 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2（定义 2.1），pp.1–3 |
| method | §3–7、Alg. 1–6，pp.3–9；附录 E 成本分析，p.15；附录 I 提示词，pp.20–21 |
| evaluation | §8、Tables 1–3、Fig. 7–10，pp.9–12 |
| limitations | §6.3 定理条件、§8.2 分类数据集收益小、§8.1 模拟 LLM 调用，pp.8–11；无单独局限章节 |
