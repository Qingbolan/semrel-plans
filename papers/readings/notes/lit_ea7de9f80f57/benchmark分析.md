# benchmark

**被测模型**：Claude Opus 4.6、Gemini 3.1 Pro Preview、GPT-5.4、DeepSeek-V3.2、Minimax M2.7、Qwen3.5-Plus、GLM-5、Kimi-K2.5，统一 OpenClaw 框架、Docker 镜像、评委提示与超时（附录 A Table 7，p.12）。没有非智能体基线。

**结果（Table 4，p.6）**：
| 模型 | Easy | Medium | Hard | Overall Acc |
|---|---|---|---|---|
| Claude Opus 4.6 | 76.8 | 62.2 | 44.8 | 63.4 |
| Gemini 3.1 Pro | 67.6 | 44.6 | 12.3 | 45.8 |
| GPT-5.4 | 23.1 | 26.5 | 12.0 | 23.4 |
| 8 模型均值 | 50.9 | 37.7 | 17.5 | 38.2 |

平均从 Easy 到 Medium 下降 13.2 个百分点，Medium 到 Hard 下降 20.2 个百分点；单模型最大降幅 55.3 个百分点（Gemini，Easy→Hard）（§4 Q1，p.5）。

**过程指标（Table 5，p.6）**：答错任务上 GPR 均值 26.9%，Claude 45.1% 最高；Hard 上 Gemini 准确率排第六、GPR 排第二。作者按 Acc/GPR/TPE 把模型分为果断型、坚持但迟、浪费式试错、早退四类（§4 Q4，pp.6–7）。

**环境消融（§4 Q5，p.7）**：Qwen3.5-Plus 在 30 道原本失败的题上，原环境全错；去噪并减少无关源后 Easy 20%、Medium 33.3%、Hard 0%；再提供完整 schema 后 40%/45%/20%。

**局限（p.9）**：只覆盖结构化与非结构化文本；里程碑受标注者判断影响，应视为一种可行参考而非唯一真值；GPR/TPE 只在答错任务上算，无法发现“答对但推理有缺陷”。

阅读者分析：环境消融只用一个模型、30 道题，结论方向可信但幅度不稳；评委 GLM-5 同时是被测模型；单次运行，原文未报告重复运行的方差。

依据：[arXiv:2605.02503v3，25 页](https://arxiv.org/pdf/2605.02503)，§4、Tables 4–6、附录 A、Limitations，PDF pp.5–9、12。
