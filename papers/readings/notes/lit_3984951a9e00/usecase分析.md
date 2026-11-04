# 具体用例

论文贯穿使用的玩具例子是一个含 continents（ContId, Continent）和 countries（CountryId, CountryName, Continent）两张表的数据库，问题为 “How many continents are there?”（Listings 1–5，pp.3–4）。

**同一问题的不同提示形态**：

- BS：只列出表名和列名，问题前缀 “Q:”，回复前缀 “A: SELECT”。
- OD：所有内容以 `#` 注释，开头加规则 “Complete sqlite SQL query only and with no explanation”。
- CR：给出完整 `CREATE TABLE` 语句（含类型、主键、外键），问题写在 `/* */` 注释里。

**DAIL 组织的少样本提示**（Listing 8，p.5）：先给若干示例的问题和 SQL，例如 “How many authors are there?” → `SELECT count(*) FROM authors`，“How many farms are there?” → `SELECT count(*) FROM farm`；示例不带各自的 schema，最后接目标问题的 CR 表示。这些示例与目标问题的骨架相同（都是 `SELECT count(*) FROM <table>`），正是 DAIL 选择所追求的问题与查询双相似。

在需要把自然语言转成结构化查询的数据管线中，这篇论文提供的是“如何构造提示”的经验规则，而不是查询执行或多表检索方案；当 schema 很大、放不进上下文时，CR 表示的代价会很高，论文没有评测这种情况（阅读者分析）。

依据：§3.1–3.3、Listings 1–8，PDF pp.3–6。
