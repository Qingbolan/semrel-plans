# Pesaran zadeh et al. — Text2Chart31: Instruction Tuning for Chart Generation with Automatic Feedback

本文用 GPT-3.5-turbo/GPT-4 分层生成 Text2Chart31 数据集（覆盖 31 种 Matplotlib 图类型、11,128 条描述/代码/图像元组，其中 8,166 条带数据表和推理步骤），并提出 SFT 后接 PPO 的指令微调方法。

PPO 使用自动构造的偏好奖励和"代码→描述"循环一致性奖励。描述生成图表任务中，SFT+RL 的 Code Llama Instruct-13B 总执行错误率为 9.21%，低于所列 GPT-4o（13.00%）等闭源模型。已阅读正文 §1–7、Limitations、Ethics 与附录 A–B；附录 C–E 的流水线提示与人工评测细节未逐项审计。

[原文](https://arxiv.org/abs/2410.04064)

版本：arXiv:2410.04064v2（2025-02-17），22 页；文中注明 Text2Chart31-v2 为 camera-ready 发布版本，本文实验用的是 v1 数据集。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1，PDF pp.1–2 |
| 方法 | §2.1–2.3、§3.1–3.2、Figure 2、Algorithm 1，PDF pp.2–5 |
| 评测 | §4、Tables 2–4、Figure 3，PDF pp.5–8；附录 A.2 Table 5，PDF p.13 |
| 局限 | Limitations、Ethics Statement，PDF p.9 |
