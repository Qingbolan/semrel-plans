# 工作负载

DDI 语料共 1,017 篇（784 DrugBank + 233 MedLine），标注 18,491 个药物实体和 5,021 个 DDI，以 Pyysalo 等提出的 PPI 统一 XML 格式发布。

| 子集 | 训练 | 9.1 测试 | 9.2 测试 |
|---|---|---|---|
| DrugBank 文档 / 句子 | 572 / 5,675 | 54 / 145 | 158 / 973 |
| MedLine 文档 / 句子 | 142 / 1,301 | 58 / 520 | 33 / 326 |
| DrugBank DDI（mech/effect/advice/int） | 1,260 / 1,548 / 819 / 178 | 0 | 279 / 301 / 215 / 94 |
| MedLine DDI（mech/effect/advice/int） | 62 / 152 / 8 / 10 | 0 | 24 / 62 / 7 / 2 |

9.1 测试集由不含 DDI 的文档组成；含 DDI 的文档构成 9.2 测试集，并保留实体标注，可作为 9.1 的额外训练数据。int 类只占全部 DDI 的 5.6%（effect 41.1%、mechanism 32.3%、advice 20.9%）；drug_n 在 DrugBank 中不足 1%。测试集金标准赛后暂不公开，计划用 web 服务评测。

依据：[SemEval 2013，pp.341–350](https://aclanthology.org/S13-2056.pdf)，§2、Table 1，PDF p.2；§3.2，p.4；§4.2，p.8；§5，p.8。
