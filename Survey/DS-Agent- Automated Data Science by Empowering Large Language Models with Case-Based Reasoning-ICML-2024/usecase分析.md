# 具体用例

**原文任务示例**（附录 B.1，p.13，开发任务 AR）：

> You are solving this machine learning tasks of regression: The dataset presented here (the Airline reviews) comprises customer feedback for British Airways. Here, we provide the textual reviews. Your task is to predict the corresponding rating in the range of {1, ..., 10} given the reviews in the test set. The evaluation metric is root mean squared error (RMSE). ... fill in the provided train.py script ...

附带的 `train.py` 已经写好读取 `train.csv`、按 9:1 划分训练/验证集、计算 RMSE 和提交测试预测等步骤；`train_model` 留空，`predict` 只随机输出 1–10。agent 要补全这两个函数。

**开发阶段的迭代过程**（附录 C.2.1，p.17，任务 chatgpt-prompt，文本分类）：

| 轮次 | 方案 | 验证集准确率 |
|---|---|---:|
| 1 | TF-IDF + 逻辑回归基线 | 75.21% |
| 2 | 预训练 BERT | 76.06% |
| 3 | 换成 RoBERTa | 47.86% |
| 4 | 调整学习率和训练轮数 | 90.59% |
| 5 | 换成 RoBERTa-large 并重新调参 | 98.46% |

第 3 轮的退步说明执行反馈确实会影响下一轮：ReviseRank 和 Planner 根据日志纠正方向。

**部署阶段**（附录 C.2.2）：部署任务 electricity（时间序列预测）检索到开发任务 ETTm2 的成功代码。那份代码用的是 Bi-GRU 与 Bi-LSTM 的集成模型；Adapter 只需轻微修改，就能适配新数据。

阅读者分析：案例库存的是“怎么做”的方法经验与代码，不是模型的输入特征，也不包含用户数据本身。

依据：[arXiv 2402.17453v2](https://arxiv.org/abs/2402.17453v2)，附录 B.1、C.2.1–C.2.2，PDF pp.12–13、17、26。
