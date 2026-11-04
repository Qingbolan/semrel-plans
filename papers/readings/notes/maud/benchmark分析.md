# 评测与边界

以处理类别不平衡的 AUPR 为主要指标，比较 BERT、RoBERTa、LegalBERT、DeBERTa、BigBird，并区分单任务和多任务。Table 3 单任务 BigBird 总体 AUPR 为 57.8%；复杂类别如 MAE 仍有明显空间。主结果的总体值按问题聚合，不是七个类别分数的简单平均。

§6.3 限定了交易类型和金额范围；主任务不覆盖完整合同的 deal point 抽取，长文本截断也影响多数基线。

依据：[EMNLP 2023, pp.16369–16382](https://aclanthology.org/2023.emnlp-main.1019.pdf)，§4、Tables 3–4、§6.3，PDF pp.4–6。
