# DS-Agent: Automated Data Science by Empowering Large Language Models with Case-Based Reasoning

DS-Agent 让 LLM agent 针对给定的训练/验证/测试数据和评价指标，自动写出能训练并评估 ML 模型的代码。它用案例推理（CBR）分两个阶段工作。开发阶段从 Kaggle 获胜方案中检索经验，再按执行反馈重排案例、修订实验计划。部署阶段直接改写开发阶段保存的成功代码，不再迭代。

GPT-4 版在 12 个开发任务上的成功率为 100%。在 18 个部署任务上，GPT-4 版的一次通过率约 99%，GPT-3.5 版为 85%，最好的基线分别只有 60% 和 56%。GPT-4 每次运行的费用在开发阶段为 $1.60，在部署阶段降到 $0.135（§1、Figure 5、Table 4）。

[原文](https://arxiv.org/abs/2402.17453v2)

版本：arXiv 2402.17453v2（2024-03-13，cs.LG），ICML 2024，共 34 页。已通读正文 §1–6 和附录 B（任务、案例收集、超参数）、C.1（与 AutoGluon 对比）、C.2（案例研究），数字已对照 PDF 核对，未复现实验。
