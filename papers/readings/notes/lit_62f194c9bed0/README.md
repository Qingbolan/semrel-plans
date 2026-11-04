# Tang et al. — ST-Raptor: LLM-Powered Semi-Structured Table Question Answering

ST-Raptor 面向 Excel 等含层级表头、合并单元格和嵌套子表的半结构化表格问答：先用 VLM 识别表头、按规则切分子表并以 DFS 构造“层级正交树”（HO-Tree），再把问题分解为子问题、生成树操作流水线执行，并以前向约束检查和后向“由答案反推问题”验证可靠性。作者同时发布 SSTQA（102 张真实表、764 个问题）；ST-Raptor（DeepSeek-V3）在 SSTQA 上准确率 72.39%，GPT-4o 为 66.45%（Table 5）。已阅读正文 §1–9 与 Table 8 案例；pp.10、12 已渲染核对 Tables 4–7。

[原文](https://arxiv.org/abs/2508.18190)

版本：arXiv 2508.18190v3（2025-09-02），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1–2.3、Fig. 1–2、Tables 1–2，PDF pp.1–5 |
| 方法 | §3–6、Algorithm 1、Figs. 3–6、Table 3，PDF pp.5–9 |
| 评测 | §7.1–7.6、Tables 4–8、Fig. 7，PDF pp.9–13；pp.10、12 已渲染核对 |
| 局限 | §7.6 末段“Regarding limitations”、§7.4 流水线错误分析，PDF pp.12–13 |
