# Santosh et al. — ECtHR-PCR: A Dataset for Precedent Understanding and Prior Case Retrieval in the European Court of Human Rights

本文基于欧洲人权法院（ECtHR）英文判决构建先例检索（PCR）数据集：查询只用案件事实部分，候选池为查询日期之前的全部判例，相关性来自判决推理部分引用的先例。基准显示 BM25 与层次化稠密检索都偏低（最佳 Recall@1000 约 67%），难负例采样不如随机负例，稠密模型随时间退化。已阅读全文（正文 §1–7），核对 Tables 1–5。

[原文](https://aclanthology.org/2024.lrec-main.486)

版本：LREC-COLING 2024，pages 5473–5483，ACL Anthology 2024.lrec-main.486 PDF，11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§4 任务定义，PDF pp.1–2、5 |
| 方法（数据构建与模型） | §3.1–3.3、§4.1–4.2，PDF pp.3–6 |
| 评测 | §5、Tables 3–5、Fig.2，PDF pp.6–8 |
| 局限 | §5.6、§7，PDF pp.8–9 |
