# Li et al. — Is Large Language Model Good at Database Knob Tuning? A Comprehensive Experimental Evaluation

这是一篇实验评测论文：把数据库旋钮调优拆成旋钮剪枝、模型初始化、旋钮推荐三个子任务，分别用精心设计的提示让 7 个开/闭源 LLM 替代传统方法，并在 SYSBENCH+MySQL 为主的设置及 JOB、PostgreSQL、TiDB、更大机器等变体上比较。核心结果是 LLM 迭代推荐在 3–25 次迭代内达到接近 SMAC/VBO（需 300+ 次）的吞吐，例如 GPT-4-Turbo 9 次迭代达到 155.30 TPS，而 SMAC 用 375 次迭代达到 157.25 TPS。已阅读全文正文 §1–10 及全部表格；未核对 GitHub 产物。

[原文](https://arxiv.org/abs/2408.02213)

版本：arXiv 2408.02213v1（2024-08-05，PVLDB 模板预印本，卷期页码为占位符），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2、Figure 1，PDF pp.1–4 |
| 方法 | §3、Figures 2–3、§4，PDF pp.4–5 |
| 评测 | §5–8、Tables 1–6、Figures 4–6，PDF pp.6–12 |
| 局限 | §6.3–6.4、§9（无独立局限章节），PDF pp.8、12 |
