# 评测与边界

**设置**：所有智能体使用 GPT-3.5（v1106），temperature 0。主指标为通过率；另报告错误传播设置（错误状态延续到同一 problemset 的后续问题）、忽略 Intact 违规、忽略呈现错误（PE）三种变体。

**实验 1（五个智能体，Table 2，通过率 %）**：

| 智能体 | Kaggle | Exercise | LeetCode | SO |
|---|---|---|---|---|
| Chapyter | 34.1 | 39.6 | 45.0 | 46.5 |
| ChatDev | — | — | 32.5 | 35.1 |
| CoML | 59.8 | 78.6 | 42.5 | 78.2 |
| Code Interpreter API | 42.4 | 67.4 | 45.0 | 58.4 |
| Jupyter-AI | 51.8 | 78.6 | 57.5 | 50.0 |

Chapyter 忽略呈现错误后显著上升（Kaggle 55.3）；错误传播下 Chapyter 和 Jupyter-AI 下降明显（Exercise 55.1）。

**实验 2（上下文，Table 3，CoML）**：只给查询时 Kaggle 与 Exercise 均为 13.9；加入代码历史后 Exercise 达 81.3；变量描述加查询放在末尾效果略好。

**实验 3–5**：LIDA 的表格编码在 Exercise 上优于 CoML（82.4 vs 78.6）但消耗更多 token；模型排序约为 CodeLlama-7B ≈ CodeLlama-34B < Gemini-Pro < GPT-3.5 < GPT-4；自我调试优于重采样，足够多次修复后 GPT-3.5 可超过 GPT-4。

**边界**：不评测开放式规划任务；结果波动可达 ±2%，LeetCode 仅 40 题波动更大；可视化题未纳入。

依据：§6.1–6.5、Tables 2–4、Figures 12–13，PDF pp.6–8；Limitations、Table 5，PDF p.9。
