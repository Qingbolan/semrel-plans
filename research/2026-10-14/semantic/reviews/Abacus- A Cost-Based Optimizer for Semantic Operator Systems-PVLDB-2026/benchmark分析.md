# 基准评测

| Table2任务 | Abacus质量 | 次高质量系统 | Abacus总费用/总时间 |
|---|---|---|---|
| BioDEX RP@K | 0.261±0.026 | LOTUS0.216±0.042 | $0.89 /450s |
| CUAD F1 | 0.662±0.010 | DocETL0.475±0.106 | $0.69 /450s |
| MMQA F1 | 0.304±0.079 | LOTUS0.284±0.046 | $13.1 /1149s |

该版摘要、§4.3叙述中的相对改进数字有不一致，本记录保留表2直接测量值，不合并成一个宣传性百分比。表2费用包括优化和执行；表3的min-cost/min-time使用execution口径。

表3也显示MMQA的min-cost均值$16.0高于max-quality execution$12.9；作者归因于embedding join估计的高方差，不能声称目标最小化在每次运行都成功。图6–8比较先验、MAB与Pareto-Cascades，约束满足率低于100%，支持“改善搜索”而非硬保证。未复现实验。

来源：[Abacus: A Cost-Based Optimizer for Semantic Operator Systems](https://arxiv.org/abs/2505.14661v3)。
