# 评测与边界

**设置**：12 个 LLM——GPT3.5Turbo、GPT4Turbo、GPT4O、GPT4O1、GPT4O3Mini，ChatLlama2-7B/13B/70B、CodeLlama2-7B，Phi3Medium、Phi4、CohereRPlus（§4.1，p.4）。temperature 0.7、top_p 0.95、最大 4,096 token；o1/o3-mini 放宽到 32,768（附录 C，p.13）。

**实验 1（主结果，Table 2，p.5）**：

| 模型 | Depth | Func. Correctness（可执行率） | 总分 /28 | 平均 token |
|---|---|---|---|---|
| GPT4O3Mini | 2.91 | 3.48（87%） | 24.11 | 4,402.94 |
| GPT4O1 | 2.80 | 3.40（85%） | 23.70 | 6,534.45 |
| GPT4O | 2.39 | 3.24（81%） | 22.43 | 3,390.74 |
| Phi4 | 2.55 | 2.16（54%） | 19.06 | 3,815.88 |
| ChatLlama2-70B | 1.51 | 0.84（21%） | 10.57 | 2,487.18 |
| CodeLlama2-7B | 1.34 | 0.60（15%） | 8.83 | 1,786.59 |

**实验 2（错误分析，Table 3–4，pp.5–6）**：无预处理比例从 GPT4O1 的 50%、GPT4O3Mini 的 51% 到 ChatLlama2-7B 的 92%；Llama 系列 53%–64% 的回答完全没有代码。CodeLlama2-7B 总分高于 ChatLlama2-13B，但可执行率（15%）低于 ChatLlama2-7B（18%）。

**实验 3（领域差异与上下文，Figure 2–3，p.6）**：GPT4O3Mini/GPT4O 各领域分差 1.67/1.82，Phi4、ChatLlama2-70B 为 4.38/5.16；o1/o3-mini 在 4k 上下文下明显变差，随上下文增大快速改善。

**实验 4（评审模型，§4.4、Table 5，pp.6–7）**：5 名专家与 GPT4Turbo、GPT4O、Phi3Medium 比较，GPT4Turbo 对齐率 90.5%；GPT4O 偏宽松，Phi3Medium 几乎无区分度。附录 Table 10 专家 Krippendorff α 为 0.76–0.93（p.14）。

**实验 5（消融，Table 6，p.7）**：在 160 条子集上去掉角色扮演或数据摘要，主要影响文本与对齐，对代码影响小；CohereRPlus 反而在去掉后得分升高。

**边界**：作者承认只覆盖预测分析，不含诊断/处方分析，且领域有限（§7，pp.8–9）；标注者文化背景单一可能带偏差（§8，p.9）。阅读者分析：主分数依赖 GPT4Turbo 评审，未测量预测值本身的准确性；功能正确性只看"无报错执行"，不等于结果正确。
