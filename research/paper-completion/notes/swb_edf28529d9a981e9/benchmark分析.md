# 评测与边界

**实验 1（标注一致性）**：Krippendorff’s α，按“该类 vs 非该类”二值计算（Table 2，p.4）。Policy 0.78、Value 0.52、Fact 0.34、claim 整体 0.52；Statistics 0.16、Hypothetical-Instance 0.70、Real-Example 0.58、Common-Ground 0.42、premise 整体 0.53；Testimony 无法计算。

**实验 2（与先前工作对比）**：在 Carlile et al. 的 102 篇（PREVIOUS）上训练，claim 准确率 76.9%（Ke et al. 2018 报告 69.5%），premise 70.1%（对方 31.2%）；作者认为提升主要来自预训练模型（§4，p.5）。

**实验 3（全语料分类）**：RoBERTa-base，仅输入 ADU 片段，冻结前半层，lr 5e-5，batch 16，10 epoch，10 次重复（附录 A，p.12）。

| ADU | 多数类基线宏 F1 | 模型宏 F1 | 模型微 F1/准确率 |
|---|---|---|---|
| Major claim | 26.2 | 75.9 | 88.1 |
| Claim | 26.9 | 77.2 | 80.0 |
| Major claim+claim 合并 | — | 78.6 | 83.6 |
| Premise | 13.5 | 56.6 | 70.2 |

数值见 §4（pp.5–6）与 Table 6（p.12）。Premise 中 testimony F1 仅 0.193，statistics 0.431。学习曲线显示增加数据对 claim/major claim 收益更明显（Figure 2，p.6）。

**实验 4（模式分析）**：首段多为单个 major claim（M:Value 0.35）；中段多为单一 claim 类型（C:Value 0.65）；policy claim 的 premise 中 common-ground 比例更高（0.59 vs 0.47/0.43），fact claim 的 statistics 比例最高（0.15）（Tables 4–5，pp.7–8）。Policy 题目下 policy claim 比例 0.33，fact 题目下 fact claim 比例 0.28（Figure 3，p.8）。

**局限（原文）**：学习者作文水平差异大；AAE 规模有限，testimony 等类稀少；未研究题目与 flow 的关系，也未分析题目/作者对 premise 类型的影响（Limitations，pp.9–10）。阅读者分析：模式结论没有统计检验，fact/statistics 等低一致性类别上的模式需谨慎解读。
