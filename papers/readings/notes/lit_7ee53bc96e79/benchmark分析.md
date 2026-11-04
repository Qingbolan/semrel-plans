# 评测与边界

基线：无训练组 ReAct、MultiAgent、Agent Harness/Biomni；训练组 Reflexion、Agent Workflow Memory、Agentic Memory、GEPA 式提示演化；同一模型家族、沙箱、任务包和评测器（§3.3）。指标：Workflow 完成度、Biology 正确性，Final=0.6·Workflow+0.4·Biology（式 7）；另报 token、API 轮数、执行时间和 Hi-C 里程碑。BioAgent Bench 报结果匹配率、最终结果到达率、平均步骤分和三者均值。

主要结果（Table 2，test35 Final）：

| 智能体 | Long | XLong | Overall |
|---|---|---|---|
| Agent Harness | 0.2386 | 0.2779 | 0.3926 |
| AWM | 0.2799 | 0.3071 | 0.4586 |
| GEPA | 0.3059 | 0.3090 | 0.4953 |
| PRTE | 0.3182 | 0.3922 | 0.5013 |

GEPA 在 small/medium 最高；PRTE 的 xlong 优势主要来自 Biology（0.4502 vs 0.3808）。

- **BioAgent Bench（Table 3）**：PRTE 与 Agent Harness 均为 8/10 匹配、10/10 完成，步骤分 0.9667 vs 0.9500。
- **消融（Table 4）**：过程奖励 0.5013、仅结果 0.4770、GEPA 0.4237（batch4）。
- **资源（Table 6）**：PRTE 测试总 token 963.454M（每任务 27.527M），MultiAgent 8,514.015M；Reflexion 最省（689.846M）。

边界：Table 2 标注只有 GEPA 与 PRTE 为 test35 实测，其他是 quick10→test35 换算估计；未报告重复运行或置信区间；Biology 断言是部分检查，不能替代专家审阅；公共 Galaxy 服务的可用性、排队和工具版本影响结果；错误的可复用修复可能伤害后续任务（Limitations，PDF p.6）。BioAgent Bench 只比较 4 个智能体，且只有 10 个短任务。代码与 tactic 制品承诺发表后发布。

阅读者分析：在“换算估计”与单次实测混合的条件下，0.006 的总分差不足以下强结论；long/xlong 的差距更值得关注。

依据：[arXiv 2606.20839v1，18 页](https://arxiv.org/pdf/2606.20839v1)，§3.3–4.5、Tables 2–6、Limitations，PDF pp.3–6。
