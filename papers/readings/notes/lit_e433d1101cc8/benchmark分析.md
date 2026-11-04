# 评测与边界

**设置**：LM 为 GPT-4（0613）、GPT-4-turbo（0125）、Claude v1.0、Claude v2.1、Claude v3 Opus、Gemini Pro、Mixtral（Instruct-v0.1）；另把 AutoGPT 与 LangChain 的 zero-shot-react-description 适配进来比较。每设置 8 次运行。

**实验 1（平均成功率与平均提升，Tables 3–4，已渲染核对）**：

| LM | 平均成功率 % | 平均提升 % |
|---|---|---|
| GPT-4 | 19.2 | 41.3 |
| GPT-4-turbo | 26.0 | 32.8 |
| Claude v1.0 | 16.3 | 8.9 |
| Claude v2.1 | 26.0 | 15.0 |
| Claude v3 Opus | 37.5 | 26.1 |
| Gemini Pro | 18.3 | -3.6 |
| Mixtral | 3.8 | 8.0 |
| Baseline | 10.4 | 0.0 |

Claude v3 Opus 在 house-price 与 spaceship-titanic 上为 100%，在 parkinsons-disease、fathomnet、BabyLM 等任务上为 0。作者指出 GPT-4 的平均提升主要由 identify-contrails（143.3%）拉高。

**实验 2（框架对比，Table 5）**：GPT-4-turbo 下本文智能体 / AutoGPT / LangChain 平均成功率为 26.0 / 2.9 / 1.0；Claude v3 Opus 下为 37.5 / 13.5 / 33.7。

**实验 3（过程与效率）**：CIFAR-10 轨迹的失败分为幻觉、坏计划、响应格式错误、提交格式错误和提升不足；运行更多步通常使指标退化，Claude v3 Opus 除外。GPT-4-turbo 平均比一般智能体少用 51.0% token；跑完整个基准一次约 600 万 token、约 60 美元，按 26% 成功率折算完成一个任务的期望成本约 231 美元。

**边界**：作者承认长程规划、幻觉与问题描述不清是主要挑战。8 次运行的成功率粒度为 12.5 个百分点，未报告置信区间；“提升 10%”对无基线任务与越低越好的指标定义不清（见 Table 4 残留批注）；Baseline 列非零成功率未解释，任务间可比性有限（阅读者分析）。

依据：§4.1–4.3，pp.6–8；Tables 3–5，pp.7–8、15；Figures 3、5–6，pp.7–9；附录 B、D，pp.15–18。
