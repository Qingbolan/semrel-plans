# Liu et al. — SUQL: Conversational Search over Structured and Unstructured Data with Large Language Models

本文提出 SUQL：在 SQL 中加入 ANSWER 和 SUMMARY 两个自由文本原语，由少样本 LLM 把对话解析成 SUQL，再交给带检索、谓词排序和惰性求值优化的编译器执行。在 HybridQA 测试集上达到 59.0 EM / 68.4 F1，比训练过的 SOTA 低 8.9 EM、7.1 F1；在自建 Yelp 餐厅数据上，对话轮次准确率为 90.3%，线性化基线为 63.4%。已读正文全部章节、局限章节和附录中的超参数、众包及提示词。

[原文](https://arxiv.org/abs/2311.09818)

版本：arXiv:2311.09818v2（2024-03-13），21 页（正文 9 页 + 参考文献与附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–4 |
| 方法 | §3–5、Tables 1–2，PDF pp.3–6；附录提示词 Tables 6–8，PDF p.14 |
| 评测 | §6、Tables 3–5，PDF pp.6–9 |
| 局限 | Limitations 章节，PDF p.9；§6.1 错误分析，PDF pp.7–8 |
