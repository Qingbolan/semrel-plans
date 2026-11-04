# 评测与边界

**实验 1（主要结果，pp.7–11 已渲染核对）**：

| 基准 | DeepAnalyze-8B | 对照 |
|---|---|---|
| DataSciBench Score（Table 1） | 61.11 | GPT-4o 64.51；GPT-4-Turbo 54.65 |
| DataSciBench F5 建模（Table 1） | 33.33 | GPT-4o 57.67 |
| DSBench 建模 成功率 / Performance（Table 2） | 90.63 / 39.41 | AutoGen+GPT-4 87.84 / 45.52 |
| DABStep 总体 / hard / easy（Table 3） | 38.88 / 32.80 / 70.83 | I2I-Agent 36.44 总体；Open Data Scientist easy 84.72 |
| DS-1000（Table 5） | 61.7 | LIMI 54.8；GPT-4-turbo 53.9 |
| TableQA 平均（Table 4） | 64.47 | Reasoning-Table (SFT+RL) 62.62 |

DataSciBench 基线数值与 DataSciBench 原文 Table 2 相同，但表中略去了 Deepseek-Coder-33B（原文 56.76）。DSBench 数据分析（Figure 7）和 DABStep-Research（Figure 8）中，DeepAnalyze 均为最高；后者对比 GPT-4o、o3-mini、DeepSeek-v3.1/R1、Seed-1.6。

§6 称在 12 个基准上超过最强闭源 LLM，与 DataSciBench 低于 GPT-4o、DSBench 建模低于 AutoGen+GPT-4 的表格结果不一致（阅读者分析）。

DABStep-Research 为作者自建并由 LLM 评审，不等同于独立评测；原文没有局限章节；§5.3 正文引用的“Table 1”应为 Table 8（阅读者分析）。

依据：§4.3、§5、§6、Tables 1–8、Figure 7–8，PDF pp.7–12。
