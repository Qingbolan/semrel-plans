# 评测与边界

**基线（§6.1.2，p.6）：** 通用 agent AutoGen、ReAct、Code Interpreter；数据科学 agent LAMBDA、Data Interpreter、DataMind-7B/14B、DeepAnalyze-8B；自进化 agent LATM、ML-Master2。除 DataMind 与 DeepAnalyze 为固定骨干的训练模型外，其余在 DeepSeek-V3.1-Terminus、GPT-4o、o4-mini 三个骨干上评测。

**主要结果（Table 1，p.7）：**

| 方法 | DABench | DA-Code | SAB | MLE-Dojo | AVG |
|---|---|---|---|---|---|
| ReAct (o4-mini) | 0.866 | 0.399 | 0.225 | 0.308 | 0.450 |
| DataMind-14B | 0.876 | 0.292 | 0.010 | 0.136 | 0.329 |
| EvoDS-8B | 0.894 | 0.337 | 0.108 | 0.302 | 0.410 |
| EvoDS-evo-8B | 0.911 | 0.355 | 0.118 | 0.311 | 0.424 |

EvoDS 关闭合成技能复用；EvoDS-evo 允许同一基准内跨任务复用（Table 1 标题）。

**消融（Table 2，p.7）：** 各变体的 AVG：

| 变体 | AVG |
|---|---|
| w/o train | 0.199 |
| w/o rl | 0.363 |
| w/ grpo（只训 Manager） | 0.399 |
| w/o tool | 0.365 |
| w/o hier | 0.389 |
| w/o asa | 0.398 |
| w/o acc | 0.355 |
| 完整 EvoDS | 0.424 |

**上下文压缩（Table 3，p.8）：** 超出 token 限制的样本比例，w/o acc 在 DABench 7/257、DA-Code 20/500、SAB 18/102、MLE-Dojo 3/10，EvoDS 全为 0。

**技能复用（Table 4）：** DA-Code 测试集 0.341→0.351，SAB 0.108→0.118。

**局限（原文）：** ScienceAgentBench 与最强闭源基线仍有差距，受底座科学知识限制（§6.2，p.7）；50 个 DA-Code 失败案例中指令遵循错误 52%、执行预算不足 18%、协调错误 18%、推理缺陷 12%（§6.5，p.8）。

**阅读者分析：** 论文称“在所有基准上为开源 SOTA”，但 ScienceAgentBench 开源模型最高只有 0.118（102 题约 12 题），绝对水平很低；未报告重复次数或方差，也未报告推理成本。“消除 out-of-token 失败”依赖具体 token 预算设定，论文给出训练最大响应长度 24K（§6.1.3），但未明确评测时的 token 上限是否相同。
