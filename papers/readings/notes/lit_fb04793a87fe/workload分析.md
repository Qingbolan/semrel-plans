# 工作负载

**任务与数据集**（Table 2，p.7；附录 B.2，pp.18–20）：

| 模态 | 任务 | 数据集 | 指标 |
|---|---|---|---|
| 图像 | 图像分类 | Butterfly（75 类，1,000 多张）、Shopee-IET | 准确率 |
| 文本 | 文本分类 | Ecommerce Text（50,425 条）、Textual Entailment（训练 4,907 / 测试 4,908） | 准确率 |
| 表格 | 分类 | Banana Quality（8,000 条）、Software Defects | F1 |
| 表格 | 回归 | Crab Age、Crop Price | RMSLE |
| 表格 | 聚类 | Smoker Status、Student Performance | Rand index（据附录 B 指令文本，pp.15–16） |
| 时间序列 | 预测 | Weather、Electricity | RMSLE |
| 图 | 节点分类 | Cora、Citeseer | 准确率 |

**设置**：每个数据集各准备一条无约束指令和一条有约束指令（附录 B，Tables 3–4），并配一份全流程骨架脚本，共评测 28 个生成模型（§4.1，p.7）。每个设置跑 5 次，取平均（§4.2，p.7）。

**补充实验**：与 SELA 的比较使用另外 6 个数据集（smoker-status、click-prediction-small、mfeat-factors、wine-quality-white、colleges、house-prices），见 Table 12（p.47）。

依据：[arXiv:2410.02958v2，48 页](https://arxiv.org/pdf/2410.02958v2)，§4.1，PDF p.7；附录 B.2，pp.18–20；Table 12，p.47。
