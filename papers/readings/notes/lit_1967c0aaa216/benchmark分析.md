# 评测与边界

**设置**（§4.1，pp.6–8）：
- Planner 用 GPT-4o 或 o1-mini，Developer 用 GPT-4o，Reader、Reviewer、Summarizer 用 GPT-4o-mini；
- 每个任务 5 次试验；
- 基线 AIDE 使用默认设置，只把模型换成 GPT-4o。

**指标**（p.7）：
- MS：生成 submission.csv 的比例；
- VS：能成功提交、无报错的比例；
- NPS：越大越好的指标取原值，越小越好的指标取 1/(1+s)；
- ANPS：成功试验的 NPS 平均；
- CS = 0.5×VS + 0.5×ANPS。

**实验 1（主结果，Table 1，p.7，8 个任务的平均）**：

| 设置 | MS | VS | CS |
|---|---|---|---|
| AutoKaggle GPT-4o | 0.85 | 0.83 | 0.821 |
| AutoKaggle o1-mini | 0.73 | 0.70 | 0.759 |
| AIDE GPT-4o | 0.60 | 0.58 | 0.641 |

AIDE 在 Task 8（多变量分类）上没有产生有效提交。o1-mini 版本的 ANPS 最高（Figure 3）。

**实验 2（消融，在 Task 1/2/3/5 上）**：
- 工具库（Table 2，p.7）：VS 为无工具 0.58、仅 DC 工具 0.88、DC+FE 工具 0.65、全部工具 0.85。加入 FE 工具反而降低了完成率；
- 单元测试（Table 3，p.9）：VS 0.10 → 0.85，CS 0.240 → 0.829；
- 调试次数（Figure 5，p.11）：调试次数达到 10 次后效果不再提升。

**实验 3（按时间分层，p.10）**：Classic 任务 VS 0.90、CS 0.842；Recent 任务 VS 0.75、CS 0.800。

**口径问题（阅读者分析）**：
- 摘要称“validation submission rate 0.85”，但 Table 1 中 0.85 是 MS，VS 为 0.83；
- 正文称 VS 比 AIDE 高 28%，按 Table 1 计算差值为 0.25（阅读者分析）；
- Table 3 中 w/ Unit Tests 的 Task 2/3 CS（0.831/0.786）与 Table 1（0.786/0.831）位置互换（阅读者分析）。

**边界**：任务仅 8 个，且刻意选择小数据；Kaggle 评分需人工提交；没有成本报告。作者在 §4.4 报告，数据清洗和特征工程阶段的出错率分别为 25% 和 22.5%。

依据：[arXiv:2410.20424v3，44 页](https://arxiv.org/pdf/2410.20424v3)，§4、Tables 1–4，PDF pp.6–11。
