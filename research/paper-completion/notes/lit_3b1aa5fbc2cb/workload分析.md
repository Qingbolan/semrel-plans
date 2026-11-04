# 工作负载

四个工作负载（Table 2，p.9；§7.2，pp.9–10），所有系统使用同样的算子实现、手工优化的查询计划和 oracle 模型 Llama-3.3-70B-Instruct（§7.1）。

| 工作负载 | 数据与规模 | 平均 token/元组 | 计划 | 结构 |
|---|---|---|---|---|
| FEVER 事实核查 | 1,000 条 claim（按 Lotus 论文抽样）；Wikipedia 5,416,568 篇（ColBERT 索引） | claim 11.8；Wikipedia 126.0 | sem_map 生成两个检索查询 → index_search top-5 → sem_filter（小模型代理 + oracle 回退） | 单 stage，3 算子 |
| MEDEC 医疗错误检测与改正 | 1,000 份患者病历样本 | 397.1 | sem_filter 是否有错 → sem_map 找出错句编号 → sem_map 生成改正句 | 单 stage，3 算子 |
| BioDEX 不良反应匹配 | 500 篇文章；11,271 个反应 | 文章 2,680.1；反应 6.3 | sem_map 抽取反应 → ICP 向量索引 join（e5-base-v2）→ 基于距离双阈值的 sem_filter，中间区域回退 oracle | 2 stage，3 算子 |
| ContractNLI 合同蕴含 | 607 份合同；17 个假设 | 合同 2,145.3；假设 36.8 | sem_filter 是否为有效合同 → 全 CP sem_join 判断蕴含 → sem_map 生成解释 | 2 stage，3 算子 |

**oracle 调用数**（Table 2，不含代理调用；括号内为 Kalypso 因内存估计不准的重试数）：

| 工作负载 | Lotus | Palimpzest | Kalypso |
|---|---|---|---|
| FEVER | 1,183 | — | 1,243 (0) |
| MEDEC | 2,098 | 2,338 | 2,143 (21) |
| BioDEX | 6,881 | — | 7,016 (0) |
| ContractNLI | 17,445 | 16,370 | 17,342 (167) |

Palimpzest 不支持把检索结果合并进单个元组，也不支持基于距离的索引搜索，因此没有 FEVER 与 BioDEX 结果。

阅读者分析：这些工作负载的价值在于覆盖了“单 stage 多算子”和“CP/ICP 分隔的两 stage”两种结构，以及短元组与长文档前缀两种极端；它们是对已有数据集的抽样再实现，不是新发布的基准，输出正确性也未被评测。

依据：[arXiv 2607.23815v2](https://arxiv.org/abs/2607.23815)，§7.1–7.2、Table 2，PDF pp.8–10。
