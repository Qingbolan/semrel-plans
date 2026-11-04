# 工作负载

| 数据集 | 用途 | 规模/说明 |
|---|---|---|
| BIRD-Train | MCTS 探索与策略训练 | 使用题量未说明 |
| BIRD-Dev | 主评测 | 1,534 道跨领域问题，11 个数据库；分 Simple/Moderate/Challenging |
| Spider-Test | OOD 评测 | 跨领域 |
| KaggleDBQA | OOD 评测 | 真实网络数据库，schema 不规范 |
| ScienceBenchmark | OOD 评测 | 政策、天体物理、癌症研究等科学数据库的专业查询 |

（§5.1，PDF p.9）OOD 数据集不做针对性训练。指标为 EX。

模型与设置：默认策略为训练后的 Qwen3-8B（另有 4B），默认动作模型为 Qwen2.5-Coder-32B-Instruct，也测试 Qwen2.5-Coder-14B-Instruct 和 Gemma4-31B-It；SFT 2 个 epoch，lr 1e-5，LoRA r=64、α=128；RL 2 个 epoch，lr 1e-6，λ=0.8，G=4；8×A100；T_max=10（§5.1）。

阅读者分析：这是典型的单轮 NL→SQL 工作负载，单位是“问题 + 数据库 → 一条 SQL”；与语义算子类查询不同，它不涉及对非结构化文本的 LLM 判断，LLM 只用于生成/修正 SQL 及中间证据。

依据：[arXiv 2606.23537v1，14 页](https://arxiv.org/pdf/2606.23537v1)，§5.1，PDF p.9。
