# 评测与边界

**指标**（Table 3，§2.2，p.4）：精确字符串 / 精确数值按 0/1 准确率；近似字符串用 ParaPluie（LLM 判定，与人工一致率 84%，附录 G.2）；近似数值用 1/(1+RAE)；列表用 F1（近似列表在匹配度 >0.9 时计入）。领域分和总分为任务分的平均。

**被测系统**（§3，pp.6–7）：
- DS-Guru 三个变体 × 6 个 LLM（GPT-o3、GPT-4o、Claude-3.5-Sonnet、Llama3.3、DeepSeek-R1-70B、Qwen2.5-Coder-32B）；
- smolagents 单智能体 Deep Research（GPT-o3、Claude-3.7-Sonnet），多智能体 Reflexion 与 PDT；
- 闭源 OpenAI Deep Research、Gemini 2.5 Pro Agentic（网页界面手工评测，无法禁止联网）；
- 9 名数据科学从业者的人类基线（每人分到部分任务，附录 F）。
尽量重复 3 次取均值，带星号的结果未重复。

**实验 1（端到端，Full / Oracle 总分，Table 5，p.7）**：

| 系统 | Full | Oracle |
|---|---|---|
| 人类基线 | 76.75 | – |
| DS-Guru few-shot（GPT-o3） | 24.98 | 43.71 |
| smolagents DR（Claude-3.7） | 55.83 | 60.67 |
| smolagents Reflexion（Claude-3.7） | 55.37 | 62.81 |
| smolagents PDT（Claude-3.7） | 12.01 | 14.38 |

Trimmed 设置下：DS-Guru few-shot（GPT-o3）37.84，smolagents DR（Claude-3.7）58.12，OpenAI Deep Research 52.18，Gemini Agentic 18.48。

**实验 2（三层评估，DS-Guru，GPT-o3，Table 8，p.9）**：流水线设计 37.99–41.71%，子任务实现 10.69–22.05%，端到端 5.87–24.98%。DeepSeek-R1 恰好相反（设计约 1%，实现最高 5.79%）。

**实验 3（混淆输入，Table 7，p.8）**：

| 系统 | Full | Oracle | 混淆 |
|---|---|---|---|
| DS-Guru few-shot（GPT-o3） | 24.98 | 43.71 | 23.02 |
| smolagents DR（Claude-3.7） | 55.83 | 60.67 | 12.77 |
| smolagents Reflexion（Claude-3.7） | 55.37 | 62.81 | 13.94 |

Claude-3.7 后端对混淆输入最敏感，作者推测这些配置很大程度上依赖参数化知识。

**其他**：OPS 每文件抽样 10–150 行，得分 22.58–24.68%，不随样本增大而提升（Table 6）；few-shot 增至 20 轮也只有小幅改进（Table 13）；smolagents DR 平均每任务 6.10 分钟，OpenAI DR 10.35 分钟，DS-Guru few-shot 0.76 分钟（§4）。人类的失败中 46% 是流水线设计错误、24% 是缺领域知识、12% 是用错输入（附录 F）。

**原文内部不一致**（阅读者分析）：
- §4 正文称 Trimmed 下 OpenAI DR 达到 58.12%，但 Table 5 中 58.12 属于 smolagents-single DR（Claude-3.7），OpenAI DR 为 52.18；
- §4.1 正文称 Reflexion 从 62.81% 跌到 12.77%，Table 7 中 Reflexion 的混淆分为 13.94，12.77 属于 smolagents DR；
- §1 说为 20% 的任务构造了混淆输入并留出，§4.1 则说为所有任务构造了混淆输入；
- §3 列出 DS-Guru 使用 Claude-3.5-Sonnet，Table 5 写作 Claude-3.7。

**边界**：作者在伦理声明中承认领域、语言与文化覆盖受人工整理成本限制；人类基线规模小且未重复。阅读者补充：答案分不检查证据链；闭源系统可联网，与其他系统不在同一条件下。

依据：[arXiv 2506.06541v3](https://arxiv.org/abs/2506.06541v3)，§2.2、§3–4、Tables 3、5–8、附录 F–G，PDF pp.4–11、27–29。
