# 第54增量：CHEMDNER 完整源核验，暂不计入合格

本轮取得新独立来源，合格保持2/10。任务是化学文献索引，关键sem_map输出实体位置与类型；不是临床决定。尚缺规范差异、实例依赖和公开构造审计，不把下载完成称为VALIDATED。

原论文[CHEMDNER corpus](https://doi.org/10.1186/1758-2946-7-S1-S2)17页2316173bytes已下载。作者Krallinger于2015上传的[完整数据仓库存档](https://mldata-static.ml.tu-berlin.de/repository/data/viewslug/chemdner-task-of-biocreative-iv/index.html)19,195,061bytes、23 tar成员全量解压，SHA256 950b2e9f502dd3de65d45b6561d4ab4150a9e3411f185e2645c3a0ab4bd84a60。它是作者发布包，不冒称Git代码仓库。原BioCreative站403。

包内2013规范25页502244bytes，SHA256 8295235dbda446d486309aeb8203457858120f34fbcd639ac2f84b186ffdca17；[后来公开规范](https://zenodo.org/records/4957519)24页732478bytes，去空白文本不同，不能静默互换。规则涉及小肽、聚合物、一般概念、非连续名称与边界，不仅七类名称。尚须核对具体差异及规则在真实记录中的作用；长上下文必要性未实测。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 为每篇摘要建立化学实体提及清单及文档索引 | 随源发布25页共享规范 | 10000篇标题+摘要；train3500/dev3500/test3000 | 84355个位置、文本、类型标注；CDI另有文档索引gold |
| 具体开发例PMID22732443 | 化学标识符与提及边界规则，待逐条对应 | 摘要中selective GluN2B antagonist Ro25-6981 (6 mg/kg...) | A[538:547]=Ro25-6981，IDENTIFIER |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `docs=scan(reviewed_abstracts)` | 10000人工审核；test原文件另有17000背景摘要，不能当人工负例 |
| `mentions=sem_map(docs, bundled_protocol)` | gold train29478/dev29526/test25351；全部偏移切片与文字匹配，无跨split PMID重复 |
| `index=mentions.groupby(doc_id).unique(surface)` | 可对照CDI gold；本轮尚未核其精确投影一致性 |
| `score(mentions,index,private_gold)` | 未执行模型；113个NO CLASS应明确评分语义，不能强映射七类 |

| 预期关键语义算子直接交给LOTUS的结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 例目标Ro25-6981及其位置；实际质量未知 | 固定sem_map读取完整摘要及同一规范，允许规则检索、字符验证、缓存 | 同一目标，未预设优于固定流程 | ==查实体范围与排除规则；查特殊边界；验证输出字符切片==→提及列表 | 规范索引→范围判断→跨度解析→类型判断→字符校验→文档聚合；尚未学习或冻结 |

来源与脚本在data/shared-environment-audit-20260908-v54及artifact/evidence/shared-environment-audit-20260908-v54。初次审计用splitlines会误把正文Unicode行分隔符当记录边界，改为源TSV物理换行解析后全量通过；未修改源文字或偏移。无模型运行/作者代码执行/新工程测试。许可页面标unknown，需核来源文件及使用条件；论文开放许可不自动覆盖全部摘要。未建public/private快照、未做示例/近重复隔离、无环境消融或成本结果。
