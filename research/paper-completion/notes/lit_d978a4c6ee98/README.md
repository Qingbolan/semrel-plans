# Ma et al. — Unifying Multimodal Retrieval via Document Screenshot Embedding

DSE 把文档截图作为统一输入，用视觉语言模型 Phi-3-vision 直接把截图编码为稠密向量做检索，省去 HTML 解析、OCR 等内容抽取。作者构建 127 万张 Wikipedia 页面截图的 Wiki-SS 回答 NQ 问题，并把 SlideVQA 改造成 5 万张幻灯片的开放域检索：DSE 在 NQ top-1 比 BM25 高约 17 点但低于同底座文本检索 Phi-3 约 4 点；在幻灯片检索上 nDCG@10 比所有基于 OCR 的文本检索高 15 点以上。已阅读正文 §1–7 和附录 A.1–A.4；未复现实验。

[原文](https://arxiv.org/abs/2406.11251)

版本：arXiv:2406.11251v2（2024-12-02），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–3 |
| 方法 | §3.2、Figure 2，PDF pp.3–4；§4.3，pp.5–6 |
| 评测 | §4–5、Tables 1–2、Figure 4，PDF pp.4–9；附录 A.1–A.2、Tables 3–4，pp.13–14 |
| 局限 | §7 Limitations，PDF pp.9–10；§5.4.3，p.9 |
