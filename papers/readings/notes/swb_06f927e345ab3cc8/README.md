# Yang et al. — BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards

BLM-Guard 是快手团队提出的短视频商业广告审核框架：先用规则驱动的交错模态思维链（ICoT）数据合成做 SFT 冷启动，再用 GRPO 强化学习结合规则奖励、格式奖励和由裁判模型给出的自适应批评奖励（SCA-R）进行优化，骨干为 Qwen2.5-VL-7B。论文同时提出带“严重度—场景—违规类型”三级标签的 BLM-Guard Benchmark；在自建基准上，严格准确率 0.914、风险类 F1 0.969，高于所列开源基线。全文共 9 页，已全部阅读；正文未给出数据集规模、划分或独立局限章节。

[原文](https://arxiv.org/abs/2602.18193)

版本：arXiv:2602.18193v2（2026-02-23），9 页，页脚标注 AAAI 2026 版权。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Introduction、Task Definition，PDF pp.1–2 |
| 方法 | Methodology（冷启动、奖励设计、GRPO）、Algorithm 1，PDF pp.2–5 |
| 评测 | Experiments、Tables 1–2、Figure 3，PDF pp.6–7 |
| 局限 | 原文无独立局限章节；边界由阅读者根据 pp.2、6–7 整理 |
