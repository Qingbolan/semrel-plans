# Li et al. — Weak-to-Strong Prompts with Lightweight-to-Powerful LLMs for High-Accuracy, Low-Cost, and Explainable Data Transformation

本文提出 MegaTran，用代码生成完成单列数据转换。微调后的 Llama3-8B 先把用户松散的说明（弱提示）改写为“算子类型 + 任务描述”的强提示，再由 GPT-4o 或 GPT-4o-mini 生成 Python 代码，并经过错误清单反思和按需检索（Lazy-RAG）修正。在 5 个数据集共 211 个任务上，GPT-4o 版本的准确率为 65.2%–78.0%，消融显示弱转强提示模块贡献最大。已读全部正文与表格；未检查 artifact 仓库。

[原文](https://www.vldb.org/pvldb/vol18/p2371-tang.pdf)

版本：PVLDB 18(8): 2371–2384, 2025，doi:10.14778/3742728.3742734，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，PDF pp.1–4 |
| method | §3–§5、Algorithms 1–2，PDF pp.4–8 |
| evaluation | §6、Tables 2–5、Fig.9，PDF pp.8–12 |
| limitations | §6 Exp-1 说明、§8，PDF pp.10、12 |
