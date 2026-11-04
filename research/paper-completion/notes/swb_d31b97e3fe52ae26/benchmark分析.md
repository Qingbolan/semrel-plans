# benchmark

Table 1 主要结果（节选）：

| 模型 | Q-Acc | I-Acc | G-Acc | CoT |
|---|---|---|---|---|
| Gemini-2.5-pro ✩ | 0.667 | 0.470 | 0.269 | 0.584 |
| o1 ✩ | 0.608 | 0.392 | 0.186 | – |
| GPT-4o | 0.571 | 0.351 | 0.198 | 0.601 |
| Qwen-2.5-VL-32B ✩ | 0.578 | 0.353 | 0.158 | 0.328 |
| QVQ-72B ✩ | 0.575 | 0.336 | 0.067 | 0.438 |
| Claude-3.7-sonnet | 0.414 | 0.085 | 0.035 | 0.526 |
| InternVL2-8B | 0.478 | 0.194 | 0.083 | 0.194 |

（✩ 为 CoT 增强变体；o1 无 CoT 分。）

**发现**：
- 最好的 I-Acc 低于 0.5，G-Acc 低于 0.3。
- 推理增强通常有帮助：QVQ 比 Qwen2-VL-72B 高约 15%，Claude-3.7 Thinking（16k）比非思考版高约 20%；MM-Eureka 相对 InternVL2.5-8B 几乎无提升（作者推测因其微调偏重数学）。
- 推理效率：标注标准推理通常不足 100 token，Qwen-2.5-VL-32B 约 120 token，QVQ 平均超过 950 token，存在冗余。
- 多轮对话中让模型二次看图：对 Gemini-2.0-flash-thinking、Qwen2VL-72B 等初始视觉较弱的模型提升明显，对 GPT-4o、QwenVL2.5-72B 提升有限（Fig.6a，正文未给具体数值）。
- o3 展示了裁剪、缩放等主动视觉推理（仅定性）。

**局限**：正文没有局限章节，检查表称局限在补充材料中；检查表也说明未报告误差棒或显著性。

阅读者分析：多轮看图和 o3 的结论仅为图示或定性；Claude-3.7-sonnet 的 Yes-Acc 仅 0.134，说明存在强烈的"否"偏置，Q-Acc 会受答案先验影响，因此 I-Acc/G-Acc 更能反映真实能力。

依据：[NeurIPS 2025 D&B 论文集 PDF，20 页](https://proceedings.neurips.cc/paper_files/paper/2025/file/2b76873e897f3de3069b2f360c65e0c2-Paper-Datasets_and_Benchmarks_Track.pdf)，Table 1（p.6）、§4.2–4.4（pp.6–9）、检查表第 2、7 项（pp.14、16）。
