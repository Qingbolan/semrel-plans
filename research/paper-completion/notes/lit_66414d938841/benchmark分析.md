# 评测与边界

**被测模型**（§3.1，PDF pp.6–7）：

- 专有模型：GPT-4、GPT-3.5、Claude-2.1、Abab5.5、Gemini-Pro；
- 开源通用模型：Vicuna、ChatGLM、Baichuan、Qwen、InternLM、AgentLM、Mistral、Yi 等；
- 开源代码模型：Code Llama、WizardCoder、Phind CodeLlama、DeepSeek Coder、XwinCoder；
- 智能体框架：XAgent、AutoGen（均用 GPT-4）和 Qwen-Agent（Qwen-72B-Chat）。

除现成框架外，所有模型都用作者的智能体框架；温度 0.2、top-p 1.0（附录 P，PDF p.14）。**指标**：准确率（所有子问题都答对的问题比例）。

**实验 1（排行榜，Table 6，PDF p.16）**：

| 模型 | 准确率（%） |
|---|---|
| gpt-4-0613 | 78.99 |
| AutoGen（gpt-4-0613） | 71.48 |
| DAAgent-34B | 64.59 |
| abab5.5-chat | 61.48 |
| gpt-3.5-turbo-0613 | 60.70 |
| Qwen-72B-Chat | 59.92 |
| Gemini-Pro | 56.42 |
| XAgent（gpt-4-0613） | 47.52 |
| Claude-2.1 | 47.47 |

作者结论（§3.3，PDF p.7）：最强的 GPT-4 也有很大提升空间；最强开源模型 Qwen-72B-Chat 比 GPT-4 低约 19 个百分点，但只比 GPT-3.5 低 0.78。

**实验 2（DAInstruct 微调，Table 5，PDF p.8）**：CodeLlama-Instruct 7B/13B/34B 为 24.61/26.67/31.13，同尺寸 DAAgent 为 51.36/55.86/64.59。

**实验 3（重新格式化消融，附录 Q、Table 23，PDF pp.15、26）**：不加重新格式化时，GPT-4 从 78.99 降到 72.76，Mistral-7B 从 38.67 降到 6.23；人工抽查 50 条，GPT-3.5 都能正确改成要求的格式。

**边界**：
- 摘要所说“超过 GPT-3.5 3.9%”是 64.59 与 60.70 的百分点差 3.89，不是相对提升（阅读者分析）。
- 评测依赖 GPT-3.5 重新格式化，只抽查了 50 条；Table 23 标题写“用 GPT-4 作为评估器”，与正文的正则精确匹配描述不一致（阅读者分析）。
- 只报告公开验证集上的单次结果，没有方差；测试集结果未给出（阅读者分析）。
- 作者承认排除了可视化问题（附录 A，PDF p.12）。

依据：§3，附录 A、P、Q，Tables 5–6、23，PDF pp.6–8、12、14–16、26。
