# 具体用例

**查询 q′（Figure 3）**：在城市与政客两个关系上，筛选年龄小于 40 岁的政客并与城市关联（如城市市长），城市还带人口条件。

执行计划：

1. 叶子 C：提示 LLM 列出城市名（键），用“Return more results”反复追问直至无新结果；
2. 选择：对每个城市名问“Has city c.name more than 1M population?”；
3. 叶子 P：列出政客名；选择 p.age<40 由模板“Has relationName keyName attributeName operator value?”实例化为“Has politician B. Obama age less than 40?”；
4. 连接前补取属性：对每个城市问“Get the current mayor of c.name”；
5. 最后两个算子（连接、投影）在 Python 中执行，不调用 LLM。

**混合查询示例**（§1）：`SELECT c.GDP, AVG(e.salary) FROM LLM.country c, DB.Employees e WHERE c.code = e.countryCode GROUP BY e.countryCode`，其中国家 GDP 来自 LLM，员工薪资来自数据库。

**失败案例**：连接时 LLM 给出的国家代码格式不一致，例如用“IT”去连“ITA”，导致连接失败。

这一用例说明逐键提示的调用量与结果规模成正比（GPT-3 平均每条查询约 110 个批量提示），也说明作者在 §6 提出的选择下推（如“列出人口超过 100 万的城市”）是减少调用的关键优化（阅读者分析）。

依据：§1，p.2；§4、Figure 3，pp.3–4；§5，p.5；§6 Query optimization，p.5。
