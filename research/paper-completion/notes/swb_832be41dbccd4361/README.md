# Li, Liang, Xie et al. — DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces

DataSpace 是数据代理基准：410 个中英跨语言任务，共 7,439 个工件、15.01 GB，涵盖 CSV、JSON、SQLite、Markdown、PDF 和视频。代理只拿到问题和任务本地工作区，须返回完整表格结果，由确定性评测器判分。任务由 DataSpace-Builder 从 EHRSQL 和 BULL 两个 Text-to-SQL 基准转换而来，并经 11 名领域专家复核；它也是 KDD Cup 2026 的官方评测基准。固定 DataSpace-Agent 时最佳骨干 Grok 4.5 准确率为 66.34%；固定骨干 MiMo-V2.5 时，不同 harness 之间相差 15.36 个百分点。已读正文 §1–7 及附录 A（选读构造细节）、A.7–A.8、B；论文没有单独的局限性章节。

[原文](https://arxiv.org/abs/2608.03451)

版本：arXiv:2608.03451v1（2026-08-04），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，Table 1，PDF pp.1–3 |
| method | §4、Figure 2，PDF pp.3–6；附录 A.1–A.6，pp.10–21（选读） |
| evaluation | §5–6、Tables 2–3、Figures 3–7，PDF pp.6–8；附录 A.7–A.8，pp.21–24 |
| limitations | 无专门局限节；§6.1 排除系统说明、§6.4 “描述性非因果”声明（PDF pp.7–8）、附录 B 竞赛协议差异（p.24） |
