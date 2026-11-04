# 评测与边界

**比较方法**（§4.1）：
- 需训练：Tapex、TaCube、OmniTab、TaPas、SaMoE、PASTA、Lever、T5（Small/Base/Large）；
- 免训练：Binder、Dater（两者自带投票）；
- 每个基准只报告表现最好的若干基线，且取其已报告的最佳结果，并非全部重跑。

**实验 1（主结果，Tables 1–3）**：

| 方法 | WikiTQ 准确率 | TabFact 准确率 |
|---|---|---|
| 最佳需训练基线 | 62.9%（Lever） | 90.8%（PASTA） |
| Binder | 61.9% | 85.1% |
| Dater | 65.9% | 85.6% |
| ReAcTable（无投票） | 65.8% | 83.1% |
| ReAcTable + s-vote | 68.0% | 86.1% |
| ReAcTable + t-vote | 66.4% | 84.2% |
| ReAcTable + e-vote | 67.2% | 84.9% |

WikiTQ 其他需训练基线：Tapex 57.5%、TaCube 60.8%、OmniTab 62.8%；TabFact：TaPas 83.9%、Tapex 86.7%、SaMoE 86.7%。

FeTaQA（Table 3，ROUGE-1/2/L）：

| 方法 | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| T5-Large | 0.63 | 0.41 | 0.53 |
| Dater | 0.66 | 0.45 | 0.56 |
| ReAcTable | 0.71 | 0.46 | 0.61 |

**实验 2（中间表消融，Tables 4–5）**：Codex-CoT 一次生成整段代码、不看中间表。WikiTQ：Codex-CoT 49.4%、加 s-vote 47.7%，ReAcTable 65.8%、加 s-vote 68.0%。TabFact：Codex-CoT 71.1%、加 s-vote 72.3%，ReAcTable 83.1%、加 s-vote 86.1%。

**实验 3（迭代上限，Tables 6–7）**：WikiTQ 上限 1/2/3/不限时准确率为 49.2%/65.1%/67.3%/68.0%。按实际迭代次数分组，2 轮的题（3,426 题）准确率最高 72.3%，5 轮的题（19 题）仅 46.2%。

**实验 4（只用 SQL 执行器，Tables 8–9）**：WikiTQ 无投票从 65.8% 降到 62.5%，s-vote 从 68.0% 降到 64.5%；TabFact s-vote 从 86.1% 降到 76.2%（降 9.9 个百分点）。

**实验 5（换 LLM，Tables 10–11）**：

| 模型 | WikiTQ（无投票 / s / t / e） | TabFact（无投票 / s / t / e） |
|---|---|---|
| code-davinci-002 | 65.8 / 68.0 / 66.4 / 67.2 | 83.1 / 86.1 / 84.2 / 84.9 |
| text-davinci-003 | 63.3 / 64.1 / 64.5 / 65.0 | 81.2 / 83.1 / 82.9 / 83.6 |
| gpt3.5-turbo | 52.4 / 51.8 / 52.5 / 不适用 | 73.1 / 72.8 / 74.4 / 不适用 |

gpt3.5-turbo 不提供 log-prob，无法做 e-vote；它倾向输出完整句子，与 WikiTQ 结构化评测器不兼容，是分数低的原因之一（§4.4）。

**边界**：
- 原文 §5.3–5.4：投票会增加提示成本，且在模型不确定时可能降低准确率；few-shot 示例需人工构造；只支持单表；最佳投票方式需自动选择。
- 阅读者整理：未报告延迟、调用次数或费用，投票方案的代价无法比较；基线数字多取自原论文，不是同环境重跑；Codex 已下线，结果难以复现；ROUGE 只衡量文本相似，不保证 FeTaQA 答案事实正确（阅读者分析）。

依据：[arXiv 2310.00815](https://arxiv.org/abs/2310.00815)，§4.1–4.4、§5.3–5.4、Tables 1–11，PDF pp.6–11。
