# 评测与边界

**指标说明**：LLM R 为交给 LLM 处理的记录比例；SEED Max 为优化器枚举的计划中效果最好者，SEED Opt 为在 G = 5% 下选出的计划（§6.1）。

**实验 1（实体匹配，Table 3，p.11）**：

| 方法 | Amazon-Google F1 / LLM R | Abt-Buy F1 / LLM R |
|---|---|---|
| DITTO（监督，数千标注） | 80.7 / — | 91.3 / — |
| MatchGPT Generic | 76.4 / 100% | 95.8 / 100% |
| MatchGPT Specialized | 85.2 / 100% | 94.4 / 100% |
| SEED LLM Only | 77.4 / 100% | 92.1 / 100% |
| SEED Max | 79.2 / 22.4% | 92.8 / 27.1% |
| SEED Opt | 76.2 / 10.4% | 88.0 / 2.9% |

Amazon-Google 上的 Opt 计划中，LLM、CacheReuse、ModelGen 分别处理 10.4%、41.7%、47.9% 的记录。作者称 LLM 调用“至少减少 90%”，但 Amazon-Google 实为 89.6%（阅读者分析）。

**实验 2（属性补全，Table 5，p.11）**：

| 方法 | Buy 准确率 / LLM R | Restaurant 准确率 / LLM R |
|---|---|---|
| HoloClean | 16.2 / — | 33.1 / — |
| IMP（监督） | 96.5 / — | 77.2 / — |
| FMs（10-shot LLM） | 98.5 / 100% | 88.4 / 100% |
| SEED LLM only | 96.9 / 100% | 89.8 / 100% |
| SEED Opt | 91.9 / 39.3% | 84.7 / 0% |

Restaurant 上 Opt 计划只用 CodeGen，完全不调用 LLM。正文称 Buy 上准确率 96.1%、与 IMP 差 6.6%，与表中 96.9、91.9 对 96.5（差 4.6）不一致（阅读者分析）。

**实验 3（信息抽取，Table 6，p.12）**：Wiki NBA token F1：SEED Opt 88.6（LLM 处理 22.5%），EVAPORATE-CODE+ 84.7，EVAPORATE-DIRECT 84.6，DOM-LM 64.8，RoBERTa-Structural 48.6。

**实验 4（数据标注，Table 7，p.12）**：OS 准确率：SEED Opt 88.3（LLM R 31.1%，借助批量查询实际调用次数仅为 1.0%），SEED LLM Only 84.2，EFL 79.8，FT 70.0。作者称相对逐条调用减少 99% 的调用和 95% 的 token。

**实验 5（数据发现，Table 8，p.15）**：

| 方法 | Spider | OTT-QA | KaggleDBQA |
|---|---|---|---|
| BM25 | 34.8 | 62.0 | 24.1 |
| DrQA | 35.5 | 50.0 | 34.7 |
| SEED LLM only | 50.7 | 71.0 | 56.1 |
| SEED（带工具） | 85.7 | 67.8 | 63.5 |

BM25 与 DrQA 在 Spider、KaggleDBQA 取 top-3，在 OTT-QA 取 top-1。

**边界**：
- 原文承认：MatchGPT Specialized 高于 SEED Max，因为其提示针对数据集调优（§6.1）；OTT-QA 表标题无意义，误导工具选择（附录 B.1）。
- 阅读者整理：成本只用 LLM R 衡量，不含代码生成和模型训练；只用 GPT-4 一种 LLM；监督基线与 few-shot 方法的标注预算不同，不能视作等预算比较；约 90% 的调用节省来自实体匹配，不能推广到探索类任务。

依据：[arXiv 2310.00749v3](https://arxiv.org/abs/2310.00749v3)，§6、Tables 3–8、附录 B.1，pp.10–15。
