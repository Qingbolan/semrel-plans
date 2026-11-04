# 评测与边界

**设置**：检索用 Qwen3-Embedding-0.6B 与 Qwen3-Reranker-0.6B；生成用 Qwen3.5-4B、Qwen3.6-35B（实际为 Qwen3.6-35B-A3B-FP8）与 Gemini-3.1-Pro。所有基线共享相同嵌入、重排和生成骨干。检索指标为 R@10、nDCG@10、FullCov@10（top-10 覆盖全部真值的问题比例）。生成指标为 Claim F1（LLM 评审，部分匹配记 0.5）和 Citation F1（条级）。

**实验 1（检索，Table 3）**：

| 方法 | RegOps R@10 | FullCov@10 | nDCG@10 | HIPAA R@10 |
|---|---|---|---|---|
| BM25 | 34.8 | 25.5 | 27.0 | 94.0 |
| LightRAG | 45.3 | 32.5 | 31.9 | 100.0 |
| HippoRAG-2 | 42.6 | 29.9 | 26.5 | 97.0 |
| PIKE-RAG | 54.6 | 37.2 | 51.4 | 97.0 |
| Dense+Rerank | 57.9 | 39.0 | 53.8 | 94.0 |
| RefWalk | 63.8 | 45.9 | 57.6 | 99.0 |

HIPAA 上检索基本饱和，LightRAG 达 100。按难度分层（Table 6），RefWalk 的 L4 FullCov@10 只有 10.5%。

**实验 2（端到端，Table 4，Qwen3.6-35B）**：

| 方法 | Claim F1 | Citation F1 |
|---|---|---|
| NativeRAG | 37.7 | 46.7 |
| LightRAG | 37.0 | 40.7 |
| HippoRAG-2 | 37.0 | 47.8 |
| PIKE-RAG | 38.0 | 44.3 |
| RefWalk | 41.1 | 54.9 |
| RefWalk w/o schema | 37.9 | 51.8 |

4B 模型下 RefWalk 的 Claim 召回（39.6）低于 NativeRAG（51.0），体现精确率优先。HIPAA 上 4B 模型的 PIKE-RAG Claim F1（73.9）高于 RefWalk（72.4）。

**实验 3（噪声预言机，Table 9）**：加入一跳引用邻域的困难负例后，NativeRAG 引用精确率从 100.0 降到 82.3，RefWalk 为 85.2。阅读者分析：RefWalk 的引用 F1（67.4）低于 NativeRAG（70.3），说明其优势在精确率而非召回。

**其他**：RRM 优势主要来自 L3（Table 8）；精确粒度引用下 RefWalk 领先更多（Table 20）；检索比 NativeRAG 多 4.18 秒，RAG 延迟比 PIKE-RAG 快约 2.6 倍（Table 18）。

**边界**：作者承认按条归属模式偏保守，以召回换精确率；确定性 OKG 依赖韩国法规的公式化引用，迁移到判例法或其他语言需要规则加 LLM 的混合抽取。阅读者分析：RegOps 的真值和难度由作者规则构造，合成题占 75.8%，且只有一个法域；结论外推到其他法规体系需谨慎。

依据：[arXiv:2605.29742v2，26 页](https://arxiv.org/pdf/2605.29742v2)，§5、Tables 3–9，PDF pp.6–8；附录 A.1、A.6–A.8、Tables 18–20，PDF pp.12、15–16；§7，PDF p.9。
