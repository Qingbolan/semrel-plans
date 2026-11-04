# 评测与边界

**比较方法**（§4.2）：
- CAESURA：作者在 ArtWork、RotoWire 上复现，用 GPT-4o 做规划、数据处理、绘图，VQA 用 BLIP-2，文本问答用微调 BART；规划时用 4-shot。
- NeuralSQL：EHRXQA 作者提供的 GPT-4o 结果（同一组 100 题），LLM 一步生成含 VQA 调用的 SQL，VQA 用 M3AE。
- M2EX：零样本；ArtWork 的 VQA 同样用 BLIP-2，RotoWire 文本分析用 GPT-4o，EHRXQA 用同一 M3AE。
- CAESURA 未在 EHRXQA 上评测：在 18 张表的发现阶段反复失败，超过最大尝试次数后终止（§4.4）。

**指标**（§4.3）：准确率（与 gold 精确匹配，或人工专家判定）、步数、token、端到端延迟、API 费用，以及是否生成正确计划、是否支持重规划。

**实验 1（ArtWork / RotoWire，Table 1 合计行）**：

| 数据集 | 系统 | 准确率 | 步数 | Token | 延迟 [s] | 费用 [$] |
|---|---|---|---|---|---|---|
| ArtWork（30） | CAESURA | 33.33% | 316 | 482,932 | 5,821.23 | 2.98 |
| ArtWork（30） | M2EX | 63.33% | 203 | 485,612 | 3,040.12 | 2.10 |
| RotoWire（12） | CAESURA | 25.00% | 157 | 233,507 | 1,459.69 | 1.50 |
| RotoWire（12） | M2EX | 66.67% | 76 | 1,042,196 | 3,760.02 | 3.62 |

ArtWork 多模态题上两者都弱：CAESURA 6.67%，M2EX 26.67%；单模态题 M2EX 为 100%。RotoWire 上 M2EX 因 GPT-4o 文本分析，token、延迟、费用都更高（§4.4）。

**实验 2（EHRXQA 100 题，Table 2）**：

| 系统 | Image Single-1 (30) | Image Single-2 (30) | Image+Table Single (40) | 二值 (50) | 分类 (50) | 总体 |
|---|---|---|---|---|---|---|
| NeuralSQL 零样本 | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% |
| NeuralSQL 10-shot | 26.67% | 20.00% | 47.50% | 48.00% | 18.00% | 33.00% |
| M2EX 零样本 | 23.33% | 43.33% | 77.50% | 74.00% | 28.00% | 51.00% |

正文把 77.50% 称为“multiple-table queries”，表中对应的是 Image+Table Single 类；M2EX 在 Image Single-1 上略低于 NeuralSQL（阅读者分析）。M2EX 生成计划的覆盖率为 98%。

**实验 3（错误分析，Table 3、附录 E）**：

| 数据集 | 系统 | 错误/题数 | 主要错误来源 |
|---|---|---|---|
| ArtWork | CAESURA | 20/30 | 计划错误；VQA 错误 |
| ArtWork | M2EX | 11/30 | 仅 VQA 错误 |
| RotoWire | CAESURA | 9/12 | 文本分析；SQL 错误 |
| RotoWire | M2EX | 4/12 | 文本分析 |
| EHRXQA | M2EX | 49/100 | VQA 错误（其中 36 个在分类题） |

CAESURA 在 6 道并行题上全部在规划阶段出错：2 题没有计划，4 题只给出部分子任务结果（附录 E）。

**边界**：
- 原文 Limitations：VQA（M3AE）是持续的错误源，分类题尤甚；未尝试其他视觉模型；只用 GPT-4o；RotoWire 多模态题错误主要来自文本理解。
- 阅读者整理：题量小，单题影响 3–8 个百分点且无方差或重复运行；RotoWire 对比混入了文本工具差异（GPT-4o 对 BART）；“token 降 18%”与 Table 1 合计不符（见“贡献与评价”）；可查看的中间步骤不等于解释忠实，论文未度量解释质量（阅读者分析）。

依据：[arXiv 2412.18428v2](https://arxiv.org/abs/2412.18428v2)，§4.2–4.5、Limitations、Tables 1–3、附录 E，PDF pp.6–9、17–18。
