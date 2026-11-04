# 评测与边界

**对比对象**（§5.1，p.10）：GPT-3.5（text-davinci-002，175B）vs Table-GPT-3.5；ChatGPT（内部版 text-chat-davinci-002）vs Table-ChatGPT。只做“调优前后”成对比较，不与 TaBERT、TURL、Ditto 等专用表格模型或提示工程方法比较。

**实验 1（主结果）**：104 组比较中调优模型胜 98、平 3、负 3（§5.2，p.12；正文写作“Table 4”，实际指 Table 3）。部分数据集结果如下（Table 3，p.11）：

| 数据集 | GPT-3.5 零样本 | +table-tune | ChatGPT 少样本 | +table-tune |
|---|---|---|---|---|
| Spreadsheets-CF（列查找） | 0.461 | 0.713 | 0.803 | 0.848 |
| Wiki（表格问答） | 0.45 | 0.486 | 0.520 | 0.527 |
| iTunes-Amazon（实体匹配） | 0 | 0.788 | 0.833 | 0.929 |
| WebTables-Real（错误检测） | 0.077 | 0.643 | 0.364 | 0.684 |
| DBLP-ACM（实体匹配） | 0.402 | 0.847 | 0.961 | 0.938 |

零样本实体匹配和错误检测的增益最大；问答提升很小；DBLP-ACM 少样本两个基座都略降（Table 3）。

**实验 2（下游优化）**：在 Efthymiou CTA 上用 200 条标注做提示选择，top-5 模板 Table-GPT-3.5 都更高（Figure 10）；在 CTA 与 WikiTableQuestions 上做单任务微调，同等数据量下 Table-GPT-3.5 更好（Figure 11，p.12）。

**实验 3（敏感性与消融）**：只训练 1 个任务会低于原 GPT-3.5，任务数增加后上升（Figure 12）；Ada/Babbage/Curie 在未见任务上几乎没有收益，175B 才明显（Figure 14）；Markdown/CSV/JSON 的 Overall 为 0.705/0.687/0.672（Table 5）。消融 Overall：完整 0.705，NoSyn 0.608，NoColPer 0.702，NoPromptVar 0.693，NoCOT 0.701（Table 6，p.13）。

**边界**：没有局限章节；未报告方差、显著性或推理成本；Figure 12–13 的正文编号与图号有错位（文字称 Figure 13 为任务数）（阅读者分析）。NoCOT 在未见任务上为 0.666，略高于完整模型的 0.663，原文只讨论了见过的任务（阅读者分析）。

依据：§5.1–5.5、Tables 3–6、Figures 10–15，PDF pp.10–14。
