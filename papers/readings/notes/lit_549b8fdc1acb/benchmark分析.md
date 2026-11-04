# 评测与边界

**设置**：GPT-3.5-turbo-16k、GPT-4-0613、GPT-4-1106-preview；temperature 0；max_round 50；默认 FSM 调度。基线 Codex、Binder、Dater、ReAcTable（Codex 版）及 ReAcTable 的 GPT-3.5/4/4-turbo 变体（不投票）。

**实验 1（单表，Tables 1–3）**：

| 方法 | WikiTQ 准确率 | TabFact 准确率 | FeTaQA ROUGE-L |
|---|---|---|---|
| Codex | 47.6 | 72.6 | 0.52 |
| Binder | 61.9 | 85.1 | — |
| Dater | 65.9 | 85.6 | 0.56 |
| ReAcTable（Codex） | 68.0 | 86.1 | 0.61 |
| ReAcTable（GPT-3.5） | 52.4 | 73.1 | — |
| ReAcTable（GPT-4） | 67.3 | 83.4 | — |
| ReAcTable（GPT-4-turbo） | 66.1 | 85.0 | — |
| AutoTQA（GPT-3.5） | 66.0 | 79.4 | 0.60 |
| AutoTQA（GPT-4） | 75.3 | 87.4 | 0.64 |
| AutoTQA（GPT-4-turbo） | 73.2 | 88.7 | 0.67 |

**实验 2（多表工业数据，Table 4）**：GPT-3.5 / GPT-4 / GPT-4-turbo 为 45.0% / 85.0% / 80.0%；没有其他方法参与比较，因为 Binder、Dater、ReAcTable 不能直接处理多表。GPT-4 单任务成本是 GPT-4-turbo 的 1.28 倍。

**实验 3（调度，Table 5、Figure 7）**：轮转调度在 50 轮内得不到正确答案（N/A）；LLM 调度 80.0% / 75.0%，FSM 85.0% / 80.0%（GPT-4 / GPT-4-turbo）；LLM 调度平均轮数是 FSM 的 1.6 倍。

**实验 4（few-shot，Table 6）**：GPT-4-turbo 从 0-shot 的 60.0% 升到 5-shot 的 80.0%。

同骨干对比：GPT-4 下 AutoTQA 比 ReAcTable 在 WikiTQ 高 8.0 个百分点（75.3 vs 67.3）、TabFact 高 4.0（87.4 vs 83.4）；GPT-3.5 下 TabFact 反而略低于 Codex 版 ReAcTable（79.4 vs 86.1）（阅读者分析，依据 Tables 1、3）。

**边界**（阅读者分析）：FeTaQA 没有同骨干的 ReAcTable 变体，那里的提升混合了模型差异；工业数据集私有且未给题目数；无独立局限章节。

依据：§5.1–5.5、Tables 1–6、Figures 6–7，PDF pp.8–12。
