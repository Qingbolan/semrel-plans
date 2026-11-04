# Liu, Pena, Santos, Wu, Freire — Magneto: Combining Small and Large Language Models for Schema Matching

本文提出 Magneto：把模式匹配拆成“小模型（SLM）检索候选 + 大模型（LLM）或二分图重排”两阶段，并用 LLM 生成的合成列微调 SLM，不需要人工标注训练数据。作者还与生物医学专家共建 GDC 基准（10 个源表对 1 个 736 列的 GDC 目标表）。

在 GDC 上，Magneto 各变体的 MRR 与 Recall@GT 均高于传统与 LM 基线；在 Valentine 数据上与基线持平或更好（Unicorn 例外，作者归因于训练数据泄漏）。关键数字：GDC 上 Magneto-ft-llm（llm-aug 微调）MRR 达 0.866（Table 5，PDF p.11），而现有最佳方法在该任务上 MRR 最多 0.45（Figure 1，§1）。已阅读正文 §1–§8 与全部表格，并渲染核对 Table 3 与 Figure 6（PDF p.8）。

[原文](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)

版本：PVLDB 18(8): 2681–2694, 2025，doi:10.14778/3742728.3742757，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1（定义 2.1–2.3），PDF pp.1–4 |
| 方法 | §2.2、§3、§4，PDF pp.3–7（Figures 2–5、Table 2） |
| 评测 | §5、§6、Tables 3–6、Figures 6–11，PDF pp.7–12；Table 3/Figure 6 已渲染核对 |
| 局限 | §6.1（Unicorn 泄漏说明）、§8 结论与未来工作，PDF pp.8、12 |
