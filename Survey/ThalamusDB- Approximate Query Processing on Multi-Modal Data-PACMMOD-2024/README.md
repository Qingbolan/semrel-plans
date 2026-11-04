# ThalamusDB: Approximate Query Processing on Multi-Modal Data

带自然语言谓词的多模态 SQL 查询（如“图片里是木椅”）要对图像、音频、文本逐项跑神经模型，推理开销远超关系运算。Jo 与 Trummer 提出 ThalamusDB：用零样本模型（CLIP、Sentence-BERT、BART、音频模型）给数据打相似度分，向用户要少量标签来确定分数阈值，只处理一部分数据就给出必定包含真实值的确定性上下界；多目标优化器按用户对误差、计算时间、标注数的约束与权重，决定先处理哪些数据、何时请求标签。

在 YouTube、Craigslist、Netflix 三个基准上，ThalamusDB 在 MindsDB 能运行的 12 个文本查询上平均快 35.0 倍（10% 误差界）；与基于采样的 ABAE 相比，在多数配置下代价更低（91.1% / 67.7%，对 ABAE_max / ABAE_min）。确定性界的前提是神经模型和阈值正确。

[原文](https://saehanjo.github.io/assets/files/thalamusdb.pdf)

版本：Proc. ACM Manag. Data 2(3)（SIGMOD 2024），Article 186，26 页，doi:10.1145/3654989。2026-10-07 初读；2026-11 按全文核对 §1–2、§4、§7（Table 4–5、Figures 7–16）；未复现实验。
