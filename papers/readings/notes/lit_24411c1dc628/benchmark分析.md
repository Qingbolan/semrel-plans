# 评测与边界

指标：任意奖牌率、银牌及以上率、金牌率，误差条为分层 bootstrap 的 95% 置信区间（Fig. 5，PDF p.9）。

主要结果（MLE-bench lite，§5.2，PDF p.9）：
- 环境本身的效果：同为 AIDE greedy o1-preview，在 AIRA-dojo 中由原报告的 35.2% 提升到 45.9%。
- 算子的效果：都用 greedy 策略时，AIRA 为 45.5%，AIDE 为 39.8%（R1）。
- 搜索策略的效果：R1 下 AIRA MCTS 最佳，为 47.7%；o3 下 MCTS 与 greedy 的任意奖牌率接近，金牌率 MCTS 高 2.2 个百分点；AIRA MCTS 的金牌率从 R1 的 25.68% 提升到 o3 的 30.91%。
- 使用 AIDE 算子时：不同 c_UCT 的 MCTS 和 Evo 都没有超过 AIDE greedy R1 的 39.77%；去掉记忆的 AIDE 与原版几乎相同（Fig. 3；图中各柱数值在 34.55–39.77 之间，因文本提取无法逐一对应到柱）。

泛化差距（Fig. 6，PDF p.10）：搜索与选解都用测试分（Test/Test）时，比都用验证分（Val/Val）高 9.4（MCTS）、12.4（Evo）、15（AIRA greedy）、16.6（AIDE greedy）个百分点；只把最终选解改为按测试分（Val/Test），就能提升 9–13 个百分点。

全量 MLE-bench（App. D Table 2，PDF p.18）：AIRA greedy o3 整体 31.6±0.8，Low 55.0、Medium 22.0、High 21.7、MLE-bench-30 25.8；AIDE greedy（o1-preview，引用值）整体 16.9。注意 55.0 来自改进后的基础设施和高推理强度设置。

局限（§7.1，PDF p.12）：只用了 LLM 算子，未使用完整的智能体算子；未微调；受 24 小时、1 块 GPU 的限制（附录有 120 小时的实验）；可能存在 Kaggle 任务的数据污染。
