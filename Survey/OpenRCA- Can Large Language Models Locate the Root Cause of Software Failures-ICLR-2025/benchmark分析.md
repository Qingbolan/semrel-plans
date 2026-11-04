# 评测与边界

**三种方法**（§3、§4.1，pp.5–6）：

- Balanced Sampling：所有遥测降采样到每分钟一条（取每分钟第一条）；再从每个指标文件轮流随机选不重复的 KPI 类型，直到数量与 Oracle 相同；跑 3 次取中位数，波动约 1%。
- Oracle Sampling：只用工程师在构建基准时标出的"黄金" KPI，从 1,263 个减到 53 个（减少 95%）；属于特权信息，是采样方法的理想化上界，并非可部署的普通基线。
- RCA-agent：Controller/Executor 加有状态 Python。因预算限制，开源模型中只测了 Llama 3.1。

两种采样方法都去掉无信息列、压缩 trace ID，prompt 约 100K token（GPT-4o 分词）。

**实验 1（总体准确率，Table 2，p.7）**：Correct / Partial（%）。

| 模型 | Balanced | Oracle | RCA-agent |
|---|---|---|---|
| Claude 3.5 Sonnet | 3.88 / 18.81 | 5.37 / 17.61 | 11.34 / 17.31 |
| GPT-4o | 3.28 / 14.33 | 6.27 / 15.82 | 8.96 / 17.91 |
| Gemini 1.5 Pro | 6.27 / 24.18 | 7.16 / 23.58 | 2.69 / 6.87 |
| Mistral Large 2 | 3.58 / 6.40 | 4.48 / 10.45 | N/A |
| Command R+ | 4.18 / 8.96 | 4.78 / 7.46 | N/A |
| Llama 3.1 Instruct | 2.99 / 14.63 | 3.88 / 14.93 | 3.28 / 5.67 |

**实验 2（按难度，Table 3，p.7）**：Correct（%），Easy/Mid/Hard 分别要求 1/2/3 个元素。

| 模型 | 方法 | Easy | Mid | Hard |
|---|---|---|---|---|
| Claude | Oracle | 8.72 | 3.50 | 0.00 |
| Claude | RCA-agent | 16.78 | 9.09 | 0.00 |
| GPT | Oracle | 9.40 | 4.90 | 0.00 |
| GPT | RCA-agent | 13.42 | 6.99 | 0.00 |
| Llama | Oracle | 7.38 | 1.40 | 0.00 |
| Llama | RCA-agent | 6.71 | 0.70 | 0.00 |

要求元素从 1 个增至 2 个，准确率至少减半；所有方法在 Hard 上都是 0。

**其他发现**（§5，pp.7–8）：

- 系统越简单越准：所有模型在 Telecom 上最高（遥测最少、根因类型最少、无容错机制）（Figure 5）。
- 约一半回答在 10 步内结束，但超过 10 步时准确率通常更高，作者推测模型推理"偷懒"（Figure 6）。
- 容错能力限制智能体：在涉及执行失败的案例中，Gemini 准确率从 2.69% 降到 0.85%（降 68.4%）；Claude 降到 9.31%（降 17.9%），GPT 降到 7.56%（降 15.6%），Llama 降到 3.18%（降 18.0%）（Table 4，p.8）。正文写"Claude 和 GPT 分别降 15.6% 和 17.9%"，与 Table 4 及 Table 2 推算的顺序相反（阅读者分析）。

**边界**：

- 作者承认：故障只来自分布式系统；查询是合成的，没有一手故障报告；RCA-agent 对模型容错要求更高（§8）。
- Claude 上的改善不能外推到所有模型，Gemini 用 RCA-agent 反而低于其 Oracle（阅读者分析）。
- 未知故障数、遥测缺失的案例、传播解释质量和跨案例复用都未在该设置中验证（阅读者分析）。

依据：[原文](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf)，§3–5、§8、Tables 2–4、Figures 5–6，pp.5–9。
