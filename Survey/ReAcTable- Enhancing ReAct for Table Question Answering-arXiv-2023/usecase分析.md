# 具体用例

**原文示例**（WikiTQ，Figures 1–2，§3.1–3.2）：

> which country had the most cyclists finish within the top 10?

表 T0 的列为 `Rank|Cyclist|Team|Time|Uci_protour_points`，国家缩写只出现在 Cyclist 值中，如 `Alejandro Valverde (ESP)`。ReAcTable 用 4 轮完成：

1. SQL：`SELECT Cyclist FROM T0 WHERE rank<=10;` → 中间表 T1（前 10 名车手）；
2. Python：用正则 `\((.*?)\)` 抽出括号内容，新增 Country 列 → T2；
3. SQL：`SELECT Country, COUNT(*) FROM T2 GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 1;` → T3，结果为 `ITA|3`；
4. 直接作答：`Italy`。

每轮的代码和中间表都追加进提示（Figure 2），后续轮次在更干净的表上推理。

**去掉 Python 执行器时**（§4.3.3）：仅 SQL 的变体第一轮生成相同 SQL，第二轮却直接回答 “Spain”，与表不符。这说明字符串变换步骤不可省略。

阅读者分析：这个例子体现的是对已给定表做语义变换，不涉及外部数据源发现，也不是论文的统计结论，只是单例演示（阅读者分析）。

依据：[arXiv 2310.00815](https://arxiv.org/abs/2310.00815)，§3.1–3.2、§4.3.3、Figures 1–2，PDF pp.2–4、10。
