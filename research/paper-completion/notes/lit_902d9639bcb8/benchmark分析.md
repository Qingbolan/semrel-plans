# 评测与边界

**基线**（§5.1，PDF p.7）：开源多图/文档 MLLM（MiniMonkey、InternVL2、MiniCPM-V2.6、LLaVA-OneVision、mPLUG-DocOwl2、IXC2.5 等）、专有模型 Gemini-1.5-Pro、GPT-4o、多模态 RAG（VisRAG、InternVL+RAG、M3DocRAG），以及以 InternVL2-8B 做 OCR 后输入长上下文 LLM（Llama3.2-3B、InternLM2.5-7B-1M）。

**主要结果**（Table 4，p.7）：

| 模型 | MP-Doc ANLS | MMLong Acc/F1 | DocGenome MP Acc | MM-NIAH 总分 |
|---|---|---|---|---|
| InternVL2-8B | 79.3 | 17.4/16.5 | 46.1 | 42.9 |
| InternVL2-8B + RAG | 78.7 | 24.2/24.5 | 46.0 | 48.4 |
| InternVL2-26B | – | 15.5/15.4 | 42.7 | 52.8 |
| M3DocRAG | 84.4 | 21.0/22.6 | – | – |
| Gemini-1.5-Pro | – | 28.2/20.6 | – | 67.1 |
| GPT-4o | – | 42.8/44.9 | 67.6 | – |
| Docopilot-2B | 76.2 | 21.8/16.0 | 37.4 | 49.2 |
| Docopilot-8B | 81.3 | 28.8/23.0 | 51.9 | 61.8 |

MM-NIAH 长档（32K–64K）Docopilot-8B 为 55.3（InternVL2-8B 32.4）。

**单页 VQA（Table 5）**：基本持平，DocVQA 8B 92.0 对 91.6，InfoVQA 73.3 对 74.8。

**数据消融（Table 6，2B，MMLongBench-Doc Acc/F1）**：无 Doc-750K 为 18.4/9.4，逐步加入 Sci-Hub、arXiv、OpenReview 后到 21.8/16.0。

**延迟（Table 7，平均每 token 输出延迟；MMLongBench-Doc Acc/F1）**：

| 模型 | 延迟 | Acc/F1 |
|---|---|---|
| InternVL2-2B | 35.9 ms | 10.5/10.8 |
| InternVL2-2B + RAG | 82.9 ms | 17.2/16.7 |
| Docopilot-2B | 35.9 ms | 21.8/16.0 |
| InternVL2-8B | 81.0 ms | 17.4/16.5 |
| InternVL2-8B + RAG | 113.4 ms | 24.2/24.5 |
| Docopilot-8B | 81.0 ms | 28.8/23.0 |

**局限**：正文无局限章节，§6 仅提及未来提升计算效率与扩展任务。

阅读者分析：
- 并非全面领先：M3DocRAG 在 MP-DocVQA 上 84.4 高于 Docopilot-8B 的 81.3；InternVL2-8B+RAG 的 MMLong F1 24.5 高于 23.0；DocGenome 单页 Acc 53.9 低于 InternVL2-8B 的 56.0；GPT-4o 在 MMLongBench-Doc 上仍领先约 14 分。
- “DocGenome 多页 QA 提升 12.6%”是相对提升（51.9 对 46.1，绝对 +5.8）。
- 延迟只比较每 token 输出时间，未包含长上下文预填充成本，“与基线推理时间相同”是在同架构同参数前提下成立。

依据：[CVPR 2025 Open Access，12 页](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf)，§5，Tables 4–7，PDF pp.7–8。
