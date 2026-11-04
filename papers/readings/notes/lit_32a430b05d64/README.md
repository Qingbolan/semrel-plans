# Yao et al. — A Query Optimization Method Utilizing Large Language Models

本文提出 LLMOpt，把微调后的 LLM（Llama3.1-8B-Instruct）放进 PostgreSQL 的“搜索—选择”查询优化流程：LLMOpt(G) 直接生成 pg_hint_plan 提示作为候选计划，LLMOpt(S) 作为列表式代价模型从 BAO 产生的候选中选出最优计划的下标。在 JOB、JOB-EXT、Stack 上两者的执行时延都低于 PostgreSQL、BAO、HybridQO；计入推理开销后只有 LLMOpt(S) 在端到端时延上全面领先。已读正文全部章节与 Tables 1–5。

[原文](https://arxiv.org/abs/2503.06902)

版本：arXiv:2503.06902v1（2025-03-10），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§4.1，PDF pp.1–2、5 |
| method | §3.2–3.3、§4.2、§5–§7，PDF pp.4–8 |
| evaluation | §8、Tables 1–5、Figure 6，PDF pp.8–12 |
| limitations | 无独立章节；§8.1、§8.6、§9，PDF pp.9–12 |
