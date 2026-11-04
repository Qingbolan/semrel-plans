# 评测与边界

**基线**（§4.1）：大型生成式推荐器 Tiger、ReaRec、Lc-Rec、OpenOneRec（数值按 [18] 设置）；在 SASRec/HSTU 上的网格搜索与贝叶斯优化；同 LLM、同动作接口但无反思/记忆/摘要的 OPRO。

**主要结果**：
- Table 1（测试集，p.4）：VirtualMLE 在两种骨干、三个数据集的 12 个指标格均为同组最好；相对同骨干最佳基线提升 +2.1% 至 +12.1%（HSTU/Baby N@5）。例如 SASRec+VirtualMLE 在 Baby 上 N@10=0.0321，贝叶斯优化为 0.0298；OpenOneRec 为 0.0289。正文称相对原始 SASRec 平均提升 29.9%–31.9%，相对原始 HSTU 21.4%–25.4%。
- Table 2（p.4）：首次达到最佳验证 NDCG@10 的试验序号（越低越好）：

| 骨干 | 方法 | Baby #Trials | Beauty #Trials |
|---|---|---|---|
| SASRec | 贝叶斯优化 | 163 | 267 |
| SASRec | OPRO | 78 | 92 |
| SASRec | VirtualMLE | 28 | 24 |
| HSTU | 贝叶斯优化 | 464 | 453 |
| HSTU | OPRO | 124 | 137 |
| HSTU | VirtualMLE | 32 | 17 |

- Table 3（p.5）消融：去掉反思或记忆都下降，如 HSTU/Baby N@10 0.0327 → 0.0313（无反思）→ 0.0298（无记忆）。
- Table 4（p.6）：换 Kimi 2.6、DeepSeek V4 Pro 后 NDCG 相近，试验数 45–53，单次会话 LLM 成本 1.5–2.2 美元，GPT-5.4 为 3.2–4.8 美元。

**局限与疑点**（阅读者分析；论文无局限性章节）：
- Table 4 中 GPT-5.4 的 #Trials（Baby 32、Beauty 27）与 Table 2 同设置的 28、24 不一致，论文未解释口径差异。
- 预算“偏向基线”只指基线试验次数多；VirtualMLE 可改结构而 HPO 基线不能，搜索空间不对等，“优于 AutoML”部分可能来自更大的动作空间。
- 生成式推荐器数字沿用他文设置，非同一流水线重跑。
- 三次运行平均但未报告方差或显著性；正文与图中的“visibly”“Pareto-better”为定性判断。
- 仅 Amazon 小规模、短序列数据集；作者在 Cognition Summary 中自己注明规则针对“小规模 Amazon 基准”。

依据：[arXiv:2606.03221v1，7 页](https://arxiv.org/abs/2606.03221)，§4.1–4.5、Tables 1–4，PDF pp.3–6。
