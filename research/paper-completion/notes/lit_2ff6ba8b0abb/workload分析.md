# 工作负载

| 用途 | 数据集 | 规模/拆分 | 指标 |
|---|---|---|---|
| PRM 训练 | 自建步级标注集 | 7K+ 实例（来自 GitHub 科学数据分析文件 + 合成查询） | — |
| TTS 评测 | ScienceAgentBench | 去掉 ML/DL 任务后保留 78 个数据分析任务 | 成功率 SR；可视化由 Qwen3-VL-235B-A22B 评判 |
| TTS 评测 | DABStep | Easy / Hard 子集分别报告，正文未给题数 | 准确率 |
| RL 评测 | DABench、TableBench | 未给题数 | Qwen3-30B-A3B 评判答案，报告 pass@1 与 pass@3 |
| 先导研究 | DABStep 子集 | 规模未说明 | Best-of-N 准确率 |

（§3、§4.2、§5.1.1，PDF pp.3、5–6）

模型：TTS 策略模型 Qwen3-235B-A22B-Instruct（Table 2 标题写作 -2507）；RL 底座 Qwen2.5-Coder-7B-Instruct。DataPRM 用 ms-swift SFT，lr 1e-5，3 epoch，全局 batch 32；推理温度 0.7、top-p 0.9、top-k 20。RL 用 verl，lr 1e-6，batch 32，β=0.5，组大小 G=4；8×H20 GPU（§5.1.3）。

阅读者分析：工作负载单位是“分析任务的一步”和“带文件环境的多步分析任务”，以 Python 代码执行为主，并非 SQL 查询；任务侧重推理与可视化，作者明确排除了模型训练类任务。

依据：[arXiv 2604.24198v2，12 页](https://arxiv.org/pdf/2604.24198v2)，§3、§4.2、§5.1，PDF pp.3–7。
