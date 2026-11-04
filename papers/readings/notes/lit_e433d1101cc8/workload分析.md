# 工作负载

13 个任务（Table 2）：

| 类别 | 任务 | 模态 | 指标 |
|---|---|---|---|
| 经典任务 | cifar10、imdb、ogbn-arxiv | 图像、文本、图 | 分类准确率 |
| 经典 Kaggle | house-price、spaceship-titanic | 表格 | MAE、准确率 |
| Kaggle 挑战 | parkinsons-disease、fathomnet、feedback、identify-contrails | 时间序列、图像、文本、图像分割 | SMAPE、MAP@20、MCRMSE、Dice |
| 近期研究 | CLRS、BabyLM | 图、文本 | MSE、困惑度 |
| 代码改进 | llama-inference、vectorization | 文本、图像 | 墙钟时间 |

**时效**：4 个 Kaggle 挑战发布于 2022-08-31 至 2023-05-11；研究数据集发布于 2023 年 1 月，用于检验对训练截止后任务的泛化。BabyLM 要求在 1,000 万词上训练语言模型；llama-inference 要加速 LLaMA 7B 自回归生成。

**基线**：多数任务起始代码实现简单基线；imdb 要求从零微调 BERT；house-price、spaceship-titanic、imdb、fathomnet 起始代码不能直接运行，与随机预测比较。CLRS 与 BabyLM 直接评测保存的检查点，代码改进任务直接计时。

**规模口径**：论文没有统一给出各数据集样本数或划分大小；评测单位是每个设置 8 次运行，而不是数据样本。

依据：§1，p.2；§2.1、§2.4，pp.3、5–6；Table 2，p.4；附录 B，p.15。
