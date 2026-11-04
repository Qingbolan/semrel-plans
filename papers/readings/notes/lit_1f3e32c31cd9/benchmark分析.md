# 评测与边界

**基线**（§5.1，pp.6–7）：长上下文 LLM（LongAlign-7B-64k、LongLoRA-13B-32k）；高级 RAG（CFIC-7B、CRAG、Self-RAG，后两者用 GPT-3.5-Turbo、经 LangGraph 复现）；Vanilla RAG（8 个 LLM，从 ChatGLM3-6B 到 GLM-4）。指标为 F1。

**实验 1（总体性能，Table 1）**：

| 系统 | HotpotQA | 2WikiMQA | MuSiQue | 平均 |
|---|---|---|---|---|
| LongLoRA-13B-32k | 47.45 | 42.92 | 29.46 | 39.94 |
| Self-RAG（GPT-3.5） | 50.51 | 46.75 | 24.62 | 40.63 |
| Vanilla RAG（GLM-4） | 57.41 | 52.91 | 27.55 | 45.96 |
| LongRAG-ChatGLM3-6B（SFT） | 55.93 | 54.85 | 33.00 | 47.93 |
| LongRAG-GLM-4（无 SFT） | 62.11 | 57.16 | 38.40 | 52.56 |

微调后的 ChatGLM3-6B 版平均 47.93，高于未微调的 GPT-3.5-Turbo 版 46.79（§5.2）。

**实验 2（消融，Table 3）**：比较 R&B（Vanilla）、R&L（直接喂源段落）、只用抽取器、只用过滤器、两者结合。多数情况下 E&F 最好；只用过滤器提升有限；R&L 输入最多但不稳定提升（§5.3，p.8）。Figure 3 显示 E&F 输入生成器的 token 少于 R&L（§5.4）。

**实验 3（附加）**：ReAct（GPT-3.5）平均 39.76（附录 A.4，Table 4）。

**比较条件与边界**：

- 基线的输出过长、F1 吃亏，作者用 GPT-3.5-Turbo 少样本把 Self-RAG、CRAG、LongLoRA、LongAlign 的输出改写成最终答案后再计分（附录 B.1）；LongRAG 自身未做此处理。
- CRAG 原本的网络检索回退被改为改写问题后在本地语料再检索（附录 B.1）。
- GLM-4 调用时只用 8k 窗口（§5.1 脚注 4）。
- 未报告方差、显著性或多次运行。（阅读者分析）
- §7 局限：只研究一次性检索；微调数据由 32B 模型自生成，可能带来标注偏差。

依据：§5，Tables 1–3、Figures 3–4，PDF pp.6–9；附录 A.4、B.1，pp.14–15；§7，p.9。
