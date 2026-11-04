# Jiang et al. — StructGPT: A General Framework for Large Language Model to Reason over Structured Data

StructGPT 提出“迭代读取-推理”（IRR）框架：为知识图谱、数据表和数据库各设计少量读取接口，让 LLM 按“调用接口-线性化-生成”循环逐步筛选证据，最后给出答案或 SQL。实验覆盖 8 个数据集；零样本下，ChatGPT 在 WebQSP 的 Hits@1 提升 11.4 个百分点，TabFact 准确率提升 4.2 个百分点，Spider 执行准确率提升 4.7 个百分点，但整体仍多低于全监督 SOTA。已读正文、局限章节和附录 A–B。

[原文](https://aclanthology.org/2023.emnlp-main.574/)

版本：EMNLP 2023 正式版（ACL Anthology 2023.emnlp-main.574，pp.9237–9251），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–3 |
| 方法 | §4.1–4.4、Figure 1，PDF pp.3–6 |
| 评测 | §5、Tables 1–3、Figures 2–3，PDF pp.6–9；附录 A Table 4，PDF p.14 |
| 局限 | §7 Limitations，PDF p.10；§5.4 错误分析，PDF pp.8–9 |
