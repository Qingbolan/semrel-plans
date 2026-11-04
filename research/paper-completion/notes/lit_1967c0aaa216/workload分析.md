# 工作负载

8 个 Kaggle 竞赛（附录 B、Table 5，pp.16–17）：

| 编号 | 竞赛 | 类别 | 任务（原文） | 难度 | 队伍数 | 训练集 | 测试集 |
|---|---|---|---|---|---|---|---|
| 1 | Titanic | Classic | 分类 | 中 | 13994 | 891 | 418 |
| 2 | Spaceship Titanic | Classic | 分类 | 易 | 1720 | 8693 | 4277 |
| 3 | House Prices | Classic | 回归 | 中 | 4383 | 1460 | 1459 |
| 4 | Monsters | Classic | 分类 | 易 | 763 | 371 | 529 |
| 5 | Academic Success | Recent | 回归 | 中 | 2684 | 76.5K | 51K |
| 6 | Bank Churn | Recent | 回归 | 易 | 3632 | 165K | 110K |
| 7 | Obesity Risk | Recent | 分类 | 易 | 3587 | 20.8K | 13.8K |
| 8 | Plate Defect | Recent | 回归 | 中 | 2199 | 19.2K | 12.8K |

**类别定义**（§4.1，p.6）：Classic 指 2023 年 10 月前开始、参赛者至少 500 人的竞赛；Recent 指 2024 年及以后开始的竞赛，用于降低 GPT-4o 训练数据泄漏的影响。

**选择原则**：刻意避开大数据集，以控制运行时间；也没有采用 MLE-Bench 的 9 个表格数据集，因为资源不足以遵循它的 24 小时窗口设置（§4.1，p.6；附录 B，p.16）。

**评测方式**：提交文件由人工上传到 Kaggle 评分，而不是从训练集切出测试集（附录 B，p.16）。

依据：[arXiv:2410.20424v3，44 页](https://arxiv.org/pdf/2410.20424v3)，§4.1，PDF p.6；附录 B、Table 5，pp.16–17。
