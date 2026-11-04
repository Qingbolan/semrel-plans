# 具体用例

一个就业法庭判决可能同时处理不公平解雇、歧视、拖欠工资、违约等多个诉求。系统对每个诉求单独预测，例如诉求描述 “discrimination due to age” 加上案件事实摘要，输出 Win/Loss/Other。

泄露线索的例子分两类。显式：判决写明诉求 “succeeds” 或 “fails”，或 “judgment for claimant”“was unfairly dismissed”。隐式：事后叙述用语，如 “respondents failed to”“claimant failed to”“sought to amend”。系数分析中，“unauthorised deduction from” 偏向 Win，“claimant failed to” 偏向 Loss。

阅读者分析：在语义查询中若要求“按事实预测诉求结果”，应把事实摘要视为可能被污染的输入，在评测时分开报告 Clean/Leaky 子集。

依据：[arXiv:2607.04261v2](https://arxiv.org/pdf/2607.04261v2)，§1，pp.3–4；§2.1，p.6；§2.4，p.8；§3.2–3.3，pp.10–11。
