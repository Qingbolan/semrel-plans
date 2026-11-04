# 工作负载

**7 个竞赛任务**（Table 1，p.2；附录 A，pp.24–27）：

| 任务（举办场合） | 领域 / 模态 | 指标 | 测试时限 | GPU |
|---|---|---|---|---|
| LLM Merging（NeurIPS 2024） | 高效 LLM / 文本 | Accuracy、ROUGE | 1 h | 48 GB |
| Backdoor Trigger Recovery（NeurIPS 2024） | LLM 安全 / 文本 | REASR、Recall | 0.5 h | 48 GB |
| Temporal Action Localisation（ECCV 2024 Workshop） | 多模态感知 / 视频、音频 | mAP | 0.5 h | 16 GB |
| Rainfall Prediction（NeurIPS 2023） | AI for Science / 卫星数据 | Critical Success Index | 0.5 h | 48 GB |
| Machine Unlearning（NeurIPS 2023） | 数据隐私 / 图像 | Forgetting Quality、Accuracy | 0.5 h | 16 GB |
| Next Product Recommendation（KDD Cup 2023） | 推荐系统 / 文本 | MRR | 0.5 h | 16 GB |
| Cross-Domain Meta Learning（NeurIPS 2022） | 小样本学习 / 图像 | Accuracy | 3.5 h | 16 GB |

附录 A 的数据细节示例：Backdoor 提供 100 条代码生成查询及正确输出，开发阶段模型带 5 对已知（触发词，目标），触发词最多 10 个 token（p.24）；Machine Unlearning 开发阶段用 CIFAR-10、测试阶段用 CASIA-SURF 年龄组（10 类）（p.26）；Meta Learning 使用 Meta Album 的 10 个图像数据集（5 训练、5 测试），任务 2–20 way、1–20 shot（p.27）。

**运行预算**（§4，p.6；§4.1，p.6）：llm-merging、backdoor-trigger、rainfall-pred 用单张 48 GB Quadro RTX 8000，其余用 16 GB V100；MLAB 每次 trial 最多 50 步、5 小时（Rainfall 为 100 步、10 小时）；每个配置 8 次 trial，报告最好一次。

阅读者分析：负载单位是"一个研究问题的代码仓库"，而不是逐条查询或样本；数据集大小随任务而异，正文未统一列出样本数。
