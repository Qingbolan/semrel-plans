# A Declarative System for Optimizing AI Workloads

- 系统：PALIMPZEST，早期愿景与原型论文。
- 作者：Chunwei Liu、Matthew Russo、Michael Cafarella、Lei Cao、Peter Baille Chen、Zui Chen、Michael Franklin、Tim Kraska、Samuel Madden、Gerardo Vitagliano（按本版本署名）。
- 来源：[原文](2405.14696v2.pdf)，arXiv:2405.14696v2，2024-05-29；首页标为预印本，按 arXiv-2024 归档。
- 版本边界：本次仅分析此 v2，不混同后续 CIDR Palimpzest 论文或 Abacus 的能力与实验。

## 阅读入口

- [出发点分析](出发点分析.md)
- [解决的问题分析](解决的问题分析.md)
- [Novelty、Strong points 与 Weak points](Novelty分析.md)

## 对本项目的直接影响

本文支持“明确语义任务已有系统化执行优化”这一前提。它已经讨论数据获取与语义处理交错，并实现中间 Dataset 缓存，因此不能把语义系统概括为只能处理结构化输入或没有结果复用。其原型仍由用户指定数据源、转换、过滤及依赖，未研究开放式探索的跨记录组织。

- [Workload：问题、数据、具体用例与Baseline](workload分析.md)

阅读更新（2026-10-07）：补充核读实验设置、基线、案例与结论边界；未复现实验。
