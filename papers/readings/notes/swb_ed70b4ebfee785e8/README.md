# Aly & Vlachos — TabVer: Tabular Fact Verification with Natural Logic

TabVer 把自然逻辑推理扩展到表格证据：为数字和算术函数结果定义集合论意义下的自然逻辑算子（NatOp），用 LLM 针对声明的显著片段生成问题，在表上抽取证据并执行受限的算术函数（ArithExp），再由确定性有限自动机给出 Supports/Refutes/NEI 判定。在 FEVEROUS 表格子集上只用 64 条训练样本，准确率 71.4，比最强基线高 3.4；不经再训练迁移到 TabFact 开发集，准确率 65.6，领先 0.5。已阅读正文、局限及附录 A–D。

[原文](https://aclanthology.org/2024.tacl-1.89)

版本：TACL vol.12，pp.1648–1671，2024（DOI 10.1162/tacl_a_00722），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头，PDF pp.1–3 |
| 方法 | §3.1–3.4、§4.3，PDF pp.3–8 |
| 评测 | §4–5、Tables 1–5，PDF pp.7–11 |
| 局限 | §6，附录 B–D，PDF pp.12–13、19–22 |
