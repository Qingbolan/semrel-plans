# Taboada et al. — Ontology Matching with Large Language Models and Prioritized Depth-First Search

本文提出 MILA，一种零样本、基于 LLM 的本体匹配方法。它在"先检索再提示"之间加入"识别"步骤：若两个实体在 SBERT 候选列表中互为第一，就直接接受为高置信双向匹配；其余边界情况按相似度顺序做优先深度优先搜索，逐个询问 LLM，遇到第一个"是"就停止。在 OAEI 2024 的 7 个任务上，作者报告 MILA 在无监督设置下 5 个任务的 F 值最高，运行时间也远低于先检索再提示的基线。全文已读，附录 A 只浏览了系统特征表的说明。

[原文](https://arxiv.org/abs/2501.11441)

版本：arXiv:2501.11441v2（2025-03-27，投稿 Elsevier 期刊的预印本），25 页；PDF 第 1 页为 Highlights，PDF 页码 = 印刷页码 + 1。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3，PDF pp.2–6 |
| 方法 | §4.1–4.4、Algorithm 1，PDF pp.6–11 |
| 评测 | §5、Tables 1–9，PDF pp.11–19 |
| 局限 | §6.1，PDF pp.20–21 |
