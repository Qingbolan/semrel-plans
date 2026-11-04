# 工作负载

**训练数据**：1,000 条 HotPotQA 与 2,000 条 MATH；教师对每题采样一条轨迹并过滤错误轨迹，最终约 2,000 条轨迹用于蒸馏（CoT 与智能体两种设置相同）（§5，PDF p.6）。

**测试集**（Table 1，PDF p.6；为降低成本，每个测试集最多 500 例）：

| 类型 | 域 | 数据集 | 说明 | 测试规模 |
|---|---|---|---|---|
| 事实 | 域内 | HotPotQA | 2 跳问答 | 500 |
| 事实 | 域外 | Bamboogle | 2 跳问答 | 125 |
| 事实 | 域外 | MuSiQue | 3 跳问答 | 500 |
| 事实 | 域外 | 2WikiMultiHopQA | 2 跳问答 | 500 |
| 数学 | 域内 | MATH（MATH500） | 大学水平数学 | 500 |
| 数学 | 域外 | GSM-Hard | 大数算术 | 500 |
| 数学 | 域外 | AIME | 奥赛级 | 90 |
| 数学 | 域外 | OlymMATH | 奥赛级 | 200 |

**环境与模型**：知识库为 Wikipedia 2018（不用在线搜索引擎，以保证可复现），检索嵌入为 e5-base-v2；教师 Qwen2.5-32B-Instruct；学生 Qwen2.5-Instruct 0.5B/1.5B/3B/7B，另测 Llama-3.2-1B-Instruct 与 Phi-4-mini-instruct（§5，PDF p.6；Table 4，PDF p.8）。

**训练设置**：LoRA（rank 64，全部线性层），2 epoch，batch 8，学习率 2e-4，4 张 A100 80GB；推理贪心解码，最多 5 步；sag 取 N=8、温度 0.4（§5，PDF p.6）。

阅读者分析：任务单位是单题问答，检索在固定 Wikipedia 语料上进行，不涉及结构化表格或多文档批处理。
