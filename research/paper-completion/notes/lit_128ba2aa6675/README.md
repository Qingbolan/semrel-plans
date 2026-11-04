# Shuai, Li, Yan, Luo, Yang — DeepVIS: Bridging Natural Language and Data Visualization Through Step-wise Reasoning

本文把思维链（CoT）引入自然语言到可视化（NL2VIS）：由文献综述与 4 位专家访谈得出五步推理（选图表类型→取数据→定粒度→排序/限制→生成 VQL），用 GPT-4o-mini 为 nvBench 自动补全推理步骤形成 nvBench-CoT，微调 Llama3.1-8B 得到 NL2VIS-CoT（测试集 All Acc 77.16%，高于 ChartGPT 73.03% 与各通用大模型），并构建可查看、可纠正推理步骤的交互界面 DeepVIS，辅以两个用例和 32 人用户研究。已阅读正文全部 9 页；数据集统计、提示词和超参数在补充材料中，未阅读。

[原文](https://arxiv.org/abs/2508.01700)

版本：arXiv:2508.01700v2（2025-09-04），IEEE TVCG 模板预印本，11 页（正文 9 页 + 参考文献）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，pp.1–2 |
| method | §3–§5，Figs.2–3，pp.3–6 |
| evaluation | §6.1–6.3，Tables 1–2、Figs.4–6，pp.6–9 |
| limitations | §6.1.3 错误分析 p.7；§7 讨论 p.9 |
