# 评测与边界

**基线**：CoT、COT-SC（5 个样本）、Self-Refine（最多 5 轮）、LLM Debate（2 轮）、Quality-Diversity、Step-back Abstraction、Role Assignment，以及提示优化方法 OPRO；全部用同一框架实现，并作为存档的初始种子。结果报告中位数和 95% bootstrap 置信区间。

**实验 1（ARC）**：Meta Agent Search 随迭代逐步超过手工基线（Figure 3a，以曲线给出）。

**实验 2（四领域，Table 1）**：

| 方法 | DROP F1 | MGSM | MMLU | GPQA |
|---|---|---|---|---|
| 最好的手工基线 | 65.8（Role Assignment） | 39.0（LLM Debate） | 65.9（COT-SC） | 31.6（Self-Refine） |
| OPRO | 69.1 | 30.6 | 67.6 | 32.9 |
| Meta Agent Search | 79.4 | 53.4 | 69.6 | 34.6 |

作者认为 MMLU 和 GPQA 提升较小是因为模型知识不足，智能体设计无法弥补。

**实验 3（迁移，Tables 2–3）**：

- 跨领域：MGSM 上的最佳智能体迁移到 GSM8K 为 69.5（最好基线 43.6），GSM-Hard 为 31.2（基线 18.0）；迁移到 DROP、MMLU 也优于手工基线，但不及在该领域直接搜索的结果。
- 跨模型：ARC 上搜得的三个智能体迁移到 GPT-4、Claude-Haiku、Claude-Sonnet 后，各模型下的最好成绩都来自搜得智能体（Claude-Sonnet 48.3 vs Self-Refine 39.3）；但并非每个搜得智能体都领先，细节见具体用例页（阅读者分析）。

**边界**：只优化单一性能目标；仅单步问答；评估函数昂贵且只用分数；生成的代码在容器中执行并经人工检查。测试集是抽样子集，结论依赖 GPT-3.5 作为评估模型。

依据：§4.1–4.3、Tables 1–3，PDF pp.5–9；§6，PDF pp.10–11；Appendix F、I–J，PDF pp.30、33–34。
