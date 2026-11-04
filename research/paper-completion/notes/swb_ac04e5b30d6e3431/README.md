# Fan et al. — Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task

本文为多模态大模型构建约 22 个工具的 Video Toolkit（时间类、空间类、通用类），并提出 STAR 框架：强制 LLM 规划器交替调用时间与空间工具、通用工具只作为最后手段，以逐步定位回答问题所需的"3D 感兴趣区域"，避免规划器直接调用通用视频问答模型的"工具链捷径"。以 GPT-4o 为规划器、约 30 帧输入时，VideoMME 准确率 70.0%（比 32 帧 GPT-4o 高 8.2 点），LongVideoBench 验证集 57.2%（高 4.6 点）。已读正文、附录与 checklist。

[原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbdd9525c5ecd3a03fee43d8fd64bd83-Abstract-Conference.html)

版本：NeurIPS 2025 会议论文（Advances in Neural Information Processing Systems 38），含 NeurIPS checklist 与附录，31 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1，PDF pp.1–3 |
| method | §3、Algorithm 1、Figs.2–3，pp.4–6；附录 A，pp.24–25 |
| evaluation | §4、Tables 1–5，pp.6–9；附录 B–I、Tables 6–10，pp.25–31 |
| limitations | §5，p.10；checklist 第 2、7 项；附录 H |
