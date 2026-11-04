# 工作负载

**四类评测**（§4.1，pp.7–8；附录 D.1，pp.19–20）：

| 评测 | 规模 | 输入 | 模型 | 指标 |
|---|---|---|---|---|
| InfiAgent-DABench | 257 题、52 个 CSV、7 类 | CSV + 带格式要求的问题 | gpt-4o、gpt-4-0613，温度 0 | 准确率 |
| ML-Benchmark（自建） | 8 个 Kaggle/sklearn 数据集，3 个难度级 | 训练/验证表、需求、建议步骤 | gpt-4-1106-preview | 综合分 CS |
| 开放任务（自建） | 20 个任务、8 类 | 图片、网页、邮箱账号等 | gpt-4-1106-preview，3 次平均 | 完成率 CR |
| MATH | 4 类 level-5 题 | 数学题 | — | 准确率 |

**InfiAgent-DABench 示例**（附录 D.1，p.19）：类别覆盖汇总统计、特征工程、相关性分析、机器学习、分布分析、异常检测、综合预处理及其组合；每题指定 CSV 路径和 `@mean[...]` 这类输出格式。

**ML-Benchmark**（Table 9，p.29）：Iris、Wine、Breast Cancer（toy，需自行切分）；Titanic、House Prices（beginner）；Santander Customer、ICR、Santander Value（industry）。Table 2 只列出 7 个任务（Iris 未列）。

**指标定义**（附录 D.2，pp.20–21）：
- CR：每个要求步骤按 缺失/失败=0、成功但不合规=1、成功且合规=2 打分，除以满分；
- NPS：准确率、F1、AUC 取原值；越小越好的指标（如 RMSLE）取 1/(1+s)；
- CS = 0.5 × CR + 0.5 × NPS；开放任务的 NPS 设为 0，CS 直接等于 CR。

阅读者分析：四类任务的指标不同，不能合并成一个“成功率”；具体列名和路径应从各题发布文件取，论文没有统一的记录批大小。

依据：[arXiv 2402.18679v4](https://arxiv.org/abs/2402.18679v4)，§4.1、附录 D.1–D.2、Table 9，pp.7–8、19–21、29。
