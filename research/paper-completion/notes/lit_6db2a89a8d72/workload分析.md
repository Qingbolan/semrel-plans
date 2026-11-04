# 工作负载

**评测集（§6.1.1，p.6；附录 B Table 5，p.13）：**

| 基准 | 样本数 | 内容 | 评分说明 |
|---|---|---|---|
| DABench (InfiAgent-DABench) | 257 | 来自 52 个真实 CSV 的数据分析题 | 格式提示把开放输出规范为封闭形式 |
| DA-Code | 500 | 数据整理、EDA、机器学习等代码任务 | 可视化题因 EvoDS 用工具直接出图，改用 LLM-as-a-judge（参照 MatPlotBench） |
| ScienceAgentBench | 102 | 44 篇论文、4 个学科的科学发现任务 | 原文未细述指标 |
| MLE-Dojo | 10（随机抽样） | Kaggle 风格机器学习工程任务 | 因计算成本高仅抽样 10 题 |

**训练数据（§6.1.3，p.6）：** 来自 DataMind-12K、DataScience-Instruct-500K、MatPlotBench、DSBench、MLE-Dojo；对轨迹型数据用 GPT-4o 抽取问题与答案；DSBench/MLE-Dojo 只抽样子集且声称与测试集无重叠；再用 Qwen3-8B 过滤过于简单的样本，得到 8K 训练实例。SFT 用 DeepSeek-V3.1 每实例 8 条 rollout，共 36K 轨迹；RL 轮次预算从 4 逐步增至 20，rollout 8，300 步，最大响应 24K token，4×A800。

**技能复用实验划分（§6.4，p.8）：** DA-Code 按 3:2 划分为验证/测试；跨基准设置用 DA-Code 验证集收集的技能评测 ScienceAgentBench。

**阅读者分析：** MLE-Dojo 只有 10 题，0.302 与 0.311 等差异对应的样本量很小；论文未给出各基准的具体指标定义与方差、重复次数。各基准的分数尺度不同，Table 1 的 AVG 是不同指标的简单平均。
