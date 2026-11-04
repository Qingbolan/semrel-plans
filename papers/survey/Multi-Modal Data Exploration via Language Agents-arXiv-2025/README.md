# Nooralahzadeh, Zhang, Fürst, Stockinger（ZHAW）— Multi-Modal Data Exploration via Language Agents

本文研究如何用自然语言同时查询关系数据库与图像、文本报告等非结构化数据。系统 M2EX 让 GPT-4o 规划器把问题直接编译成工具调用 DAG（text-to-SQL、文本分析、VQA、数据准备、绘图），独立节点并行执行，工具自调试一次，由决策器检查结果并按需局部重规划。

在 ArtWork、RotoWire 上相对 CAESURA，准确率由 33.33%/25.00% 升至 63.33%/66.67%；在 EHRXQA 100 题上相对 NeuralSQL（10-shot）由 33% 升至 51%（Tables 1–2）。

[原文](https://arxiv.org/abs/2412.18428v2)

版本：arXiv 2412.18428v2（2025-11-25，cs.AI），v2 将系统名改为 M2EX；目录按 v2 标题与年份归档。已通读正文 §1–5、Limitations、附录 A–E；2026-11 按全文重新核对数字，未复现实验。
