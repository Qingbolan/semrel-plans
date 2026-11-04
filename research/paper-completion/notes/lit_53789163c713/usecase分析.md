# 具体用例

论文贯穿全文的例子：表含 Date、Cyclist、Medal、Age 四列，问题是“哪个国家在二月获得的奖牌最多？”。

**Planner**：CoC 先生成 Analysis Sketch：`SELECT f(Country, Cyclist) AS Country, SUM(Medal) AS Total FROM w WHERE Date LIKE '02-%' GROUP BY Country ORDER BY Total DESC LIMIT 1`。逐子句得到：从 Cyclist 派生 Country；把 Medal 中带引号和星号的值转成整数；把 “02-28”“Jan. 1st”“02/22” 统一为 %m-%d；过滤掉 Age 列。

**Programmer / Executor**：Derive 选 `extract` 函数并给出正则；执行时 “Dav. ITA” 不含括号导致报错，Executor 汇总错误与相关取值交回 Programmer 修正 lambda。

**Analyzer**：在准备后的表上用 NL2SQL 得到答案 ITA。

对比的直接提示法会错误地删掉 Cyclist 列，并漏掉对 Date 的归一化，因为问题里没有提示日期格式不一致。

依据：§3 Example 3、Figure 4，PDF pp.5–6；§4.1 Example 4、§4.2 Example 5、Figure 5，PDF pp.5–7；§5.1、Figure 6，PDF pp.7–8。
