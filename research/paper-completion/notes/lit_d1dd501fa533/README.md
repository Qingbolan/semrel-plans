# Fan et al. — Cost-Effective In-Context Learning for Entity Resolution: A Design Space Exploration

本文提出批量提示框架 BatchER，用于实体解析（ER）的匹配阶段：一次提示中放入多对待判定的实体对，并配一组示例。作者系统比较了 3 种问题分批方式和 4 种示例选择方式，并提出基于集合覆盖的示例选择。在 8 个 Magellan 数据集上，批量提示的 API 成本比逐对的标准提示低 4–7 倍，F1 在 7 个数据集上更高。已阅读全文 §I–§VIII；Table IV 的完整 12 种组合只核对了文字结论。

[原文](https://arxiv.org/abs/2312.03987)

版本：arXiv:2312.03987v1（2023-12-07），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §I–§II，pp.1–3 |
| 方法 | §III–§V（Table I，Figures 2–5，Algorithm 1），pp.3–7 |
| 评测 | §VI（Tables II–VII，Figures 6–7），pp.7–12；Tables III、V–VII 已渲染核对 |
| 局限 | 无专门章节；限制散见于 §II-A、§VI-B、§VI-F，pp.2、8–11 |
