# 评测与边界

**实验 1（来源发现，CMDBench，§5.2，Figure 7）**：按问题难度比较各模态的发现效果。

| 模态 | 发现方法 | 指标 | 难度分组 |
|---|---|---|---|
| 图 | gpt-3.5-turbo、gpt-4-turbo | Node F1 | node / edge / subgraph |
| 文档 | BGE-base、BGE-large（基于 LlamaIndex） | R-Precision | single-doc / multi-doc |
| 表 | BGE-base、BM25 | Recall@1 | easy / hard |

结论（§5.2）：除表上的 BGE-base 外，问题越难发现效果越差；表上的难题常含列名等更多上下文，反而更易检索。作者称即使用最好的发现模型，各模态准确率也有 46% 的下降。Figure 7 只有柱状图，正文未给出数值。

**实验 2（图查询生成，CypherBench，§5.3，Table 1）**：零样本执行准确率 EX（%）。

| 类别 | 模型与 EX |
|---|---|
| 开源 <10B | llama3.2-3b 11.20；llama3.1-8b 18.82；gemma2-9b 18.61 |
| 开源 10–100B | mixtral-8x7b 19.21；qwen2.5-72b 41.87；llama3.1-70b 38.84 |
| 闭源 | yi-large 33.82；gemini1.5-flash 25.26；gemini1.5-pro 39.95；gpt-4o-mini 31.43；gpt-4o 60.18；claude3.5-sonnet 61.58 |

最好模型 61.58%，最好开源模型 41.87%，10B 以下模型均低于 20%。

**边界**：
- 两个实验都是单组件基准，不是对设想系统的评测；没有基线系统对比，也没有端到端答案准确率、延迟或代价。
- “46% 下降”的比较口径（相对什么基准、哪个任务）本文未说明，需查 CMDBench 原文，不宜单独引用（阅读者分析）。
- 61.58% 是图查询生成的绝对准确率，不代表本文系统相对旧方法的提升（阅读者分析）。
- §4 的优化问题（跨模态代价估计、谓词下推、并行子计划）均未实现或测试。

依据：[arXiv 2504.02059v1](https://arxiv.org/abs/2504.02059v1)，§5.1–5.3、Figure 7、Table 1，PDF pp.5–6。
