# Workload分析

**验证的问题。** 弱统计、慢来源和有限内存下，部分执行后重规划以及可调整连接算子能否降低等待与完成时间。

**数据与任务。** dbgen 1.31生成10MB与50MB TPC-D，存于DB2；属于合成业务基准。测试两表/三表连接及较复杂连接查询；查询答案按关系语义确定，无人工gold。WAN实验把华盛顿来源数据经法国INRIA echo server转发回来，是真实网络路径上的受控实验，不是独立异构业务源。

**最清楚的use case（原文§6.2、图3b）。** 输入 `partsupp ⋈ part`，一个或两个来源变慢→持续产出连接结果。传统hybrid hash join受阻塞侧影响；double pipelined join利用两边已到的数据继续匹配，提前产出。图3报告的是整条输出曲线，未提供可单独引用的业务记录成功案例。

**Baseline与公平性。** 连接比较 `Hybrid Hash Join` 与 `Double Pipelined Join`；溢出比较 `Left Flush`、`Symmetric Flush`、足够内存配置。§6.4比较 `Materialize`、`Materialize and replan`、`Pipeline`，计入物化代价；§6.5比较从头重规划、保存状态及usage pointers。相同关系与查询，但“足够内存”是资源参照，不是等资源baseline；保存状态不带指针甚至更慢。

**依据与边界。** §6.1–6.5，图3–5。成本指标包含首批结果、随时间输出与总耗时；来源启停策略的完整实证弱于连接和重规划实证。不能据此宣称任意来源发现或状态复用都受益。

[论文来源与版本](README.md)。
