# workload

| 子集 | 规模与构造 | 位置 |
|---|---|---|
| QRData-Verified | 原 411 → 质检后 391 → 捷径过滤后 251 | Figure 5，p.6（已渲染核对） |
| DAEval-Verified | 原 257 → 质检后 197 → 捷径过滤后 181 | Figure 5，p.6（已渲染核对） |
| DABStep | 金融多步分析，分 easy/hard；原文列为纳入子集，未见对它做捷径过滤的统计 | §4.1，p.6；Table 2，p.9 |
| DSBio | 90 题：单细胞 56、遗传学 21、空间转录组 13；来自 8 篇论文的数据（多来自 cellxgene） | §4.2，p.7；附录 A.2 Table S1–S2，pp.20–21 |
| MLEBench-Lite | 作为预测基准原样接入 | p.7 |
| DSPredict | 爬取 2017 年后仍可提交的 276 个 Kaggle 竞赛，规则过滤（CSV 提交、数据 < 15GB、有效 ML 题、有排行榜、与 MLE-Bench Lite 少重叠）后得到 Easy 38、Hard 54 | §4.3，p.8；Figure 6，p.7 |
| 合计 | 数据分析 972 题、数据预测 114 题 | Table 1，p.8 |
| DSGym-SFT | 由 QRData 与 DABStep 种子生成 3,700 个候选查询，过滤后 2,000 对查询–轨迹 | §6.2，p.12 |

DSBio 的构造分两类：把论文中的结论转为可执行查询（要求不依赖看图、答案确定），以及专家在 notebook 中深入探索后设计的后续分析题；每题由一名专家起草并给出 Gold Notebook，另一名专家仅凭提示和数据独立求解，二者一致才接受（§4.2，pp.7–8）。

阅读者分析：分析类任务无训练/测试划分，全部作评测；SFT 数据由合成产生，与评测题来源（QRData/DABStep 种子）相近，比较时应注意。

依据：[arXiv:2601.16344v1，37 页](https://arxiv.org/pdf/2601.16344)，§4、§6.2、Table 1、Figure 5、附录 A.2，PDF pp.6–8、12、20–21。
