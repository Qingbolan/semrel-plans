# Dong & Wang — From Interpretation to Compilation: A Compilation-Based Execution Engine for Semantic Operator Systems

本文提出 SemBaker：一个外挂式“编译执行”引擎，对选中的 sem_filter / sem_map / sem_join 只调用一次 LLM 生成确定性 Python 函数，再在本地逐行/逐对执行，用代价模型逐算子决定走原生（LLM 解释）还是编译路径，并让编译与执行重叠。在 ManyModalQA、HybridQA、MMQA 三个 200 题 QA 工作负载上，相对 PZ/LOTUS/Nirvana 原生执行平均加速 4.8–6.3×、成本降低 5.4–10.7×，质量“接近”原生。全文 6 页均已阅读（含 Tables 1–3）。

[原文](https://arxiv.org/abs/2608.06677)

版本：arXiv:2608.06677v1（2026-08-07），6 页（ACM 模板，会议信息仍为占位符）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Figure 1，PDF pp.1–2 |
| method | §2.1–2.4、Figure 2，PDF pp.2–4 |
| evaluation | §3.1–3.4、Tables 1–3，PDF pp.4–6 |
| limitations | §2.2 末（可编码性筛查）、§2.4（refine/validate 默认关闭）、§3.1（排除图像题）、§3.4 消融讨论，PDF pp.3–5 |
