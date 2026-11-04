# DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?

已有数据科学评测多是短指令、单模态、只考代码补全，与真实任务差距大。DSBench（Jing、Huang 等，Tencent AI Lab 实习工作）从 ModelOff 金融建模竞赛收集 466 道数据分析题、从 Kaggle 收集 74 个端到端建模任务，题目带长背景描述、多表 Excel、图片和大数据文件，并提出相对性能差距（RPG）统一不同建模指标。

最好的 agent（AutoGen + GPT-4o）在分析题上只答对 34.12%，人类在抽样的 10 个 challenge 上为 64.06%；建模任务中最高 RPG 为 AutoGen + GPT-4 的 45.52，人类为 65.02（Tables 4、6）。

[原文](https://arxiv.org/abs/2409.07703v2)

版本：arXiv 2409.07703v2（2025-02-22，cs.AI），ICLR 2025 会议论文，56 页（含附录）。该版本分析任务来源写作 ModelOff。这是 benchmark 论文，底层题目来自已有竞赛。已通读正文 §1–5 与附录 B、E、F，数字已对照 PDF 复核（2026-11）；未复现实验。
