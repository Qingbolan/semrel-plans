# 工作负载

本文没有数据集、查询集、数据规模或划分，也没有任何实验设置。文中出现的只有说明性示例：

| 示例 | 用途 | 位置 |
|---|---|---|
| 1980 年代电影好评比例最高的前 5 位导演 | 动机：结构化表与影评文本混合 | §1，p.57 |
| “Select the documents that are related to swimming” | 粗匹配：转换为逻辑表示 “Select the documents that [Condition]” | §2.4，p.65 |
| 50 岁及以上获得菲尔兹奖的数学家 | 剪枝：两个条件互斥，可提前终止 | §2.5，pp.66–67 |
| Table Filter 算子的选择过程 | 编排示例 | Fig.4，p.64 |

**嵌入对齐的训练数据**：作者只说明收集了“来自多种来源、配有真实相关文本段落的表格”，用 Multiple Negatives Ranking Loss 训练；语料规模、来源和评测均未给出（§2.3，p.63）。

阅读者分析：如需评测 iDataLake 类系统，必须另找 workload；作者本人在 §3 也把 benchmark 缺失列为开放问题。

依据：§1–§3、Fig.4，印刷页 pp.57–67。
