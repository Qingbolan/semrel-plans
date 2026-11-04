# 具体用例

论文贯穿全文的 BIRD 例子（Figure 1、3、4；附录 B.2）：

- 问题：List school names of charter schools with an SAT excellence rate over the average.
- evidence：特许学校指 frpm 表中 `Charter School (Y/N)` = 1；优秀率 = NumGE1500 / NumTstTakr。
- 相关表：frpm、satscores（以及被 Selector 判断为无关的 schools 表的大部分列）。

流程：

1. **Selector** 保留 frpm 与 satscores 的相关列；
2. **Decomposer** 拆为子问题 1“求特许学校 SAT 优秀率平均值”（`SELECT AVG(CAST(NumGE1500 AS REAL)/NumTstTakr) ... WHERE Charter School (Y/N) = 1`）和子问题 2“列出优秀率高于平均的特许学校名”，后者把子问题 1 的 SQL 作为嵌套子查询；
3. **Refiner** 在 SQLite 执行时遇到 `near "(": syntax error`（多余括号），据报错修正后返回最终 SQL。

阅读者分析：这一例子同时涉及跨表连接、派生指标（需 evidence 提供公式）和嵌套聚合，代表 BIRD 中“外部知识 + 多步”的典型难点；MAC-SQL 的增益来自分步生成与执行反馈，而不是对数据内容的语义理解（单元格值只以少量示例形式进入提示）。

依据：Figure 1，p.1；Figures 2–4，pp.2、4；附录 B.2，pp.13–15。
