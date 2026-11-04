# 评测与边界

**环境**（§6.1，pp.7–8）：2×AMD EPYC 9755、2.2 TiB 内存、3×H200 NVL（各 141 GiB）；模型 Qwen3-14B/32B 与 GPT-OSS-20B；vLLM 0.11.0、SGLang 0.5.6、PostgreSQL 18.0；DP 内循环用 Rust（PyO3）实现。所有系统共用同一 vLLM 与 PostgreSQL 后端。

**基线**：vLLM 逐查询执行（一条查询的整个 DAG 跑完才开始下一条）；OpWise（与 Halo 同一处理器，但逐层缓冲后批执行）；LangGraph 1.0.4；AgentScope 1.0.9；Parrot 0.1.0（整批预先提交）。

**实验 1（端到端 batch，N=1024，§6.2，Figure 6，pp.8–9）**：Halo 在所有 workload 上延迟最低。

| 对比 | 结果 |
|---|---|
| vLLM 逐查询（W1） | 超过 71 小时（2.56×10^5 s）对 676 s，400× 以上 |
| OpWise（W1） | 1595 s 对 676 s，2.4× |
| OpWise（W6） | 1.6× |
| LangGraph/AgentScope/Parrot（W1–W4） | Halo 领先 1.03–2.6× |
| 同上（W5–W6） | Halo 领先 2.4–3.6× |

400× 来自逐条串行的基线，不代表相对现代并发框架的提升。

**实验 2（调度器最优性，N=256，Table 4，p.9）**：Opt. 是相邻 GPU 节点对与 MILP 最优解的匹配率，不是答案准确率。

| 调度器 | W1 延迟 | W1 Opt. | W1 求解 | W6 延迟 | W6 Opt. | W6 求解 |
|---|---|---|---|---|---|---|
| Random | 367.27 s | 0.4 | – | 672.08 s | 0.0 | – |
| RR（Ray） | 351.17 s | 0.4 | – | 844.46 s | 0.0 | – |
| Greedy（HEFT） | 338.28 s | 0.6 | – | 768.18 s | 0.2 | – |
| Halo | 323.64 s | 1.0 | 2.24 s | 545.55 s | 1.0 | 1.15 s |
| MILP（Oracle） | 322.17 s | – | 1.44 h | 544.06 s | – | 172.84 s |

**实验 3（在线吞吐，§6.4，Figure 7，p.10）**：W1–W5 上相对 OpWise 1.53–1.74×（如 W3 0.82 对 0.47 QPS）；相对 LangGraph 最高 2.58×（W5，0.85 对 0.33 QPS）；纯 LLM 的 W+ 上 Halo 4.57、LangGraph 4.22、OpWise 3.59 QPS。

**实验 4（消融，Table 5，p.10）**：相对完整 Halo 的延迟增量。

| 去掉的组件 | W1 | W6 |
|---|---|---|
| 基于 profile 的打分 | +20% | +8% |
| CPU 负载引导（T_prep） | +1% | +18% |
| 机会式执行 | +1% | +56% |
| 合并工具调用 | +16% | +154% |

**实验 5（扩展性与敏感性，§6.6–6.7，Figures 8–11，pp.10–11）**：输入批量 256–2048 近线性；1–3 块 H200 近线性加速；A100/H100/H200 上均优于 OpWise；Processor batch size 存在拐点。W3（256 条）案例中累计 GPU 使用 14,690 对 OpWise 28,889 unit·s，约 2.0×。

**边界**：
- 原文 §6.8：单机多 GPU；逻辑 DAG 固定且语义严格等价。
- 阅读者整理：workflow 为作者构造；只报告延迟与吞吐，没有逐查询输出质量对比；每个 workflow 最多 3 种模型是为了让基线可部署；最优性只在 W1、W6 两个 workflow 上与 MILP 对照。

依据：[arXiv 2509.02121v2](https://arxiv.org/abs/2509.02121v2)，§6.1–6.8、Tables 3–5、Figures 6–11，PDF pp.7–11。
