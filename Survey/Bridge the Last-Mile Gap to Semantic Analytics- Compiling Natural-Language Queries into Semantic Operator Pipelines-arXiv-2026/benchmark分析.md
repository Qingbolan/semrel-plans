# 评测与边界

**基线**（§4.0.2，pp.7–8）：Naive（单次调用，给官方文档 + 数据描述 + 问题）；Hardcoded（每种问题类型一个人写模板，LLM 模拟人工填谓词，不计编译费用）；CodeTree（最多 5 个候选策略、3 层分支、10 轮执行-修复）；Codex (model)（同 Naive 提示，换 gpt-5.1-codex-mini）；Codex (agent)（best-of-3，每题生成并执行三条流水线）。

**指标**（§4.0.3，p.8）：EM、token 级 F1、LLM-as-judge（六条规则的固定提示）；每题平均编译费用（美元，不含后端执行）；编译延迟 t_m、执行延迟 t_e、总延迟 t；质量/千分之一美元。

**实验 1（端到端，Tables 1–3，p.9）**：NL2Pipe 与次优方法的 EM / F1 / LLM 对比（摘录）。

| 后端 / 数据集 | NL2Pipe | 次优方法 | NL2Pipe 编译费用 |
|---|---|---|---|
| PZ / HybridQA | 59.3 / 68.6 / 73.3 | Hardcoded 39.3 / 47.5 / 51.0 | $0.0156 |
| PZ / MMQA | 51.7 / 57.1 / 63.3 | Hardcoded 34.3 / 42.3 / 52.7 | $0.0134 |
| PZ / TAT-QA | 45.7 / 55.2 / 67.7 | Hardcoded 24.0 / 40.5 / 64.7 | $0.0125 |
| LOTUS / MMQA | 24.4 / 34.7 / 51.2 | CodeTree 27.4 / 36.3 / 47.8 | $0.0133 |
| LOTUS / HybridQA | 32.3 / 46.3 / 66.3 | CodeTree 36.0 / 46.3 / 58.7 | $0.0177 |
| Nirvana / HybridQA | 29.3 / 35.4 / 40.0 | CodeTree 31.0 / 38.8 / 45.7 | $0.0179 |
| Nirvana / HotpotQA | 57.7 / 69.0 / 81.0 | Hardcoded 30.0 / 46.3 / 70.3（EM 次优为 CodeTree 30.3） | $0.0121 |

作者称平均编译费用约 $0.013/题，约为 CodeTree（$0.024）的 1/1.8，与 Codex (model)（$0.014）相当，是 Codex agent 的 1/30–1/20（§4.1，p.8）。离线参考文档每个（后端，数据集）花 $0.40–0.70，摊到 300 题为每题 $0.001–0.002（§4.1，p.9）。

**实验 2（对 Codex，Table 4，p.10，每组 100 题）**：例如 Palimpzest-HybridQA 上 Codex (agent) F1 52.9、$0.2521、t_m 311.2 s，NL2Pipe F1 67.3、$0.0156、t_m 111.3 s。LOTUS-ManyModalQA 与 Nirvana-MMQA 的 LLM-judge 分数 Codex (agent) 略高（73.0 对 72.0、37.0 对 35.0）。

**实验 3（延迟，Tables 5–6，p.11）**：三后端平均的每题延迟（秒）。

| 数据集 | NL2Pipe t_m / t_e / t | CodeTree t | Codex (model) t | Naive t |
|---|---|---|---|---|
| TAT-QA | 92.7 / 16.2 / 109.0 | 159.6 | 36.0 | 58.1 |
| HotpotQA | 78.0 / 16.1 / 94.0 | 175.8 | 28.7 | 64.4 |
| HybridQA | 117.0 / 66.6 / 183.5 | 213.1 | 73.0 | 87.3 |
| MMQA | 87.8 / 15.9 / 103.7 | 195.1 | 34.3 | 56.1 |
| ManyModalQA | 67.2 / 12.2 / 79.4 | 127.4 | 24.3 | 40.0 |

Palimpzest 上 Phase A（Linker）占编译耗时 53.4–60.6%（Table 6）。作者报告的是未做提示缓存等工程优化的延迟。

**实验 4（消融，Table 7，p.12）**：去掉 Planner 在 LOTUS-MMQA 上 LLM-judge 从 51.2 降到 20.3，Nirvana-MMQA 从 36.0 降到 10.3；去掉参考文档在 Palimpzest 上降幅最大（MMQA −37.6，TAT-QA −21.7）。PZ TAT-QA 上同时去掉 Linker 和 Planner（72.0）反而高于只去其一，作者解释两阶段是耦合而非可加的。

**边界**：
- 费用只计编译，后端执行费用不计（§4.0.3）；Hardcoded 的费用与编译延迟不可比（§4.0.2）。
- 阅读者整理：NL2Pipe 的编译延迟是 Codex (model) 的 2.5–4 倍；正文“在 Nirvana 上除 HybridQA 外全部最优”与 Table 3 不完全一致（ManyModalQA、TAT-QA 的 LLM-judge 低于 CodeTree）；Nirvana-MMQA 去掉 Linker 反而更好（Table 7）；只用一种编译模型和一种执行模型；各题数据上下文很小。

依据：[arXiv 2606.04641v1](https://arxiv.org/abs/2606.04641v1)，§4.0–4.3、Tables 1–7、Figure 4，pp.7–12。
