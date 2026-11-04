# 工作负载

论文没有正式的基准工作负载或查询集。出现的数据与查询：

| 内容 | 规模/细节 | 位置 |
|---|---|---|
| research_papers(id, title, abstract, content) 示例表 | 未给行数，仅用于说明 Query 1–2 | §2，PDF p.2 |
| research_passages(idx, content) | 未给规模；Query 3 向量检索与 BM25 各取 top-100，融合后取 top-10 再 rerank | §2.2，PDF p.3 |
| Kaggle Bank Review 数据集 | 用于批处理加速测试，单个标量函数的表扫描查询；行数、模型、批大小均未报告 | §2.3，PDF p.4 |
| 演示数据 | 多个 Kaggle 表格数据集，涉及生物医学、学术、产品评论；示例 NL 查询“list reviews mentioning technical issues and assign a severity score to each issue” | §3，PDF p.4 |

使用的模型包括 gpt-4o-mini、gpt-4o、text-embedding-3-small（Queries 1–3），提供方为 Azure、OpenAI 或本地 Ollama（§2.2）。

没有划分、标注或质量真值，因此该文不能作为语义查询质量的评测来源。（阅读者分析）
