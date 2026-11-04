# 工作负载

| 基准 | problemset 数 | 问题数 | 多轮对话 | 真实场景 | 平均难度 | 来源 |
|---|---|---|---|---|---|---|
| DSEval-Exercise | 21 | 187 | 是 | 否 | 17.3 | pandas-exercises 的 27 个笔记本、252 题，去掉可视化题 |
| DSEval-SO | 202 | 202 | 否 | 是 | 16.1 | PandasEval 与 NumpyEval 的 StackOverflow 题 |
| DSEval-LeetCode | 40 | 40 | 否 | 否 | 56.0 | 2023 年 8 月免费可用的 LeetCode pandas 题 |
| DSEval-Kaggle | 31 | 396 | 是 | 是 | 35.9 | 2023 年 4 月后发布、小于 10 MB、超过 100 票的 31 个 Kaggle 数据集及最高票笔记本 |

难度按参考代码中函数调用、表达式、条件和循环的数量计算。四个基准的参考代码共 2,240 次 API 调用、448 个不同 API，覆盖 12 个库，以 pandas、sklearn、numpy 为主。多轮基准中依赖图平均入度 2.08，最长依赖链 10；每题平均涉及 3.68 个变量（最多 29），变量数据中位数 1.12 KB，极端情况 268 MB。

依据：§4.2、§5、Table 1、Figures 7–9，PDF pp.4–6；Appendix E，PDF pp.16–17。
