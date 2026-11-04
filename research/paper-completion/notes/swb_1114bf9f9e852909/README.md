# Lu, Zhang et al.（快手）— VLM as Policy: Common-Law Content Moderation Framework for Short Video Platform

本文提出快手的短视频内容审核框架 KuaiMod，并发布 1,000 条视频的审核基准。方法借"判例法"思路：用用户反馈与人工审核得到的案例，经 YuanQi-20B 生成 Tag2CoT/CoT2Tag 状态转移推理数据，对 YuanQi-7B 做 SFT 与 mistake-oriented DPO，上线后再按用户反馈做每日 DPO 更新（RLUF）。关键结果：基准上 KuaiMod-7B 总体准确率 0.9240，高于所有基线（Table 2）；线上 A/B 中举报率下降 24.34%（NEBULA）与 18.98%（Featured）（Table 4）。已读正文 12 页及附录 A。

[原文](https://arxiv.org/abs/2504.14904)

版本：arXiv:2504.14904v1（2025-04-21），20 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1–3.2，PDF pp.1–4 |
| 方法 | §3.3、§4.1–4.4，PDF pp.5–9；附录 A.1，pp.17–18 |
| 评测 | §5–6，Tables 1–5，PDF pp.9–12；附录 A.2，pp.19–20 |
| 局限 | 无独立局限章节；§3.2、§5.1.2、§6.2 中的口径说明，PDF pp.4、9、12 |
