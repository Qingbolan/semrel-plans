# Pourreza & Rafiei — DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction

DIN-SQL 把 text-to-SQL 拆成模式链接、查询分类与分解、按类别生成 SQL、自我修正四个提示模块，全部用少样本/零样本提示实现，不做微调。论文报告 GPT-4 版本在 Spider 隐藏测试集上执行准确率 85.3%，BIRD 隐藏测试集 55.9%，均为当时最高。已阅读正文 §1–7 及附录 A 的提示结构；未逐条核对附录中的全部提示示例。

[原文](https://arxiv.org/abs/2304.11015)

版本：arXiv 2304.11015v3（2023-11-02，NeurIPS 2023 版），34 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3（含 Figure 1 错误分布），PDF pp.1–4；Figure 1 已渲染核对 |
| 方法 | §4.1–4.4，PDF pp.4–6；附录 A，PDF pp.15–34 |
| 评测 | §5、Tables 2–5、Figure 4，PDF pp.6–10 |
| 局限 | §7，PDF p.10 |
