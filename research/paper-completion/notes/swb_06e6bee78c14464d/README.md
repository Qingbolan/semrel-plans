# Bergmann, Batzner, Fauser, Sattlegger, Steger（MVTec）— Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization

本文把图像异常分为“结构异常”（划痕、凹陷、污染等新局部结构）和“逻辑异常”（违反数量、位置、组合等约束，如多一个零件、标签与果汁不符），发布同时覆盖两类异常的工业检测数据集 MVTec LOCO AD（3,644 张图、5 个类别、89 种缺陷），提出容忍定位歧义的 sPRO 指标，以及局部+全局双分支的无监督方法 GCAD。GCAD 在 LOCO 上的结构/逻辑平均 sPRO 为 0.701，高于 Student–Teacher 的 0.626（Table 5）。已阅读全文 §1–§7 与附录 A–D 正文；表格内容取自 Springer 文章的表格子页面。

[原文](https://link.springer.com/article/10.1007/s11263-022-01578-9)

版本：International Journal of Computer Vision 130:947–969（2022，开放获取，CC BY 4.0），期刊 23 页；保存的是 Springer 开放获取全文 HTML（无 PDF 页码，以下用章节、表、图定位）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1、Figures 1–2 |
| 方法 | §3.2–3.4（sPRO）、§4（GCAD）、§5.2，Figures 4–5、7 |
| 评测 | §5.3–5.5、§6、Tables 1、3、5、8（表格子页面已解析核对） |
| 局限 | §5.3 失败案例（Fig. 11）、§5.4 阈值敏感性、§7 |
