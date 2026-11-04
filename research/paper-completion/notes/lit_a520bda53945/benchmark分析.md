# 评测与边界

基线（§7.1，pp.9–10）：DABStep 榜首 Amity、第二 MultiStep；CodeAgent（DABench 使用的 ReAct 编码框架）；ReFoRCE（Spider-2.0-Lite 榜首 NL2SQL）；Palimpzest（人工编写语义流水线）；Zero-shot、Few-shot（GPT-5）；Hand-crafted（专家约两个月手写计划）。Fig.8 中还有 CombiaML。指标为答案准确率。

Fig.8 读数（p.11，已渲染核对；AgenticData 为 GPT-5 / Qwen3 版）：

| 基准 | AgenticData | 主要基线 | Hand-crafted |
|---|---|---|---|
| DABStep-hard | 72.2 / 70.6 | CombiaML 57.6、Amity 41.0、MultiStep 19.8 | 57.6 |
| DABench | 89.7 / 87.1 | CodeAgent 69.6 | 64.3 |
| Spider-2.0-Lite | 49.6 / 49.6 | ReFoRCE 35.6 | 40.2 |
| Real-Bank | 70 / 75 | ReFoRCE 50 | 80 |
| Wikipedia | 95 / 95 | Palimpzest 94 | 100 |

DABStep-easy 上 AgenticData 约 95.8，多数基线在 80–94 之间。

其他结果：五次重复的准确率波动 5%–10%（§7.2.3）；消融显示去掉画像后 Real-Bank 总体准确率降至 5%（§7.3，p.11）；Wikipedia 上在各质量阈值下成本约为 Palimpzest 的一半或更低（Fig.12，p.12）；规划耗时每题 2.8–9.8 分钟，Wikipedia 执行 390.17 秒（Table 2）。

阅读者分析与局限：
- 在 Real-Bank 与 Wikipedia 上，手工计划高于 AgenticData；Wikipedia 上对 Palimpzest 仅领先 1 个百分点（95 vs 94），正文“outperformed”幅度有限。
- 正文“Real-Bank 上超过 ReFoRCE 19.75%”与图中 70/75 vs 50 的差值不对应，可能是不同口径；Spider 规划时间正文为 8.4 分钟而 Table 2 为 5.1 分钟，前后不一致。
- 基线所用 LLM 不统一（Gemini 2.5、GPT-o3、Qwen3、GPT-5），比较并非同模型控制；Real-Bank 与部署数据不公开。
- 没有局限性章节；未报告记忆积累顺序对结果的影响。

依据：[arXiv:2508.05002v2，13 页](https://arxiv.org/abs/2508.05002)。
