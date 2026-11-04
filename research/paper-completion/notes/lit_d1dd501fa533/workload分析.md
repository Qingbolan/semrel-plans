# 工作负载

8 个 Magellan 基准数据集（Table II，p.7）：

| 数据集 | 领域 | 属性数 | 实体对数 | 匹配对数 |
|---|---|---|---|---|
| Walmart-Amazon (WA) | 电子产品 | 5 | 10,242 | 962 |
| Abt-Buy (AB) | 产品 | 3 | 9,575 | 1,028 |
| Amazon-Google (AG) | 软件 | 3 | 11,460 | 1,167 |
| DBLP-Scholar (DS) | 引文 | 4 | 28,707 | 5,347 |
| DBLP-ACM (DA) | 引文 | 4 | 12,363 | 2,220 |
| Fodors-Zagats (FZ) | 餐厅 | 6 | 946 | 110 |
| iTunes-Amazon (IA) | 音乐 | 8 | 532 | 132 |
| Beer | 啤酒 | 4 | 450 | 68 |

**单位与划分**：样本单位是一对已阻断的候选实体对，标签为匹配或不匹配。标注对按 3:1:1 划分为训练、验证和测试集，与已有 ER 研究一致（§VI-A，p.7）。Beer 测试集约 91 对（§VI-B，p.8）。

**默认配置**（§VI-A，p.8）：
- 批大小 8；固定、Topk-batch、Topk-question 每批都用 8 个示例。
- 覆盖阈值 t 取所有问题两两距离的第 8 百分位。
- 默认 LLM 为 GPT-3.5-turbo-0301，温度 0.01；另测了 GPT-3.5-turbo-0613、GPT-4-1106-preview 和 Llama2-chat-70B。

**成本口径**：API 费用按 token 计；标注费用按 AMT 每任务 0.08 美元、每任务 10 对，折合每对 0.008 美元（§VI-A，p.8）。

依据：§VI-A，Table II，pp.7–8。
