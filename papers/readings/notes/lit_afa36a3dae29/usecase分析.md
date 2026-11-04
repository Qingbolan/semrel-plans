# 具体用例

Figure 1：用户上传 baro_2015.csv，要求计算 WINDSPEED 列在排除空值后的算术平均，保留三位小数。

DatawiseAgent 先用 markdown 写出步骤目标，再生成读取 CSV 并求均值的代码；执行时出现 KeyError。自调试发现列名含空白，加入 `data.columns.str.strip()` 修复。

后过滤把调试过程压缩为一段说明和最终正确代码，最终输出“Mean Wind Speed: 5.979”。

附录 B 另有 DSBench 第 48 题的预测建模案例：多轮探索、划分数据、设计并训练模型、预测，中间多次报错后修复。

此例展示的是 schema 细节（列名空白）导致执行错误后被自动修复，这是表格分析 agent 的常见失效点（阅读者分析）。

依据：Figure 1、附录 B，PDF pp.2、12、18。
