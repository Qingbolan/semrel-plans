# 评测与边界

**基线**：Pandas Agent（LangChain，gpt-4o）与 AgentPoirot（gpt-4o、gpt-4-turbo、gpt-3.5-turbo、llama-3-70b 四种骨干）。InsightPilot（无代码）、Data-Copilot（仅中文金融）、OpenAgents（公开版限 10 次请求）、InfiAgent-DABench（表现极差）、PowerBI（闭源）被排除（§3.1，PDF pp.6–7）。温度 0，5 个种子取均值±标准差（§3.2，PDF p.7）。

**实验 1（主结果，Table 1，PDF p.8）**：

| 智能体 | insight 级 ROUGE-1 | insight 级 LLaMA-3-Eval | summary 级 ROUGE-1 | summary 级 LLaMA-3-Eval |
|---|---|---|---|---|
| PA (gpt-4o) | 0.35±0.03 | 0.54±0.01 | 0.35±0.01 | 0.40±0.04 |
| Ours (gpt-4o) | 0.32±0.02 | 0.60±0.03 | 0.37±0.09 | 0.44±0.03 |
| Ours (gpt-4o) 通用目标 | 0.30±0.03 | 0.40±0.03 | 0.30±0.08 | 0.33±0.12 |
| Ours (gpt-4-turbo) | 0.30±0.02 | 0.56±0.02 | 0.35±0.08 | 0.35±0.04 |
| Ours (gpt-3.5-turbo) | 0.34±0.01 | 0.50±0.02 | 0.27±0.14 | 0.31±0.06 |
| Ours (llama-3-70b) | 0.33±0.02 | 0.52±0.04 | 0.36±0.01 | 0.33±0.01 |
| Ours (llama-3-70b) 非多样跟进 | 0.29±0.01 | 0.51±0.03 | 0.32±0.01 | 0.28±0.03 |

原文称 AgentPoirot 在 ROUGE-1 与 LLaMA-3-Eval 上均优于 PA（§4，PDF p.7），但 Table 1 中 insight 级 ROUGE-1 实为 PA 0.35 高于 Ours 0.32（阅读者分析）。

**实验 2（分组）**：按难度 Hard 明显下降；按 insight 类型，描述性最好（0.52–0.62），其后依次为诊断、规范、预测（§4、Figure 4，PDF pp.8–9）。

**实验 3（通用目标）**：gpt-4o 的 insight 级分数从 0.60 降到 0.40，说明 SMART 目标对表现关键（§4，PDF p.9）。

**实验 4（趋势强度/温度）**：斜率 <0.1（含负值）时所有模型都未“发现”该 insight，原文以 LLaMA-3-Eval>0.5 为发现阈值并据此称无误报；斜率 >0.1 时 gpt-4o/gpt-4-turbo 每次都发现。温度 0.2 时表现最好（§4、Figure 8，PDF pp.9、20）。

**实验 5（评测器）**：前 10 个数据集上 G-Eval 与 LLaMA-3-Eval 排序一致；many-to-many 匹配分数更低且常错配（附录 C Table 4、§4，PDF pp.9、20）。

**边界**：数据为合成且仅来自 ServiceNow 模式；评分完全依赖 LLM 评判，人类一致性只通过与 G-Eval 对照间接说明（阅读者分析）；Eq.1 不惩罚多余 insight；§7 与附录 A 承认可能强化偏见、需随业务演进持续评估、未覆盖非结构化数据与图表视觉理解（PDF pp.10、14）。

依据：§3–4、§7、Table 1、Figure 4、Figure 8、附录 A、附录 C，PDF pp.6–10、14、20。
