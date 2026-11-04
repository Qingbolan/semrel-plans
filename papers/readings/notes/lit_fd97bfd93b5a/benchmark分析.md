# benchmark

**基线与变体**：DuckDB 默认优化器；Teacher Only；Teacher+Bandit；Teacher+Bandit+Cost（T+B+C）；Student（LR）；Student（HGBC）。指标：中位延迟、约束满足率（CSR）、规划时间、student 复现准确率、代价模型 MAE/R²、规划开销（§III-C，PDF p.3）。

**主要结果**（Tables III–V，PDF pp.4–5）：
| 方法 | 中位延迟 ms | CSR % | 规划 ms |
|---|---|---|---|
| DuckDB 默认 | 340.2 | 72.3 | 0.0 |
| Teacher Only | 285.7 | 85.1 | 12.3 |
| T+B | 262.4 | 94.2 | 45.7 |
| T+B+C | 251.8 | 96.1 | 38.2 |
| Student LR | 268.9 | 91.4 | 2.8 |
| Student HGBC | 259.3 | 93.7 | 3.1 |

随机森林 MAE=18.4ms、R²=0.87（Fig.3）；student 准确率 LR 86.3%、HGBC 89.1%，加速 13.6x / 12.3x（Table V）。

**原文内部不一致**（阅读者核对）：
- 摘要与结论称“23% 延迟降低”，但按 Table III 计算 (340.2−251.8)/340.2≈26.0%，且 Fig.4 的消融 16.0%+6.9%+3.1% 也合计约 26%。
- 摘要称 student “15x faster”，Table V 为 13.6x/12.3x，§V-A 又写 12–14x。
- Table II 与 Table III 内容完全相同。
- Table VI 中 Bandit Search 的 “Overhead Ratio 82.2%” 与 Total 11.5% 的口径无法对应，原文未解释。

**局限**：原文 §V-B 承认仅在中等规模 schema 上评估、缺少负载漂移适应、未扩展到分布式。阅读者补充：只有 DuckDB 一个基线，未与 Bao/Neo/Balsa 等学习型优化器对比；未报告方差/重复次数和硬件；未验证 sampling 带来的结果误差。上述数字只能视为作者报告值，证据强度弱。

依据：[arXiv:2605.17831v1，6 页](https://arxiv.org/abs/2605.17831)，§III-C、§IV、§V，Tables II–VI，PDF pp.3–5。
