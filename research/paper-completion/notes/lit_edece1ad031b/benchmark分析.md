# benchmark

**被测对象**：13 个 LLM/VLM，包括 Claude-Sonnet-4.5、GPT-5.2、Gemini-3-Pro、MiMo-V2-Pro/Flash、GLM-4.6V、MiniMax-M2.7/M2、DeepSeek-V3.2、Qwen3-VL-30B、Ministral-3-14B 等（§4.1，p.6）。没有非 LLM 基线。

**评委**：先比较 GPT-5.1、Claude-Haiku-4.5、Doubao-Seed-1.8，三者均不在被测名单内；以三名数据科学博士生对 Gemini-3-Pro 全部 641 条轨迹的共识为参照，前两者整体 MSE 为 0.855、0.896，Doubao 为 4.530 被剔除；最终分取两个评委的平均（Table 4，p.8）。双评委均值与人类共识 Pearson 0.872、MAE 0.364、Spearman 0.895（Table 5，p.9）；两评委在 8,314 个输出上 Pearson 0.813、MAE 1.004（Table 6，p.9）。

**主要结果**：
- 总分：Claude-Sonnet-4.5 8.164 > MiMo-V2-Pro 7.912 > GPT-5.2 7.713 > MiniMax-M2.7 7.699 > Gemini-3-Pro 7.309 > Grok-4.1-fast 7.254；Qwen3-VL-30B 5.324、Ministral-3-14B 5.182（§5，p.7）。
- 领域：CV、NLP 平均 6.31、6.25，最弱；任务类型中预测与预报 6.03、模型训练与优化 6.49 最低（pp.7–8）。
- 成本：Claude-Sonnet-4.5 约 $1.08/题，MiMo-V2-Flash 约 $0.007/题（p.8，按 OpenRouter 价格）。
- 多模态消融：3 个视觉模型 × 4 类（DA/CV/PAD/EDA）全部提升，相对增益 2.04%–11.30%，90% 配对 bootstrap 区间多数下界为 0.0，PAD 中有两组下界为负（Table 2，p.6）。
- 权重敏感性：各权重下排名 Spearman ≥ 0.940，只有仅看代码时榜首变化（Table 3，p.8）。
- 附录 K：8,308 条不完美轨迹的评委理由中，需求覆盖不全 52.1%、可视化/结果解读 41.8% 最常见（Table 15，p.34）。

**边界**：LLM 随机性与人类主观性；Kaggle 来源存在训练数据污染风险；不覆盖需求获取、数据治理与生产部署；人工校准只覆盖一个被测智能体；多模态消融只有三个模型族（Limitations，pp.9–10）。阅读者分析：多模态增益的区间很窄且贴近 0，单题提升幅度有限；分数是 0–10 的评委打分，不同于精确匹配准确率，不宜与 DSBench 等封闭式基准的数字直接比较。

依据：[arXiv:2601.13591v3，35 页](https://arxiv.org/pdf/2601.13591)，§4–5、Limitations、Tables 2–6、附录 K，PDF pp.5–10、34。
