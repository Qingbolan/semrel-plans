# Chen, Fan et al. — Automatic Database Configuration Debugging using Retrieval-Augmented Language Models (Andromeda)

Andromeda 把 DBMS 配置调试表述为：给定自然语言问题与数据库，诊断相关 knob 子集并推荐取值。它用对比学习对齐历史问答与手册的嵌入，以 LLM 逻辑链合成训练数据，并用 STL+MAD 检测异常遥测后转成文本，一并作为 RAG 上下文。

在 MySQL Run 的 100 个可运行问题上，专家判定的 SuccessRate 为 0.79（GPT-3.5）/0.76（GPT-4），直接提示为 0.37/0.43。DOI 落地页（ACM DL）未下载，读的是 OpenAlex 指向的 arXiv v2；已读正文 §1–7 与附录案例。

[原文](https://doi.org/10.1145/3709663)

版本：arXiv:2412.07548v2（2025-01-17），19 页；PACMMOD 正式版 DOI 10.1145/3709663 的开放预印本，页眉含 ACM 2836-6573/2025/1-ART013 信息。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–3 |
| method | §3–5、Figs.3–6，PDF pp.3–9 |
| evaluation | §6、Tables 1–9、Figs.9–11，PDF pp.9–14 |
| limitations | §6.1 Runnable 设定说明、§7、附录案例 Improvement，PDF pp.9、14、17 |
