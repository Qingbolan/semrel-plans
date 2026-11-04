# 评测与边界

**设置**（§5.1，p.7）：在 100 个测试案件上评测。TL Agent 基座为 GPT-4o-mini（temperature 0.6）。基线分四组：未用 TL 数据微调的小模型（ChatGLM-6B、LexiLaw、Lawyer Llama v2）、用 TL 数据微调的 6B 模型、以中文为主的 API 模型、以英文为主的 API 模型。

**实验 1（主结果，Table 2，PDF p.7，已渲染）**：

| 方法 | Sfact-1 | Pre | Rec | Fevi | Sexp-1 | Sc |
|---|---|---|---|---|---|---|
| ChatGLM-6B | 18.26 | 3.65 | 7.42 | 4.89 | 20.69 | 11.54 |
| LexiLaw 微调 | 29.91 | 8.87 | 27.09 | 13.37 | 19.37 | 23.46 |
| Qwen-max | 25.01 | 12.28 | 15.90 | 13.85 | 27.84 | 30.94 |
| Deepseek-v3 | 29.47 | 10.74 | 19.10 | 13.75 | 31.61 | 30.35 |
| GPT-4o | 29.86 | 9.72 | 19.84 | 13.05 | 28.71 | 25.74 |
| TL Agent | 32.99 | 10.38 | 40.73 | 16.53 | 30.92 | 31.50 |

TL Agent 在 Sfact、Rec、Fevi 和 Sc 上最高，但精确率低于 Qwen-max，子任务 III 低于 Deepseek-v3；子任务 II 精确率普遍很低（≤12.28），原文归因于模型倾向冗余连接（§5.2）。

**实验 2（与推理模型比较，Table 4，PDF p.18）**：在随机抽取的 10% 数据上评测，使用 3-shot 提示。TL Agent（4o-mini）Sc=36.62，TL Agent（4o）36.11，GPT-4o 3-shot 36.52，Deepseek-R1 3-shot 36.01。o1/R1 在子任务 II 上优于其基座，在 I、III 上较差（附录 F）。

**实验 3（消融，Table 5）**：同为 10% 子集；去掉法律知识或知识检索后各项指标下降（如 Sfact-1 从 37.92 降到 35.70/35.65）。事实抽取头和反思工具是格式化输出所必需的，未做消融（附录 G）。

**边界**：Limitations 承认效果原因未深入分析，提示设计依赖领域专家；附录 D 声明不鼓励用 LLM 做最终判决。

Table 4 上 TL Agent 与 GPT-4o 3-shot 的 Sc 仅差 0.10，子集只有约 10 个案件且没有方差报告，“全部任务最优”的结论偏强；Table 2 与 Table 4 的评测集合不同，数值不可直接比较（阅读者分析）

依据：[Findings of ACL 2025, pp.17252–17274，23 页](https://aclanthology.org/2025.findings-acl.887.pdf)，§5、Limitations、Tables 2、4、5、附录 D、F、G，PDF pp.7–9、14、16–18。
