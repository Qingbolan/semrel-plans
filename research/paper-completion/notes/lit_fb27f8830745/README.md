# Gulati et al. — Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing

BRTR（PwC）把 FRTR 的单次多模态混合检索改为 LLM 迭代调用检索工具，并加入规划器-执行器 DAG 处理组合式表格工作流。在 FRTR-Bench 上前沿模型达 0.99（单次 FRTR 最佳 0.74），FINCH 上达 95.3%；消融显示去掉 agent 循环为 0%、去掉规划器降至 68%。已阅读全文正文与附录 A–D。

[原文](https://arxiv.org/abs/2603.06503)

版本：arXiv:2603.06503v1（2026-03-06，cs.CL），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | 摘要、§1–2，PDF pp.1–4 |
| method | §3.1–3.3、Algorithm 1，附录 D，PDF pp.4–5、14–15 |
| evaluation | §4.1–4.5、Tables 1–5，附录 A–C，PDF pp.5–10、13–14 |
| limitations | 原文无独立局限节；§4.2 讨论、§4.3 失败分析、§4.5 成本、附录 B，PDF pp.8–10、14 |
