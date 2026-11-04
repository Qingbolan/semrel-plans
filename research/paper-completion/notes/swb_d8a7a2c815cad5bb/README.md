# Kannan, Shapiro & Bilgic — Hindsight Analysis of the Chicago Food Inspection Forecasting Model

本文是对芝加哥公共卫生局（CDPH）2015 年部署的餐馆检查风险预测模型所做的首个独立事后分析。该模型是 16 个特征的逻辑回归，用于给例行检查排序。作者没有提出新模型，而是用 CDPH 公开的训练/测试数据与公共检查记录审视特征、指标和假设，给出五项发现：检查员簇特征影响最大且有失公平；时间不变假设可能不成立；2015 年后命中率上升未必来自模型；命中率不是理想指标；特征集不够丰富。例如 Purple 检查员簇的系数为 1.555（赔率比 4.735），测试集中上次由该簇检查的 99 家店全部被排进前 234 次检查（前 14.3%）（Finding 1）。已读全文正文（§1–5）。

[原文](https://arxiv.org/abs/1910.04906)

版本：arXiv:1910.04906v1（2019-10-10），AAAI Fall Symposium 2019（AI in Government and Public Sector），8 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF p.1 |
| 方法 | §2.1–2.3（数据、特征、模型、指标），Tables 1–3、Figure 1，PDF pp.1–4 |
| 评测 | §2.3、§3 Findings 1–5，Figures 2–4，PDF pp.3–6 |
| 局限 | §3 Findings 2–5、§4.2、§4.4，PDF pp.5–7 |
