# 工作负载

| 数据集 | 任务 | 评测样本数 | 语料/检索器 | top-k | 示例数 | 指标 |
|---|---|---|---|---|---|---|
| 2WikiMultihopQA | 多跳 QA（含 CoT） | 500 | Wikipedia / BM25 | 2 | 8 | EM、F1、Prec.、Rec. |
| StrategyQA | 常识推理（是/否，含 CoT） | 229 | Wikipedia / BM25 | 3 | 6 | EM |
| ASQA、ASQA-hint | 歧义问题的长答 QA | 500 | Wikipedia / BM25 | 3 | 8 | EM、Disambig-F1、ROUGE、DR |
| WikiAsp | 开放域方面摘要（20 个领域） | 500 | 开放网络 / Bing | 5 | 4 | UniEval、实体 F1、ROUGE |

（Table 7，p.16；§5，p.6）

**采样与构造**：

- 因成本原因，沿用 Trivedi et al.（2022）的做法从每个数据集最多子采样 500 条（§5，p.6）。
- Wikipedia 语料用 Karpukhin et al.（2020）的 dump（§3.3，p.5）。
- ASQA-hint 是作者新建设置，为每题加一句歧义方向提示（§5，p.6）。
- WikiAsp 原为多文档摘要，作者去掉给定参考文献改为开放网络检索，并从 Bing 结果中排除 wikipedia.org 等 4 个 Wikipedia 相关域名以防泄漏（附录 B、Table 8，pp.14–16）。
- 只有 2WikiMultihopQA 为示例也附检索文档（Table 7）。

**超参**（Table 9，p.16）：θ 在 StrategyQA 为 0.4，其余 0.8；β 均为 0.4；多跳 QA 与 StrategyQA 用隐式查询，ASQA 与 WikiAsp 用显式查询并合并单次检索结果。

依据：§3.3、§5、附录 B–C、Tables 7–9，PDF pp.5–6、14–16。
