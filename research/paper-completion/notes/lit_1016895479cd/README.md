# Zhao, Huang, Li et al. — LLMIA: An Out-of-the-Box Index Advisor via In-Context Learning with LLMs

LLMIA 是一个免微调的 LLM 索引推荐器：离线用 GPT-4-Turbo 合成 SQL 工作负载、用多种启发式索引算法标注"当前索引 → 调整动作"示例，在线以列/谓词/统计特征加相似示例构造提示，让 GPT-4o-mini 多次采样候选动作、投票合并后按数据库反馈（估计代价或实测延迟）择优迭代。在 PostgreSQL 上与 12 个基线比较，实测延迟模式 LLMIA(L) 仅需 10 次收益评估，在 TPC-H、JOB、SSB 上多为最优或接近最优；但其在线推荐时间可能很长（TPC-H SF=50 平均约 82,819 秒）。

已阅读正文全部 12 页；Figure 4/5 只有柱状图，未逐柱读数。

[原文](https://arxiv.org/abs/2503.07884)

版本：arXiv 2503.07884v2（2026-03-19），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §I、§III-A，pp.1–3 |
| method | §III-B、§IV、§V，pp.4–7 |
| evaluation | §VI、Tables I–VII、Figures 4–5，pp.7–11 |
| limitations | §VII 讨论（微调对比、应用场景、写负载），p.12 |
