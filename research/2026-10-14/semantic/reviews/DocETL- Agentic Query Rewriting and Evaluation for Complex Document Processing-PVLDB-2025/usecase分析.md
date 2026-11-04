# 具体用例

| 任务 | 输入表/字段 | 数据环境需求 | 输出 |
|---|---|---|---|
| CUAD | 每行合同文本 | 41类条款说明 | clause_type,text_span列表 |
| Steam | 每游戏聚合300条含ID和timestamp的review | 无独立外部库；评分只作gold | 10正面+10负面review并按时间排序 |
| BlackVault | 733篇解密事件文章 | 无独立外部库；地理编码用于评测核验 | 各统一事件类别的不同地点 |
| BioDEX | 250篇医学文章 | 24300反应标签表 | 每篇文章的反应标签排名 |

辅助输入必须按用途区分：Steam的用户评分在任务输入中省略而用于评价；BlackVault的Nominatim地理编码是评测工具，不是查询检索环境。警务案例来自真实合作场景，但不应把示例代码自动归为全部公开benchmark query。

来源：[DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing](https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf)。
