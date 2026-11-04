# 具体用例

原文贯穿的用例是研究人员用 SQL 检索论文（§2，PDF pp.2–3）：

1. 用 `CREATE GLOBAL MODEL('model-relevance-check','gpt-4o-mini','openai')` 和 `CREATE PROMPT('joins-prompt', ...)` 定义可复用资源（Query 1）。
2. 在 CTE 中用 `llm_filter` 依据标题和摘要筛出与连接算法相关的论文，再用 `llm_complete`（gpt-4o）一句话总结摘要，用 `llm_complete_json` 抽取三个关键词和“实证/理论”类型（Query 2）。
3. 对段落表做混合检索：`llm_embedding` 计算查询向量并取余弦相似度 top-100，FTS 扩展 BM25 取 top-100，FULL OUTER JOIN 后按各检索器最大分归一化并 fusion 取 top-10，最后 `llm_rerank` 按“mentions cyclic joins”重排（Query 3）。

Query 3 的向量检索对每个段落在查询时调用 llm_embedding，没有使用预计算索引（作者说明可改用 VSS 扩展，此处仅为展示函数灵活性）；这对大表的成本含义原文未讨论。（阅读者分析）
