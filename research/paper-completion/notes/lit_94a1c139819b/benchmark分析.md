# 评测与边界

**被测对象**（§3.1，p.6）：开源与闭源 LLM（DeepSeek、Qwen2.5、Llama-3.1-405B、Gemini-Pro-1.5、Claude-3.5-Sonnet、GPT-4o/GPT-4/o1-preview/o3-mini），温度 0；智能体框架 Reflexion、CodeR、AutoEval、Spider-Agent；text-to-SQL 方法 DIN-SQL、DAIL-SQL、CHESS、SFT CodeS-15B（提示中加入采样单元格值、外部知识和方言说明）。

**实验 1（Spider 2.0 成功率，Table 6，p.7）**：

| 框架 + 模型 | SR |
|---|---|
| Spider-Agent + o1-preview | 21.36% |
| Spider-Agent + Claude-3.5-Sonnet | 14.87% |
| Spider-Agent + GPT-4o | 12.34% |
| Spider-Agent + Llama-3.1-405B | 2.21% |
| CodeR + GPT-4o | 7.91% |
| Reflexion + GPT-4o | 7.28% |
| AutoEval + GPT-4o | 5.70% |

**实验 2（lite / snow，Spider-Agent，Table 4，p.7）**：

| 模型 | lite 总体 EX | snow 总体 EX |
|---|---|---|
| o1-preview | 23.22% | 23.77% |
| o3-mini | 23.40% | 19.20% |
| Claude-3.5-Sonnet | 15.54% | 15.54% |
| GPT-4o | 13.16% | 12.98% |
| DeepSeek-V3 | 8.78% | 8.78% |

**实验 3（传统 text-to-SQL，Table 5，p.7）**：DAIL-SQL + GPT-4o 在 Spider 1.0 / BIRD / snow / lite 上为 86.6% / 57.4% / 2.20% / 5.68%；CHESS + GPT-4o 为 87.2% / 66.7% / 1.28% / 3.84%；SFT CodeS-15B 在 lite 上 0.73%。

**实验 4（分项与错误分析，§4，pp.8–9）**：

| 子集 | 有 | 无 |
|---|---|---|
| 嵌套列（Table 7） | 10.34% | 27.38% |
| 外部文档（Table 8） | 11.54% | 26.64% |
| DBT 项目（Table 9） | 12.82% | 23.22% |

300 例错误中，数据分析错误 35.5%（方言函数 10.3%、高级计算 7.5%、查询规划 17.7%），模式链接错误 27.6%，JOIN 错误 8.3%（Fig. 4）。少样本（0/1/3-shot：5.68%/6.40%/6.76%）与提供“oracle 函数文档”帮助有限（Tables 10–11）。

**成本**（Table 21，p.39）：每实例平均 Spider-Agent + o1-preview 0.75 美元、+ GPT-4o 0.32 美元，DAIL-SQL + GPT-4o 0.09 美元。

**边界**：难度只按 SQL 长度划分；评测允许多余列。

Table 10 中 DAIL-SQL + o1-preview 加 oracle 函数后 EX 为 9.51%，反而低于不加时的 12.60%（p.9 渲染核对），正文仅概括为“略有提升”（阅读者分析）。附录 Table 20 的 Spider 2.0 总体 SR 为 17.0%，与 Table 6 的 21.36% 不一致，论文未说明所用模型（阅读者分析）。

依据：§3–4、Tables 4–6、10–11、20–21、Fig. 4，PDF pp.6–9、38–39。
