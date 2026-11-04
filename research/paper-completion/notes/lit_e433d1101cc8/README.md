# Huang et al. — MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation

MLAgentBench 是评测 LLM 智能体端到端做机器学习实验的基准：13 个任务，每个任务给出任务描述、起始文件（代码与数据）和自动评测器，智能体可读写文件、执行 Python 并最终提交结果。作者同时给出基于 ReAct 的智能体（带研究计划与事实核查条目）；7 种 LM 中 Claude v3 Opus 平均成功率最高（37.5%），但在近期 Kaggle 挑战与 BabyLM 上接近 0。已阅读正文 §1–6、附录 A–E，附录 F 的完整提示样例只浏览。

[原文](https://arxiv.org/abs/2310.03302)

版本：arXiv:2310.03302v2（2024-04-14），39 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。Tables 3–4 已渲染核对。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，pp.1–2 |
| 方法 | §2（任务规格、环境、评测、任务）、§3（智能体），pp.2–6；Tables 1–2 |
| 评测 | §4、Tables 3–5、Figures 3–6，pp.6–9、15；附录 B–E，pp.15–18 |
| 局限 | §4.1–4.3 失败模式与成本，pp.7–8；附录 D.2–D.3，pp.17–18；正文无独立局限章节 |
