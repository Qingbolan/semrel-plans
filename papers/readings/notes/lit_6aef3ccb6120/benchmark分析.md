# 评测与边界

**基线**（§4.1，p.8；附录 D）：KNN（N=5，sklearn）、MICE（sklearn IterativeImputer）、TabCSDI（扩散模型，在作者数据上训练）、直接 LLM、CoT、代码生成、MetaGPT（DataInterpreter）。

**指标**：Accuracy（填补值与真值一致的比例）、FindAccuracy（只统计至少被正确填补一次的变量）、RMSE（§4.1，p.8）。

**实验 1（GPT-4o，各数据集汇总 RMSE，Table 2，p.9）**：

| 方法 | Bajaj | Bmi | Supermarket | GreenTrip | LOLChampion |
|---|---|---|---|---|---|
| KNN | 13.9704 | 5.1197 | 58.4225 | 1.9419 | 15.5253 |
| MICE | 10.3246 | 1.3871 | 3.3497 | 0.7845 | 12.3606 |
| TabCSDI | 17.2945 | 5.0527 | 53.9156 | 5.8039 | 27.1722 |
| LLM | 11.3127 | 0.4323 | 10.0895 | 1.6319 | 24.6731 |
| CoT | 11.7800 | 0.3294 | 12.1913 | 1.6766 | 45.3338 |
| 代码生成 | 14.6939 | 10.8948 | 46.5009 | 7.4250 | 21.3097 |
| MetaGPT | 14.8918 | 8.3418 | 89.3225 | 2.0785 | 23.8936 |
| SketchFill | 1.4666 | 0.0000 | 0.1292 | 0.5551 | 0.3926 |

逐变量看，SketchFill 在 RSI8（8.7993 vs MICE 2.5590）、GrossIncome（0.7749 vs MICE 0）、CongestionSurcharge、TollsAmount、PRateplusBRate 上不是最优（Table 2）。

**实验 2（准确率，Fig. 4 与正文）**：Bmi 准确率 100%；GreenTrip 74%；LOLChampion 79%（§4.2，pp.9–10）。结论称总体准确率 84.2%，比 CoT 高 56.2%、比代码生成高 59%、比 MetaGPT 高 78.8%（§5，p.10）；未说明是绝对百分点还是相对提升（阅读者分析）。

**实验 3（Llama3-8B，附录 C.3，Fig. 5）**：在 Bmi 上高于 MICE 和 MetaGPT，在 Supermarket、GreenTrip 上不如 MICE。

**边界**：无消融；未报告 LLM 调用次数、成本或耗时；TabCSDI 只报告汇总 RMSE；KNN 准确率被省略（§4.2）。§5 中“with fabricated data inside the datasets”的含义论文未解释（阅读者分析）。

依据：§4–5、Table 2、Fig. 4、附录 C–D，PDF pp.8–10、18–19。
