# 具体用例

**SQL 风格提示（Figure 10 与 Figure 15，PDF pp.9、12）**：数据库含 `airports(City, AirportCode, AirportName)` 与 `airlines(uid, Airline, …)`。提示先以注释给出 `CREATE TABLE` 形式的 schema，再写入问题"What are airport names at City 'Aberdeen'?"，目标输出：

`SELECT AirportName FROM airports WHERE City = "Aberdeen";`

**SuperSQL 的提示组织（Figure 15）**：先用 RESDSQL 的 schema linking 去掉无关表和列；再借 BRIDGE v2 的 DB content 模块，把与问题匹配的单元格值（如 Aberdeen）以注释形式附在对应列旁；然后加入按相似度选出的 few-shot 示例，由 GPT-4 贪心生成多个候选，最后以 self-consistency 投票（§5.3，PDF p.12）。

**BI 场景的动机例子**：同一意图的不同问法，如"Return all customers whose total consumption is greater than 1000"与"What is the list of customers who spent more than 1,000?"，应生成同一条 SQL。这正是 QVT 要衡量的稳定性（§1 Example 1，PDF p.2）。

例子中的值匹配（Aberdeen 出现在 City 列）依赖库内字符串匹配；若条件是语义性的（如"沿海城市"），本文方法不覆盖，需另行处理（阅读者分析）。
