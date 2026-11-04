# 工作负载

**数据集**（§5.1，p.6；附录 B，Table 7，p.13）：

| 数据集 | 用途 | 测试集规模 |
|---|---|---|
| Natural Questions (NQ) | 训练 + 测试 | 3,610 |
| TriviaQA | 仅测试（域外） | 11,313 |
| WebQuestions (WebQ) | 仅测试（域外） | 2,032 |
| SQuAD | 仅测试（域外） | 10,570 |

NQ 训练集 58,880 条；划分沿用 DPR（Karpukhin et al., 2020）（附录 B，p.13）。

**检索文档**：评测时每个问题取稠密检索器的 top-10 文档（§5.1，p.7）。NQ、TriviaQA 用 FiD-distilled 检索器；SQuAD、WebQ 从 Contriever-msmarco 出发训练（附录 C，p.13）。检索器自身 Hit@10：NQ 80.00、TriviaQA 81.78、WQ 75.89、SQuAD 68.51（Table 8）。

**训练细节**：LLaMA2-Base 7B，学习率 1e-6，batch 64，1 epoch，8×A100-40G（§5.1、附录 D）。

单位：一个样本是一个问题（附带 10 篇检索文档）；答案为短实体/短语。论文未报告查询类型分布或文档长度统计。

依据：§5.1、附录 B–D、Tables 7–8，PDF pp.6–7、13–14。
