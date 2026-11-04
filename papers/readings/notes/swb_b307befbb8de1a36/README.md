# Zhao & Goto — Can Frontier LLMs Replace Annotators in Biomedical Text Mining? Analyzing Challenges and Exploring Solutions

本文先复现此前 GPT-4 在生物医学 NER、关系抽取和多标签分类上的评测，归纳出三类失败原因：未学到数据集隐含特征、结构化输出压制推理、未遵循标注指南。随后用动态 few-shot、两步推理、自动提示优化和“从标注指南检索指令”改进 GPT-4o：在 LitCovid（F1 0.873 对 0.861）和 BC5CDR-RE（0.781 对 0.650）上超过基线，其余 5 个数据集仍低于微调 BERT。用 GPT-4o 标注新文献蒸馏出的 BioLinkBERT 接近人工训练集效果。已阅读正文与附录 7.1–7.4。

[原文](https://arxiv.org/abs/2503.03261)

版本：arXiv:2503.03261v2（2025-05-17），21 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2、Table 2，PDF pp.1–6 |
| 方法 | §3.1–3.3、附录 7.3，PDF pp.6–10、20–21 |
| 评测 | §4、Tables 3–7、附录 7.2 Tables S2–S3，PDF pp.10–13、20；Table 5 已渲染核对 |
| 局限 | §5、附录 7.4，PDF pp.13、21 |
