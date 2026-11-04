# Urban & Binnig — ELEET: Efficient Learned Query Execution over Text and Tables

本文提出 ELEET：在关系查询计划中加入多模态算子（MMOps：scan、join、union、selection、aggregation），用约 1.4 亿参数、抽取式解码的小语言模型从文本中按需抽取表格值，而不是调用 GPT 类 LLM。作者自建 4 个数据集、70 个查询计划的基准；每个数据集只用 64 篇标注文本微调时，ELEET 比所有基线都快，最多快 575 倍，F1 通常不低于基线。已阅读正文 §1–§8 与附录 A；主结果以散点/密度图呈现，正文没有逐查询数值表，本解析不从图上读数。

[原文](https://arxiv.org/abs/2410.22522)

版本：arXiv:2410.22522v1（2024-10-29，技术报告，PVLDB 论文扩展版），23 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§3，PDF pp.1–6 |
| method | §3–§5（数据模型与代数、ELEET-model 结构与预训练、MMOp 实现、预训练语料），PDF pp.3–12 |
| evaluation | §6 Exp.1–7、Tables 3–5、Figures 7–13，PDF pp.12–17；附录 A 查询清单 pp.22–23 |
| limitations | §6.1 基线与硬件说明、§6.7、§8，PDF pp.12–13、16–18 |
