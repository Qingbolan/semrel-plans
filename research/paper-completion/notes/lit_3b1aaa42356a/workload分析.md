# 工作负载

论文没有使用基准数据集或查询集合，也没有报告数据规模。唯一的工作负载是演示任务 **“Global Sales Performance Analysis”（全球销售业绩分析）**（§1 Demonstration Scenarios，p.2；§3，p.4）：

| 组成 | 内容（论文描述） |
|---|---|
| 结构化数据 | 上传到 Data Sources Panel 的销售记录（以 @Sales Database 绑定） |
| 非结构化知识 | 上传到知识库的领域知识文档（以 @Financial Metrics 绑定） |
| 用户请求 | "Help me analyze the 2025 global sales performance." |
| 期望输出 | 数据视频、仪表盘、分析报告 |
| 生成的工作流特征 | Knowledge Search Node 与 Datasource Read Node 位于同一执行层并行执行 |

支持的数据源类别见 Fig.1（p.2）：结构化、半结构化、非结构化数据源，文件系统，PostgreSQL，Amazon S3 等。销售记录的表结构、行数，知识文档的数量与类型，均未给出。

阅读者分析：如果 atlas 要把 DeepEye 当作工作负载来源，只能引用它的“结构化表 + 指标定义文档联合分析”这一场景描述；它不提供可复现的查询、标注或评测指标。
