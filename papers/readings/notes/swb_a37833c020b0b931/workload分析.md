# 工作负载

**数据集 1：Brown**（§4，p.1759）：Brown 语料 popular lore 小节的 20 篇文本，人工切分为 4,391 个子句，两名标注者，Cohen's κ=0.52，经裁决得最终标签；用于复现 UT07，测试集 787 个实例（Table 5）。

**数据集 2：MASC + Wikipedia**（§4，Table 1–2，p.1759）：

| 语料 | 词数 | SE 数 | Fleiss' κ |
|---|---|---|---|
| MASC（12 个书面体裁） | 357,078 | 30,333 | 0.69 |
| Wikipedia | 148,040 | 10,607 | 0.66 |

类型分布差异大：MASC 中 STATE 占 49.8%、EVENT 24.3%、GENERIC 7.3%；Wikipedia 中 GENERIC 占 49.7%、STATE 24.3%（Table 2）。补充 Wikipedia 正是因为 MASC 类指句少且无百科体裁。

**划分**（§6.2，p.1762）：按 SE 数取 80% 作开发集做 10 折交叉验证，20% 为留出测试集，两者文档不重叠，各体裁文档分布到各折。原文括注“共 32,855 个已标注 SE”，留出测试集 7,937 个实例（Table 7）。阅读者分析：Table 1 合计 40,940 个 SE，32,855 + 7,937 = 40,792，故 32,855 应指开发部分；两者差额可能来自未进入实验的 undecided 等标签，原文未说明。

13 个体裁：blog、email、essays、ficlets、fiction、govt-docs、jokes、journal、letters、news、technical、travel、wiki（Table 11）。

依据：§4、§6.2、Table 1–2、5、7、11，pp.1759–1764。
