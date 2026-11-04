# Zhang, Wu, Nan（中山大学 / HKUST）— FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse

用 coding agent 批量做 Android 应用的 source-to-sink 数据流分析时，每个源点由一个上下文隔离的 agent 实例负责，不同源点的路径常汇入同一段回调、分发或组件间通信代码，于是同一段代码被反复阅读和推理。FlowArk 在每个任务完成后让 agent 提炼可复用的“知识条目”，附上基于代码锚点（符号、方法调用、字段、包前缀）的匹配规则；后续 agent 的工具输出一旦命中锚点，就把条目注入其上下文，让它跳过已分析的共享代码。

在 49 个 F-Droid 应用、4,649 个任务上（GLM-4.7，基于 OpenCode），端到端 API 费用从 $600.37 降到 $438.81（−26.91%，已计入知识管理费用），输入 token 降 32.23%；抽样人工审计显示质量与标准 OpenCode 相近。

[原文](https://arxiv.org/abs/2607.11308)

版本：arXiv 2607.11308v2（2026-10-10，cs.SE），21 页；2026-11 按 v2 全文通读 §1–8 并重写。早先笔记依据 v1（2026-07-13），v1 的数字为 50 个应用、4,685 个任务、$603.49→$441.59（−26.83%），与 v2 不可混用。会议未定。未复现实验。
