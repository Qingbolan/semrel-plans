# 评测与边界

**基线**（§4.1）：单查询改写/抽象 IterCQR、ADACQR、ConvSearch-R1；扩展类 LLM4CS-RAR、CHIQ-Fusion、RETPO、AdaQR；复杂查询设置无专门方法，作者用少样本提示改造基线，另有 DeepSeek-V3.1、Qwen2.5-3B-inst（有/无分解）、普通 RL 与原始查询（Raw）。

**主要结果**：
- Table 2（TopiOCQA，p.7）：ACQO BM25 下 MRR@3 34.9、R@10 62.6、R@100 83.2（召回最好）；ANCE 下 MRR@3 36.6、R@10 65.6。ConvSearch-R1 在 BM25 下 MRR@3 37.8，在 ANCE 下 MRR@3 50.5、R@10 72.0，均高于 ACQO。
- Table 3（HotpotQA，p.7）：ACQO BM25 下 R@4 86.9、MAP@10 51.2；ANCE 下 R@4 82.2、MAP@10 49.6（ConvSearch-R1 为 44.4）。
- Table 4（MultiHop-RAG 零样本，p.8）：llm-embedder R@4 49.7 对 Raw 45.7；bge R@4 65.5 对 62.5。
- Table 9（端到端 QA，HotpotQA-ANCE，p.15）：Qwen2.5-7B-Instruct 作阅读器、DeepSeek-R1 判分，ACC_L 为 Raw 16.4%、ConvSearch-R1 27.7%、ACQO 31.6%。
- Table 10（p.16）：单张 H20 上 ACQO 平均延迟 355 ms，ConvSearch-R1 3,255 ms（9.16 倍）；完整训练 12.1 GPU 小时，普通 RL 8.4 GPU 小时但 MAP@10 只有 41.1。

**局限与疑点**（阅读者分析；论文无局限性章节）：
- 在 TopiOCQA 的 ANCE 设置下 ConvSearch-R1 的 MRR@3/NDCG@3 比 ACQO 高 10 个百分点以上，正文“competitive”的表述偏宽松；作者以 token 量与延迟作为折中理由。
- Table 5 消融中 HotpotQA-BM25 去掉 Stage II 的 MAP@10（52.0）高于完整 ACQO（51.2），去掉 RSF 时持平（51.2），与正文“每个组件都必要”的结论不完全一致；同表 HotpotQA-ANCE 的 ACQO MAP@10 为 49.4，Table 3 为 49.6。
- 未报告多次运行的方差；“复杂查询”在 TopiOCQA 上主要是单金标准文档的消歧。

依据：[arXiv:2601.21208v1，16 页](https://arxiv.org/abs/2601.21208)，§4、Tables 2–5、9–10，PDF pp.7–9、15–16。
