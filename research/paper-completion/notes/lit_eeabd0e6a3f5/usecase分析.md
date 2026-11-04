# 具体用例

Example 1 / Fig.2 / Example 5（PDF pp.2、3、9）：用户反映 INSERT 语句执行很慢。Andromeda：

1. 检索到相似历史问题（“插入大量数据耗时超过 15 分钟”），其采纳方案是关闭 foreign_key_checks 和 unique_checks；
2. 检索到 MySQL Manual 10.5.5「InnoDB 批量加载」中“导入时关闭 autocommit”的句子，对应 autocommit = 0；
3. 遥测分析发现 innodb_log_write_requests 等指标异常（如由 46,492 变为 96,561），并给出相关 knob innodb_log_file_size；
4. LLM 输出 knob 及取值，如 SET unique_checks = OFF、SET autocommit = OFF、tmp_table_size = 256M。

附录失败案例（PDF p.17）：用户想屏蔽警告，正确 knob 是 sql_notes，但检索到 sql_warning、max_error_count、log_warnings 等功能相近的 knob，系统难以区分。

阅读者分析：该用例展示把“自然语言故障描述 + 运行遥测”转为结构化配置动作的流程；若项目把它视为语义查询或工具调用任务，应保留知识源、遥测窗口和人工确认步骤。这些是项目派生用法。

依据：§1、§3、§5.2、附录案例，PDF pp.2–4、9、17。
