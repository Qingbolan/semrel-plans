# Data Interpreter: An LLM Agent For Data Science

数据科学流程由相互依赖的多步任务组成，中间数据和报错会改变后续步骤，一次性生成全部代码难以持续修正。Data Interpreter（Hong、Lin 等，DeepWisdom / MetaGPT 团队）用分层图建模：先把需求拆成任务图（DAG），每个任务再展开为由代码片段组成的动作图；执行失败时修复代码，仍失败则重生成任务图并复用未变化的已完成任务。

在 InfiAgent-DABench 上，配 gpt-4o 的准确率为 94.93%，比直接调用 gpt-4o（75.92%）高 19.01 个百分点（相对 25%）；ML-Benchmark 综合分 0.95，开放任务完成率 0.97（§4.2，Tables 1–3）。

[原文](https://arxiv.org/abs/2402.18679v4)

版本：arXiv 2402.18679v4（2024-10-15，cs.AI），29 页；正式发表于 ACL Findings 2025（不要把 2024 预印本日期写成 ACL 2024）。已通读正文 §1–5 与附录 A、D.1–D.2，数字已对照 PDF 复核（2026-11）；未复现实验。
