# 工作负载

**数据集（附录 C.1，PDF p.17）**：均由已有判别式数据集改造，隐藏标签列后，在非结构化列上做分析，并用隐藏的标签计算真值。

| 数据集 | 模态 | 规模 | 查询条件（在数据中的占比，Table 6） |
|---|---|---|---|
| IMDB | 影评文本 | 50K 条 | positive_review 50% |
| ABCD | 客服对话 | 10,042 条对话，10 种意图 | account_access 10.44%，single_item_query 10.41% |
| AirDialog | 订票对话 | 402,037 条对话，5 种结局 | book 51.40%，no_flight 23.08%，no_reservation 23.89%，cancel 1.46% |
| Clevr | 图像 | val 集 15,000 张，降采样至不超过 128×128 | obj_count < 4 为 12.65%，# spheres > 3 为 17.53% |

**查询模板**（§6.1，PDF pp.8–9）：

- 条件聚合：`SELECT COUNT(*) FROM {table} WHERE {自然语言条件}`；
- 语义检索：`SELECT * FROM {table} WHERE {自然语言条件} LIMIT B`，B = 256；
- 抽象聚合：`SELECT derived_attribute, COUNT(*) FROM {table} GROUP BY {自然语言抽象}`，在 AirDialog 与 ABCD 上进行。

**设置**：文本嵌入用 voyage-2，图像嵌入用 Vertex（512 维）；聚合查询用 faiss 聚为 10 组再分层抽样；带预算约束的查询默认最多访问 128 行（§6.1、附录 C.2，PDF pp.8、18）。

§6.1 的默认预算写作 128 行（Table 5 中 IMDB 聚合的主结果即对应 B=128），而语义检索写 LIMIT B = 256（Table 4 检索 F1 0.978 对应 B=256）；两处 B 取值不同，正文未集中说明（阅读者分析）。
