# 评测与边界

**实验 1（Bio-ML 无监督，与 14 个系统比较）**：对比数据整理自 OAEI 2023/2024 公布的结果和文献（§5.4，PDF p.13）。Tables 1–2（p.15）中的 F 值：

| 任务 | MILA | 最强对比系统 |
|---|---|---|
| OMIM-ORDO | 0.831 | LogMapBio 0.715 |
| NCIT-DOID | 0.948 | HybridOM 0.918 |
| SNOMED-FMA | 0.894 | BERTMap / HybridOM 0.790 |
| SNOMED-NCIT (Pharm) | 0.864 | HybridOM 0.902 |
| SNOMED-NCIT (Neoplasm) | 0.903 | LogMapBio 0.771 |

**实验 2（半监督，70% 测试集）**：MILA 在 NCIT-DOID（0.970）和 SNOMED-NCIT(Neoplasm)（0.893，Matcha-DL 为 0.757）上最好；在其他任务上落后第一名 3–4 个百分点，例如 SNOMED-FMA 上 BioGITOM 为 0.923，MILA 为 0.884（§5.4.2、Tables 3–4，pp.13、16–17）。

**实验 3（Anatomy 与 Biodiversity）**：MOUSE-HUMAN 上 MILA 为 0.922，次于 Matcha 的 0.941；ENVO-SWEET 上 MILA 为 0.837，LogMap 为 0.713（Table 5，p.17）。

**实验 4（运行时间）**：Table 8（p.18）比较了两种管线，均使用 LLaMa-3.3-8B。例如 SNOMED-FMA 上，MILA 用时 0:44:59，先检索再提示的基线用时 46:46:53。由于成本原因，70B 模型没有跑基线（§5.3，p.13）。

**实验 5（配置对比）**：Table 9 比较只用 HCB、HCB+8B、HCB+70B 三种配置（p.19）。

边界：原文"超出 17%"等提升幅度是相对值，按 Table 1 计算，OMIM-ORDO 的绝对差为 0.116（阅读者分析）。对比系统的数字来自公开结果，并非统一重跑；MILA 的结果是至少 20 次运行，但表中没有给出方差区间。§6.1 列出的局限包括：贪心搜索只看相似度值、提示过于简单、只做等价匹配、嵌入检索在大本体上的扩展性问题（pp.20–21）。

依据：[arXiv:2501.11441v2，25 页](https://arxiv.org/pdf/2501.11441v2)，§5、§6.1、Tables 1–9，PDF pp.13–21。
