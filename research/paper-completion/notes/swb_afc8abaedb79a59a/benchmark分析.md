# 评测与边界

**被评模型**（§5.1，p.6）：闭源 GPT-4.1、4.1-mini、4o、4o-mini，Claude 3.5v2 Sonnet、3.7 Sonnet、3 Haiku；开源 Llama-4-Scout-17B、LLaVA（mistral-7B、qwen2-7B）、Qwen2.5-VL（3B/7B/32B/72B）、Gemma 3（4B/12B/27B）、InternVL3（2B–78B）；另外在 MMST 训练集上对 Qwen2.5-VL 3B/7B/32B 做 LoRA 微调。MMMT 还评测了 Llama 4 Maverick、Llama 3.2 90B 等（Table 3）。

**评测方法**（§5.2）：评审团由 DeepSeek-R1-Distill（Llama-70B）、Qwen3-32B、Phi-4-Reasoning 组成；每个被评模型生成 3 次，每次都由 3 个评审打分，共 9 次评估。ID 任务二分类判定的 Fleiss' κ 约在 0.75–0.88 之间；还用 Kendall's W 衡量序数一致性（细节见附录 D.1.1，本次未逐项核对）。

**MMST Standard 主要结果**（Table 2，p.8，三评审平均）：

| 模型 | ID 准确率 | 推理分 | MG Acc | W-Sum |
|---|---|---|---|---|
| GPT-4.1 | 43.9% | 3.01 | 3.24 | 0.82 |
| GPT-4o | 39.3% | 2.49 | 2.77 | 0.71 |
| Claude 3.7 Sonnet | 33.9% | 2.64 | 2.82 | 0.72 |
| Qwen2.5-VL-72B | 29.8% | 2.47 | 2.72 | 0.69 |
| Qwen2.5-VL-32B | 25.1% | 2.43 | 2.87 | 0.71 |
| Gemma-3-27B | 18.9% | 2.22 | 2.77 | 0.70 |
| InternVL3-78B | 22.4% | 2.24 | 2.60 | 0.67 |
| LLaVA-v1.6-mistral-7B | 7.1% | 1.34 | 2.20 | 0.55 |

**微调**（§5.4、Figure 2、附录 p.40）：Qwen2.5-VL-3B 在已见实体上的准确率由 22.3% 升至 28.4%（第 6 轮），未见实体仅 14.6%，几乎不变；32B 在已见实体上峰值为 37.6%、推理分 3.04；收益主要出现在前 4 轮。

**MMMT**（Table 3，p.10；决策准确率 % 与 Clarify/Respond 目标相关性）：

| 模型 | 零样本 Acc | 零样本 Clarify/Respond | CoT Acc | CoT Clarify/Respond |
|---|---|---|---|---|
| GPT-4o | 62.98 | 70.75 / 77.07 | 65.50 | 72.80 / 78.50 |
| Claude 3.7 Sonnet | 57.80 | 24.39 / 23.45 | 62.40 | 34.90 / 28.70 |
| LLaMA 4 Maverick 17B | 53.75 | 65.08 / 70.65 | 59.80 | 69.10 / 74.20 |
| LLaMA 4 Scout 17B | 49.81 | 61.79 / 68.67 | 56.00 | 66.40 / 71.30 |
| LLaMA 3.2 90B | 45.09 | 52.43 / 62.27 | 50.40 | 56.20 / 65.10 |
| Qwen 72B | 31.33 | 58.76 / 75.00 | 37.40 | 63.90 / 76.50 |

CoT 对所有模型都提升了决策准确率和两项相关性。

**局限**：
- 原文 §6–7 承认：没有用真实用户或用户模拟器做交互式对话评测；首轮之后的用户轮被假定为纯文本，不建模视觉追问；数据主要反映小农户和家庭园艺场景，不代表大规模商业农业；尚未覆盖土壤科学、农业工程、经济、政策等维度。
- 阅读者整理：除 ID 准确率外，其余指标都依赖 LLM 评审，而评审模型本身未在农业领域验证（正文仅报告评审间一致性，没有报告与人类专家的一致性）；金标准答案经 GPT 系列改写，可能有利于 GPT 系列被评模型；Claude 3.7 在 MMMT 上相关性极低（约 24）而决策准确率不低，原因论文未解释，可能与输出格式或解析有关。

依据：[NeurIPS 2025 D&B](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1fdee6bdc130776e489719d25d422073-Abstract-Datasets_and_Benchmarks_Track.html)，§5–7、Tables 2–3、Figure 2，PDF pp.6–10；附录 p.40。
