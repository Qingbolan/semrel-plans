# Workload 分析

**要验证的问题。** 检验整体表达工具依赖并并行调度，能否降低工具调用延迟、token成本，且保持答案质量；包含静态依赖和重规划两种情况。

**数据、任务单位与gold。** HotpotQA只用约1500个comparison dev问题；BIG-bench Movie Recommendation500题；作者构造ParallelQA113题，限定Wikipedia首段足够回答；Game of24用100个数值实例，按表达式是否合法得到24评分。前两者是基准问答，ParallelQA是设计任务，24点为合成算术；任务单位一次问答。指标准确率、墙钟时间和token/估计费用。

**具体use case：输入目标 → 使用前 → 使用后。** 图3原文例子：“Stanford和UCLA诺奖数相加是否超过UC Berkeley？”使用前ReAct逐次查3个学校再算；使用后3次查找并行，结果就绪后做加法和比较。这里依赖图可预知，只是数字待绑定；§5.3的24点则根据候选评估结果继续重规划，不能把系统局限为前一种。

**Baseline与比较条件。** 比较ReAct、修复重复调用/提前结束提示的ReAct†、OpenAI Parallel Function Calling；24点比较Tree-of-Thoughts。相同任务采用相同工具；主HotpotQA排除了lookup，仅测comparison；附录补bridge。表1原版ReAct部分延迟未报告，因此加速基准应指ReAct†而非随意用原版。

**证据边界。** ParallelQA通过筛题排除检索失败，所以能证明依赖调度而不能证明大环境证据发现。没有跨独立任务证据复用实验。

来源：[阅读版本](https://www.stat.berkeley.edu/~mmahoney/pubs/icml2024_kim24y.pdf)，§5.1–5.3、图3、表1–2、附录A/B/C/I/K。本文为原文工作负载分析，未复现实验。
