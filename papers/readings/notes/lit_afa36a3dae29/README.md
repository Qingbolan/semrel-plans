# You et al. — DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation

DatawiseAgent 是以 notebook 为中心的数据科学 agent 框架：所有交互都表示为 markdown/代码单元，由有限状态转换器（FST）在 DFS 式规划、增量执行、自调试、后过滤四阶段间切换。在 InfiAgent-DABench、MatplotBench、DSBench 数据建模三个基准上，用 GPT-4o、GPT-4o mini、Qwen2.5-72B 评测；DSBench 任务成功率 98.64%，RPG 最高 53.18。已读正文、成本附录与实现细节，结果表已渲染核对；提示词附录只浏览了部分。

[原文](https://arxiv.org/abs/2503.07044)

版本：arXiv:2503.07044v2（2025-10-03），25 页（正文 8 页 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–2，PDF pp.1–3 |
| method | §3、Algorithm 1、Figure 2–3，附录 C、Table 8，PDF pp.3–5、12–13 |
| evaluation | §4、Tables 1–5、Figure 4–5，附录 A Tables 6–7、D.1，PDF pp.5–8、12–14；Tables 1–5（pp.6–7）已渲染核对 |
| limitations | Limitations、Ethics Statement，PDF p.8 |
