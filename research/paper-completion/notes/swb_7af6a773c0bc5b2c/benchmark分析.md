# benchmark

本文**没有自动系统的基线或实验**。评测对象是人工标注的一致性和语料分布。

**一致性**（Table 16）：在 104 篇双标注摘要上，Kappa（正文未说明具体变体）分别为：

| 维度 | Kappa |
|---|---|
| Polarity | 0.929 |
| Source | 0.878 |
| CL | 0.864 |
| Manner | 0.864 |
| KT | 0.843 |

作者的解释：取值少的维度一致性更高；KT 有 6 个取值，且常需要线索词以外的上下文，所以最低。最大的分歧在 KT 的 Observation 与 Fact 之间，两者都常用现在时，且多数没有线索词。作者据此认为，不论标注者是生物学背景还是语言学背景，都能可靠完成该任务。

**局限**（含阅读者分析）：
- Kappa 的具体变体没有在正文中逐一说明。
- 一致性只在 10% 的样本上计算。
- 类别分布极不均衡，例如 Source=Other 只占 1.5%、Manner=Low 只占 0.8%，整体 Kappa 可能掩盖稀有类别上的分歧。
- 只覆盖摘要。
- 没有展示自动识别的效果；作者把机器学习系统列为未来工作（Conclusion）。

依据：[BMC Bioinformatics 12:393，PMC3222636 全文 XML](https://doi.org/10.1186/1471-2105-12-393)，Results（Inter-annotator agreement、Annotation discrepancies）、Conclusion。
