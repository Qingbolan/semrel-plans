# 具体用例

Figure 3 的例子：用户提交“分析用户 Eugene 在 2024 年 1 月 10 日的计费记录”。

1. User agent 附上 PingCAP 业务 SOP（含 DoD 分析等要求），Planner 据此给出 9 步计划。
2. FSM 调度器把计划交给 Engineer，Engineer 逐步细化，并把需要写 SQL 或计算的子任务交给 Executor。
3. Executor 调用 LinguFlow 部署的 text-to-SQL 应用，经 Trino 连接器查询多个系统中的表；若返回错误或空值（工业数据中常因大小写导致空结果），错误信息作为常识反馈给 Engineer 重试。
4. Critic 检查是否完成初始任务，若有缺口则交回 Planner 修订计划；完成后汇总报告并输出 TERMINATE。

图中未给出每步执行结果和输出格式。

依据：§3.2、Figure 3，PDF pp.3–4；§4.3、Figure 5，PDF pp.6–7；§4.4，PDF p.8。
