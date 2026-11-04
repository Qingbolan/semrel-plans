# Xu, Cui, Shi, Ma et al. — E3-Rewrite: Learning to Rewrite SQL for Executability, Equivalence, and Efficiency

E3-Rewrite 不依赖预定义改写规则，而是训练 LLM 直接生成 SQL 改写：输入前置线性化的执行计划作为“执行提示”，用 GRPO 强化学习按可执行性、等价性、优化器估计代价三项奖励训练，并分两阶段课程（先正确性、后效率）；推理时按 AST 树编辑距离与语义相似度检索示范改写，且把提速超过 1.5× 的等价改写加入示范池。

在 PostgreSQL 14 上的 TPC-H、IMDB(JOB)、DSB（各约 2,000 条查询）上，Qwen 版本平均延迟最低（TPC-H 从 78.81 s 降至 29.67 s），等价率 98.8%–99.6%。已阅读正文全部；训练配置与超参数在补充材料中，未阅读。

[原文](https://arxiv.org/abs/2508.09023)

版本：arXiv:2508.09023v2（2025-08-15），AAAI 2026 版权页模板，9 页（正文约 7.5 页 + 参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Introduction 与 Problem Definition，pp.1–3 |
| method | Methodology（执行提示、GRPO 奖励、课程训练、混合检索），Figs.1–2，pp.3–5 |
| evaluation | Experiments，Tables 1–4、Fig.3，pp.5–7 |
| limitations | 无单列局限章节；阅读者根据实验设置与表格补充 |
