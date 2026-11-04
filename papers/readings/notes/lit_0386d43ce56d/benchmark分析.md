# 评测与边界

**基线**：HoloClean、ED2、Raha、dBoost、Pandas 缺失值检测（MVD）、Fahes、Katara、Min-K、RTClean（Figures 8–9）；修复使用 Baran、均值/众数插补、ML 插补（KNN + MissForest）（§6.2.3）。**指标**：检测精确率、召回率、F1、运行时间；数值修复用 RMSE，类别修复用 P/R/F1（§6.1）。

**实验 1（提示集成，LM-KBC）**：两个 few-shot 示例即可使 F1 约翻倍；最佳集成平均比最佳单提示高 11.2%；参数量越大越好，7b+集成优于 13b 单提示；Non-FT+集成比 FT+单提示、FT+集成、Non-FT+单提示分别高 11.2%、4.6%、7.67%。14 个关系的平均 F1 为 62.53%，最低 PersonHasEmployer 34.97%，最高 PersonHasNobelPrize 98.00%（§6.2.1、Table 2）。

**实验 2（错误检测，Figure 8）**：

| 数据集 | 原文报告 |
|---|---|
| IoT | F1 分别比 HoloClean、ED2、MVD、Raha 高 53%、5.4%、21.3%、28.7%；标记 868 个单元格（ED2 1,222、Raha 1,131、HoloClean 3,316） |
| Hospital | 比 ED2、Raha、dBoost 高 22.7%、23.2%、34.7%；标记 404 个；HoloClean 标记 13,044 个，F1 不足 1% |
| CONTEXT | Raha、ED2 因规模无法完成；比 MVD 与 HoloClean 高 6.2% |

**实验 3（运行时间，Figure 9）**：IoT 用 2 条规则约 0.98 分钟，Hospital 21 条规则约 10.56 分钟，CONTEXT 6.8 分钟（dBoost 5.6、MVD 1.6）。运行时间不含生成 OFD 的时间（§6.1）。

**实验 4（修复，Figure 10）**：IoT 数值 RMSE 0.22；IoT 类别 LLMClean+Baran F1 85%；Hospital 数值 LLMClean+Baran RMSE 8.44E-05；Hospital 类别 LLMClean+ML 插补 78.7%（§6.2.3）。CONTEXT 修复结果被省略。

**原文承认的边界**（§6.3）：能力依赖依赖数据中出现明确传感器名及网上可查的技术规格；LLM 结果不稳定，跨运行会变化；非 IoT 数据的上下文更难生成。

**阅读者分析**：所列 “+x%” 未说明是绝对百分点还是相对提升。§6.2 宣布的三个场景（S1 上下文变化、S2 上下文模型、S3 传感器能力）只在 §6.3 用文字描述了 S1，没有数值。运行时间排除 LLM 生成上下文模型的开销，因此不能代表端到端成本。错误均为人工注入，未在自然错误数据上验证。

依据：[arXiv:2404.18681v1](https://arxiv.org/pdf/2404.18681v1)，§6、Table 2、Figures 5–10，PDF pp.6–11。
