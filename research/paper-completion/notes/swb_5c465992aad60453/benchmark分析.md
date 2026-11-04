# 评测与边界

**设置**：RoBIn_Ext 基于 Biomed RoBERTa，RoBIn_Gen 基于 BioBART，各训练 10 epoch，结果为 10 次运行平均；LLM（GPT-4o-mini、Llama3.1 8B、Gemma2 9B）0/1/3-shot 只跑一次；SVM/LR 用 1K 个最高频 1–3 gram 的 TF-IDF（§6.1–6.2、§6.4，PDF pp.10–11）。

**指标**：MRC 指标为 token F1、BERTScore F_BERT、EM；RoB 指标为宏 P/R/F1 和 ROC AUC，显著性用 t 检验（§6.3）。

**实验 1（MRC 总体，Table 2，PDF p.12）**：

| 系统 | F1 | F_BERT | EM |
|---|---|---|---|
| RoBIn_Ext | 97.10 | 91.30 | 87.76 |
| RoBIn_Gen | 93.81 | 89.52 | 82.09 |
| Gemma2 few-shot | 61.90 | 80.91 | 34.99 |
| GPT-4o-mini few-shot | 56.71 | 75.36 | 32.37 |
| Llama3.1 few-shot | 53.25 | 74.68 | 27.29 |

报告偏倚是 EM 最差的类型（RoBIn_Ext 78.33）。

**实验 2（RoB 推断总体，Table 3，PDF p.13）**：

| 系统 | 宏 F1 | 宏 P | 宏 R |
|---|---|---|---|
| RoBIn_Ext | 74.18 | 75.49 | 73.62 |
| RoBIn_Gen | 72.75 | 73.21 | 74.51 |
| SVM | 71.29 | 70.84 | 73.02 |
| Gemma2 few-shot | 70.03 | 71.16 | 69.35 |
| LR | 69.11 | 68.96 | 71.26 |

ROC AUC：两种 RoBIn 0.83，SVM 0.80，LR 0.78（Figure 5b）。Ext 与 Gen 差异不显著，与基线差异显著（§6.5，PDF p.12）。

**按类型**：实施偏倚中 GPT-4o-mini few-shot（F1 76.40）领先，RoBIn 仅胜过经典方法；失访偏倚中 Llama3.1 few-shot（57.81）的 F1 最高（Table 3）。

**边界**：数据集规模小且类别不平衡，主要错误来自少数类（高/不明风险），而假阳性（把高风险判为低风险）在医学上代价最大；标注自动生成、人工干预少；失访偏倚常需表格，自动流程取不到（§6.5、§7，PDF pp.12、14）。阅读者分析：LLM 只跑一次、未报方差；把 GPT-4o-mini 标为 "8B" 的依据，原文未给出。
