# Li, Zhou, Zhou, Sun, Luo, Fan — Data Agents: Agentic Data Systems

本文提出“Data Agent”范式：一个在最少人工干预下自主管理、处理和分析数据的数据系统，由六个组件构成——语义数据组织、语义算子、智能体式流水线编排与优化、反馈闭环、记忆管理、主动适应，并在其上设计数据分析智能体与数据科学智能体。它把自然语言任务编排成由 SQL、关系算子、语义算子（semantic filter/join/group/extract）和系统 API 组成的流水线，再用多候选交叉验证、合成数据检查、Pipeline2NL 等手段检查语义错误。

以 Qwen 3 为骨干，DABStep 上 easy/hard 准确率 94.44%/50.79%，Spider 2.0-Lite 上执行准确率 44.50%，均列各自排行榜表第一；平均每查询耗时比基线快 2.32×（DABStep）和 1.45×（Spider 2.0-Lite）（§6，Tables III–V）。

[原文](https://arxiv.org/html/2609.24137v1)

版本：arXiv 2609.24137v1（2026-09-21，cs.DB；IEEE TKDE 模板占位卷期），14 页。阅读范围：2026-11-04 对照 PDF 全文重读 §1–8、Algorithm 1、Tables I–VII 并核对数字；未复现实验，未查看代码。
