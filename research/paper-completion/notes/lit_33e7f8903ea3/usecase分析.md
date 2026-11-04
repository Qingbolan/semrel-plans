# 具体用例

**异常检测**（§8.1，pp.17–18；§2–§3 的动机例子）：时间序列存于 sqlite3 数据库。开发者只提供两个插件：`pull_data_sql(nl_query)` 返回 SQL 和 DataFrame；`anomaly_detection` 用 3-sigma 规则标出偏离均值超过 3 个标准差的点。读写文件等通用操作不需要插件。

Planner 的计划为：(1) 让 CI 从 time_series 表拉数据；(2) 确认要检测的列；(3) 调用异常检测；(4) 向用户报告。第 1 步 CI 生成 `SELECT * FROM time_series` 并调用插件；随后 TaskWeaver 向用户确认列名，用户给出 ts 和 val；第 3 步调用插件，最后报告检测到 11 个异常（pp.17–18）。

**股票预测**（§8.2，pp.18–19）：用户要求用 ARIMA 预测 QQQ 未来 7 天价格。第一次用 pandas_datareader 拉数据失败，CI 根据报错改用 yfinance 后成功，展示了自动纠错。

对数据管线而言，TaskWeaver 的“插件 = 带类型 schema 的函数、数据留在 kernel 中”接近把外部能力当作算子调用；但它不做查询优化、批量调度或代价估计，正确性主要依赖 LLM 生成的代码（阅读者分析）。

依据：§2–§3、§8，Figure 3，PDF pp.2–5、17–19。
