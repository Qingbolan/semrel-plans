# 评测与边界

**对比设置**：只比较 TaskWeaver 分别以 GPT-3.5 和 GPT-4 为底座的结果，没有与 LangChain、AutoGen、Data Interpreter 等框架比较，也没有组件消融（§7，pp.12–17）。作者另提出 Examiner + Judge 的对话式评测思路，由 Examiner 监督对话、Judge 对照标准答案判分（§7，p.12）。

**实验 1（总体）**（Table 3，p.14）：

| 基准 | GPT-3.5 | GPT-4 |
|---|---|---|
| Eval-Cases | 0.42 | 0.87 |
| DS-1000 | 0.40 | 0.60 |
| InfiAgent-DABench | 0.70 | 0.88 |
| DSEval | 0.36 | 0.72 |

**实验 2（Eval-Cases 逐项）**：GPT-3.5 只在 stock_forecasting 和 list_files 两项胜过 GPT-4；GPT-4 在 list_files 上以无法访问本地文件系统为由未执行（Table 4，p.15）。正文写 GPT-4 平均归一化分为 0.85，Table 4 与 Table 3 为 0.87，原文未解释差异（阅读者分析）。

**实验 3（DSEval 分项 %PASS）**（Table 5，p.16）：

| 子集 | GPT-3.5 | GPT-4 | GPT-4 去除 PE 与 IV 后 |
|---|---|---|---|
| LeetCode | 42.50 | 75.00 | 77.50 |
| SO | 37.13 | 70.79 | 80.20 |
| Kaggle | 4.80 | 35.35 | 50.51 |
| Exercise | 20.32 | 63.64 | 78.61 |

PE 指输出格式或展示方式错误，IV 指不必要地修改了原数据（§7.6，p.17）。DS-1000 上 Matplotlib 得分最高、Pandas 最低，作者归因于 DataFrame 比较的索引、类型差异（§7.4，p.14）。

**边界**：作者承认同一 LLM 端点的表现随时间和主机波动（§7.3，p.14），自动比较可能低估实际可用的答案（§7.6，p.17）。§9 的设计验证（ReAct 文件链、仅插件模式、拒绝删除系统文件）均为单例演示，没有统计结果（pp.19–21）。

依据：§7–§9、Tables 3–5，PDF pp.12–21。
