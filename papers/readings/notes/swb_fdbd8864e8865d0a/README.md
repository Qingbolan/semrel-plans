# Hewett & Stede — Extractive summarisation for German-language data: a text-level approach with discourse features

本文为德语报纸评论语料 Potsdam Commentary Corpus（PCC）新建了每篇 3 个关键句的抽取式摘要标注，分析关键句与修辞结构理论（RST）特征（局部核性、全局深度、most-nuclear、关系）的联系，并把这些特征用于逻辑回归、前馈网络和 bi-LSTM 的句子二分类。最佳 FFN 在关键句类上 F1=.506，测试集 ROUGE-1 F1=.690。已通读全文（含附录超参数）；Figure 2、3 只依据正文与图注描述，未渲染核对图中数值。

[原文](https://aclanthology.org/2022.coling-1.63)

版本：COLING 2022 论文集 pp.756–765（ACL Anthology 2022.coling-1.63），10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–2 |
| 方法 | §3–5.2、Table 2、公式 (1)，PDF pp.2–7 |
| 评测 | §5.3、Tables 3–4，PDF pp.6–8；附录超参数 p.10 |
| 局限 | §3.2–3.3、§6，PDF pp.2–3、8 |
