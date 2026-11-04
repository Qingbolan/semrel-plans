# 工作负载

论文没有基准数据集或实验负载，只有三个演示示例：

| 示例 | 数据 | 规模（原文输出） | 位置 |
|---|---|---|---|
| 分词与渲染 | 句子"Self-isolation for 14 days is required!" | 9 个 basedata 元素 | §2.1，PDF p.3 |
| 加载与校验 | ACL Anthology 共指语料（Schäfer et al. 2012）中的 C02-1001 文档 | 2,471 个 basedata；coref 层 216 个 markables，sentence 层 126 个 | §2.2，PDF p.4 |
| 从预标注数据创建项目 | LitCovid（近 45,000 篇 Covid-19 文献，BioC XML，6 种生物医学实体类型）中的文档 32393453 | 179 个 basedata；passages 层 2 个、entities 层 4 个 markables | §2.3，PDF pp.4–5 |

校验示例：临时从 coref 层方案的 `np_form` 属性中删除可选值 `ne` 后，加载同一文档产生 58 个异常（§2.2，PDF p.4）。

阅读者分析：这些数字只是演示输出，不构成评测；论文没有给出处理速度、内存或大规模语料上的运行情况。

依据：§2.1–2.3，PDF pp.3–5。
