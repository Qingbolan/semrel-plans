# benchmark

**被测系统**（§5.1，PDF p.6）：OpenCode 框架下的代码智能体，模型为 Gemini 3 Flash、GPT-5.4 Nano、Claude Haiku 4.5（高效型）与 Gemini 3.1 Pro、GPT-5.4（前沿型），工具与环境相同。统计：单侧配对 Wilcoxon（Full>Ambig.、Ask>Ambig.）与配对 bootstrap 95% CI。

**主要结果**（Table 1，PDF p.7，归一化分）：
| 套件 | 模型 | Full | Ambig. | Ask | Δ_ambig | Δ_ask |
|---|---|---|---|---|---|---|
| Target | GPT-5.4 | 0.61 | 0.32 | 0.52 | −0.29 | +0.20 |
| Target | Claude Haiku 4.5 | 0.56 | 0.32 | 0.52 | −0.24 | +0.20 |
| Target | GPT-5.4 Nano | 0.49 | 0.39 | 0.45 | −0.10 | +0.06 |
| Objective | Gemini 3 Flash | 0.31 | 0.22 | 0.31 | −0.09 | +0.09 |
| Objective | GPT-5.4 | 0.26 | 0.22 | 0.26 | −0.04 | +0.04 |

目标套件 Δ_ambig 介于 −0.10 至 −0.29，指标套件 −0.04 至 −0.09，五个模型的 Full>Ambig. 检验均显著。

**框定诊断**（Tables 2–3，PDF pp.7–8）：Ambig. 下替代目标提交 39–63%（Ask 下降至 2–24%）；指标套件静默失败 16–62%，其中误框定 5–18%、退化提交（复制基线/常数）8–49%；Ask 把替代目标指标降到 ≤4%，但弱模型的退化提交仍在。

**提问校准**（§5.4、Figure 2，PDF pp.8–9）：permissive 策略在完整任务上过度提问（如 Claude Haiku 4.5 在 Target 上 88% 的提问是风格偏好问题）；conservative 策略在指标套件上几乎不问（GPT-5.4 与 Nano 0%）。20 个单元中没有组合在两个套件上都校准良好。

**局限**（§6，PDF p.9）：受控诊断而非普查；只研究两个框定变量；轴与源基准混淆，不能跨套件比较效应大小；构造与 oracle 依赖 Claude 模型；θ* 是评分约定；oracle 理想化，Ask 应读作上界；数据集规模有限；Ambig. 条件无澄清通道，Δ_ambig 不能完全区分“未识别”与“识别后仍提交”。

依据：[arXiv:2605.09698v1，32 页](https://arxiv.org/abs/2605.09698)，§5–6，Tables 1–3、Figure 2，PDF pp.6–9。
