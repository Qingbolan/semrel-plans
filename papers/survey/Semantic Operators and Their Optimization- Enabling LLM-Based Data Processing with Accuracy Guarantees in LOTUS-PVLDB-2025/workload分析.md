# 工作负载

**四类应用、五个数据集**（§5.1–5.4，pp.4178–4181）：

| 应用 | 数据 | 规模 | 指标 |
|---|---|---|---|
| 事实核验 | FEVER 开发集 claim，检索 Wikipedia（550 万篇）语料 | 抽 1,000 条 claim | 准确率（三类标签合并为 Supported / Not Supported） |
| 生物医学多标签分类 | BioDEX 医学文章 + 约 24,000 个反应标签 | 抽 250 篇 | RP@5、RP@10 |
| 检索排序 | BEIR SciFact | 300 条 claim，每条先检索 100 篇再重排 | nDCG@10 |
| 推理型排序 | HellaSwag-bench（作者合成） | 200 篇摘要，20 次试验，温度 0.7 | nDCG@10 |
| 主题分析 | arXiv cs.DB/IR/CR/RO 论文 | 647 篇，发现 5 个主题 | 分类准确率 |

**默认配置**（§5 p.4177）：4 张 80GB A100，Llama-3-70B 作为 oracle，E5 嵌入，vLLM 推理 batch size 64，温度 0。使用 OpenAI 模型（GPT-4o-mini、GPT-4o、text-embedding-3-small）时限制为 64 路线程并发，这是并发度，不是每个提示装 64 条记录。

**LOTUS 默认参数**（§5.0.1 p.4178）：γ=0.9，δ=0.2；采样 0.01% 的数据，最少 100 条。filter 的代理是 Llama-8B（FEVER），§5.5 另测 TinyLlama-1B。

**基线如何实现**（§5.0.1）：AI UDF 用 LOTUS 自身在 vLLM 上实现，只允许 sem_map、sem_search、sem_sim_join；UQE 未开源，作者用约 100 行 Python 重写其 filter；DocETL 用指定 commit，优化器必须用 GPT-4o，约 1/3 的运行失败，只报告 3 次成功运行的均值。

阅读者分析：这里的“批”是一个查询对整个关系或 join 候选执行模型调用；论文不涉及把多个独立用户查询合成一批。

依据：[PVLDB 18(11)](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)，§5.0–5.4，pp.4177–4181。
