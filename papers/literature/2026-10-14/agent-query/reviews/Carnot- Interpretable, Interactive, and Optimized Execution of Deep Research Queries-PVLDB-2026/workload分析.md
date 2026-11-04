# 工作负载与输入

§3.1演示两组数据：行业伙伴1000条消费品评论，去除真实产品名/ID并由LLM改写标题和review text后人工检查情绪/内容；KramaBench legal workload。1000条评论是真实来源经过匿名化改写的数据，不应标为未经处理的原始用户评论。

| 用例 | 查询输入 | 环境需求 |
|---|---|---|
| 找主要投诉与负面属性 | 已选产品评论dataset中的评分、标题、文本等 | 上传的数据文件、dataset描述、workspace |
| KramaBench法律分析 | legal workload的文件集合；文中未给此演示完整query清单/规模 | 能访问该命名dataset |
| 图2筛选AI论文 | research papers文件集合 | 文件读取和文档处理；数量未在正文明确 |

API key、S3/Postgres是部署支撑，不是每条问题需要推理的业务数据。论文没有给record batch size、query batch size或并发数，不能把1000评论等同一次模型调用的batch。
