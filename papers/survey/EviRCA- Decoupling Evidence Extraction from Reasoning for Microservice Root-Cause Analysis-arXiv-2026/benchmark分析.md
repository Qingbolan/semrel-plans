# 评测与边界

**基线**（§IV-A，p.6）：

- RCA-Agent：OpenRCA 的 controller–executor 智能体，规划器反复指挥执行器在有状态内核中对原始遥测写并运行 Python；
- Oracle Sampling：从领域工程师预选的诊断 KPI（把 KPI 空间缩小 95%）中采样，单次 LLM 调用作答，带特权先验，是采样类方法的理想化上界。

**实验 1（准确率，§IV-B，Table III，p.7）**：Correct / Partial（%），Overall 按案例数加权。

| 方法 | LLM | Bank | Telecom | Market | Overall |
|---|---|---|---|---|---|
| Oracle Sampling | deepseek | 12.5 / 20.7 | 19.6 / 25.1 | 14.9 / 22.3 | 14.6 / 22.1 |
| Oracle Sampling | qwen | 9.6 / 17.6 | 29.4 / 36.6 | 15.5 / 32.4 | 15.2 / 27.0 |
| RCA-Agent | deepseek | 17.6 / 23.1 | 11.8 / 19.6 | 9.5 / 19.1 | 13.1 / 20.8 |
| RCA-Agent | qwen | 22.1 / 29.1 | 9.8 / 16.0 | 6.8 / 16.3 | 13.4 / 21.5 |
| EviRCA | deepseek | 52.2 / 63.2 | 62.7 / 65.4 | 29.7 / 46.7 | 43.9 / 56.2 |
| EviRCA | qwen | 47.8 / 60.8 | 56.9 / 60.8 | 28.4 / 46.2 | 40.6 / 54.4 |

hard 档（完整三元组）上，EviRCA 在 Bank 解出 17.6–29.4%、在 Telecom 解出 55.6%；基线所有 hard 单元格不超过 11.8%（§IV-B、Figure 3）。

**实验 2（效率，§IV-C，Table IV，p.8）**：deepseek-v4-pro，单案例开销。

| 系统 | EviRCA token | RCA-Agent token | 倍数 | EviRCA 时间 | RCA-Agent 时间 | 倍数 |
|---|---|---|---|---|---|---|
| Bank | 101.8K | 1.53M | 15.0× | 182.3 s | 577 s | 3.2× |
| Telecom | 48.3K | 1.24M | 25.7× | 31.7 s | 622 s | 19.6× |
| Market | 66.4K | 1.54M | 23.3× | 40.8 s | 685 s | 16.8× |

Bank 时间收益小，是因为其调用链没有调用状态和显式被调方，需按案例重建调用图；Telecom 与 Market 预先汇总为每分钟调用摘要供所有案例复用。

**实验 3（留一消融，§IV-D，Table V，p.8）**：Correct 变化（百分点），deepseek-v4-pro。

| 去掉的模块 | Bank | Telecom | Market |
|---|---|---|---|
| Trace | −3.7 | −45.1 | −0.7 |
| Co-location rollup | – | −37.3 | −1.4 |
| Per-system guidance | +0.7 | −11.8 | 0.0 |
| Golden signal | 0.0 | −3.9 | 0.0 |
| Safety net | −2.9 | 0.0 | −3.4 |
| Log modality | −1.5 | – | – |

阅读者分析：正文称 Market 上"没有任何单项消融使 Correct 变化超过 3 个百分点"，但表中 Safety net 为 −3.4，二者略有出入（阅读者分析）。

**实验 4（失败分析，§IV-E，Figure 4、Table VI，p.9）**：单故障失败中，真实组件未进入证据的只占 22.5%；其余是在已呈现证据上判断错：选了异常更强的下游组件（35%）、候选原因选错（21%）、传播链错（14%）。两个模型都失败的案例占至少一个失败案例的 81–87%。Market 失败的网络原因案例中，89.6% 的真实组件从未进入证据（Bank 8.5%，Telecom 0%）。

**边界**：

- 继承 OpenRCA 的封闭候选集、已知故障数和拓扑可用假设，作者承认在真实生产中未必成立（§V-B）。
- 证据层决定性能上限，Market 的网络信号覆盖不足（§V-B）。
- 不能据此推出所有任务都应预抽取，也不能直接与不给故障数的设置比较（阅读者分析）。

依据：[arXiv 2609.19825v1](https://arxiv.org/abs/2609.19825v1)，§IV–V、Figures 3–4、Tables III–VI，pp.6–10。
