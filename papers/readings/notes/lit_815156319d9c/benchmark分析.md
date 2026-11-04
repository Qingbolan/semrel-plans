# 评测与边界

**比较方式**：主表（Tables 1–3、6）中的基线大多直接引用原基准论文或排行榜的数值，骨干从 BART-Large 到 GPT-4o、Claude Sonnet 4 不等；作者在 §5.1 承认这使"智能体设计"与"模型质量"难以分离（PDF p.7）。为此另在同一 Qwen3.6-27B 上重实现 TradingAgents、FINCON、SheetBrain，仅限 FinQA 与 MultiHiertt。

**指标**：按各数据集官方协议的 Exact Match 或执行准确率；另报告内部诊断（代码执行率、代码—答案一致性、平均市场置信 Γ̄）（§4.2，PDF p.6；Table B.9）。

**主要结果**

| 数据集 | MoCA | 对比（原文所选最强） | 位置 |
|---|---|---|---|
| FinQA | 78.29 | Fino1-14B 74.18 | Table 2 |
| DM-Simplong / Complong | 70.00 / 50.67 | GPT-4o 60.00 / DeepSeek-V3 42.33 | Table 2 |
| FinanceMath val | 76.00 | GPT-4o PoT 67.0 | Table 2 |
| TabMWP / WTQ | 96.00 / 81.40 | CREATOR 94.70 / ARTEMIS-DA 80.80 | Table 1 |
| HiTab | 77.27 | SS-CoT 79.10（MoCA 落后） | Table 1 |
| MultiHiertt dev | 71.17 | Fortune RL 56.78 | Table 1 |
| ESGenius | 86.88 | Gemma-3 12B+IT+RAG 83.80 | Table 3 |
| FinChart TF/MC/QA | 97.27/84.85/74.65 | Claude Sonnet 4 QA 63.59 | Table 6 |

**固定骨干对比（Table 4）**：FinQA 78.29 vs TradingAgents 74.50；MultiHiertt 71.17 vs 63.70。
**骨干替换（Table 5）**：十项平均 Qwen3.6-27B 76.23、Gemma-4 31B 74.77、Qwen-3.5 9B 71.62。
**消融（Table 7，两数据集平均）**：去交易市场（换成单一 FORMULA 交易员）−3.79，去修复 −2.98，去基线方案 −5.13，去仲裁 −2.83。

**原文承认的局限**（PDF p.9）：每题 6–10 次 LLM 调用，约为单次 PoT 的 5 倍；假设问题可分解为 ≤10 条声明，HiTab 这类以表头规范化为主的任务无法追上微调专用模型；VLM 转写只做一次，转写错误不会再被交易；只在英文、金融风格任务上验证。

阅读者分析：论文未说明运行次数，也未报告方差或显著性；消融与固定骨干对比只覆盖两个数据集；§5.2 由骨干替换得出"收益来自智能体而非基础模型"，但替换实验中没有"无智能体的同一骨干"对照，这个推论不够直接。
