# 评测与边界

**基线与模型**：多数类；SVC（tf-idf / GFCC 自训 word2vec 加权平均句向量）；专家编写的规则方法；BiLSTM 与 BiLSTM-CRF（新训词向量 / 预训练句向量）；BERT 线性层、BERT-BiLSTM、BERT-BiLSTM-CRF，各用 bert-base-multilingual-uncased 与 dbmdz/bert-base-german-uncased（§5）。**指标**：正类 Precision/Recall/F1 与 Accuracy，五折平均（§5.4）。

**实验 1（句级二分类，Table 6，五折均值）**：

| 模型 | P | R | F1 | Acc |
|---|---|---|---|---|
| BERT-BiLSTM-CRF（德语） | 0.708 | 0.478 | 0.561 | 0.905 |
| BERT-BiLSTM（德语） | 0.782 | 0.410 | 0.491 | 0.905 |
| BiLSTM-CRF（句向量） | 0.519 | 0.499 | 0.489 | 0.865 |
| 规则 | 0.893 | 0.111 | 0.197 | 0.884 |
| SVC（句向量） | 0.724 | 0.147 | 0.241 | 0.884 |
| 多数类 | 0 | 0 | 0 | 0.872 |

作者结论：引入 BiLSTM（跨句上下文）是关键；CRF 只带来小幅改进（多语 BERT 情形下反而略差）；德语 BERT 在所有配置都优于多语 BERT；新训词向量的 BiLSTM 精度极高但召回仅 0.02–0.03（§6.1）。

**局限**：无德语法律 BERT（§6.1.3）；最佳召回仍低于 0.5；错误几乎都出现在含比例原则的判决中（测试集 37 份无比例原则判决仅 2 句误判，§6.2）。

**评测边界**：未报告折间方差或显著性检验；Accuracy 受 87% 负类主导，不宜用于比较；只评测句级二分类，未评测四步细分类（阅读者分析）。

依据：[Lüders & Stohlmann，AI & Law 33:1051–1078，28 页](https://link.springer.com/article/10.1007/s10506-024-09415-9)，§5–§7、Table 6，PDF pp.14–23。
