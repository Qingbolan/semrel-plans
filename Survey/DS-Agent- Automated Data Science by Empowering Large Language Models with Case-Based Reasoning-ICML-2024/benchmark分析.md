# 评测与边界

**比较对象**：
- 开发阶段：ResearchAgent（Huang et al., 2023），分别基于 GPT-3.5 和 GPT-4，超参数按其原文设置（§4.2.1、附录 B.3）；
- 部署阶段：Zero-shot（直接让 LLM 写代码）和 One-shot（从案例库随机放一个案例，相当于去掉检索的消融），分别基于 GPT-3.5、GPT-4 和 Mixtral-8x7b-Instruct（§4.3.1）。

**开发阶段结果**（Figure 4、Table 1，12 个任务，5 次重复；rank 越低越好）：

| 模型 | Agent | 平均 mean rank | 平均 best rank |
|---|---|---:|---:|
| GPT-3.5 | ResearchAgent | 12.6 | 11.8 |
| GPT-3.5 | DS-Agent | 7.5 | 3.3 |
| GPT-4 | ResearchAgent | 9.8 | 5.4 |
| GPT-4 | DS-Agent | 5.0 | 1.5 |

GPT-4 版 DS-Agent 在 6 类任务上的成功率都是 100%，并在 12 个任务中的 9 个取得最好表现。GPT-3.5 版 DS-Agent 在所有任务类型上的成功率都高于 GPT-4 版 ResearchAgent。各 agent 在表格任务上更容易成功，因为这类任务通常只需调用 sklearn（§4.2.1）。

**部署阶段结果**（Figure 5、Table 3，18 个任务，10 次运行）：
- 一次通过率：DS-Agent 用 GPT-4 时为 99.44%，用 GPT-3.5 时为 85.00%；最好的基线在 GPT-3.5 下为 56%，在 GPT-4 下为 60%；
- Mixtral 版的一次通过率从 zero-shot 的 6% 提高到 31%；
- 平均 mean rank（9 个 agent 一起排名）：GPT-4 版 DS-Agent 为 12.7，GPT-3.5 版为 17.1，Mixtral 版为 35.5；GPT-4 的 zero-shot/one-shot 分别为 28.2/28.0。

**成本**（Table 4，单次运行）：

| 模型 | 开发阶段 | 部署阶段 | 降幅 |
|---|---:|---:|---:|
| GPT-3.5 | $0.06 | $0.0045 | 92.5% |
| GPT-4 | $1.60 | $0.1350 | 91.5% |

**与 AutoML 的对比**（附录 C.1，Table 6，4 个表格开发任务）：AutoGluon 只跑一次（作者称它没有随机性）；DS-Agent 跑 5 次，同时报告平均值和最好值。GPT-3.5 版在 spaceship-titanic 上有一次失败，因此不报告其平均值。

**边界**：
- 部署阶段的前提是新任务与开发任务“同分布”；
- 任务只有 30 个，数据规模不大，属于单机训练的分类/回归任务；
- 成功率衡量的是能否建出可运行的模型，不等于预测效果最好；
- 费用只算 API 调用，不含模型训练所用的算力（阅读者分析）。

依据：[arXiv 2402.17453v2](https://arxiv.org/abs/2402.17453v2)，§4.2–4.3、Tables 1、3、4、Figures 4–5、附录 C.1，PDF pp.5–8、16–17。
