# 具体用例

**市政议程项目统计（Figures 1、5、9、10，PDF pp.1–3、8–9）**：

1. 用户定义表：`CREATE TABLE Projects WITH DESCRIPTION "…civic agenda projects"`，再 `ALTER TABLE` 追加 name、type、begin_time 三个带描述的属性。
2. 查询（Figure 9）：对每个会议时间早于 "2023 October" 的文档，统计 type 为 "Capital Improvement" 且 begin_time 晚于 "2022-06-01" 的项目数，Projects 与 Agenda_Meeting 按 doc_id 连接。
3. 预处理：SHT 中 A1 节点为"Capital Improvement and Disaster Recovery Projects (Design)"，其子节点 B1、B2（如"PCH Median Improvement Project"）各对应一个项目元组；表填充在一个文档上用 `table_oracle`、`tuple_oracle` 两种提示定位表节点和元组节点，同模板其余文档按规则推广。
4. 执行（Figure 10）：Agenda_Meeting 只有 1 个元组、Projects 有 40 多个，故先评估前者；对 Projects 的每个元组，在其子树上用 `search_oracle` 检查节点摘要是否包含"项目类型"信息，再用 `evaluate_oracle` 判断谓词；由于节点摘要带有父标题"Capital Improvement Projects (Design)"，B2 可被识别为候选。

这个用例展示了"类型判断"这类语义谓词如何借助文档结构定位证据；若文档没有清晰的标题层次，该流程的优势会减弱（阅读者分析）。
