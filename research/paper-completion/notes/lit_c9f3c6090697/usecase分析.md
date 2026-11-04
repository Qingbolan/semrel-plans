# 具体用例

**查询改写**（Fig. 1 与 §3.2，pp.1、7–8）：

- **提示**：指令要求 “Rewrite the input SQL query to produce an equivalent query that can be executed on a PostgreSQL database with decreased latency”；示例给出一个分步说明的复杂改写；输入是待改写的 SQL。
- **输出 1**：模型把相关子查询 `sku_id > (...detail.store_id = info.id)` 改写为 INNER JOIN，使子查询不再依赖外层查询。
- **输出 2**：把 `exists(...)` 改写为 INNER JOIN，尽管示例里没有这条规则。

**索引调优**（p.8）：对谓词 `person_info.person_id > 4158523 AND person_info.info_type_id <> 22`，模型建议建 `person_info(person_id, info_type_id)` 复合索引。

两个例子都说明 LLM 是作为规则应用者被调用，输出的正确性（等价性、空间预算）由外部机制保证；论文自己承认目前对超出空间的索引是贪心截断（阅读者分析）。

依据：Fig. 1，p.1；§3.2，pp.7–8。
