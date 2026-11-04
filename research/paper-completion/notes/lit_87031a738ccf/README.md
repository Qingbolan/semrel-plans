# Lei, Meng et al. — DAComp: Benchmarking Data Agents across the Full Data Intelligence Lifecycle

DAComp 是一个 210 题的数据智能体基准，覆盖仓库级数据工程（DE-Arch 30、DE-Impl 30、DE-Evol 50）与开放式数据分析（DA 100），另有题目集相同的中文版 DAComp-zh。确定性 DE 任务在 DuckDB 中按表/节点做执行比对，开放式 DA 与 DE-Arch 由 Gemini-2.5-Flash 依据分层 rubric（DA 另加 GSB 对比）打分。主要结果：DE-Evol 严格成功率最高仅 20%（GPT-5），DA 总分最高约 50.84（Table 5）。

已阅读正文 §1–5 及附录 A.1、E、F；未逐项审计附录 B–D 的扩展表格与案例。

[原文](https://arxiv.org/abs/2512.04324)

版本：arXiv:2512.04324v1（2025-12-03），41 页（正文 pp.1–12，参考文献 pp.13–15，附录 pp.16–41）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.1，PDF pp.1–3 |
| method | §2.2–2.4、Tables 1–2，PDF pp.3–6；附录 A.1、E.1–E.3，pp.16–17、34–39 |
| evaluation | §3、Tables 3–10、Figures 4–9，PDF pp.6–11 |
| limitations | 附录 F.1–F.4，PDF pp.40–41；正文未设独立局限章节 |
