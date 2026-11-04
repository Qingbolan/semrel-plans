# workload

- **实验条件（Table 2）**：
  | 条件 | 数据表示 | 提示 | 仿真与信号 |
  |---|---|---|---|
  | Exp 1（参考） | 原始数据 | 短 | 设置 1，清晰强信号 |
  | Exp 2 | 原始数据 + 冗余汇总表 | 短 | 设置 1 |
  | Exp 3 | 原始数据 | 无歧义 | 设置 1 |
  | Exp 4 | 原始数据 | 短 | 设置 2，清晰但较弱信号 |
- **模型**：8 个家族、15 个模型-推理档位配置（GPT-5.4、GPT-5.2、GPT-5.4 mini、Claude Sonnet 4.6、Claude Haiku 4.5、Gemini 3.1 Pro、Gemini 3 Flash 各有 low/high 或 xhigh 档；Mistral Large 仅 default）。均用 OpenCode harness v1.2.27 默认设置、默认温度，无 agents.md 等自定义指令。
- **规模**：每配置每条件 5 条轨迹 → 每配置 20 条，共 300 条（每条件 75 条）。平均耗时 783.56 秒。
- **数据规模**：正文未报告仿真的表结构、行数或实体数；仅说明数据集与项目材料公开于 deepsense-ai/agent-based-simulation-benchmark 仓库。
- 无训练/测试划分：这是纯评测，所有配置使用同一任务实例（每条件一个仿真）。阅读者分析：因此"每条件"实际上只有一个问题实例，方差估计反映的是 agent 运行随机性，而非任务分布。

依据：[arXiv:2606.00051v1，16 页](https://arxiv.org/abs/2606.00051)，§4.3–4.4、Table 2、§5.1，PDF pp.6–8；p.14。
