# Lin et al. — Towards Accurate and Efficient Document Analytics with Large Language Models

本文提出 ZenDB：利用模板化文档（论文、市政议程、违规通知）共享的视觉格式，抽取语义层次树（SHT），让用户用扩展 SQL 定义"文档表"，并以带摘要的树搜索、谓词下推和投影上拉执行查询。在三个真实文档集合上，ZenDB 相对整篇文档调用 GPT-4-32k 的基线成本最多降低约 29×，精度与召回相当或更好；相对 RAG 基线，精度最多高 61 个百分点、召回最多高 80 个百分点。已阅读全文 §1–9；Figure 11–14 的柱值未逐项核对。

[原文](https://arxiv.org/abs/2405.04674)

版本：arXiv:2405.04674v1（2024-05-07），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1（Example 1.1、Figures 1–3）、§2，PDF pp.1–4 |
| 方法 | §3 SHT 构建（Theorem 3.1、Algorithm 1）、§4 数据模型与查询语言、§5 表填充、§6 查询引擎（Algorithms 2–3），PDF pp.4–11 |
| 评测 | §7.1–7.2、Tables 1–7、Figures 11–14，PDF pp.11–13 |
| 局限 | §4.2 查询子集与一致性说明、§9 Conclusion 未来工作，PDF pp.7、14 |
