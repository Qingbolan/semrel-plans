# 第十九增量：CIViC历史版本审计

本轮是来源补证，不新增独立数据湖。复用第十八轮已下载原论文及完整官方仓库，新下载[官方2021-04-01快照](https://civic-aws-opendata.s3.us-west-2.amazonaws.com/01-Apr-2021/01-Apr-2021-ClinicalEvidenceSummaries.tsv)，4,203,379 bytes，SHA256 `3a31ae791e952d050073fa3af689408577b3587ca7ab9f41c8285f9ad4049d64`。原材料在`data/shared-environment-audit-20260908-v19/`，可重跑脚本/统计/私有字段差异/收据在`artifact/evidence/shared-environment-audit-20260908-v19/`。

结论：旧快照并不能自动解决规范版本绑定。2021快照3753条全部accepted，与2026快照共有3730个ID；1250个共有ID在所检查字段中至少一处文字变化。571个significance、130个direction、35个level、104个rating、3个citation_id变化。**这是字段差异，不是1250个错误**：571个significance变化中395个是Uncertain Significance→Predisposition，很多反映模型迁移。当前官方[策展规范](https://docs.civicdb.org/en/latest/curating/evidence.html)明确讨论v1/v2 Predisposing模型差异。23个旧ID在新文件缺失不能直接解释为被拒绝。

旧快照2610条last_review_date早于论文发表日2019-11-29；不证明它们不合规范，也不能证明按该版本规范策展。KIT EID2477所选字段前后未变，旧审核日期2019-02-08。尚需使用实际适用的规范版本或冻结当前规范并审计相关标签映射。不能通过选择“没变化的标签”来获得无偏确认集。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 根据冻结CIViC规范，为profile/disease/therapy/source生成证据集合，并筛选支持Reduced Sensitivity项 | 2019论文+61页补充规范，已下载；当前规范网页可读但本地HTTP403 | 2021完整3753条accepted，其中Predictive2382；与2026同一湖，不计第二湖 | KIT PMID18955451摘要已在v18；本轮欧洲PMC全文XML返回404，PMC网页为验证码，未绕过 | 两快照标签分别保留，禁止把variant_summary/evidence_statement等策展产物当无标签原文 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `old.join(new,on=evidence_id).compare(selected_fields)` | 3730共有ID，1250有至少一个所查字段变化 | 构造侧诊断，禁止提供被测系统 |
| `normalize_schema(version).group_by(query).sem_map(curate,E)` | 旧3753/新4906条，尚未做语义等价映射 | 未执行预测；不能直接合并 |
| `sem_filter(Supports & ReducedSensitivity).project(id).count()` | KIT2477前后均Supports/B/Reduced Sensitivity | gold只是目标，不是方法输出 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| KIT例目标仍为B/Supports/Reduced Sensitivity，未实测 | 使用同一冻结规范与原始论文，固定抽取比较对象并分类；构造端先确定版本 | 同一目标，不能预言优于LOTUS | ==查冻结规范的比较情境==→==分离论文中的跨变异和跨剂量证据==→输出集合；不可访问前后gold差异表 | `CurationOperator(E_hash,schema_version,comparison_extractor,label_set,abstain)`；版本由构造确定，不让Agent根据gold猜测 |

本轮读取发现的CIViC Evidence摘要分类论文2407.04466只用于定位已有相关研究，没有下载其仓库/论文、没有列为新合格任务、没有引用其模型指标。后续可用作固定分类对照来源，但不能冒充本次实测。

当前仍未完成十湖目标。接下来优先重新核对CGBench现有完整输入与官方SOP的具体规则依赖：**数据可行性与方法优势是两个门槛**。用户要求求证数据结构及预期方法，不应额外要求先证明Agent优势才能承认数据湖可行；但输入缺失、任务不明确和gold来源不明仍必须解决。
