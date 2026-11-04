# 评测与边界

**模型与基线**（§4.1，p.4）：GPT-3-175B（text-davinci-002，OpenAI API）。基线为 EM 的 Ditto（微调 BERT）与 Magellan；DI 的 IMP（微调 RoBERTa）与 HoloClean；ED 的 HoloClean 与 HoloDetect；模式匹配的 SMAT；数据转换的 TDE。

**实验 1（实体匹配，Table 1，F1）**：

| 数据集 | Magellan | Ditto | GPT3 k=0 | GPT3 k=10 |
|---|---|---|---|---|
| Fodors-Zagats | 100 | 100 | 87.2 | 100 |
| Beer | 78.8 | 94.37 | 78.6 | 100 |
| iTunes-Amazon | 91.2 | 97.06 | 65.9 | 98.2 |
| Walmart-Amazon | 71.9 | 86.76 | 60.6 | 87.0 |
| DBLP-ACM | 98.4 | 98.99 | 93.5 | 96.6 |
| DBLP-Google | 92.3 | 95.60 | 64.6 | 83.8 |
| Amazon-Google | 49.1 | 75.58 | 54.3 | 63.5 |

**实验 2（数据清洗，Table 2）**：填补用 accuracy，错误检测用 F1。

| 方法 | 填补 Restaurant | 填补 Buy | 检错 Hospital | 检错 Adult |
|---|---|---|---|---|
| HoloClean | 33.1 | 16.2 | 51.4 | 54.5 |
| IMP | 77.2 | 96.5 | – | – |
| HoloDetect | – | – | 94.4 | 99.1 |
| GPT3-175B k=0 | 70.9 | 84.6 | 6.9 | 0.0 |
| GPT3-6.7B k=10 | 80.2 | 86.2 | 2.1 | 99.1 |
| GPT3-175B k=10 | 88.4 | 98.5 | 97.8 | 99.1 |

**实验 3（数据集成，Table 3）**：数据转换 accuracy（StackOverflow/Bing）：TDE 63.0/32.0，k=0 32.7/24.0，k=3 65.3/54.0。模式匹配 Synthea F1：SMAT 38.5，k=0 0.5，k=3 45.2。

**实验 4（提示消融，Table 4，≤200 样本）**：去掉属性选择平均降 13.7 F1；"same"改为"equivalent"平均差 9.4 F1；人工示例比随机示例平均高 14.7 F1（随机为 3 个种子）。

**局限**（§4.2.2、§5.2–5.3，pp.5–6）：行话密集领域表现差；隐私数据不能发往第三方 API；FM 非确定、难调试；提示需人工迭代。

零样本 ED 几乎失效（Adult 0.0），说明"SoTA"结论主要取决于人工示例；Walmart-Amazon 上 Prompt 2 反而更高（100 vs 88.9），所以 9.4 应理解为平均绝对差，不是固定方向的下降（阅读者分析）。

依据：§4、Tables 1–4，PDF pp.4–5；§5，pp.5–6。
