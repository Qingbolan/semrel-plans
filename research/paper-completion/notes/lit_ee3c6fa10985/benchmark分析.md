# 评测与边界

**基线（§4.2，PDF p.7）**：无检索的 Llama2 7B/13B、Alpaca、ChatGPT、Llama2-chat-13B、CoVE-65B；有检索的 RAG 版 Llama2/Alpaca、Llama2-FT（同数据训练但不含反思 token 和检索段落）、Ret-ChatGPT、Ret-Llama2-chat、perplexity.ai、SAIL、Toolformer。ASQA 所有方法统一使用作者提供的 GTR-XXL top-5 文档。

**主结果（Table 2，PDF p.8）**：

| 模型 | PopQA | TQA | Pub | ARC | Bio FS | ASQA em | ASQA 引用 P/R |
|---|---|---|---|---|---|---|---|
| Ret-ChatGPT | 50.8 | 65.7 | 54.7 | 75.3 | – | 40.7 | 65.1/76.6 |
| Alpaca13B+检索 | 46.1 | 66.9 | 51.1 | 57.6 | 77.7 | 34.8 | 2.0/3.8 |
| Self-RAG 7B | 54.9 | 66.4 | 72.4 | 67.3 | 81.2 | 30.0 | 66.9/67.8 |
| Self-RAG 13B | 55.8 | 69.3 | 74.5 | 73.1 | 80.2 | 31.7 | 70.3/71.3 |

Self-RAG 在 ASQA em 上低于 Ret-ChatGPT 和 Alpaca13B+检索，在 ARC 上也低于 Ret-ChatGPT（阅读者分析）。

**实验 2（消融，Figure 3a，PDF p.9）**：使用 50k 训练数据的 7B 模型，ASQA 只抽 150 条。完整模型 PopQA/PubHealth/ASQA 为 45.5/73.5/32.1。No Critic 的 ASQA 降为 18.1；推理时不检索的 PopQA 降为 24.7。

**边界**：v1 没有局限章节，Ethical Concerns 承认仍会生成未被引用完全支持的输出。人评只抽 50 条；部分基线结果引自其他论文（标 *）。
