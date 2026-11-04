# Feuer, Liu, Hegde, Freire — ArcheType: A Novel Framework for Open-Source Column Type Annotation using Large Language Models

ArcheType 把基于 LLM 的列语义类型标注（CTA）拆成四个阶段：上下文采样、提示序列化、模型查询和标签重映射，并逐一消融。零样本下，它在 SOTAB-27 和作者新建的 D4/Amstr/Pubchem 三个基准上优于或持平两个基于 GPT 方法改造的基线。微调 LLAMA-7B 加规则重映射后，在 SOTAB-91 上的 Micro-F1 为 85.97，超过 DoDuo 的 84.82。已阅读正文 §1–§6；附录中的类别级表格只做了浏览。

[原文](https://arxiv.org/abs/2310.18208)

版本：arXiv:2310.18208v3（2024-08-19），对应 PVLDB 17(9):2279–2292，PDF 共 18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2（Table 1），pp.1–4 |
| 方法 | §3（Algorithms 1–4，Figures 1–3），pp.4–8 |
| 评测 | §4–§5（Tables 2–6，Figures 4–7），pp.8–12；Tables 3–5 已渲染核对 |
| 局限 | §5.5，pp.12–13 |
