# 评测与边界

**基线：** 各后端原生（LLM 解释式）执行——PZ、LOTUS、Nirvana、DocETL（§3.1、Table 2）。不与其他加速方法（如模型级联、代理模型）比较。

**指标（§3.1，p.4）：** EM 与 F1（只在成功的查询上计算）；LLM 语义等价判分；每查询（QA、SemBench）或每作业（DocETL）的时间与费用，不含评判开销。单算子以与原生输出的 Acc/P/R/F1 一致性衡量（Table 1）。

**单算子（Table 1，p.5）：** filter Acc 0.914/F1 0.890，原生 130.0s vs 编译 28.3s + 执行 1.34ms；map 0.912/0.911，138.7s vs 15.5s；join 0.994/0.961，703.4s vs 22.6s（作者称最高 31.1× 加速）。

**端到端（Table 2，p.6，选摘）：**

| 数据集/引擎 | EM 原生→编译 | 时间(s) 原生→编译 | 费用($) 原生→编译 |
|---|---|---|---|
| ManyModalQA/PZ | 0.633→0.568 | 159.05→13.72 | 0.0184→0.0031 |
| HybridQA/Nirvana | 0.399→0.430 | 661.48→50.68 | 0.2789→0.0180 |
| MMQA/LOTUS | 0.200→0.155 | 23.97→36.12 | 0.0820→0.0120 |
| SemBench/LOTUS | 0.928→1.000 | 8.20→20.42 | 0.0233→0.0042 |
| Steam/DocETL | 0.870→0.686 | 67.98→56.40 | 1.0529→0.0083 |

**消融（Table 3，p.6）：** Prompt v1 在 ManyModalQA+PZ/Nirvana、SemBench+Nirvana 上提升质量，但 SemBench+PZ F1 从 1.00 降到 0.50；强制全编译（All-CX）在 HybridQA 上提升 PZ、Nirvana 的 F1 并降时延，在 MMQA+PZ 上 F1 降 14.9%；Refine+Validate 有时提升（SemBench+Nirvana）有时下降，故默认关闭（§3.4，p.5）。

**阅读者分析：** Table 3 的 “Shared Baseline” 应与 Table 2 的 Ours 相同，但 MMQA 三行和 Steam 行不一致（如 MMQA/PZ 0.425/0.475 vs 0.415/0.467，时间 50.33 vs 38.20；Steam 0.711 vs 0.686），论文未解释。每格似乎是单次运行，未报告方差。
