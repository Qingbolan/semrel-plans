# 评测与边界

**模型**：GPT-4o、Sonnet-3.5、Llama-3.1-70B、Llama-3-8B（含在训练集上微调版本）；SSR 另测 GritLM-7B、OpenAI-v3-large 嵌入；主任务另测 RobotReviewer、SVM、LR。生成模型用思维链，温度 0（§5.1，pp.6–7）。

**实验 1（主要结果，Tables 3–5，p.6，已渲染核对）**：

| 模型 | SSR 平均（Aspect Recall） | SJS 平均（准确率） | 主任务平均 Macro-F1 |
|---|---|---|---|
| OpenAI-v3 嵌入 | 22.7 | — | — |
| GPT-4o | 47.5 | 47.2 | 42.1 |
| Sonnet-3.5 | 39.2 | 59.9 | 41.9 |
| Llama-3.1-70B | 45.6 | 53.2 | 38.8 |
| Llama-3-8B | 22.7 | 26.5 | 30.1 |
| Llama-3-8B 微调 | 40.8 | 29.6 | 36.3 |

作者解读：GPT-4o 长于检索，Sonnet-3.5 长于综合推理（§6.1，p.7）。主任务正确的样本在 SSR、SJS 上得分也更高（§6.2，Figure 4）。

**实验 2（检索/推理交叉，Table 6，313 条，p.7）**：GPT-4o 推理配 Sonnet 检索 31.5、配 GPT-4o 检索 40.3、配真实支持句 46.1；Sonnet 推理配真实支持句 49.4。

**实验 3（非 Cochrane 测试，Table 7，p.8）**：给全文加 o4-mini 找到的高亮句，GPT-4o 从 42.5 到 44.1，Sonnet 从 40.3 到 44.5，提升有限。

**实验 4（传统模型，Table 8，p.8）**：只取 RobotReviewer 可评的 4 类偏倚、两级标签，平均 Macro-F1：

| 模型 | 平均 Macro-F1 |
|---|---|
| RobotReviewer | 56.7 |
| LR | 53.1 |
| SVM | 44.8 |
| GPT-4o | 65.6 |
| Sonnet-3.5 | 67.5 |

置信区间重叠，作者称结论不确定。

**边界**：仅英文、开放许可文献；SSR 金标准由 GPT-4 生成；提示词可能还有改进空间；BERT 类模型 512 token 不足以处理平均 8k token 的论文；o4-mini 高亮使用了真实风险等级作为引导，属于概念验证（Limitations、§6.4–6.6，pp.8–9）。

依据：§5–6、Limitations，PDF pp.6–9；Tables 3–8。
