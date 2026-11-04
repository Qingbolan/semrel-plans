# 工作负载

本文没有基准实验，只有案例研究。附录 Table 2（p.38）列出案例所用数据：

| 案例 | 数据集 | 规模（原文） | 分析目标 |
|---|---|---|---|
| 1 | Wine Quality（UCI） | 4898 × 11 | 酒精含量对质量的影响；训练模型并自动生成报告 |
| 2 | Auto MPG（UCI） | 398 × 7 | 线性回归预测 MPG，残差图与 Breusch–Pagan 检验 |
| 3 | Wine Quality | 4898 × 11 | 红葡萄酒平均酒精含量的 95% Bootstrap 置信区间（1000 次重采样） |
| 4 | Salary Data（Kaggle） | 6750 × 6 | 按年龄组可视化平均薪资 |
| 5 | Breast Cancer Wisconsin（UCI） | 569 × 30 | 二分类预测良性/恶性 |

§4.4 的可扩展性案例还用到 Data Interpreter 的自定义网页抓取工具，以及在 LAMBDA 知识库中加入 FPNNN 代码并在 MNIST 上训练（pp.22–25）。

**口径差异**：Table 2 与 §4.1 都写 Wine Quality 为 4898 × 11，但 Figure 5 中 ChatGPT-ADA 读入的文件显示 6497 行、13 列（含 color 列），说明案例实际使用的是红白合并版本（p.19）。这是阅读者对照原文发现的不一致（阅读者分析）。

案例没有训练/测试划分说明，也没有重复次数或评分规则。

依据：[arXiv:2412.14222v2，46 页](https://arxiv.org/pdf/2412.14222v2)，§4.1–4.4，PDF pp.18–25；附录 Table 2，p.38。
