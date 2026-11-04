# 评测与边界

**指标**：TES（达到峰值的迭代数，越少越好）、ODP（最佳 TPS 或最低延迟）；初始化额外用 PE=(ODP_init−ODP_orig)/ODP_orig 与 Speedup=(TES_orig−TES_init)/TES_orig；推荐额外报告首轮改进后的 IR TPS/IR Latency（§4、§6.3、§7.2，PDF pp.5、7–9）。

**实验 1（旋钮剪枝，Figure 4、Table 1，PDF pp.6–7）**：基线为 SHAP（约 6,000 条观测）与一名数据库专家，剪枝后用 SMAC 优化 120 轮。Claude-3-Opus、GPT-4o、GPT-4-Turbo 与专家相当或更好；几乎所有 LLM 优于 SHAP；闭源明显优于开源。结果只以曲线图给出，正文无具体数值。

**实验 2（模型初始化，Table 2，PDF p.8）**：

| 方法 | ODP | PE | TES | Speedup |
|---|---|---|---|---|
| VBO | 154.73 | 0% | 316 | 0% |
| VBO + Mapping (OtterTune) | 154.37 | −0.23% | 279 | 11.71% |
| RGPE + Model Ensemble (ResTune) | 158.02 | 0.42% | 215 | 42.67% |
| DS-DDPG + Pre-training (QTune) | 162.15 | 33.10% | 313 | −216.16% |
| VBO + GPT-4-Turbo | 152.01 | −1.93% | 84 | 73.41% |
| VBO + Claude-3-Opus | 126.09 | −18.65% | 2 | 99.37% |
| VBO + Llama3-70B-Instruct | 154.68 | −0.03% | 90 | 71.51% |

LLM 平均 speedup 71.42%；GPT-3.5、GPT-4o、Claude-3-Opus 的 PE 约 −17% 至 −19%，原因是它们只改少数旋钮、10 个配置高度相似；此处开源模型反而优于闭源（§6.3–6.4，PDF p.8）。表中 QTune 的 PE 写作 33.10%，但按其 ODP 162.15 与 VBO 154.73 计算只有约 4.8%，原表数值可能有误（阅读者分析）。

**实验 3（旋钮推荐，Table 3，PDF p.9）**：

| 方法 | IR TPS | ODP | TES |
|---|---|---|---|
| Default | – | 17.45 | – |
| DDPG / SMAC / VBO | – | 120.71 / 157.25 / 155.10 | 99 / 375 / 316 |
| GPT-4-Turbo | 145.06 | 155.30 | 9 |
| Claude-3-Opus | 26.70 | 148.51 | 23 |
| Llama3-70B-Instruct | 28.84 | 145.12 | 3 |
| Qwen2-7B | 143.58 | 154.94 | 14 |

**实验 4（泛化，Tables 4–6，PDF pp.11–12）**：JOB 上 GPT-4-Turbo 最低延迟 643.77 秒（7 轮），优于 SMAC 的 675.28 秒（146 轮）。TiDB 默认 164.00 TPS 已较强，DDPG 只到 109.59；Claude-3-Opus 以 265.71 TPS/21 轮略超 SMAC 263.53/342 轮。机器 B 上 Claude-3-Opus 达 2424.77 TPS，SMAC 为 1343.68。

**边界**（阅读者分析，依据原文表格设置）：单次运行、无方差；LLM 30 轮与传统 400 轮预算不同，TES 不含 LLM 调用耗时与费用；旋钮集合由人工预选（20 个或 7 个）；只有 SYSBENCH 与 JOB 两个基准。原文没有独立局限章节，仅在 §6.3 承认部分闭源 LLM 初始化配置缺乏多样性、§9.1 承认无单一 LLM 始终最优（PDF pp.8、12）。

依据：§4–9、Tables 2–6、Figure 4，PDF pp.5–12。
