# benchmark

**设置**：三个“模型 + harness”组合——Claude-Sonnet-4.6（Claude Code）、GPT-5.5（Codex）、Gemini-3.1-Pro（作者实现的 ReAct）。每题试验 5 次，指标为 pass@k，按“查询→数据集→17 个数据集”分层平均，另记录美元成本和轨迹统计。

**主结果（Table 3，提供 descriptions 和 hints）**：

| 组合 | pass@1 | 总成本 |
|---|---|---|
| Claude-Sonnet-4.6（Claude Code） | 0.48 | $705.4 |
| GPT-5.5（Codex） | 0.57 | $484.0 |
| Gemini-3.1-Pro（ReAct） | 0.52 | $294.3 |

最好的 pass@5 约为 70%；patents 上三者均为 0。三种条件共 4,680 次试验，花费 $4,346。

- **消融（Table 5）**：去掉 hints，或同时去掉 descriptions 和 hints，pass@1 变化不超过 5 个百分点，有时反而上升，因为数据集级 hint 可能误导与之无关的查询。
- **失败模式**：答错轨迹中，GPT-5 判定器标出实现错误（FM4）57%、计划错误（FM2）31%、数据选择错误（FM3）11%；人工复核 30 条轨迹，与判定器完全一致 67%，换用 GPT-5.4 判定后排序不变。
- **共享 ReAct harness**（只用最便宜的 54 条查询，pass@1/pass@5）：GPT 5.2 29%/44%、Claude Opus 4.6 55%/69%、Gemini 3.1 Pro 60%/75%。

**局限（§6）**：只覆盖四种开源 DBMS；只含只读分析查询；每题只有单一确定答案；排除外部 API；规模为 104 条查询。

阅读者分析：主实验中模型与 harness 是捆绑比较，不能把差距单独归因于模型；验证脚本只检查“包含”正确答案，对夹带错误信息的回答较宽松；单次完整评测要数千美元，复现门槛高（§7 亦承认）。

依据：[arXiv:2603.20576v3（2026-10-07），27 页](https://arxiv.org/abs/2603.20576)，§4、§6–7，Tables 3–5、Figure 3–4，PDF pp.6–10；附录 C、E，pp.22–25。
