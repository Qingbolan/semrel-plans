# Leban, Saarinen & Sun — CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

CausalDS 是一个面向数据科学智能体的因果推理基准：每个实例（scene）由一个采样的结构因果模型（SCM）、按其生成的表格数据（可带噪声测量层）、一段与因果图一致的合成自然语言故事以及覆盖 Pearl 三层阶梯的任务组成，不可识别的目标以"弃答"为正确答案。论文报告 12 个智能体在 100 任务"真实组成"考试与 200 任务"困难"考试上的结果：结构恢复近乎饱和，而可识别性判断、弃答和区间估计明显分化（真实考试由 GPT-6 Astra 领先，困难考试由 GLM 5.3 领先）。已阅读正文 §1–6 与附录 A.9、A.10（部分）、A.17、A.18；未逐项核对 A.11–A.16 的全部误差分类与消融表。

[原文](https://arxiv.org/abs/2607.08093)

版本：arXiv:2607.08093v2（2026-10-14），74 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–2 |
| method | §3.1–3.8（场景生成、观测层、任务、评分），PDF pp.3–5；App. A.9，pp.28–31 |
| evaluation | §4、Tables 1–2、Figs. 3–4，PDF pp.6–8；App. A.10、Table 17，pp.30–33 |
| limitations | App. A.17，PDF pp.60–61；App. A.18 执行设置，p.61 |
