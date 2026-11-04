# 第三批原论文解析

完成两篇，均为 READ（单人阅读、自查）；累计 22 篇，剩余 428 篇。

| 论文 | 阅读入口 | 关键边界 |
|---|---|---|
| CodiEsp | [七栏解析](notes/codiesp/README.md) | 1,000 篇金标准；测试 250 篇；3,001 篇提交包含背景集合；不同指标/运行不能混用 |
| Veterans Semantic Types | [七栏解析](notes/veterans-semantic-types/README.md) | ICAIL 2017 预出版稿；20 份决定、5,674 句；类型体系与频次分析，没有分类器性能实验 |

## 来源核对

- 原 Veterans URL `https://ceur-ws.org/Vol-2385/paper1.pdf` 的标题是 Automatic Classification of Rhetorical Roles for Sentences: Comparing Rule-Based Scripts with Machine Learning（2019）。下载件保留为被拒绝的来源证据，不计 READ。
- 目标 2017 年作者主页 PDF 请求返回 403；作者 LLTLab/VetClaims 仓库成功获取。当前 `catalog/sources.jsonl` 的来源地址、出版年份和版本已纠正，既有 `swb_561a653983f0f575` source_id 保持不变，避免丢失派生查询关联。历史导入/注册资料中旧链接作为原始记录保留，本次来源更正以当前来源表和收据为准；重新导入历史快照时须保留此更正。
- DrugProt 当前目录实际指向 2023 Database 文章（baad080），入口返回 HTTP 418。搜索到的 2021 会议综述既请求返回 403，又不是同一目标版本，因此未使用。已发现 2023 年机构仓库候选入口，下一批继续获取；不能把暂未获取说成全文不存在。
- 获取结果在 `acquisition-batch-03.json`，完成项及逐条证据在 `reviews.json` / `sources.json`。没有独立复核，不能标 EVIDENCE_CHECKED。

## 人工检查

渲染核对 CodiEsp PDF pp.9、12、18（Tables 4、7、8）及 Veterans p.9（Table 3）。CodiEsp 摘要 168 runs 与正文分项总计 167 不同；句子/token 数也有两套统计，均在 workload 栏标明。

第三批校验完成：8 项论文测试通过；来源收据审计无错误，22 份全文哈希一致。页面重建及完整性校验通过，当前工作区为 4,656 条查询、43 篇有查询关联的论文（已纳入工作区既有的查询扩充）。本批两篇关联均保留；未提交、推送。
