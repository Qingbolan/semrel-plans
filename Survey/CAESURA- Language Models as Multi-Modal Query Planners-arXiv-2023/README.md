# CAESURA: Language Models as Multi-Modal Query Planners

传统查询规划器只能把 SQL 翻译成关系计划，无法查询数据湖中的图像和文本。本文提出用 LLM 做查询规划：CAESURA 把自然语言查询分发现、逻辑规划、物理映射三阶段翻译成含 SQL、VisualQA、TextQA、Python 和绘图算子的多模态计划，物理映射与执行交替进行，出错时由 LLM 判断回退到哪个阶段。

在作者自建的 Artwork（表+图）与 Rotowire（表+文本）两个数据集共 48 个查询上，假定检索完美时，GPT-4 生成正确逻辑计划 93.8%、正确物理计划 87.5%；ChatGPT-3.5 分别为 64.6% 和 56.2%（Table 1）。

[原文](https://arxiv.org/abs/2308.03424v1)

版本：arXiv 2308.03424v1（2023-08-07，TU Darmstadt，7 页愿景论文；PDF 中的会议模板是占位信息，不据以认定发表）。已通读 §1–6、Figures 1–4、Tables 1–2，数字已对照全文核对，未复现实验。
