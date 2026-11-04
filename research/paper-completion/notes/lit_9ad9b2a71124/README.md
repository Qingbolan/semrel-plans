# Zhang et al. — DeepAnalyze: Agentic Large Language Models for Autonomous Data Science

DeepAnalyze-8B 是专门为数据科学训练的 agentic LLM，基座为 DeepSeek-R1-0528-Qwen3-8B。它用五种动作标记与数据环境交互，训练分两阶段：单能力微调，以及多能力 agentic 训练（冷启动 SFT + GRPO）；训练数据约 500K，来自蒸馏与多 agent 合成的轨迹。在 12 个基准上评测，DataSciBench 总分 61.11（仅次于 GPT-4o），DABStep 总体 38.88。已读正文与附录 A，结果表已渲染核对；附录 C 案例只浏览了部分。

[原文](https://arxiv.org/abs/2510.16872)

版本：arXiv:2510.16872v1（2025-10-19），23 页（正文 12 页 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–2，PDF pp.1–4 |
| method | §3.1–3.4、Algorithm 1、Figure 3–6，PDF pp.4–8 |
| evaluation | §4–5、Tables 1–8、Figure 7–8，附录 A，PDF pp.7–11、16–17；pp.7–11 结果表已渲染核对 |
| limitations | 原文无局限章节；§6 Conclusion，PDF pp.11–12（局限由阅读者从实验表推断） |
