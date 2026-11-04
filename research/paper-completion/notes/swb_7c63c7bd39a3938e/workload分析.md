# 工作负载

9 个公开 EM 数据集，沿用 Li et al.（2020）的线性化与 3:1:1 训练/验证/测试划分（§2.1，PDF p.2；附录 B，PDF p.13）。

| 数据集 | 领域 | 规模（原文所述） |
|---|---|---|
| Abt-Buy | 消费电子 | 9,575 实例 |
| Amazon-Google | 软件产品 | 11,460 对 |
| Walmart-Amazon | 一般消费品 | 10,242 对 |
| iTunes-Amazon | 歌曲 | 539 对 |
| Beer | 啤酒 | 450 对 |
| WDC-Computers / Cameras / Watches / Shoes | WDC Products | 训练规模 68,461 / 42,277 / 61,569 / 42,989；每类测试 800 负例 + 300 正例 |

WDC 每条记录有 title、description、brand、specTable 四个属性（附录 B，PDF p.13）。另有 WDC-All 作为训练集，测试于 Abt-Buy、Amazon-Google、Walmart-Amazon（Table 2，PDF p.4）。

**样本单位**是候选记录对，标签为二值匹配。Table 2 共 28 个"训练集→测试集"组合（跨领域 15、跨 schema 4、跨分布 9）（阅读者按渲染后的 Table 2 行数统计，PDF p.4）。

**人工评测子集**：从 Abt-Buy 选 300 个实例做 H1（鲁棒性）与 H2（事实性）（§3，PDF pp.7–8）。

阅读者分析：附录 B 对 WDC 括号中数字的含义没有明确说明是训练对数量，上表按上下文理解，引用时需谨慎。
