# 评测与边界

**被测模型（§4.1）**：6 个 API 模型（o1-mini、GPT-4o-2024-05-13、GPT-4o-mini、GPT-4-Turbo、Claude-3.5-Sonnet、GLM-4-Flash），8 个开源通用模型，9 个开源代码模型，共 23 个。

**指标（§4.2）**：CR 对每个 TFC 记 0/1/2 分，CR=Σs/(2T)；SR 为 10 次运行、k=1 的 pass@1，一个提示的所有 TFC 都通过才算成功；另有 VLM 分与 F1–F5。总分 Score = 0.05×ΣF + 0.05×VLM + 0.05×SR + 0.65×CR。

**实验 1（Table 2 主结果，已渲染 p.6 核对）**：

| 模型 | SR (%) | CR (%) | Score |
|---|---|---|---|
| GPT-4o-2024-05-13 | 66.31 | 68.44 | 64.51 |
| Deepseek-Coder-33B-Instruct | 55.86 | 61.23 | 56.76 |
| GPT-4-Turbo | 51.93 | 58.87 | 54.65 |
| o1-mini | 29.77 | 45.26 | 38.78 |
| CodeLlama-13B-Instruct | 10.49 | 14.64 | 12.64 |
| CodeLlama-34B-Instruct | 0.90 | 1.47 | 1.33 |

摘要称 API 模型“在所有指标上”优于开源模型，但 Table 2 中 Deepseek-Coder-33B（56.76）高于 GPT-4-Turbo、o1-mini 等 API 模型；§5.1 的“平均而言”更准确（阅读者分析）。

**局限**：原文承认可视化指标与 VLM-as-a-judge 可能不精确（Limitations）。附录 A.5 记录了模型记忆公开数据集、预处理时编造列名、选错中文编码等问题。§5.4 指出 o1-mini 失败主要源于不遵循指令、错误调用、遗漏导出。

依据：§4–5、Table 2、Limitations、附录 A.5，PDF pp.5–9、12。
