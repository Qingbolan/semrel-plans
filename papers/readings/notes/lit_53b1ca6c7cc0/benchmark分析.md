# 评测与边界

**基线**（§4，pp.5–6；附录 G）：(a) 传统模型 ARIMA、ETS、DLinear、PatchTST；(b) 时序基础模型 Chronos-2、Lag-Llama、Moirai-Large；(c) 时序 LLM/agent：UniTime、Time-LLM、TS-Agent、TSci；(d) 开源 LLM/VLM/TSLLM（TSRBench 原文结果）；(e) 通用 agent 流程：Direct、CoT、ReAct、Self-Reflection、Multi-Agent Reflection；TSAIA 另加 FinCon、FinTeam、TradingAgents。

**主要结果**：

| 基准 | TimeClaw | 最强基线 | 原文表述 |
|---|---|---|---|
| CiK（Table 1，p.5） | 平均 RCRPS 0.1145、sMAPE 52.45、35,553 tokens | Multi-Agent Reflection：0.1294、55.57、63,033 tokens | RCRPS 相对改进 11.5%，token 少 43.6%；5 类上下文中 4 类 RCRPS 最好（见下注） |
| TSRBench 20% 子集（Table 2，p.6，均用 GPT-5-nano） | 平均准确率 49.76%，15,979 tokens | Multi-Agent Reflection 42.96%（45,279 tokens） | 相对提升 15.8%，token 最少；感知 64.29 次于 TSci 65.71 |
| TSAIA（Figure 4，p.7） | 柱状图最高值 67.6% | 次高 48.6% | 相对提升 38.9% |

注：Table 1 中 TimeClaw 在 Intemporal 0.1303、Historical 0.0886、Future 0.0703、Covariate 0.1239 四列最低；Causal 列为 0.1597，TS-Agent 为 0.1596，近乎持平，与原文“4/5 最佳、其余几乎持平”一致。

Figure 4 的柱状图方法名为图片，本次文本提取只得到数值；67.6% 归属 TimeClaw 是阅读者按 67.6/48.6≈1.389 与正文“38.9%”吻合推断。

**消融**（§4.4，Figure 5）：检索规模 k 从 0 增到 3，sMAPE/RCRPS 改善；更强骨干（GPT-5 nano→mini→GPT-5）更好；去掉工具、演化或记忆任一组件都会变差。

**局限（阅读者整理，原文无 Limitations 节）**：
- 只有单一骨干的主实验，未报告方差或多次运行；
- TSRBench 只评 20% 子集，而 Table 3 开源模型数值引自原论文（推测为全集），评测集合可能不一致；
- 记忆库与演化工具依赖同分布训练半部分（train ratio 0.5、每族至少一条训练记录），基线是否同样能利用这些训练样本未说明，比较并非严格同条件；
- 能力演化只在金融上展示。

依据：[arXiv 2606.05404v1](https://arxiv.org/abs/2606.05404)，§4、Tables 1–3、Figures 3–5，PDF pp.5–8；附录 E.1、E.3、G。
