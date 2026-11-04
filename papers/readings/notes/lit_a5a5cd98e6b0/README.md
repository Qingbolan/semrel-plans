# Glenn et al. — BlendSQL: A Scalable Dialect for Unifying Hybrid Question Answering in Relational Algebra

本文提出 BlendSQL：一个 SQLite 超集方言，用 {{LLMMap}}、{{LLMQA}}、{{LLMJoin}}（及事实核查用的 LLMValidate）等“ingredient”函数把 LLM 推理嵌入 SQL，把表格+文本混合问答的多跳分解编码为一条可解释、可执行的查询。用 GPT-4-0613 与约 10 个上下文示例，在 HybridQA dev 上 BlendSQL+端到端回退达 57.76（端到端 49.13），且提示 token 更少；在 FEVEROUS 上不如端到端。已阅读正文、局限与附录 A–C 及 Table 6。

[原文](https://arxiv.org/abs/2402.17882)

版本：arXiv:2402.17882v2（2024-06-10，cs.CL），14 页。PDF 本身未印出会议名；Sema-SQL 等后续论文将其引为 Findings of ACL 2024。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1（含问题分解、Agents、Hybrid QA、BINDER 对比），PDF pp.1–3 |
| method | §2 Ingredients 与 §2.3 查询优化，pp.3–4；§4.1–4.2 预处理与上下文学习，pp.5–6；附录 A–B，pp.12–13 |
| evaluation | §3 数据集、§4.3 指标、§5 结果（Table 2–4、Figure 4）、§6 错误分析、§7 开放模型（Table 5），PDF pp.4–9 |
| limitations | Limitations 节，p.10；§5.3 FEVEROUS 失败原因，p.7；§8 未来工作，p.9 |
