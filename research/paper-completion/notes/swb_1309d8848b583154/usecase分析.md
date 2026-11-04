# usecase

用例：用 CRAFT 训练或评测"文本→本体概念"的识别系统。例如为小鼠功能基因组学文献中的化学实体标注 ChEBI ID，或为基因提及标注 Entrez Gene/PRO 概念。

原文给出的具体难点：
- **ChEBI**：分子、氨基酸残基、取代基团分属不同子图，例如 serine、serine residue、seryl group。标注者起初把 "serine 132" 这类残基提及错标为分子，经负责人指出后才更正（IAA 部分）。
- **CL**：同一篇文章中几十处 PMN 提及，两名标注者分别标为 granulocyte 和它的子类 mature neutrophil，导致该数据点的 IAA 大幅下降。
- **Entrez Gene**：物种和序列类型都有歧义，提及常需要标多个物种的 ID；作者认为 PRO 的标注比 Entrez Gene 更一致、更可用（Entrez Gene、PRO 分节）。

阅读者分析：如果在图谱中把 CRAFT 作为抽取或语义匹配的工作负载，评分时应注意：
- 默认按精确 span 和精确概念匹配；
- 原文认为，适度放宽 span 或允许上下位概念，会得到更高的一致性；
- 多 ID 标注可以采用部分得分。

以上评分方案的取舍是项目派生决策，本文没有评测自动系统。

依据：[BMC Bioinformatics 13:161，PMC3476437 全文 XML](https://doi.org/10.1186/1471-2105-13-161)，Results（IAA）、Discussion、Methods 各术语分节。
