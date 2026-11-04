# Hu et al. — InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks

InfiAgent-DABench 是评估 LLM 智能体做数据分析的基准：智能体读取 CSV、在 Python 沙箱中写代码并执行，最后给出答案。为了自动评测，作者用 GPT-4 把开放式问题加上约束和 `@answer_name[answer]` 格式要求，变成可用正则抽取、精确匹配的封闭式问题。公开验证集 DAEval 含 52 个 CSV、257 个问题；34 个模型中 GPT-4 最高（78.99%）。作者还用 DAInstruct 训练了 DAAgent。

已阅读正文 §1–5 和附录 A、C、D、H、J、K、L、P、Q；提示模板附录仅浏览。

[原文](https://arxiv.org/abs/2401.05507)

版本：arXiv:2401.05507v3（2024-03-11），27 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §2.1–2.5（Figure 2、Tables 1–4），PDF pp.3–6；附录 J、K、L，PDF pp.13–14 |
| 评测 | §3（Figures 5–6、Table 5），附录 D、P、Q（Tables 6、23），PDF pp.6–8、14–16、26 |
| 局限 | 附录 A，PDF p.12；附录 H 的评估器试点，PDF p.13 |
