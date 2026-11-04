# 评测与边界

比较 BERT、ALBERT、RoBERTa、DeBERTa；采用 AUPR、Precision@80% Recall 和 Precision@90% Recall。片段匹配基于词集合 Jaccard 相似度，阈值 0.5。Table 2 中 DeBERTa-xlarge 的 P@80 为 44.0%，P@90 为 17.8%；这反映高召回下仍有较多复核负担。

不同类别差异明显，论文也分析了训练数据量。结果不构成自动完成合同风险评估的证据。

依据：[arXiv:2103.06268v2, 2021-11-08](https://arxiv.org/pdf/2103.06268v2)，§4、Table 2、Figures 3–6，PDF pp.5–8。
