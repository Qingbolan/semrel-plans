# Bizarro, Babu, DeWitt, Widom（UW–Madison / Stanford）— Content-Based Routing: Different Plans for Different Data

传统优化器为一个查询选一个计划，但数据的不同子集可能统计性质差别很大。本文提出基于内容的路由（CBR）：在 Eddies 中抽样画像每个算子，用信息增益比（gain ratio）找出与算子选择率相关的“分类属性”，把元组按属性取值分成类，每类用各自的选择率估计决定算子顺序；学习在执行中持续进行，不需离线训练。

在 TelegraphCQ 中实现后，与只看全局选择率的 SBR 相比：合成星型流上路由调用最多减少 67.8%，执行时间最多改善约 35%；真实传感器数据 Lab 上改善较小（50 个随机查询平均路由调用 −8%、执行时间 −5%）；路由加学习的总开销约占执行时间的 4–5%（§6–7）。

[原文](https://www.vldb.org/conf/2005/papers/p757-bizarro.pdf)

版本：VLDB 2005（Trondheim），pp.757–768。2026-11-04 用全文 PDF（SHA-256 `037a258ab7db13e930f64d8a970dc9d72dd6c1c6ae9bba67c043ba3bb3c8fdf1`，与会议版一致）复核 §1–8 与实验数值；未复现实验。

阅读者分析：本文直接否定“同一查询的不同记录走不同路径、且路径在线学习”本身具有新颖性。（阅读者分析）
