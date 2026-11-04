# 评测与边界

**代理配置**（§4.1–4.2，pp.6–7）：以 MLAB（ReAct 式，无网络搜索）为主框架，比较 gemini-exp-1206、Llama 3.1 405B Instruct、o3-mini、Claude 3.5 Sonnet v2、GPT-4o；并在 GPT-4o 上比较加入 CoI-Agent（o1 骨干，可访问 Semantic Scholar）生成的想法或人工整理想法。

**实验 1（主结果，Table 3，p.7）**：相对人类最佳的提升（%）：

| 配置 | rainfall | unlearning | backdoor | 平均 |
|---|---|---|---|---|
| MLAB（gemini-exp-1206） | 43.1 | 5.6 | 12.9 | 9.3 |
| MLAB（llama3.1-405b） | 31.5 | 6.2 | 11.5 | 6.3 |
| MLAB（gpt-4o） | 47.5 | −18.0 | 10.4 | 5.4 |
| MLAB（o3-mini） | 25.1 | 3.6 | 6.2 | 4.2 |
| MLAB（claude-3.5-sonnet-v2） | 14.6 | −94.7 | 39.9 | −5.2 |
| + 人类想法（gpt-4o） | 12.3 | 6.8 | 8.8 | 3.5 |
| + CoI 想法（gpt-4o） | 39.4 | 11.8 | 4.0 | 7.1 |

其余 4 个任务（temporal-action-loc、llm-merging、meta-learning、product-rec）各配置在 −4.9 到 5.0 之间。作者解释：rainfall 的 47.5 可能因为 U-Net 类方案网上易得；backdoor 的 GCG 基线接近随机，门槛低（§4.2，p.7）。

**实验 2（LLM 评审可靠性，§4.3、Figure 2–3，pp.7–8）**：客观与主观指标的 Spearman 相关整体很弱，创新性与效果为 −0.06；去掉代码输入后结论相似。

**实验 3（开发过程，Figure 4，p.9）**：迭代中运行时间和代码量持续增加，性能未成比例提升；附录 F 的轨迹分析称 11.5% 的步骤是错误工具参数，代码执行错误只修复了 17.2%。

**实验 4（成本与扩展，Figure 5–6，pp.9–10）**：Llama 3.1 405B 的性价比最好；以"填补至少 5% 差距"为成功定义的 pass@k 中，人类想法优于 AI 想法，固定预算下多想法与多 trial 分配无显著差异。

**边界**：附录 D（p.31）承认只有 7 个竞赛、只评测了通用 MLAB 一种实现框架。阅读者分析：每配置 8 次取最好、任务数少，平均分容易被个别任务主导（如 rainfall、unlearning）。
