# Jin et al. — LogicAD: Explainable Anomaly Detection via VLM-based Text Feature Extraction

LogicAD 是一个免训练的单样本（one-shot）逻辑异常检测方法：用 GPT-4o 等自回归多模态模型（AVLM）配合 Guided CoT 提示和 GroundingDINO 区域裁剪，把图像转成文本描述；再把描述整理为 JSON，用嵌入余弦距离打分；同时转换为一阶逻辑公式，交给 Prover9 判断是否违反"正常规格"并给出最小解释。MVTec LOCO AD 逻辑异常部分的平均 AUROC 为 86.0、F1-max 为 83.7，分别比 AnomalyMoE 高 18.1、4.6 个点。已阅读 arXiv v2 正文全部内容；正文引用的附录 A.1–A.6 不在本 PDF 中，未阅读。

[原文](https://arxiv.org/abs/2501.01767)

版本：arXiv:2501.01767v2（2025-01-08），9 页（正文 7 页 + 参考文献，不含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、Introduction、Related Work，PDF pp.1–2 |
| 方法 | LogicAD 各节（Text Feature Extraction、Format Embedding、Logic Reasoner），Figs. 2–5，PDF pp.3–5 |
| 评测 | Experiments and Results、Tables 1–6，PDF pp.5–7；Table 1 已渲染核对 |
| 局限 | Limitations，PDF p.7 |
