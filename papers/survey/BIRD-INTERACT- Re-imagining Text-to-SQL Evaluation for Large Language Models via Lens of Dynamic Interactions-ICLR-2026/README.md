# BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation for Large Language Models via Lens of Dynamic Interactions

单轮 text-to-SQL 基准衡量不了真实数据库助手要做的事：澄清含糊需求、查找缺失的业务知识、根据执行报错调试，以及在修改过的数据库状态上继续回答后续问题。BIRD-INTERACT 在 LiveSQLBench 之上构建交互式基准：每个数据库配分层知识库、元数据文件和一个“函数驱动”的用户模拟器，任务覆盖 BI 查询与数据管理类 CRUD，并用可执行测试用例判定对错。

基准含 FULL 600 题与 LITE 300 题，每题两个有状态依赖的子任务，分对话式 c-Interact 和智能体式 a-Interact 两种设置。在 FULL 上，最好的模型端到端完成率也只有 16.33%（c-Interact，Gemini-2.5-Pro）和 17.00%（a-Interact，GPT-5）；GPT-5 在 c-Interact 只完成 8.67%。

[原文](https://arxiv.org/abs/2510.05318v3)

版本：arXiv 2510.05318v3（2026-03-24），ICLR 2026，PDF 49 页。2026-10-07 初读；2026-11 按全文核对正文 §1–9、Tables 1–3 及附录 A、F、H.5、J；未复现实验。
