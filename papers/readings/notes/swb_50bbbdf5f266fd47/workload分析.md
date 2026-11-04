# 工作负载

| 政策 | 政策文本 | 训练集（用于生成 PRT） | 测试集 |
|---|---|---|---|
| HIPAA | Subpart E §164.500–164.530，约 15 个条款节，≈3.9K tokens | GoldCoin-HIPAA 309 个合成法院案例 | GoldCoin-HIPAA 107 个 |
| GDPR | 第 1–90 条，≈8.8K tokens | GDPRHub 真实 DPA 案件 764 个 | 326 个 |
| ModelSpec | OpenAI ModelSpec 全部 20 节，≈4.1K tokens | ModelSpec 中 64 个标为 good/bad 的交互示例 | XSTest 450 条 |

所有样本标签均为 COMPLIANT / NON-COMPLIANT，作者称训练与测试无重叠。政策文本经 GPT-5-mini 做了格式统一和少量摘要（附录 H），因此模型看到的不是逐字原文。学习模型需支持 ≥8192 token 上下文。PRT 生成温度 0.7、最大 2048 token，多数不超过 1500 token（附录 B）。

阅读者分析：ModelSpec 的训练示例与测试集 XSTest（衡量“过度拒答”的提示集）来源和标注口径不同，所谓“合规”在这里更接近安全响应判断，与 HIPAA/GDPR 的法律案例不是同一类任务。

依据：[arXiv:2509.23291v1](https://arxiv.org/pdf/2509.23291v1)，§3，PDF pp.4–5；附录 B，p.18。
