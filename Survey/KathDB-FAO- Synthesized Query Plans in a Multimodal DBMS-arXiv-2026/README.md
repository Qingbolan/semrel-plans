# KathDB-FAO

**KathDB-FAO: Synthesized Query Plans in a Multimodal DBMS**

- 作者：Guorui Xiao、Douglas Brown、Artur Borycki、Magdalena Balazinska。
- 来源：[原文](2609.28761v1.pdf)，arXiv:2609.28761v1，2026-09-23。
- 发表状态：按 arXiv-2026 归档。首页 PVLDB 卷期、2020 年及 DOI 含模板占位信息，不能作为正式发表依据；本次未外部核验。
- 定位：从自然语言生成多模态查询计划，通过原子动作分解、契约、动作融合及函数复用减少模型推理与规划成本。

## 阅读入口

- [出发点分析](出发点分析.md)
- [解决的问题分析](解决的问题分析.md)
- [Novelty、Strong points 与 Weak points](Novelty分析.md)

## 对本项目的直接影响

本文已经支持根据中间结果生成代码、按组提前停止推理及让历史函数影响后续规划。不能将“查询级规划”一概描述为执行前固定所有实现或不能利用中间观察。需要进一步区分这些能力与执行中发现未绑定数据源、判断新增证据需求及跨记录共享探索。

- [Workload：问题、数据、具体用例与Baseline](workload分析.md)

阅读更新（2026-10-07）：补充核读实验设置、基线、案例与结论边界；未复现实验。
