# EviRCA: Decoupling Evidence Extraction from Reasoning for Microservice Root-Cause Analysis

现有 LLM 根因分析智能体（如 OpenRCA 的 RCA-Agent）让一个模型在原始遥测上反复写代码，同时负责取证、定位和归因，开销大且不稳定。EviRCA 把异常检测与候选定位交给确定性代码，把指标、调用链和日志压缩成"证据卡"，LLM 只通过少量只读工具在证据卡上判断根因，不读原始遥测、不执行代码；系统差异全部放在一个声明式适配器里。

在 OpenRCA 三个系统共 335 个案例上，EviRCA 用两种 LLM 的 Correct 率为 40.6–43.9%，同模型基线最高 15.2%；token 减少 15–26 倍，单案例时间缩短 3.2–19.6 倍。失败分析显示主要瓶颈是对已呈现证据的判断，而不是找证据。

[原文](https://arxiv.org/abs/2609.19825v1)

版本：arXiv 2609.19825v1（2026-09-17，浙江大学等，cs.SE；发表会议待确认），PDF SHA-256 `ae9600133948bfbc97694ffdae88ae6d4f2140deb24dbb44d6c579062aa36b51`。已通读 §I–V、Figures 1–4、Tables I–VI，数字已对照全文核对，未复现实验。
