# 工作负载

**评测基准**（§3.2）：15 个，使用原测试集。

| 类别 | 基准 |
|---|---|
| 文本类文档 | DocVQA、DUDE、SlideVQA、MMLongBench-Doc |
| 网页类 | VisualMRC、InfographicVQA |
| 图表类 | ChartQA、CharXiv |
| 表格类 | TableVQA-Bench、TableBench |
| 通用 | ScienceQA、RealWorldQA |
| 数学 | MathVista、Math-Vision、MathVerse |

各基准的样本数、划分细节与指标（ANLS、F1 等）在 Tab. 8 与附录 8.2，v2 未包含，本笔记无法给出。多数基准用 LMMs-Eval 配合 GPT-4o 作为评判模型判定正误。

**训练**（§3.1）：三组基模型——Qwen2.5-VL-7B + Qwen2.5-7B/3B；MiMo-VL-7B-SFT + MiMo-7B-SFT；InternVL3-9B/8B/2B。第一阶段 SFT：在文档与非文档数据上训练 VLM（混合有无思维链数据），用 GPT-4o 与规则生成的判断标签训练判断 LLM，用前序输出与标准答案训练作答 LLM；第二阶段用 GRPO 与预训练奖励模型强化。训练数据的具体来源与规模在附录，v2 未给出。原文“11B/7B/7B VLM”的写法与所列基模型尺寸对不上，含义不清（阅读者分析）。

依据：[arXiv:2508.03404v2，10 页](https://arxiv.org/abs/2508.03404v2)，§3.1–3.3，pp.5–7。
