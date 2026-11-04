# 评测与边界

**比较方法**（§4.1，p.7）：Simple（不重排）；PZ（5% 样本估全局选择率、全局静态顺序）；Quest（5% 样本、按 s_i/c_i 逐行排序）；OraclePZ / OracleQuest（使用全集真实全局选择率，且不付采样成本，作为这两种方法的上界）；Optimal（逐行穷举，作为下界）；Larch-A2C；Larch-Sel。PZ 与 Quest 由作者重新实现，非原系统。

**指标**：总 token（主指标）与 LLM 调用数，并报告相对 Optimal 的超额百分比。

**主要结果**（Table 1，token 超额）：

| 数据集 / 模式 | Simple | PZ | Quest | Larch-A2C | Larch-Sel |
|---|---|---|---|---|---|
| GovReport Mix | 41.5% | 21.3% | 33.6% | 17.8% | 5.1% |
| GovReport Conj | 14.0% | 31.8% | 31.8% | 11.2% | 7.1% |
| GovReport Disj | 23.4% | 17.6% | 17.6% | 11.9% | 5.8% |
| PubMed Mix | 71.7% | 26.1% | 29.5% | 20.4% | 6.5% |
| PubMed Conj | 45.9% | 30.4% | 30.4% | 10.2% | 5.0% |
| PubMed Disj | 64.7% | 31.8% | 31.8% | 20.6% | 13.2% |
| BigPatent Mix | 79.0% | 28.3% | 29.7% | 17.0% | 3.6% |
| BigPatent Conj | 33.2% | 32.0% | 32.0% | 5.6% | 1.7% |
| BigPatent Disj | 102.4% | 31.9% | 31.9% | 10.7% | 3.8% |

GovReport Conjunction（选择率 1%）中，PZ/Quest 因 5% 前置采样成本反而比 Simple 更耗 token（§4.2）。

**其他实验**：
- 选择率分组：Larch-Sel 在每个区间都最低且接近 1.0×，PZ/Quest 在极低或极高选择率时变差（§4.3，Figure 3）；
- 叶子数 2→10：PZ/Quest 在 PubMed/BigPatent 上升到 1.5× 以上，Larch-Sel 基本平稳（§4.4，Figure 4）；
- 规模：BigPatent 文档数 8K→67K，Larch-Sel 收敛到 1.02×（§4.5，Figure 5）；
- 对 Oracle 基线 8 胜 1 平（§4.6，Table 2）；
- 开销：单步推理 A2C <2 ms、Sel 8–10 ms，训练 A2C 9–11 ms、Sel <7 ms（Table 3）；
- 延迟更新：对 token 的平均影响在 ±0.6% 以内，A2C 标准差 3.7–4.7%，Sel <0.7%（Table 4，每数据集 135 个查询）。

**边界**：
- 原文 §5 承认：依赖查询时可用的嵌入（否则需现算，作者认为成本可摊销）；AI_FILTER 用很小的模型时优势缩小；上游改写算子会使已存嵌入失效；冷启动问题留待跨查询迁移学习；目前只覆盖 AI_FILTER。
- 阅读者整理：所有结果来自基于缓存判定的模拟器，没有真实端到端时间或美元成本；未计入嵌入与本地训练开销；PZ/Quest 为重新实现；只用一个判定 LLM 与一个嵌入模型；Table 2 中个别 Larch-A2C 数值与 Table 1 有小差异（例如 GovReport Conj token 35.9M 对 35.8M，PubMed Disj 86.1M 对 85.9M），未影响结论。

依据：[arXiv 2606.07923v1](https://arxiv.org/abs/2606.07923)，§4–5、Tables 1–4、Figures 3–5，PDF pp.7–12。
