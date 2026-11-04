# 工作负载

Stat-Closed：404 题，18 个主题（Table 2，p.3）：非参数统计、描述统计、多重比较、相关分析、因果推断、分布检验各 30 题；GLM 25；生存分析、点估计、高维数据、列联表检验、A/B 测试、回归、方差检验各 20；贝叶斯 18；时间序列、探索性数据分析各 15；置信区间 11。其中 198 题为实际应用题（§4.1，p.6）；其余三种题型的具体数量原文正文未列出。

来源（附录 E.1，p.13）：开放教材（Introduction to Probability、Learning Statistics with jamovi、Linear Regression Using R、Think Bayes）；已有基准 StatQA 91 题、CLADDER 11 题、CORR2CAUSE 11 题；在线资源 Kaggle 数据集与 LibreTexts 习题。实际应用题通过两条路径生成：基于真实数据集让 Gemini 2.5 Pro 出题并给出参数，或无合适数据时由模型同时生成问题与合成数据代码（§3.2，p.4）。

Stat-Open：30 题，来自 MCM/ICM（多为数据洞察类 C 题）、CUMCM、全国应用统计专业学位研究生案例大赛（MAS），各带数据文件（§3.3、附录 E.2）。

评测规模：Stat-Closed 评 9 个模型（温度 0），另在 198 道实际应用题上评 5 个模型 × 4 个智能体框架；Stat-Open 评 2 个框架。原文没有给出数据划分（无训练/开发集），属于纯测试基准。
