# benchmark

**参与**：M 赛道 30 队（110 人）107 runs，L 赛道 9 队 21 runs。讨论部分写作“107 people from 30 teams”，与 107 个 run 混淆，阅读者认为是原文笔误。

**基线**：最大召回基线（同句共现即判为所有关系）P=0.0022、R=1.0、F1=0.0044；Turku-BSC 系统（BioBERT-base，允许跨句、128 token 窗口、实体标记）F1=0.744。

**主要结果**：

| 赛道 | 队伍 | micro F1 | 位置 |
|---|---|---|---|
| M | Humboldt（P=0.7961、R=0.7986） | 0.7973 | Table 5 |
| M | NLM-NCBI | 0.7948 | Table 5 |
| M | KU-AZ | 0.7894 | Table 5 |
| L | NLM-NCBI | 0.7886 | Table 6 |

- M 赛道最后几队 F1 接近 0。NLM-NCBI 从 M 到 L 只降 0.006，作者据此认为规模化后性能下降很小。
- 报告的推理耗时从 KU-AZ 用 16 块 GPU 的 9 小时到 FSU2021 的 5 天，硬件不同，不可直接比较。
- 主流方法：句子分类 + 生物医学预训练 Transformer + [CLS] 线性/softmax 分类；集成（多数投票）提升最明显；Humboldt 用 CTD 实体描述增强。
- 误差分析：inhibitor、substrate、direct-regulator 假阴性最多；同一提及在训练/测试中关系类型不同（如 BAY 50-4798、cyclin D1）造成泛化错误。

局限：评测只覆盖 750 篇测试摘要；不评测耗时；无实体归一化；不含全文和专利；关系层无标准 IAA。

依据：[Miranda-Escalada et al., Database 2023, baad080，JATS 全文](https://doi.org/10.1093/database/baad080)，Baseline systems；Results：Shared task participation、Evaluation results、Tables 5–7、Participating systems、Error analysis；Discussion。
