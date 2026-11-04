# Zhang et al. — Benchmarking Data Science Agents

论文提出数据科学智能体的评测范式 DSEval：把查询和运行时会话作为输入，用一组可组合的验证器检查生成代码、执行结果和会话状态（包括原始数据是否被意外修改）。作者用 DSEAL 标注语言和“LLM 自举 + 人工修订”流程构建了四个基准，共 825 个问题，并评测了 Chapyter、ChatDev、CoML、Code Interpreter API、Jupyter-AI 五个智能体。

主要结果（GPT-3.5 后端，Table 2）：CoML 在 Kaggle（59.8%）、Exercise（78.6%，与 Jupyter-AI 并列）和 SO（78.2%）上通过率最高，Jupyter-AI 在 LeetCode 上最高（57.5%）。已读正文和附录 E。

[原文](https://arxiv.org/abs/2402.17168)

版本：arXiv:2402.17168v1（2024-02-27），23 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§3、Figures 1–3，PDF pp.1–3 |
| 方法 | §3.2、§4、Figures 4–6，PDF pp.3–5；Appendix E，PDF pp.16–17 |
| 评测 | §5–§6、Tables 1–5、Figures 7–13，PDF pp.5–9；p.7 已渲染核对 |
| 局限 | Limitations、Table 5，PDF p.9 |
