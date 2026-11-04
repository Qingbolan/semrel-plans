# 工作负载

**HybridQA（§6.1，PDF pp.6–7）**：约 7 万个问答对，对齐 13,000 张 Wikipedia 表，表中实体链接到多段自由文本，每题都需同时使用表格和文本。SUQL 只用少于 10 个上下文示例，不使用 6.2 万训练样本。报告了开发集和留出测试集结果；单元格链接的段落被存入单独的 `C_Info` 列（§4，PDF p.4）。

**Yelp 餐厅（§6.2，PDF p.8）**：
- 4 个城市共 1,828 家餐厅，每家附 top 20 条评论和 20 道热门菜；
- 列包括 name、cuisines、price、rating、num_reviews、address、phone_number、opening_hours、location、reviews、popular_dishes；
- 通过 Prolific 众包得到 100 个单轮问题，以及 20 段对话共 96 轮，其中 62 轮是搜索查询。

| 集合 | 仅结构化 | 结构化+文本 | 合计 |
|---|---|---|---|
| 单轮 | 45 | 55 | 100 |
| 对话 | 37 | 25 | 62 |

（Table 4，PDF p.8）

餐厅评测规模小，且由人工逐条判断真/假阳性，没有可复用的金标准答案集合；数据声称“将会公开”（Ethical Considerations，PDF p.9）（阅读者分析）
