# 具体用例

附录 B（p.10）的测试案例展示了一次真实诊断：

1. Chief DBA 调用 `obtain_anomaly_time`，得到异常起止时间 2023-08-05 23:38:30 至 23:43:30；
2. CPU Agent 调用 `whether_is_abnormal_metric` 判断 CPU 使用异常，再用 `obtain_cpu_metrics` 读取 Prometheus 指标，如 node_procs_running=18、node_load1/5/15 = 7.33/2.4/0.89，判断系统负载高；
3. CPU Agent 用 `knowledge_matching` 匹配到 workload_contention 经验，给出"监控运行进程数、排查资源争用"的建议；
4. Memory Agent 发现非活动匿名内存偏高，再调用 `obtain_slow_queries` 读取 `pg_stat_statements`，找出多表连接的慢查询，匹配到 poor_join_performance 经验（如 `enable_hashjoin` 被关闭等四种情形），建议优化 SQL 结构、检查索引。

§9（pp.6–7）给出的对比说明：在 INSERT_LARGE_DATA 案例中，基线只看到 node_procs_running 偏高就停止；D-Bot 进一步查看 `pg_stat_statements`，指出大量 UPDATE/INSERT 导致内存使用高。在 CORRELATED_SUBQUERY 案例中，基线看到 SORT 操作就归因为"大量数据读取排序"；D-Bot 结合查询优化知识识别出相关子查询结构。

阅读者分析：这个用例的输出是自然语言诊断报告与建议，不是可执行的修复动作；论文没有报告按建议执行后性能是否恢复。

依据：§9、附录 B、Figure 5，PDF pp.6–7、10。
