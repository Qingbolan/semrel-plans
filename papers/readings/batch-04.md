# 第四批原论文解析

完成两篇，累计 24 篇，剩余 426 篇。状态均为 READ；未进行独立复核，也未复现实验。

| 论文 | 七栏解析 | 已核对的关键边界 |
|---|---|---|
| CLEF 2019 TAR | [阅读卡](notes/clef2019-tar/README.md) | 31 测试 topic，123 开发/测试 topic；Task 1 无提交，Task 2 为 36 runs；摘要相关与全文相关不同，标签受原布尔检索候选集限制 |
| TREC 2021 Overview | [阅读卡](notes/trec2021/README.md) | 八个 track 各有输入单位和指标；CAsT 改为文档评测，DL 57/53 密集判断 topic 并非全部 477 测试问题 |

全文已经保存，SHA256、版本、阅读章节和逐条页码见 reviews.json / sources.json。CLEF TAR 阅读正文和所引用附录统计/结果，未声称逐行审计所有附录运行。TREC 2021 阅读全部 track 正文；该综述不是完整 topic 数据包，也不是逐模型排行榜。

获取过程：CEUR PDF 直接成功；NIST PDF 首次 HTTP 403，添加常规浏览器 User-Agent 后成功，失败与成功均保留在 acquisition-batch-04.json。

视觉核对：CLEF TAR PDF p.16 Table 9；TREC 2021 p.10 的标签和复用限制。没有借后续系统论文补造这两篇综述未报告的结果。已有来源 ID 及查询关系不作改写。

第四批验证：8 项论文测试通过；24 份全文哈希一致，来源收据审计无错误；页面重建与 4,656 条查询完整性检查通过，43 篇论文的查询关联保留。未提交或推送。
