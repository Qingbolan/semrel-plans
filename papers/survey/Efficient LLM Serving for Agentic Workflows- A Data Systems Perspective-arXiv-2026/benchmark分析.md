# 评测与边界

**环境**（§7.1，p.8）：AMD EPYC 9554 + 2×94GB H100 NVL；Qwen3-8B / Qwen3-14B，每个 GPU 一个独立引擎实例；除 KVFlow（用其 SGLang 实现）外均用 vLLM v0.16.0，开启自动前缀缓存与 chunked prefill；所有调用 greedy 采样。指标为端到端延迟，Helium 的延迟包含优化与调度时间。

**基线**：vLLM（逐查询顺序执行）、OpWise（逐算子跨批执行，模拟 Spark/Dask）、LangGraph、AgentScope v0.1.6、Parrot、KVFlow。基线经 OpenAI API 访问同机推理服务，作者另写了按队列长度路由的负载均衡器（实测每请求 89 µs，HTTP 往返约 3.1 ms，§7.5）。

**实验 1（原语工作流，Qwen3-8B）**：相对 Helium 的延迟倍数（Table 2，p.8）。

| 系统 | 平均 | 最小 | 最大 |
|---|---|---|---|
| vLLM | 66.27 | 38.18 | 100.92 |
| OpWise | 1.25 | 1.02 | 1.58 |
| LangGraph | 1.28 | 1.09 | 1.83 |
| AgentScope | 2.10 | 1.07 | 4.32 |
| Parrot | 1.44 | 1.02 | 2.21 |
| KVFlow | 1.32 | 1.14 | 1.56 |

**实验 2（Trading 端到端，Figure 7）**：批大小 8–80，Helium 相对 vLLM 最高 39.50×、OpWise 4.25×、LangGraph 1.49×、AgentScope 1.46×、Parrot 2.51×、KVFlow 1.34×（§7.2，pp.9–10）。

**实验 3（消融，Trading，batch=16，Qwen3-8B）**：完整系统 130.14 s；去掉计划剪枝 160.53 s（−23.35%），去掉缓存感知调度 153.12 s（−17.66%），去掉提示缓存 147.79 s（−13.56%），去掉主动 KV 缓存 134.76 s（−3.55%）（Table 3，p.10）。

**实验 4（调度策略，关闭缓存，Trading）**（Table 4，p.10）：

| 调度 | 延迟 (s) | 前缀缓存命中率 |
|---|---|---|
| QueryWise | 658.54（4.40×） | 42.3% |
| OpWise | 419.03（2.80×） | 40.8% |
| Random | 193.54（1.29×） | 37.1% |
| LSPF | 188.93（1.26×） | 37.9% |
| Helium（仅 CAS） | 149.76 | 56.5% |

**实验 5（调度最优性）**：7 个缩小配置（2–4 agent × 2–4 查询，单 worker，8192-token KV 上限），MILP 求解器每例限时 6 小时。Helium 最优性差距平均 0.9%、最大 3.6%；QueryWise 平均 72.4%，OpWise/Random/LSPF 平均 14.5–17.6%、最大约 30%（Table 5，p.10）。

**其他**：批越大、辩论轮数越多优势越大（Figure 8）；模型越大优势越大（Figure 9a）；在前缀共享配置 P1/P4 上相对 LangGraph 最高 2.07×（Debate，Figure 10）；规划开销 <230 ms，TRT 元数据 552 KiB 对 SGLang RadixCache 14.8 MiB（§7.5，Figure 11）。附录 D：Qwen3-14B 下 vLLM 的前缀命中率（43.0%）略高于 Helium（42.9%），但延迟远差。

**边界**：
- 作者承认（§9）：DAG 不能表达条件循环与动态 fan-out；外部 API 调用只能 best-effort；
- 阅读者整理：只测了同一基础模型、本地 2 GPU；未报告输出等价性的单独验证（由 greedy 采样和确定性缓存保证）；profiling 用单独查询集离线完成，不计入延迟；MILP 最优性只在很小实例上验证。

依据：[arXiv 2603.16104v1](https://arxiv.org/abs/2603.16104v1)，§7.1–7.6、§9、Tables 2–5、Table 7、Figures 7–12，PDF pp.8–13、18。
