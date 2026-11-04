# 工作负载

三个公开基准（§4.1、附录 D.1）：

| 基准 | 规模 | 单位与指标 |
|---|---|---|
| InfiAgent-DABench | 257 题 | 每题一个 CSV 加若干问题，分 easy/medium/hard；指标 ABQ（按问题计准确率） |
| MatplotBench | 100 例 | 查询、输入数据与专家校验的参考图；GPT-4o 视觉评分 0–100 |
| DSBench 数据建模 | 74 个 Kaggle 竞赛任务 | 训练/测试数据、提交样例、详细描述；指标为任务成功率与 RPG，单题超过 3600 秒记为未完成 |

消融用 InfiAgent-DABench 中 175 个 medium/hard 题和 DSBench 的 74 题，模型为 GPT-4o mini（Table 5）。规模实验用 Qwen2.5 7B/14B/32B/72B 在 InfiAgent-DABench 上进行（Figure 5）。

三个基准均为公开基准原样复用，本文没有构造新数据（阅读者分析）。

依据：§4.1、Table 5、Figure 5、附录 D.1，PDF pp.5–7、13–14。
