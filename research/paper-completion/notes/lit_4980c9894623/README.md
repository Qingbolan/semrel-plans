# Pourreza et al. — CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL

CHASE-SQL 是 Google Cloud 与 Stanford 提出的 Text-to-SQL 框架：用三种生成器（分治 CoT、查询计划 CoT、在线合成示例）产生多样候选 SQL，经查询修正后，由微调的二元选择模型做两两比较选出最终答案。论文报告 BIRD dev 73.01%、BIRD test 73.0% 执行准确率，Spider test 87.6%。已阅读正文 §1–5 与附录 A.1–A.5、A.9/Table 8；未逐页审读全部提示词附录。

[原文](https://arxiv.org/abs/2410.01943)

版本：arXiv:2410.01943v1（2024-10-02），30 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、Table 1，PDF pp.1–2 |
| 方法 | §3.1–3.5、Alg.1–3，PDF pp.3–6；附录 A.2，p.14 |
| 评测 | §4、Tables 2–7，PDF pp.7–11；附录 A.4、Table 8，pp.16–19、28 |
| 局限 | 无独立局限章节；附录 A.4 错误分析，PDF pp.16–20 |
