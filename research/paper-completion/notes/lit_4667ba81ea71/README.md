# Ye et al. — Large Language Models are Versatile Decomposers: Decomposing Evidence and Questions for Table-based Reasoning

本文提出 Dater：用 Codex 少样本提示先把大表裁成与问题相关的子表（证据分解），再用“解析—执行—回填”把复杂问题拆成带 SQL 执行结果的子问题（问题分解），最后由 LLM 联合推理作答。在 TabFact 小测试集上 Codex+Dater 准确率 85.6%，把分解结果注入微调模型 PASTA 后达到 93.0%，作者称首次超过人类（92.1%）。已阅读正文 §1–6 与全部结果表；第 13–16 页为参考文献。

[原文](https://doi.org/10.1145/3539618.3591708)

版本：arXiv:2301.13808v3（2023-04-27），16 页；ACM DOI 下载返回 HTML 页面而非 PDF，故以 arXiv 预印本作为全文，标题与 SIGIR 2023 版略有差异（“Decompose” vs “Decomposing”），未逐字核对正式版。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，pp.1–3、5 |
| 方法 | §4.1–4.4、Prompt 4.1–4.5、Figure 2，pp.4–7 |
| 评测 | §5、Tables 1–6、Figure 3，pp.7–12 |
| 局限 | §6 末段，p.12（正文无独立局限章节） |
