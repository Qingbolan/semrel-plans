# Fučka, Zavrtanik, Skočaj — SALAD – Semantics-Aware Logical Anomaly Detection

SALAD 是一种工业图像逻辑异常检测方法：在局部外观分支（EfficientAD）和全局分支之外，新增一个直接在“对象组成图”（部件分割图）上判别式训练的组成分支；组成图由 DINO 聚类加 SAM-HQ 掩码生成伪标签，再训练 UNet 得到，无需人工标注。在 MVTec LOCO 上图像级 AUROC 达 96.1%，比此前不使用监督掩码的最佳方法 PUAD（93.1%）高 3.0 个百分点。已阅读全文正文；补充材料（定位结果、更多聚类数）未获取，未阅读。

[原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Fucka_SALAD_--_Semantics-Aware_Logical_Anomaly_Detection_ICCV_2025_paper.pdf)

版本：ICCV 2025 CVF Open Access 版（与录用版一致，仅加水印），pp.21843–21852，10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3，PDF pp.3–5 |
| 评测 | §4–5、Tables 1–5，PDF pp.5–8 |
| 局限 | §5 推理速度、§6，PDF p.8；无独立局限章节 |
