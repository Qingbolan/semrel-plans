# KramaBench: A Benchmark for AI Systems on Data-to-Insight Pipelines over Data Lakes

现有数据科学基准多测孤立步骤（按细粒度提示写代码、text-to-SQL、在整理好的输入上建模），不测“从一整个数据湖出发，自己找文件、清洗、整合、分析并得出结论”的完整流水线。KramaBench（MIT CSAIL）给出 104 个人工整理并求解的任务，覆盖 6 个领域、24 个数据源、1,764 个文件（约 1.7GB），每个任务附参考流水线、关键功能清单和 633 个子任务，从端到端自动化、流水线设计、子任务实现三个层面评估系统。

在完整数据湖设置下，最好的系统（smolagents Deep Research + Claude-3.7）端到端得分 55.83%；只提供正确文件（Oracle）时最高 62.81%；9 名人类从业者为 76.75%。作者据此认为检索不是主要瓶颈，细粒度的数据依赖推理才是。

[原文](https://arxiv.org/abs/2506.06541v3)

版本：arXiv 2506.06541v3（2026-03-05，cs.DB），ICLR 2026 会议论文，首版 2025-06；正文 10 页，含附录共 30 页；资产在 github.com/mitdbg/Kramabench。阅读范围：正文 §1–6 与附录 A–G 中的相关表格；2026-11 对照全文复核数字。未复现实验。
