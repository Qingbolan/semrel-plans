# Agent Workflow Memory

网页智能体做长步骤任务时，每个任务都从头摸索，不会复用以前做过的子过程。AWM（Wang、Mao、Fried、Neubig，CMU/MIT）让 LM 从成功轨迹中归纳“工作流”：带参数的常用子过程（如“按名称找地点”），并写入智能体记忆指导后续任务。它支持离线（从训练样例归纳）和在线（边做测试任务边归纳，用 LM 评估器判断是否成功）两种模式。

在 WebArena 上，GPT-4 下任务成功率 35.5%，比 BrowserGym 的 23.5% 相对提高 51.1%，也超过使用 14 个人写工作流的 SteP（33.0%）；在 Mind2Web cross-task 上步骤成功率相对 MindAct 提高 24.6%（36.2→45.1）。已核读正文 §1–7 与附录 A–C，数字已对照 v1 全文。

[原文](https://arxiv.org/abs/2409.07429v1)

版本：arXiv 2409.07429v1（2024-09-11，cs.CL），16 页；[作者代码](https://github.com/zorazrw/agent-workflow-memory)。会议未核实。阅读范围：正文与附录全文（2026-11-04 复核），未复现实验。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.1，PDF pp.1–2 |
| method | §2.2–2.3、Figures 2–4，pp.2–4；附录 A.1 提示词，p.14 |
| evaluation | §3–5、Tables 1–9、Figures 5–7，pp.4–10；附录 A.3、C（Tables 10–11），pp.15–16 |
| limitations | 无独立章节；散见 §3.2.1（偏离工作流）、§3.2.2（在线误判）、§4.3（HTML 噪声）、§5（Figure 7 动态页面） |
