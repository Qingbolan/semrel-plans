# Duan, Chen, Hu, Wang et al. — Docopilot: Improving Multimodal Models for Document-Level Understanding

本文构建文档级多模态问答训练集 Doc-750K（758K 问答、3.1M 图像、5.2B 文本 token，来源 Sci-Hub、arXiv、OpenReview），并在 InternVL2 上以混合数据 SFT 一个 epoch 得到 Docopilot-2B/8B，不依赖检索即可处理多页文档。

Docopilot-8B 在 MM-NIAH 总分 61.8，比 InternVL2-8B 高 19.9 分，超过 InternVL2-26B；在 MMLongBench-Doc 上 Acc 28.8，高于 Gemini-1.5-Pro 的 28.2。已阅读 PDF pp.1–8 正文，补充材料未纳入。

[原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf)

版本：CVPR 2025 CVF Open Access 版（与录用版一致，仅加水印），会议页码 4026–4033，PDF 共 12 页（正文 8 页 + 参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，PDF pp.1–2 |
| method | §3–§4，Figs.2–4、Tables 1–3，PDF pp.3–6 |
| evaluation | §5，Tables 4–7，PDF pp.7–8 |
| limitations | §6 结论中的未来工作，PDF p.8（无单列局限章节）；阅读者从表格补充 |
