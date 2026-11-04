# Dias, Moreira & Comba — RoBIn: A Transformer-Based Model For Risk Of Bias Inference With Machine Reading Comprehension

本文用 Cochrane 系统综述（CDSR）中的偏倚风险（RoB）判断和引文作远程监督，标注 PubMed 开放获取临床试验论文，构建公开的 RoBIn 数据集（13,554 训练 / 3,404 测试实例）。模型分两步：先从上下文中抽取或生成证据句（MRC），再判断低风险或高/不明风险。抽取式 RoBIn_Ext 的 MRC 总体 F1 为 97.10，RoB 分类宏 F1 为 74.18，两种变体 ROC AUC 均为 0.83。已阅读全文 §1–7。

[原文](https://arxiv.org/abs/2410.21495)

版本：arXiv:2410.21495v1（2024-10-28，当前唯一版本），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §4–5、Figures 1–4，PDF pp.5–10 |
| 评测 | §6、Tables 2–3、Figure 5，PDF pp.10–14 |
| 局限 | §6.5、§7，PDF pp.12–14 |
