# 具体用例

论文用 Radev（2000）的英文例子说明 CST 在多文档摘要中的作用（Example 3）：

- 句 a：“John Doe was found guilty of the murder.”
- 句 b：“The court found John Doe guilty of the murder of Jane Doe last August and sentenced him to life.”

b 包含 a 的关键信息并补充了“法院”“去年八月”“判处终身监禁”，所以 b→a 为 Subsumption（非对称、有方向）。按 CSTNews 的定义（Figure 5），Subsumption 属于 Content → Redundancy → Partial 类型，约束为 S1 包含 S2 的信息外加额外信息。

在 CSTNews 中，同一新闻事件的 2–3 篇报道被切成句子，标注者对跨文本句对标注此类关系。阅读者分析：多文档摘要系统可利用 Subsumption/Overlap 等冗余关系只保留信息更全的句子，再用 RST 核心性在单篇内部挑重要命题；但本文没有实际运行这样的摘要流程，这些是作者陈述的用途与阅读者推断。

依据：[RST 2011 workshop，pp.88–105，18 页](https://sites.icmc.usp.br/taspardo/RST2011-CardosoEtAl1.pdf)，§2 Example 3，PDF p.6；§3.2 Figure 5，PDF p.13；§1，PDF p.3。
