# DiscoveryBench: Towards Data-Driven Discovery with Large Language Models

本文问：给定数据集和一个自然语言研究目标，LLM 智能体能否自己设计分析流程、得出数据支持的假设？作者把假设形式化为“上下文—变量—关系”三要素，从 20 多篇已发表论文中人工复现出 264 个真实任务（DB-REAL，6 个领域），另用 LLM 合成 903 个任务（DB-SYNTH，48 个领域），并用按三要素打分的 HMS 指标评测。最好的智能体在 DB-REAL 上也只有约 25 分（满分 100）。

[原文](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d70af566e69f1dfb687791ecf955e28-Paper-Conference.pdf)

版本：ICLR 2025 正式会议版，24 页（已替换最初取得的 arXiv v1）；2026-11 重新取得全文，按 §3–5、Figure 1/4/7、Table 2、附录 A/D 核对本目录数字。未复现实验。
