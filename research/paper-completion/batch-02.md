# 第二批：原论文阅读索引

2026-10-14。10 篇均与现有查询关联，状态 READ，仅单人阅读与证据自查。本表帮助选择适合的任务设定，不对跨任务论文做优劣排序。实际模型输入、数据单位及比较条件见各篇分栏。

| 论文 | 原论文实际任务 / 输入 | 接入查询时必须保留的边界 | 证据 |
|---|---|---|---|
| [CAIL2018 数据集](notes/cail2018/README.md) | 案件事实 → 法条、罪名、刑期 | 标签来自结果段，结果段不能混进事实输入；准确率与宏召回不同 | cail2018:E02/E06，PDF pp.2–3 |
| [CAIL2018 竞赛](notes/cail2018-overview/README.md) | 同一事实的三个预测子任务 | 第二阶段 35,922 份新文书；刑期是分段评分 | cail2018-overview:E04/E06，PDF pp.2–4 |
| [ShARC](notes/sharc/README.md) | 已给定规则、情境、历史 → 答案或追问 | 逐轮指标不是整个对话成功率；不包含法规检索 | sharc:E02/E06，PDF pp.2–3、6–8 |
| [CASIE](notes/casie/README.md) | 安全新闻 → 事件触发、论元、角色、现实性 | 多次提及不等于多个独立事件；共指和图谱整合未在本文完成 | casie:E02/E05/E06，PDF pp.2、6–8 |
| [ChEMU-Ref](notes/chemu-ref/README.md) | 反应描述片段 → 提及与有向指代/桥接链接 | 220 个已评测片段与未来 1,500 片段计划分开；oracle mention 单列 | chemu-ref:E04/E06，PDF pp.5、7–9 |
| [STAC](notes/stac/README.md) | 多人聊天 → 对话行为与话语图 | 保留 EDU/CDU、关系边/成员边差异；不能把转换后图当作原始标注 | stac:E02/E03/E06，PDF pp.3–6 |
| [PARSEME 1.2](notes/parseme12/README.md) | 句子及形态句法 → 多词表达实例 | unseen 相对于 train+dev；闭合与开放赛道分开 | parseme12:E02/E06，PDF pp.2–4、6、8–9 |
| [MAVEN-ERE](notes/maven-ere/README.md) | 文档及给定触发位置 → 四类事件关系 | 文档数与边数不同；包含规则补全关系；限文档内 | maven-ere:E02/E04，PDF pp.3–6、9、16 |
| [FrameNet](notes/framenet/README.md) | 目标义项与例句 → 框架语义资源 | 1998 年建设实绩与未来目标分开；没有模型基准实验 | framenet:E04/E06，PDF pp.1、5 |
| [DeepPCB](notes/deeppcb/README.md) | 配准模板/待测图对 → 缺陷框与类型 | IoU>0.33；含人工增加缺陷；模型 FPS 不等于产线吞吐 | deeppcb:E02/E04/E06，PDF pp.2–4 |

## 来源获取

原文取自 ACL Anthology、arXiv 和 CASIE 作者机构。实际下载 URL、时间（Asia/Singapore）、SHA256、可解析页数保存在 `acquisition-batch-02.json`；全文与提取文本分别在 `papers/` 和 `text/`，发布收据在 `reviews.json`。论文事实根据本地原文阅读，不从搜索摘要推断。

本轮网络检索用于核对 CASIE 正式发表来源及 ChEMU-Ref 官方全文，精确查询为：

- `CASIE Extracting Cybersecurity Event Information from Text IJCAI 2019 pdf`：结果定位到 AAAI 2020；以取得的论文首页修正年份/会议，未沿用查询中的年份和会议假设。
- `ChEMU-Ref A Corpus for Modeling Anaphora Resolution in the Chemical Domain acl`：定位到 ACL Anthology 2021.eacl-main.116 的正式全文。

同时访问 ShARC、CAIL 两篇、STAC、PARSEME 1.2、MAVEN-ERE、DeepPCB、FrameNet 的官方论文页核对身份。本轮其余候选保持待补，没有因本次未选入而标记为不可获取。
