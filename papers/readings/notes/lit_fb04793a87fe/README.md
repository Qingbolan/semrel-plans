# Trirat, Jeong & Hwang — AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML

AutoML-Agent 是一个覆盖“数据检索 → 部署”全流程的多智能体 AutoML 框架。核心机制有三项：检索增强规划（RAP，生成 P=3 个计划）、按角色分解计划后由 LLM“模拟执行”（不实际训练），以及请求、执行、实现三阶段验证。评测覆盖 7 类任务、14 个数据集，各在无约束和有约束两种设置下运行，共 28 个生成模型，每个取 5 次运行平均。有约束设置下平均成功率为 0.871，综合得分为 0.841。已阅读正文 §1–§5，以及附录 A.2–A.4、B.2、B.4 和 Tables 6–9、12。

[原文](https://arxiv.org/abs/2410.02958)

版本：arXiv:2410.02958v2（2025-06-06），ICML 2025（PMLR 267），48 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §3、Figure 2、Algorithm 1，PDF pp.3–6 |
| 评测 | §4、Figure 4–7，PDF pp.6–9；附录 B.2、B.4，pp.18–21；Tables 6–9、12，pp.45–47 |
| 局限 | 附录 A.2、A.4，PDF pp.13–14 |
