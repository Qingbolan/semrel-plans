# 评测与边界

**设置**：VLM 为 InternVL2.5-26B，通用 LLM 为 DeepSeek-V3，嵌入模型为 Multilingual-E5-Large。9 个基线覆盖五类：NL2SQL（OpenSearch-SQL）、基础模型（GPT-4o、DeepSeek-V3）、微调模型（TableLLaMA、TableLLM）、智能体（ReAcTable、TAT-LLM）、VLM（TableLLaVA-7B、mPLUG-DocOwl1.5）。指标为答案准确率 Acc 与 ROUGE-L，并用通用 LLM 比较预测与标准答案，以弥补精确匹配的不足。

**实验 1（总体，Table 5）**：

| 方法 | WikiTQ-ST Acc | TempTabQA-ST Acc | SSTQA ROUGE-L | SSTQA Acc |
|---|---|---|---|---|
| OpenSearch-SQL | 38.89 | 4.76 | 23.87 | 24.00 |
| ReAcTable | 68.00 | 35.88 | 7.49 | 37.24 |
| TAT-LLM | 23.21 | 61.86 | 19.26 | 39.78 |
| GPT-4o | 60.71 | 74.83 | 43.86 | 66.45 |
| DeepSeek-V3 | 69.64 | 63.81 | 46.17 | 63.22 |
| ST-Raptor | 71.17 | 77.59 | 52.19 | 72.39 |

（其余基线见 p.10，SSTQA Acc 均不高于 40.39。）

**实验 2（表+问题难度，Table 6，Acc）**：ST-Raptor 简单/中等/困难为 93.97/62.66/58.43；DeepSeek-V3 为 92.94/61.83/47.19；GPT-4o 为 86.64/59.75/43.26。

**实验 3（消融，Table 7，SSTQA Acc）**：完整 72.39；去 Table2Tree 57.24（−15.15）；去数据操作 65.09（−7.30）；去验证器 66.10（−6.29）；去问题分解 68.06（−4.33）；去对齐 71.07（−1.32）。

**其他（§7.4）**：未微调的 VLM 表头识别准确率在 SSTQA、TempTabQA、WikiTQ 上为 93.14%、94.32%、92.31%；每个问题约 30 秒、平均 2.89 个操作；VLM 识别错误会让耗时从 10 秒增至 40 秒。

**边界**：

- 原文局限：会把水平合并的内容单元格误判为表头；对类似多层嵌套 SQL 的复杂流水线分解困难，作者称这类情况不多见。
- 数值不一致：Table 7 中 GPT-4o、DeepSeek-V3 的 SSTQA Acc 为 62.12、62.26，与 Table 5 的 66.45、63.22 不同；正文“比第二名高 10.23%”与 Table 5 的差距 5.94 点不符，更接近 Table 7 的 10.27（阅读者分析）。
- 准确率部分依赖 LLM 判定，未报告判定模型和一致性；无多次运行方差。
- WikiTQ-ST、TempTabQA-ST 子集规模与筛选细节未给出，跨基准比较的样本量不明。

依据：§7.1、§7.3–7.6、Tables 5–7，PDF pp.9–13；Tables 4–7 已在 pp.10、12 渲染核对。
