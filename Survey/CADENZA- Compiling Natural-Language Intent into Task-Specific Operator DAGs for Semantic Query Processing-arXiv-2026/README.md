# CADENZA

**CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing**

- 作者：Jaehyun Ha、Yongjoo Park、Wook-Shin Han。
- 来源：[本地原文](2606.29151v3.pdf)，arXiv:2606.29151v3；PDF 标注版本日期为 2026-07-13，共 27 页。
- 发表状态：按 arXiv 预印本归档。首页虽出现 SIGMOD ’27，但同时保留 2018 年、Woodstock 和占位 DOI；不能据此确认录用或正式会议年份。本次依据用户提供的 PDF，未核验外部发表记录。
- 定位：将单个语义算子实例编译为 typed task DAG，并联合优化质量、延迟和成本。

## 阅读入口

- [出发点分析](出发点分析.md)
- [解决的问题分析](解决的问题分析.md)
- [Novelty 分析](Novelty分析.md)

## 与本项目的关系

它是“显式暴露中间任务输出以实现数据系统优化”的直接相关工作。比较重点应是已绑定输入上的任务优化与执行中发现数据、补充证据的边界，不能把 CADENZA 描述为没有逐记录适应、批量执行或复用能力。

- [Workload：问题、数据、具体用例与Baseline](workload分析.md)

阅读更新（2026-10-07）：补充核读实验设置、基线、案例与结论边界；未复现实验。
