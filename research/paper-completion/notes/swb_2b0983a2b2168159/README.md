# Graus — From Legal Text to Executable Decision Models: Evaluating Structured Representations for Legal Decision Model Generation

本文用荷兰《环境与规划法》（Omgevingswet）配套政府门户 Omgevingsloket 中实际上线的 95 个 DMN 决策模型及其对应法条，比较四种输入（纯法条、+语义角色标注 srl、+输入/输出规格 io、两者都加）下 GPT-5.1 生成可执行决策模型的效果。主要结论：io 规格带来主要提升（图核相似度相对基线 +37%/+54%），srl 作用有限；在可测试的 58 个模型上，宏平均结果一致率为 51–53%，结构相似与结果等价并不一致。已阅读正文全部章节（§1–§5）及全部 6 张表；未复核作者发布的代码与数据。

[原文](https://arxiv.org/abs/2604.17153)

版本：arXiv:2604.17153v1（2026-04-18，ICAIL 2026 论文），10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1、§2.5，PDF pp.1–3 |
| 方法（数据与实验设计） | §3.1–3.6、Table 1、Figure 1，PDF pp.3–5 |
| 评测 | §4.1–4.5、Tables 2–6、Figures 2–3，PDF pp.5–9 |
| 局限 | §4.2.3、§5.1 Limitations、§5.2，PDF pp.7、9–10 |
