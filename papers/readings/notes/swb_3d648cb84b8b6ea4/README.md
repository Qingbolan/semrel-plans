# Jiang et al. — AnomalyClaw: A Universal Visual Anomaly Detection Agent via Tool-Grounded Refutation

AnomalyClaw 是一个免训练的跨领域视觉异常检测（VAD）智能体：VLM 在最多 5 轮中提出候选异常特征，调用 13 个工具逐一与正常参考图对照“反驳”，再与一次 Direct VLM 判断按 0.5:0.5 融合。作者同时构建 12 个领域的 CrossDomainVAD-12 基准（测试 1,418 项），在 GPT-5.5、Seed2.0-lite、Qwen3.5-VL-27B 上相对单次 Direct 的宏平均 AUROC 分别提升 +6.23、+7.93、+3.52 pp。已阅读正文全部章节及附录 A、C、R、S、U；附录 D–Q 的旧路由架构与逐表细节只做浏览。

[原文](https://arxiv.org/abs/2605.10397)

版本：arXiv:2605.10397v1（2026-05-11），30 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–3 |
| 方法 | §3.1–3.4、Figure 2，PDF pp.4–6；附录 S（工具来源），pp.28–29 |
| 评测 | §4.1–4.6、Tables 1–3，PDF pp.6–9；附录 A、C、R、U，pp.15–17、27–29 |
| 局限 | §4.5 Limitations，p.9；附录 R “Limitations of this section”，p.28；附录 S “What this section does not rule out”，p.29 |
