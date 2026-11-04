# 评测与边界

基线：MLAB、OpenHands、AIDE（GPT-4o，结果取自 MLE-Bench 官方运行报告），以及作者用 o3-mini、DeepSeek-V3 重跑的 AIDE（§4.1，PDF p.5）。指标：MLE-Bench 胜率（超过的人类参赛者比例），报告 best@3 与 avg@3；OAG 用 AUC，BELKA 用 AP。

**实验 1（主结果）**：Table 1，PDF p.5，Overall。

| 方法 | 骨干 | best@3 | avg@3 |
|---|---|---|---|
| AIDE | o3-mini | 0.34 | 0.28 |
| AIDE | DeepSeek-V3 | 0.48 | 0.36 |
| AutoMind w/o Knowledge | DeepSeek-V3 | 0.52 | 0.33 |
| AutoMind | o3-mini | 0.54 | 0.39 |
| AutoMind | DeepSeek-V3 | 0.58 | 0.41 |

摘要称“平均超过 40% 参赛者、比先前 SOTA 提升 8.0%”，§4.3 则给出 38.7%/41.2% 与 11.0%/5.2%（avg@3）；8.0% 应为两者平均，但原文未明写（阅读者分析）。

**实验 2（消融）**：消融（DeepSeek-V3，仅 Medium 5 任务，Fig.3）：去知识库胜率降 11.8%、有效率降 5.6%；去自适应编码分别降 13.2%、27.6%。

**实验 3（检索与效率）**：检索评估（Table 2）：混合检索 P=84%、R=74%、F1=0.79，基于 15 任务 × top-5 = 75 次检索。效率：达到 AIDE 24 小时水平平均用 15 小时；Table 3 中 AutoMind 输入 2.15M + 输出 0.27M 与所列总计 2.25M 不相加一致（阅读者核算），9.6% token 节省按总计列计算（阅读者分析）。

局限（阅读者归纳，原文无局限节）：任务子集小且经筛选；GPT-4o 基线为借用结果，骨干与运行环境不同；每设置仅 3 次运行，未报告置信区间；BELKA、OAG 为抽样版本；硬件描述前后不一致。

依据：§4–5、Tables 1–3、Figs.2–3，PDF pp.5–8。
