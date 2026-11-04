# 具体用例

**DBA 视角的 CPU 高负载诊断**（§1，p.1；Figure 1c）：
1. 用户反馈日常查询比平时慢 120%。
2. DBA 看到 CPU High 告警（总 CPU 使用率超过 90%，持续 2 分钟）。
3. 查看运行和阻塞进程数、查询调用次数等 5 个 CPU 相关指标。
4. 从视图中取出 top-k 慢查询模板，发现其中一条占用近 60% 的 CPU 时间。
5. 建议为这条查询加索引或改写。

**D-Bot 的多步对应**（Figure 7，p.7）：LLM 若在第一步只得出"CPU 使用率高"就输出 Finish，属于过早停止。在匹配到 `cpu_resource_contention` 知识后，它会继续调用 `obtain_metric_values` 查看 node_procs_running 等指标，再调用 `optimize_index_selection` 给出索引建议。

**内存异常示例**（Example 1，p.3）：内存使用率超过 90%。查看 node_memory_inactive_anon_bytes 等指标后，推断原因是对某张表的大量插入，建议做分区。

报告中提到的一个复合异常 k（含两个根因）诊断用时 5.38 分钟，消耗约 40k token，约 1.8 美元（§8.3，p.10）。

阅读者分析：这个用例中，LLM 的每一步都是"选工具或知识 → 调用 → 解读观测"，与语义查询中"LLM 驱动的多跳检索"结构相似，可用来对照 agentic 算子的代价（轮数、token）和可信度（HEval）指标。

依据：§1、§2.2、§5、§8.3，pp.1–10。
