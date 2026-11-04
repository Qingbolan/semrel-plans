# Du, Yan et al. — MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

MLEvolve 是一个面向端到端机器学习工程（MLE）的 LLM 多智能体搜索框架：把候选解组织成带"参考边"的有向图（Progressive MCGS），配合检索式经验记忆和"规划—编码"分离的多种代码生成模式。论文报告在 MLE-Bench 75 个 Kaggle 任务上以 12 小时预算取得 65.3% 平均奖牌率（3 个种子），并在 AlphaEvolve 的 15 个数学优化任务上声称 11 项最好。已阅读正文 §1–5 及附录 A–H；未审计附录 C 证明细节，未复现实验。

[原文](https://arxiv.org/abs/2606.06473)

版本：arXiv:2606.06473v2（2026-10-22），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–3、5 |
| method | §3.2–3.4、附录 A–B、E（Table 4），PDF pp.5–9、16–19 |
| evaluation | §4、Tables 1–3、附录 D、F、G（Tables 5–6），PDF pp.9–12、18–20 |
| limitations | 原文无独立局限性章节；§5 仅列未来工作（PDF p.13），局限由阅读者从实验设置归纳 |
