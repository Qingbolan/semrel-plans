# Li, Zhang, Fan et al. — Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search

Alpha-SQL 把零样本 Text-to-SQL 看作在“部分推理状态”树上的搜索：用 MCTS 在 7 种 SQL 构造动作（问题改写、schema 选择、列值识别、列函数识别、SQL 生成、SQL 修正、终止）间探索，由 LLM 执行每个动作（LLM-as-Action-Model），并以候选 SQL 与多次采样 SQL 执行结果的一致性作为无标注奖励。使用不微调的 Qwen2.5-Coder-32B，在 BIRD dev 上执行准确率 69.7%，高于基于 GPT-4o 的零样本方法 RSL-SQL（67.2%）。已读正文 §1–6 与附录 A.1 算法；附录提示词仅浏览。

[原文](https://arxiv.org/abs/2502.17248)

版本：arXiv:2502.17248v2（2025-06-15，ICML 2025 / PMLR 267 版式），21 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–3 |
| method | §3.2、§4（动作空间 Table 1、MCTS、值检索），PDF pp.3–7；附录 A.1，p.12 |
| evaluation | §5、Tables 2–5、Fig.4–5，PDF pp.7–9 |
| limitations | 无独立局限章节；§5.1 子采样开发集说明、Impact Statement，PDF pp.7、9 |
