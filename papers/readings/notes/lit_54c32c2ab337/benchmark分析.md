# benchmark

**设置**：闭源 GPT-5.1（high/none 等）、GPT-5、GPT-4o、Claude Sonnet 4.5/4；开源 Qwen3-Coder 480B、Qwen3 235B、GPT-OSS-120B、DeepSeek-V3.1、Kimi-K2；小模型 Qwen2.5-7B、Qwen3-4B。统一用默认 CodeAct 智能体、温度 0，所有工具（含网络搜索）关闭（§5.1，p.9）。

**通用分析（Table 2，p.9）**：QRData-Verified 约 48%–64%（Kimi-K2 63.68 最高）；DAEval-Verified 大模型在 82%–93% 之间；DABStep-hard 普遍很低（GPT-4o 7.41，Claude Sonnet 4.5 37.04 最高）。

**DSBio（Table 3，p.10）**：最好为 Kimi-K2 43.33%，Claude Sonnet 4.5 42.22%；小模型 4.44%/6.67%。

**预测（Table 4，p.10）**：MLEBench-Lite 与 DSPredict-Easy 上多数模型有效提交率 > 80%；DSPredict-Hard 上获奖率最高 4.8%，超中位数率最高 14.3%（GPT-5.1 high）。

**失败分析**：每个模型、每类任务抽 50 个失败轨迹人工标注；DSBio 中领域扎根错误占 85%–96%（Figure 8，p.11）。捷径过滤后同一 QRData 子集上所有模型准确率下降，最多约 21% 相对下降，小开源模型下降最大（§5.3 Finding 3、Figure 9a，pp.11–12）。

**SFT（Table 5，p.13）**：Qwen3-4B 基座 → DSGym-SFT-2k：QRData 45.27→59.36，DABStep-hard 2.9→33.07，DAEval 64.47→86.19，DSBio 6.67→21.11；部分对照数字（带 *）直接引用其他报告。

**局限（§8，p.14）**：只做确定性评测，不覆盖可视化、开放式探索和多解释任务；领域只做了生物信息；RL 训练的奖励设计尚未解决。阅读者分析：DSBio 只有 90 题、每个子领域 13–56 题，单个模型百分点差异的置信区间较宽，原文未报告方差或重复运行。

依据：[arXiv:2601.16344v1，37 页](https://arxiv.org/pdf/2601.16344)，§5–6、§8、Tables 2–5、Figures 8–9，PDF pp.9–14。
