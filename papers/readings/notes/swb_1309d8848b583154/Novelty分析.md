# novelty

原文强调的特点（Background、Discussion）：
- 全文标注，涵盖遗传学、生化、细胞、发育乃至计算生物学等学科；
- 使用 9 个大型社区本体/术语的完整内容作为标注 schema，规模从约 800 类（CL）到约 41 万概念（NCBITaxon），以及约 720 万条 Entrez Gene 记录；
- "语义等同"标注原则；
- 纯句法的 span 规则，并允许不连续标注；
- 对无法消歧的情况显式给出多个概念；
- 规模大：67 篇首发约 56 万 token、近 10 万条标注；全集约 79 万 token、超过 14 万条标注。

此外，同一批文章还有句法标注和共指标注，分别见配套论文。

阅读者评估：
- 贡献是资源和标注方法论，没有模型或基线。
- 本文中的全集 token 数前后不一致：摘要和 Table 3 写约 790,000，Conclusions 写 830,000。
- 质量证据主要来自单盲 IAA（见 benchmark 分析），双盲样本很少。

依据：[BMC Bioinformatics 13:161，PMC3476437 全文 XML](https://doi.org/10.1186/1471-2105-13-161)，Abstract、Background、Discussion、Conclusions、Table 3。
