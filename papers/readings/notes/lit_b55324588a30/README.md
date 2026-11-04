# Qian et al. — UniDM: A Unified Framework for Data Manipulation with Large Language Models

UniDM 把数据湖上的数据填补、格式转换、错误检测和实体解析统一表述为 `F_T(R, S, D)`，并用三步 LLM 流程（自动上下文检索、上下文解析为自然语言、生成完形填空式目标提示）求解。

以 text-davinci-003 为主模型，在 Restaurant/Buy 填补、TDE 转换、Hospital/Adult 检错和 Magellan 实体解析上与 FM（Narayan et al., 2022）等基线比较，多数设置达到或接近最高分（如 Restaurant 填补 93.0 对 FM 88.4），但每条查询的 token 消耗比 FM 高约 30–40 倍（6,860 对 174）。

已阅读正文 §1–6 及附录 A–E（提示模板、案例、TableQA、连接发现、信息抽取）；未复现实验。

[原文](https://arxiv.org/abs/2405.06510)

版本：arXiv:2405.06510v1（2024-05-10），18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3，PDF pp.1–4 |
| 方法 | §4.1–4.5、Figure 2，PDF pp.4–7 |
| 评测 | §5、Tables 1–10，PDF pp.7–10；附录 D–E、Table 11、Figure 5，PDF pp.16–17 |
| 局限 | §6.1，PDF p.11；§5.2 实体解析与 Table 7 讨论，PDF p.9 |

阅读者备注：首页页脚写作 “Proceedings of the 5th MLSys Conference, 2024”，本记录以 arXiv v1 为版本依据。
