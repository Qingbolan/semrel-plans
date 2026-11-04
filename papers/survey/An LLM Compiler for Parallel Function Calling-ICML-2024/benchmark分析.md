# 评测与边界

**比较方法**：ReAct；ReAct†（加了防循环、防过早停止提示）；OpenAI parallel function calling（仅 GPT）；24 点比较 Tree-of-Thoughts；WebShop 比较 ReAct、LATS、LASER（§5，表 1、表 3）。原版 ReAct 因循环和早停延迟不稳定，HotpotQA/Movie 的加速比以 ReAct† 为基准（§5.1，p.7）。

**指标**：准确率（或成功率）、端到端延迟、输入/输出 token 与估计美元成本。

**实验 1（准确率与延迟，表 1，p.6）**：

| 基准 | 方法 | GPT 准确率 | GPT 延迟 (s) | GPT 加速 | LLaMA-2 准确率 | LLaMA-2 加速 |
|---|---|---|---|---|---|---|
| HotpotQA | ReAct† | 62.47 | 7.12 | 1.00× | 54.40 | 1.00× |
| HotpotQA | OAI Parallel | 62.05 | 4.42 | 1.61× | – | – |
| HotpotQA | LLMCompiler | 62.00 | 3.95 | 1.80× | 57.83 | 1.40× |
| Movie Rec. | ReAct† | 72.47 | 20.47 | 1.00× | 70.60 | 1.00× |
| Movie Rec. | OAI Parallel | 77.00 | 7.42 | 2.76× | – | – |
| Movie Rec. | LLMCompiler | 77.13 | 5.47 | 3.74× | 77.80 | 2.82× |
| ParallelQA | ReAct | 89.09 | 35.90 | 1.00× | 59.59 | 1.00× |
| ParallelQA | OAI Parallel | 87.32 | 19.29 | 1.86× | – | – |
| ParallelQA | LLMCompiler | 89.38 | 16.69 | 2.15× | 68.14 | 2.27× |
| Game of 24 | ToT | 74.00 | 241.2 | 1.00× | 30.00 | 1.00× |
| Game of 24 | LLMCompiler | 75.33 | 83.6 | 2.89× | 32.00 | 2.09× |

GPT 下 HotpotQA 准确率 LLMCompiler 略低于 ReAct†（62.00 对 62.47），收益主要是延迟。

**实验 2（成本，表 2，p.6）**：每千题估计成本 HotpotQA $5.00→$1.47（3.37×），Movie $20.46→$3.04（6.73×），ParallelQA $480→$103（4.65×）；均优于 OpenAI parallel function calling。原因是调用 LLM 次数少，且 Planner 示例只含计划不含观察。

**实验 3（WebShop，表 3，p.9）**：gpt-4 下成功率 LLMCompiler 55.6%、LASER 50.0%、ReAct 35.2%；gpt-3.5-turbo 下 48.2%（N=500）对 ReAct 19.8%。延迟相对 LATS 101.7×、LASER 2.69× 加速，但比 ReAct 慢（26.73 s 对 19.90 s）。

**其他**：流式 Planner 在 ParallelQA 上 1.30× 加速，HotpotQA/Movie 仅 1.01×/1.03×（表 C.1）；ParallelQA 失败中 Planner 占 8%、Executor 64%、最终汇总 28%（附录 B）；HotpotQA bridge 上 26.3% 对 ReAct† 23.1%，延迟 4.70 s 对 6.42 s（表 E.2）。

**边界**：
- ParallelQA 排除了检索失败，只能说明分解与调度能力（附录 I）。
- 准确率提升主要来自避免 ReAct 的循环与早停（附录 A），而不是更强的推理。
- 没有跨问题复用中间结果的实验（阅读者分析）。

**原文内部不一致**（阅读者核对）：
- §5.3 正文写 LLaMA-2 在 24 点上 2.01× 加速，表 1 为 2.09×（952.06/456.02≈2.09）。
- 附录 A 说“HotpotQA + LLaMA-2 70B 的 70.00 对 77.80”，但表 1 中这组数字属于 Movie Rec. 的 LLaMA-2 行；HotpotQA LLaMA-2 是 54.74 对 57.83。

依据：§5、表 1–3，PDF pp.5–9；附录 A、B、C.1、D、E.3，pp.13–18。
