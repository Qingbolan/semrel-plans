# 评测与边界

**基线**：① 未针对 RAG 微调的开源 LLM（LLaMA2-Chat 7B、Mistral-It 7B、Baichuan2-Chat 7B、ChatGLM3 6B）采用两种提示——直接拼接 top-10 文档、RobustLM 式 4-shot 先判断相关再回答（只给 top-1 文档）；② 专门的 RAG 微调方法 Self-RAG 7B、RobustLM 7B，使用与 REAR 相同的检索文档（§5.1，p.6）。

**指标**：EM、F1；相关性判断用 JAcc（判断正确的文档比例）与 Hit@1（最终答案所用文档是否相关）（§5.1，p.6）。

**实验 1（主结果，Table 3，p.6）**：

| 方法 | NQ EM | TriviaQA EM | WebQ EM | SQuAD EM | 平均 EM / F1 |
|---|---|---|---|---|---|
| Self-RAG 7B（Acc） | 41.02 | 52.38 | 31.40 | 35.28 | 40.02 / – |
| RobustLM 7B | 44.40 | 62.86 | 32.48 | 27.52 | 41.82 / 51.90 |
| REAR w/ Source Rel. | 51.33 | 65.36 | 33.02 | 36.78 | 46.62 / 57.25 |
| REAR w/ Knowledge Con. | 51.41 | 66.26 | 33.51 | 37.21 | 47.10 / 57.68 |

Self-RAG 以较宽松的 Acc 而非 EM 计分（Table 3 注）。

**实验 2（相关性判断，Table 4，p.7）**：REAR 的 JAcc 在 NQ/TriviaQA/WebQ/SQuAD 为 74.04/80.79/65.99/59.36，Hit@1 为 66.79/74.98/56.69/53.26，均高于 RobustLM 与 Self-RAG。

**实验 3（消融，Table 5，p.7）**：去掉评估模块 Hit@1 66.79→13.80、EM 53.13→38.14；去掉抗噪训练 EM 降到 25.54。

**实验 4（单/多文档，Table 6、Fig. 3，p.8）**：NQ 上只给 top-1 文档且文档无关时，REAR EM 20.09，其他模型 2.00–6.40；换用 BM25 等较弱检索器时仍领先。

**边界**：作者承认只做到文档级相关性，未处理句子/token 级；未在 KILT 等更广的 RAG 任务上验证（Limitations，p.9）。

Table 5 中完整 REAR 的 EM/F1 为 53.13/61.84，与 Table 3 的 NQ 数值 51.41/60.50 不一致，论文未说明 Table 5 所用数据集或设置（阅读者分析）。Table 6 中 Self-RAG 的 40.03 也与 Table 3 的 41.02 不同（阅读者分析）。§5.2 写“even the fine-tuned generative approaches adequately discriminate relevance”，按上下文应为“不能充分判别”（阅读者分析）。

依据：§5、Tables 3–6、Fig. 3、Limitations，PDF pp.6–9。
