# 评测与边界

**基线**：PostgreSQL 16.1 优化器；BAO（用相同的计划—时延数据训练 Tree-CNN）；HybridQO（MCTS + Tree-LSTM）；消融中另有 GPT-4o 少样本提示、LLaMA3-8B 与 DeepSeek-Coder-6.7B 主干。

**指标**：测试集总执行时延 Exec、端到端时延 E2E（含统计收集、推理、规划、执行）、尾时延分位数、候选集 Min/Avg/Std、LLM_S 选择准确率。

**主要结果**：
- Table 1（p.10）：Exec（秒）JOB 上 PG 129.26、BAO 70.68、HybridQO 175.56、LLMOpt(G) 42.42、LLMOpt(S) 36.45；Stack 上分别为 334.66、405.71、1,084.91、300.50、219.86。E2E 方面 LLMOpt(G) 在 JOB 为 148.78，高于 PG 的 129.34；LLMOpt(S) 在三个基准都最低（62.51、61.07、236.15）。
- Table 2：LLM_G 候选集 Min/Avg/Std 均低于 Bao_arms 和 MCTS，如 JOB 上 33.74/53.68/16.05 对 Bao_arms 35.62/118.88/86.56。
- Table 4：组合 LLMOpt(G+S) 只在 JOB-EXT 最好（42.12），JOB 和 Stack 上不如 LLMOpt(S)；作者归因于训练与推理候选分布不一致。
- Table 5：选择准确率 LLM_S 为 76.10/66.66/63.16%，Tree-CNN 为 31.86/50.00/46.05%，Tree-LSTM 为 43.36/25.00/26.32%。
- Table 3（JOB 消融）：去掉全部统计信息后 LLMOpt(G) 由 42.42 升至 56.66；GPT-4o 少样本为 69.30/75.15。

**局限与疑点**（阅读者分析）：
- 正文计算 JOB-EXT 上 LLMOpt(G) 相对 PG 提升 29.6% 时用的是 46.72，而 Table 1 为 45.22，口径不一致。
- 消融中多数投票（38.30）与贪心解码（39.25）都优于默认的“采样+Tree-CNN”（42.42）；去掉 Main_Value 时 LLMOpt(S) 反而更好（35.29 对 36.45）。
- 每种设置只报告单次测量，没有方差；不支持嵌套查询；需要在每个数据库上收集执行数据并重新微调。

依据：[arXiv:2503.06902v1，13 页](https://arxiv.org/abs/2503.06902)，§8.2–8.7、Tables 1–5，PDF pp.9–12。
