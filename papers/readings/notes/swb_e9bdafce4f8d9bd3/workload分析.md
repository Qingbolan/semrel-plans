# 工作负载

MAC-v1 的五个领域（附录 C，pp.19–20）：

| 领域 | Deval | Dtest | 评分 |
|---|---|---|---|
| 数学（AIME） | AIME 2022–2023 共 60 题 | AIME 2024–2025 共 60 题 | 整数答案规则匹配 |
| 科学（GPQA/HLE） | HLE 多选子集 591 题 | GPQA Diamond 198 题 | 选项字母精确匹配 |
| 竞赛编程（LiveCodeBench） | 732 题 | 323 题 | 隐藏测试 pass@1 |
| 仓库级修 bug（SWE-Bench Verified） | 250 实例 | 250 实例（仓库重叠最少） | 单元测试，经 Harbor |
| 终端任务 | Terminal Bench Pro | Terminal Bench 2.0 | 每任务二值，经 Harbor |

资源（§4，p.6）：前三领域开发时限 12 小时，后两领域 24 小时；前三领域生成的 agent 调用 A100 上 vLLM 部署的 Qwen3-8B，后两领域调用 Claude Haiku 4.5 商用接口（§5.2，p.7）；科学领域另有每阶段 2,500 次搜索 API。每个配置跑 3 次（Table 1 说明，p.7）。

阅读者分析：科学与终端领域的开发集与测试集来自不同基准，存在有意的分布差异；Terminal-Bench 两个版本的任务数原文未给出。

依据：[arXiv:2606.04455v1，20 页](https://arxiv.org/pdf/2606.04455v1)，§4–5.2、附录 C，PDF pp.6–7、19–20。
