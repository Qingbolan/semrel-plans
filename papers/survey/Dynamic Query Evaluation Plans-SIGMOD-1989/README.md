# Graefe, Ward（Oregon Graduate Center）— Dynamic Query Evaluation Plans

嵌入在应用程序里的查询通常在编译时优化一次，但谓词中的程序变量（如金额门槛）、可用内存和数据库状态在运行时才知道，固定计划可能长期次优。本文提出动态查询计划：优化器预先准备若干等价计划片段和一个决策过程，访问模块被激活时再按实际参数选择并链接；在 Volcano 中以 choose-plan 算子实现。

在 13,229 条站点记录的账单数据上，同一查询的索引计划与扫描+哈希连接计划成本相差悬殊：只有 1 条结果时索引计划快约 10 倍，全部记录命中时慢 3 倍以上（Table 1）。自动生成多计划的 EXODUS 优化器扩展仍是进行中工作。

[原文](https://sigmodrecord.org/?download_id=10724&smd_process_download=1)

版本：SIGMOD 1989，SIGMOD Record 18(2)，pp.358–366（DOI 10.1145/67544.66960）。2026-11-04 用全文 PDF（SHA-256 `c128847cda52926d78c7a176dfafc2a38ec498664701f1b65bcd7ab18a57e32e`）复核 §1–8 与 Table 1 数值；未复现实验。
