# Zhao, Liskowski et al.（Snowflake）— Larch: Learned Query Optimization for Semantic Predicates

本文研究 AI SQL 查询中多个 AI_FILTER 组成的 AND/OR 表达式树应按什么顺序求值，以借助短路减少 LLM token 消耗。Larch 在查询执行中在线学习：Larch-A2C 用算子感知的门控图神经网络编码表达式树并以 A2C 学习排序策略；Larch-Sel 用小型 MLP 从预计算的文档/谓词嵌入逐行预测通过概率，再用动态规划求最小期望代价顺序；训练放在后台线程，与 LLM 调用重叠。

在 GovReport、PubMed、BigPatent 上，用缓存的 LLM 判定结果做模拟，Larch-Sel 相对最优下界的 token 超额比 PZ/Quest 低 3–19 倍。已通读正文 §1–5。

[原文](https://arxiv.org/abs/2606.07923)

版本：arXiv 2606.07923v1（2026-06-06，cs.DB；ACM 模板占位会议信息），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.2–2.4、§3.1，PDF pp.1–5 |
| method | §3.2–3.4，PDF pp.5–7 |
| evaluation | §4.1–4.8、Tables 1–4、Figures 3–5，PDF pp.7–12 |
| limitations | §5 第 3–4 段（嵌入可得性、小模型、上游改写、冷启动），PDF p.12 |
