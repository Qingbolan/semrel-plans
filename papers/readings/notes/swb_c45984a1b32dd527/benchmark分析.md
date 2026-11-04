# 评测与边界

**基线**：CoT、PoT、ReAct，以及经验适应方法 AWM、ACE、ASI，均使用相同的基础 ReAct 智能体、训练划分和请求上限。

**实验 1（主结果，Table 2，测试准确率 %）**：

| 方法 | DeepSeek-V3 平均 | Gemini 2.5 Flash 平均 |
|---|---|---|
| CoT | 49.6 | 69.3 |
| PoT | 52.9 | 60.3 |
| ReAct | 38.8 | 68.2 |
| AWM | 47.8 | 71.6 |
| ACE | 56.6 | 67.6 |
| ASI | 49.8 | 66.2 |
| ARISE 内容作技能 | 51.8 | 66.1 |
| ARISE 内容作代码 | 48.3 | 69.8 |
| ARISE | 67.4 | 77.7 |

**实验 2（AIME，Table 4）**：Gemini 3.1 Flash-Lite 上 ARISE 79.1%，ACE 60.5%、ReAct 44.2%；Gemini 2.5 Flash 上 81.4%，CoT 79.1%。

**实验 3（跨模型迁移，Table 5）**：Gemini 2.5 Flash 归纳的库直接用于 Gemini 3.5 Flash-Lite，比其 ReAct 高 10.7（团队分配）至 32.8（NBA）个百分点。

**实验 4（附录）**：K∈{3,5,10} 均高于 ReAct；20 样本自洽在谋杀和物品放置上分别低于 ARISE 9.0 和 23.6 个百分点；DeepSeek-V3 在 MuSR 上三次重复运行，ARISE 均值最高。

**成本（Table 12）**：Gemini 2.5 Flash 上 ARISE 3.63 美元/任务，ACE 13.14 美元；DeepSeek-V3 上 ARISE 5.23 美元，各方法中最高。

**边界**：归纳只能用于基础智能体能解出部分训练题的任务（旅行规划所有方法接近 0）；长数值计算任务更适合代码。部分 DeepSeek-V3 基线由 OpenRouter 提供，与其他行的服务方不同（Table 2 †）。阅读者分析：主表多为单次运行，置信区间只在附录 J 给出；论文没有单独的局限节（阅读者分析）。

依据：[arXiv:2606.02994v2，27 页](https://arxiv.org/pdf/2606.02994)，§4–5、Tables 2–5、附录 D、G、H、I、J、K、L，PDF pp.5–9、17–27。
