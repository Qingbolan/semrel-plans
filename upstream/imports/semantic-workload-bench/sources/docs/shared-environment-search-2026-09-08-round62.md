# 第62增量：C3PA原论文与完整仓库，披露标注不等于完整合规

合格保持3/10。C3PA是独立真实隐私政策来源，与OPP115不同；但本次不能据论文标题把其标注直接称为CCPA批准/拒绝或完整合规gold。

[EMNLP2024原论文](https://aclanthology.org/2024.emnlp-main.217.pdf)13页1126207bytes完整下载，SHA256 990be4fe95fbbf6fa29d7ae53a314bf49ca5732c444b941c5a155dc62c50ee2c。[完整作者仓库](https://github.com/MaazBinMusa/C3PA_Dataset)commit d482b942542dc434d3052064504d64133b7f5ab6，31810590bytes ZIP、812条目CRC通过，递归tree非截断、804blob逐个Git SHA1匹配。未运行作者代码或原HTML脚本。

实际发布Annotations：DB230文件27971行，WS170文件18512行，共400政策46483条标注员记录；按(文件,Text,Label)去重39004条。每份CSV都能按README同名编号找到HTML，共400份，无此层join缺失。六位标注员，12种披露标签加Others。论文称411组织和48K+，本轮保留差异，不补造11份或以论文数覆盖当前文件数，也未完成跨DB/WS同网站重复审计。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 提取逐政策响应12类CCPA披露要求的原文，形成审查证据索引 | 论文Table1及section3把标签连接到1798.130等条文；完整历史法规/标注手册尚未下载或在仓库发现 | 400真实政策HTML与crawl表；必须构造保留必要信息的公开文本 | 46483标注员记录；不是46483独立政策或裁决结果 |
| VentiveIQ，DB/223 | Updated Privacy Policy定义 | Last updated: Oct 25, 2022 | ra5标为Updated Privacy Policy；只证明此文字被标为更新日期披露，不证明满足特定评估日的12月更新要求 |

| 类python的DAG | 实际数值/状态 |
|---|---|
| `docs=join(crawl, html, id)` | 按README编号，400annotation文件各有对应HTML；完整URL/日期join尚未核 |
| `provisions=sem_map(policy, frozen_disclosure_schema)` | 原46483记录；唯一(文档,文字,标签)39004；无模型执行 |
| `groupby(policy,disclosure_type).collect(evidence)` | 12标签+Others，当前gold粒度为文本披露类别 |
| `compliant=all_requirements_satisfied(provisions)` | **没有直接gold支持这个节点，不能擅自加入任务或把缺标当违法** |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 日期例目标Updated Privacy Policy；其他披露标签准确性未知 | 固定全文映射、类别定义和文本证据匹配；允许同资源检索 | 同一目标，未预设更好 | ==区分一般联系方式与行使权利的方法；核语句是否回应指定披露要求；保留证据==→标签及文字 | schema索引→披露证据识别→上下文分类→原文校验→政策汇总；未执行或提取 |

论文解释标签集中来自1798.130(a)(5)和相关要求，当前没有证明必须反复理解整部长法规，而非短披露schema即可完成。不能为满足长E条件人为附加无用途的法律全文。论文报告人工训练/一致性改进；尤其一般联系信息是否算行使权利方法曾有争议，需冻结准确规范与gold聚合方式。

仓库只有README/.gitignore及CSV/HTML，未发现独立标注长手册或LICENSE；公开可下载不等于任意再分发许可。原HTML含网站噪声，DB155首条Text=Decline被标收集类别的含义需原文/标注回查，不自动断言错误。未建public快照，没有offset规范/实体去重/历史法规版本绑定或独立确认。无模型、prompt/种子/预算/缓存、作者程序、新工程测试（0）；下载与审计脚本/哈希见artifact/evidence/shared-environment-audit-20260908-v62，原资产见data同名v62。
