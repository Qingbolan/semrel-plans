# 工作负载

**队列**（Fig. 2a；列为病例数 / 平均词数 / 试验库规模）：

| 队列 | 来源 | 病例 | 平均词数 | 试验数 | 评审方式 |
|---|---|---|---|---|---|
| OPR | NIH 患者招募电话记录 | 19 | 22 | 1,373 | top-ranked |
| CCF | 胆管癌基金会咨询 | 10 | 33 | 649 | top-ranked |
| UIC | 肿瘤委员会转诊 | 15 | 194 | 1,871 | top-ranked |
| UPMC | 社区放疗会诊 | 144 | 987 | 17 | top-ranked |
| NCI | 免疫肿瘤转诊 | 100 | 325 | 9 | 穷尽评审 |
| UIC 前瞻 | POTB 实时病例 | 27 | 168 | 1,871 | 前瞻评审 |
| NIH-TrialBench | 合成病例 | 126 | 116 | 1,373 | top-ranked |

回顾性评测共 288 例、1,340 个患者–试验对：前四个队列 440 对，NCI 900 对（PDF pp.3、8）。前瞻性评测 27 例、339 个系统候选；NIH-TrialBench 有 990 个已评审对（PDF pp.10、12）。

**公开基准**：SIGIR 58 例 / 3,835 个已判对，TREC 2021 75 例 / 35,832 个，TREC 2022 50 例 / 35,394 个；只在已判对内排序，不做首轮检索（PDF pp.24–25）。

**标签**：Recommended / Eligible but Not Recommended / Ineligible。NCI 的原始标签另行映射到三类输出（PDF pp.19–20）。

依据：[arXiv:2609.01202v2，44 页](https://arxiv.org/abs/2609.01202)，Fig. 2a、Results、Methods，PDF pp.3、5–8、10、12、18–25。
