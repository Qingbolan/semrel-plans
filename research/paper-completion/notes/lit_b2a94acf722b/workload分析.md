# 工作负载

| 数据集 | 任务 | 测试规模 | 表数 | 指标 |
|---|---|---|---|---|
| WikiTableQuestions（WikiTQ） | 表格问答 | 4,344 | 421 | 准确率 |
| TabFact | 表格事实核验（二分类） | 2,024 | 298 | 准确率 |

两者都是公开标准测试集（§4.1）；论文未说明 TabFact 用的是哪个官方子集名称，只给出 2,024 例与 298 张表。没有使用训练集做微调，提示中的少样本示例与初始的 2 个模板来自作者设计，具体见附录 E 的提示词。

底座模型三种：Qwen2.5-72B-Instruct、LLaMA3.3-70B-Instruct（SGLang 部署）和 GPT-4o-mini（API）；温度 0.0，最大迭代 K=5（§4.4 的收敛分析放宽到 K=10）。成本按 token 计：WikiTQ 上 Chain-of-Table 输入 73.5M、输出 1.6M，Table-Critic 输入 135.5M、输出 3.8M（附录 C Table 4）。

依据：[ACL 2025，pp.17432–17451，20 页](https://aclanthology.org/2025.acl-long.853/)，§4.1、附录 B.2、C，PDF pp.5、12–13。
