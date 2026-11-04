# 贡献与评价

| 贡献 | 内容 | 位置 |
|---|---|---|
| 全文人工标注 | 106 篇论文全文，24,518 实体、12,083 关系，平均每篇 114 条关系；SciERC 每篇约 9.4 条 | §3.3、Table 1 |
| 细粒度关系集 | 9 种关系，区分 TRAINED-WITH / EVALUATED-WITH，用 SUBTASK-OF / SUBCLASS-OF 表达层级 | §3.2、Table 2 |
| OOD 测试 | 6 篇 2023–2024 年论文，其中 4 篇为前 100 篇未覆盖的 AI4Science 主题 | §3.1 |
| 基线 | 3 个监督方法 + 3 个 LLM 的零/少样本 pipeline 与 joint 抽取，含标注指南提示消融 | §4–5 |

阅读者分析：前 100 篇的实体标注来自 SciDMT 验证集再复核，实体一致性 kappa 94.2% 部分源于此；真正从零标注的只有 6 篇 OOD 文档（实体 kappa 74.1%）。OOD 集只有 6 篇、582 条关系，个别关系（TRAINED-WITH 仅 2 条）统计意义有限。实体只有三类且不含嵌套实体，作者在 Limitations 中承认。

依据：[EMNLP 2024，pp.13083–13100](https://aclanthology.org/2024.emnlp-main.726.pdf)，§1、§3，PDF pp.2–4；附录 A.3 Table 7，p.13；Limitations，p.9。
