# Cheng, Xie et al.（HKU / UW 等）— Binding Language Models in Symbolic Languages（Binder）

Binder 是一个免训练的神经–符号框架：用 Codex 把问题解析成 SQL 或 Python 程序，并在程序中嵌入统一的语言模型 API 调用 `f(问题; 列)`，用来处理原语言语法覆盖不了的部分（如判断国家是否在北美）；执行时再由 Codex 实现这些 API 调用，结果回填给标准解释器。仅用 14 个上下文示例，在 WikiTableQuestions 测试集上执行准确率 64.6%，在 TabFact 小测试集上 85.1%（加检索选例 86.0%）（Tables 1–2）。已阅读正文 §1–§6 与附录 A.2、C.4。

[原文](https://arxiv.org/abs/2210.02875)

版本：arXiv 2210.02875v2（2023-03-01，ICLR 2023 会议版），27 页（正文约 9 页 + 参考文献与附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2 任务定义，PDF pp.1–3 |
| 方法 | §2.1–2.3、附录 A.2 与 Table 8，PDF pp.3–4、18 |
| 评测 | §3–§4、Tables 1–7、Figures 2–3，PDF pp.4–9；Tables 1–4、6–7 已用版面文本核对 |
| 局限 | 无独立局限章节；§3.2 时间成本、§4.2 错误分析、附录 C.4，PDF pp.5–7、23 |
