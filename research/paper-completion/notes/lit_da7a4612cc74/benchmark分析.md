# benchmark

**基线**（§6.1，PDF p.13）：
- Text-To-Table：BART-base，需微调；
- LLaMA-2 7B：in-context（ic）和 Q-LoRA 微调（ft）两种用法；
- gpt-3.5-turbo-0125 与 gpt-4-0613：few-shot。

所有基线都先把整个文本集合转成表，再执行传统算子。未比较 WannaDB（需要用户交互）和 Evaporate-Code（面向半结构化文档）。

**硬件**：DGX A100。预训练用 4 块 GPU，约 8 天，6 个 epoch；微调和推理用 2 块 GPU。GPT 模型跑在 OpenAI 的硬件上，运行时间不可直接比较，Exp.2/3 中不再使用。

**指标**：值与标签完全匹配（Exact Match）才算对，标签允许多个等价写法；每篇文本计算 F1 后取平均；聚合查询按组计算 F1 后取平均；效率指标为单个查询的运行时间。

**主要结果**：
- Exp.1（p.13，Figure 7）：ELEET 在所有查询上都最快，其他方法最多慢 575 倍。aviation 和 corona 的多数查询 F1 超过 90%；rotowire 和 T-REx 集中在约 75%–80%。GPT-4 在 aviation 和 corona 上也很准。只用 64 个样本时，Text-To-Table 和 LLaMA-ft 在 rotowire 上约为 25%。
- Exp.2（p.14，Figure 8）：只有 4–16 个样本时，ELEET 和 LLaMA-ic 约为 40%；用全量数据时，ELEET 在 scan/join/union 上达到 87%。
- Exp.4（p.15，Figure 11）：消融预训练，ELEET 权重优于 TaBERT 权重，TaBERT 权重优于 BERT 权重。
- Exp.5（pp.15–16）：在 SQuAD 上，生成式解码比抽取式多用约 25% 的时间；Table 4 中，去掉 vertical attention 后，在歧义列名数据上 F1 从 0.99/0.99 降到 0.41/0.55。
- Exp.6（Table 5）：GPT-3.5 对 4 个数据集全部 latent 表的键和多行性都判断正确。
- Exp.7（Figure 13）：用滑动窗口处理超过 512 token 的文本，F1 没有下降。

**局限**（含阅读者分析）：
- 575 倍是最大倍数，不是平均值。
- 主结果以图呈现，没有逐查询数值。
- aviation 和 corona 的测试集各只有 30 篇文本。
- T-REx 只评测 nobel 领域。
- 基准由作者自建，没有独立复现。
- 未接入真实查询优化器（§8）。

依据：[arXiv:2410.22522v1，23 页](https://arxiv.org/abs/2410.22522)，§6–§8，Figures 7–13、Tables 4–5，PDF pp.12–18。
