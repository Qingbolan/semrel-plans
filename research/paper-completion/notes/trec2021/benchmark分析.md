# 评测与边界

不存在一个覆盖八个 track 的统一总榜。本文报告协议和提交规模，未给出逐模型胜者分数，因此本栏不补造排行榜。各 track 的指标口径如下：

| Track | 指标与口径注意 |
|---|---|
| Clinical Trials | 主指标 nDCG@5/10 对 eligible/excluded 赋 gain 2/1；P@5/10、R-Precision、MRR 仅把 eligible 当正例，二者标签口径不能混用 |
| CAsT | 段落切分库版本导致 ID 不一致，最终按文档判断并对结果去重；深度 7 pool，评价 nDCG@3/5/500、AP@500，而非原计划的段落级评测 |
| Deep Learning | 文档二值正例包含等级 1，段落二值正例只含 2/3；段落 nDCG 又给等级 1 非零 gain |
| Fair Ranking | 结合曝光与相关性 |
| Health Misinformation | 同时考虑有用性、立场正确性和可信度 |
| News | 背景链接主指标 nDCG@5 |
| Incident Streams | 另用 Accumulated Alert Worth |

**边界**：Deep Learning 的 CAL/LOU 分析指出新系统在该集合可能被不公平评价；参赛 top-10 pool 的高精度分数不能证明集合对任意后续模型可复用。

依据：[NIST TREC 2021 proceedings overview，Ian Soboroff，17 页](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)，§2.2、§3.1–3.7，PDF pp.5–15；重点复核 p.10。
