# Yi, Li et al. — ReSS: Learning Reasoning Models for Tabular Data Prediction via Symbolic Scaffold

ReSS 先在表格数据上训练决策树，取被正确预测样本的根到叶路径作为“符号脚手架”，让 GPT-4.1 依据特征、标签和路径生成逐步自然语言推理，再用这些数据对 Qwen-2.5-3B-Instruct 做全参数 SFT；另提出保持路径不变的扰动增广（含把非路径特征置为 unknown）。在 2 个医疗、3 个金融数据集上，ReSS 准确率均为最高（如 Diabetes 85.71% vs 决策树 76.62%），并用幻觉率、解释充分性和必要性评估推理忠实度。已阅读正文 §1–6 及附录 A（序列化）、D（超参与算力）、E（补充实验）；附录 B/C 的提示词和样例仅抽查。

[原文](https://arxiv.org/abs/2604.13392)

版本：arXiv:2604.13392v2（2026-05-19，NeurIPS 投稿格式预印本），55 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、§3 Notations，PDF pp.1–3 |
| method | §3.1–3.3、Fig.1，PDF pp.4–5 |
| evaluation | §4–5、Tables 1–3、Figs.2–3，附录 D–E，PDF pp.5–9、45–48 |
| limitations | §6 Conclusions（单句局限）及 NeurIPS checklist 第 2 项，PDF pp.10、49 |
