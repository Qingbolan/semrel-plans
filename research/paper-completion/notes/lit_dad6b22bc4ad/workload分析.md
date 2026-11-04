# 工作负载

**基准**（§4.1）：DSEval 与 QRData，共 705 个 problem-set、1,236 个问题。

| 数据集 | 规模 | 形式 |
|---|---|---|
| DSEval-LeetCode | 40 个 problem-set | 单轮 |
| DSEval-StackOverflow (SO) | 202 个 problem-set | 单轮 |
| DSEval-Exercise | 21 个 problem-set | 多轮 |
| DSEval-Kaggle | 31 个 problem-set | 多轮 |
| QRData | 411 个统计与因果推理问题 | 答案为数值或多选 |

阅读者核对：40+202+21+31+411=705，与正文一致；1,236 个问题在各数据集的分布正文未给出（阅读者分析）。

**评测方式**：DSEval 采用其原始 Pass Rate（答对问题数/总问题数），不考虑变量违规与多轮题的错误传播；QRData 直接比较代码执行输出与标准答案（数值或多选）。作者称在附录中修正了 DSEval 低估 agent 能力的评测问题，但该附录不在 arXiv 版本中。

**划分**：所有数据都作为测试集使用，没有训练集；记忆由测试过程中自身的解题结果在线积累。Mentor 与 Student 使用同一基础模型（Claude-3.5-Sonnet 或 Llama-3.1-70b，经 AWS Bedrock 的模型 ID 给出），嵌入模型为 cohere.embed-english-v3，温度 0。

阅读者分析：工作负载是单脚本/单 notebook 单元的数据科学代码题（pandas 操作、统计与因果分析），不是 SQL 或多表数据库查询；题目顺序本身是方法的一部分，因此结果依赖于"同一批题一起求解"这一前提。

依据：[arXiv:2505.14163v1](https://arxiv.org/abs/2505.14163)，§4.1，PDF p.6。
