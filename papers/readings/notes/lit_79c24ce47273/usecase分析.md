# 具体用例

**数据整理示例**（Fig. 4，p.8）：任务说明为“According to the pre-defined database information, sort the data in the data folder and load it into the database”。环境中有 Citi Bike（JC）骑行数据、天气数据及预定义数据库 schema。参考计划包括：

1. 查看 schema 中五张表及列名，检查 `./data` 中的文件；
2. 由 `trip_duration` 计算分钟和小时；把降雨、降雪数值转换为布尔标志以匹配 schema；
3. 合并五个月数据并核对缺失列；
4. 创建 stations 表并用 SQL INSERT 载入。

**另一数据整理示例**（Fig. 2，p.3；§2.2 称 Fig. 2 与 Fig. 4 为数据整理示例）：基于 NYC Parking 数据库，把 `vehicle_color` 字段中表示同一颜色的不同写法统一，例如统一为 gray。评测检查结果表中指定的列是否与参考表完全一致（§3.4，p.4）。

这类任务把 schema 理解、文件探索、清洗规则与 SQL 写入组合在一个多步过程中，结果按最终数据库状态判分，而不是比对中间代码（阅读者分析）。

依据：Fig. 2，p.3；Fig. 4，p.8；§3.4，p.4。
