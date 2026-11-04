# 工作负载

| 数据集 | 任务数 | 来源 | 位置 |
|---|---|---|---|
| StackOverflow (SO) | 49 | TDE benchmark，StackOverflow 上的转换问题 | §6.1，p.9 |
| Bing-QueryLogs (BQ) | 50 | TDE benchmark，Bing 日志中高频 “convert A to B” 查询 | §6.1，p.9 |
| ETL | 46 | 由 DTT 论文的任务改写 | §6.1，p.9 |
| CommonSense (COM) | 43 | 作者构造，常见转换模式 | §6.1，p.9 |
| Science (SCI) | 23 | 作者构造，物理、化学等主题 | §6.1，p.9 |

五个数据集共 211 个任务（作者称“超过 200 个”）。数据处理流程沿用 TDE、FM、UniDM 等基线；每个任务的前 3 个示例作为提示，其余作为测试用例，所有方法使用相同的测试用例（§6.1，p.9）。

**微调**：基座模型 Llama3-8B-Instruct，LoRA，借助 LLaMA-Factory 在 8 张 GPU 上训练不到 30 分钟；在线推理用 vLLM 单卡（§6.1，pp.9–10）。

**生成与检索**：GPT-4o 与 GPT-4o-mini，温度 0.2；FAISS 向量库，text-embedding-3-small，取 top-3 文档（§6.1，p.10）。

Fig.8 展示了需要外部库的测试任务：经纬度转 UTM、伊斯兰历转公历、MGRS 坐标转经纬度（p.9）。

依据：§3.2、§6.1、Fig.8、Table 2，PDF pp.6、9–10。
