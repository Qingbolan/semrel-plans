# 评测与边界

**设置**：被测模型为 Llama-3.1 70B/405B、Qwen-2.5 72B、Claude-3.5 Sonnet、GPT-4o、o1-preview；默认使用 CoT，比较 0-shot 和 1-shot（§4.1，PDF p.5）。

**实验 1（主结果，Table 3，PDF p.6）**：Acc(t) 普遍很低。下表为选取的 0-shot 结果。

| 模型 | Airline L1 | Airline L3 | NBA L1 | Tax L1 | Tax L3 |
|---|---|---|---|---|---|
| GPT-4o | 0.02 | 0.00 | 0.40 | 0.42 | 0.00 |
| Claude-3.5 Sonnet | 0.04 | 0.01 | 0.38 | 0.32 | 0.00 |
| o1-preview | 0.54 | 0.21 | 0.44 | 0.72 | 0.19 |

Airline 和 Tax 的 P(t) 都是 1.000，NBA 仅约 0.47–0.75。NBA 题没有逐步计算标注，因此不报 AC(t)（Table 3 脚注）。

**实验 2（规则层面，Tables 4–7，PDF pp.7–8）**：低召回的多为非必用规则，低正确率的多为需要组合多个中间结果的规则；NBA 的低精确率来自可互相替代的相似规则。

**实验 3（因素分析，附录 D.2，PDF pp.19–22）**：

- R(t) 与 Acc(t) 近似线性相关；Tax 中 R(t) 低于 0.95 时准确率即为 0。
- NBA 难题上 1-shot 反而降低 Acc(t)。
- 把表格规则改写成文本后 R(r) 上升，但 Acc(t) 基本不变（Table 9）。
- 加入置零的税表作为干扰规则会明显降分，同等长度的无意义 token 只轻微影响（Figure 8）。
- 让模型写 Python 计算（工具增强）后，GPT-4o 在 Airline L1 的准确率从 1-shot 默认设置的 0.32 升至 0.44（Table 10；与上表 0-shot 的 0.02 不是同一设置）。

**边界**：使用 GPT-4o 解析回答，未报告解析准确率；没有微调实验（Limitations，PDF p.10）。结论写“最强的 Claude-3.5 和 GPT-4o 也很难解决最难题”，但 Table 3 中 Acc(t) 多数列最高的是 o1-preview（阅读者分析）。
