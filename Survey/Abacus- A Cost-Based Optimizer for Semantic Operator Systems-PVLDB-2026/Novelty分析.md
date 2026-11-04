# 贡献与评价

**论文声称的贡献**（§1 p.3）：
1. 可扩展的代价优化器，新增语义算子和优化规则时不必改宿主框架（§2）；
2. 让搜索高效并支持约束优化的算法：Pareto 版 MAB 采样与 Pareto-Cascades（§3）；
3. 质量比现有系统最多高 39.4%，费用和运行时间分别比次优系统低 10.8 倍和 3.4 倍（§4）；
4. 实验表明先验、Pareto-Cascades 和 MAB 采样都能改善优化结果（§4）。

**已实现的物理规则**（§4.1 p.8）：

| 规则 | 适用算子 | 参数 |
|---|---|---|
| Model Selection | map、filter | 单次 LLM 调用，在可用模型中选择 |
| Mixture-of-Agents | map、filter | 1–3 个提议模型、聚合模型、提议温度 0.0/0.4/0.8 |
| Reduced-Context | map、filter | 文本切块后按与指令的嵌入相似度取 top-k；块长 1000/2000/4000 字符，k=1/2/4 |
| Critique-and-Refine | map、filter | 生成、批评、改写三步各用一个模型 |
| Top-K | top-k | 返回对象数 k |
| Nested Loops Join / Embedding Join | join | 逐对 LLM 判断；或按嵌入高低阈值直接丢弃/接受，阈值之间仍调用 LLM |

除比较实验外，默认可用模型为 GPT-4o、GPT-4o-mini、Llama-3.1-8B、Llama-3.3-70B、Mixtral-8x7B、DeepSeek-R1-Distill-Qwen-1.5B（§4.1）。

**阅读者评价**：
- 新意在于把“算子级采样估计”与“约束下的计划组合”拆开：MAB 负责在有限预算内找到前沿候选，Pareto-Cascades 负责多目标组合。LOTUS 是在单个算子上做带统计保证的代理级联，DocETL 是用 LLM 做逻辑重写，三者侧重点不同（阅读者分析）。
- 算子独立假设是核心前提，Theorem 3.1 也依赖它；作者在 §5 承认会带来估计误差，计划用贝叶斯优化改进。
- 优化开销不可忽视：Table 2 中优化时间占总时间的 52%–71%（BioDEX 303/450 s，CUAD 318/450 s，MMQA 598/1149 s），对小规模、一次性的数据需要把优化和执行一起算（阅读者分析）。
- LLM judge 可以代替缺失的中间标签，但它不是独立的真值；论文没有单独评估 judge 误差对计划选择的影响（阅读者分析）。
- “可扩展框架”不等于已实现所有重写；当前采样只用实现规则（§2.2）。

依据：[arXiv 2505.14661v3](https://arxiv.org/abs/2505.14661v3)，§1、§2.2、§4.1、§5–6、Table 2，PDF pp.3、8–9、12。
