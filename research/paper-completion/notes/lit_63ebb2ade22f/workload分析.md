# 工作负载

论文用 12 类 LM 程序作为基准（§6.1，p.7）：

| 工作负载 | 设置 | 主要优化来源（§6.2，p.8） |
|---|---|---|
| MMLU | 5-shot，解码 1 个 token | 复用少样本前缀 |
| HellaSwag | 20-shot，用 `select` 选答案 | 少样本 + 题干两级共享 |
| ReAct 智能体、生成式智能体 | 从原论文提取轨迹回放 | 复用模板与历史调用 |
| 思维树（GSM-8K）、思维骨架（建议生成） | 程序内并行 | 并行 + KV 复用 |
| LLM 评审 | branch-solve-merge | fork 并行 |
| JSON 解码 | 正则模式约束 | 压缩 FSM |
| 多轮对话 short / long | 4 轮，每轮输入 256–512 token；输出 4–8 / 256–512 token | 复用对话历史 |
| DSPy RAG 管线 | DSPy 官方示例 | 复用公共上下文示例 |

**模型与硬件**：Llama-2 7B/70B、Mixtral-8x7B、LLaVA-v1.5-7B（图像，llava-bench-in-the-wild）、LLaVA-NeXT-34B（视频，ActivityNet）、GPT-3.5；fp16；主要在 AWS G5（A10G 24GB），部分用 A100 80GB（§6.1、附录 C）。

**开销测试**：ShareGPT 上 100 个请求（无复用机会）（§6.3，p.9）。**生产**：Chatbot Arena 部署一个月（§6.2，p.8）。

单位：一个“程序实例”；吞吐在足够大的批上测最大值，延迟为逐个执行取平均（§6.1）。论文未给出各基准的实例数量。

依据：§6.1–6.3、附录 C，PDF pp.7–9、18。
