# Yan, Xi, Hou — MCTuner: Spatial Decomposition-Enhanced Database Tuning via LLM-Guided Exploration

MCTuner 是 PostgreSQL 参数（knob）调优框架：先用 7 个领域 LLM "专家"组成的 MoE 结合手册/网页/LLM 知识选出关键 knob 并收窄取值范围，再以 MCTS 引导的空间递归划分（聚类 + 软间隔 SVM）配合 BO 在高潜力子空间中采样。在 8 个 OLAP/OLTP/HTAP 基准、各 100 次迭代的设定下，作者报告相对最强基线最高 19.2% 的性能提升，单次迭代算法耗时 5.54 s。已阅读正文全部章节；正文多次提到的附录（LASSO 与 zero-shot LLM 的详细分析）在该 arXiv 版本中不存在。

[原文](https://arxiv.org/abs/2509.06298)

版本：arXiv:2509.06298v1（2025-09-08），16 页（ACM 模板，会议信息为占位符）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1（挑战 C1–C3）、§3 问题定义，PDF pp.1–4 |
| method | §4–6、Figure 1–5、Algorithm 1–2，PDF pp.4–9 |
| evaluation | §7.1–7.4、Figure 6–11、Table 1–3，PDF pp.9–14 |
| limitations | 无独立局限章节；§8 结论的未来工作，p.14；§7.4.1 迁移不一致的说明，p.13 |
