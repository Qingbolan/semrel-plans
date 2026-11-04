# 工作负载

| 数据集 | 规模（原文） | 用途 |
|---|---|---|
| BIRD dev | 1,534 个 (NL, SQL) 对，含 CASE、IIF 等领域性写法；按 simple/moderate/challenging 报告 | 主结果（Table 2） |
| Spider dev | 1,034 个 (NL, SQL) 对；按 easy/medium/hard/extra hard 报告 | 主结果（Table 3，仅 7B、14B） |
| SDS（BIRD 子采样开发集） | 沿用 CHESS-SQL：每个数据库取 10%，共 147 题（81 simple、54 moderate、12 challenging） | rollout 数分析、基线 LLM 对比、动作消融（§5.3–5.5） |

无训练集：方法为零样本，不使用训练划分。超参：N_rollout=24、N_expansion=3、T_expansion=0.8、N_reward=5、T_reward=1.0、N_revision=10（§5.2，p.7）。硬件：开源模型在 8 张 80GB GPU 上本地部署（§5.1，p.7）。

阅读者分析：查询单位是单数据库上的单条 SQL，数据为结构化关系库，不涉及非结构化文本或语义算子；原文没有报告每题的 LLM 调用次数、token 或耗时。

依据：[arXiv:2502.17248v2（ICML 2025，PMLR 267），21 页](https://arxiv.org/abs/2502.17248)，§5.1–5.2，PDF p.7。
