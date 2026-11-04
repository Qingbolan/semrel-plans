# 评测与边界

基线（§5.1）：模型级训练 CodeS、Reasoning-SQL、SQL-R1、OmniSQL；固定流水线 CHESS、DeepEye-SQL（提示式），XiYan-SQL、CSC-SQL、CHASE-SQL、OpenSQL（含训练模型）；动态工作流 Alpha-SQL（MCTS 搜索）、SquRL（先规划后执行）。

BIRD-Dev（Table 1，EX %）：

| 方法 | 动作/底座模型 | Total |
|---|---|---|
| OmniSQL-32B | Qwen2.5-Coder-32B（训练） | 67.0 |
| Alpha-SQL | Qwen2.5-Coder-32B | 69.7 |
| DeepEye-SQL | Qwen2.5-Coder-32B | 70.6 |
| CSC-SQL | Qwen2.5-Coder-32B（训练） | 70.7 |
| CHASE-SQL | Gemini-1.5（Flash/Pro） | 73.0 |
| SQLConductor 4B 策略 | Qwen2.5-Coder-32B | 70.3 |
| SQLConductor 8B 策略 | Qwen2.5-Coder-32B | 71.2 |
| SQLConductor 8B 策略 | Gemma4-31B-It | 73.2（Simple 78.5 / Moderate 66.1 / Challenging 61.8） |

**OOD（Table 2，8B + Qwen2.5-Coder-32B）**：Spider 88.9、KaggleDBQA 66.0、ScienceBenchmark 62.3，均值 72.4，高于 OpenSQL 71.0、Alpha-SQL 69.6、OmniSQL-32B 69.1；Spider 上 OmniSQL-32B 89.8 更高。

**成本（Table 3，均用 Qwen2.5-Coder-32B 动作模型）**：

| 方法 | EX | 总耗时 (h) | 每题输入 / 输出 (k token) | 每题成本 ($) |
|---|---|---|---|---|
| CHESS | 67.8 | 21.8 | 268.0 / 37.5 | 0.109 |
| DeepEye-SQL | 70.6 | 4.9 | 20.3 / 21.5 | 0.024 |
| Alpha-SQL | 69.7 | 29.1 | 124.4 / 68.7 | 0.094 |
| SQLConductor | 71.2 | 5.6 | 7.1 / 12.2 | 0.012（策略另加 0.001） |


**消融（BIRD-Dev EX）**：
- 训练阶段（Table 4）：SFT+RL 71.2、仅 SFT 70.7、仅 RL 70.2、未训练 68.3；
- 策略对比（Table 5）：固定工作流 69.2，未训练 8B 策略 68.3（低于固定流程），未训练 32B 69.7，训练后 4B 70.3；
- 监督数据整理（Table 6）：“最短正确工作流”仅 67.9，top-1 70.4，稳定性加权 top-3 70.7。

边界（阅读者整理）：73.2% 的最高值依赖换成 Gemma4-31B 动作模型，与其他方法并非同底座比较；同底座下领先幅度为 0.5–1.5 个百分点，且未报告方差或多次运行；成本只统计了可从轨迹获得的部分基线，不含离线 MCTS 与训练成本；论文没有讨论局限性。

依据：[arXiv 2606.23537v1，14 页](https://arxiv.org/pdf/2606.23537v1)，§5.1–5.5、Tables 1–6，PDF pp.9–12。
