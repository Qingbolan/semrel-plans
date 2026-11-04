# 第二十八增量：USClassActions 的真实诉状与结果语义

**累计仍1/10，本候选不计入严格合格清单。** 本轮从劳动争议检索进入包含FLSA案件的USClassActions，下载原论文、完整代码仓库及完整公开3,000条数据。其输入来源比裁决全文更接近实际预测时点，但标签合并了和解、无争议撤诉与其他裁决。不能据此建立“共享规范决定案件是否符合条件”的gold。

## 下载和实际核验

| 来源 | 本次取得 | 可复核位置/版本 |
|---|---|---|
| [原论文 ClassActionPrediction](https://arxiv.org/abs/2211.00582) | PDF16页，正文已提取 | `data/shared-environment-audit-20260908-v28/paper.pdf`；版本v1 |
| [完整作者仓库](https://github.com/darrow-labs/ClassActionPrediction) | ZIP完整解压、5个Git blob逐项SHA1验证 | commit `2094d324b8bd4f91ae6f401620c4fa14678d2856` |
| [完整公开数据](https://huggingface.co/datasets/darrow-ai/USClassActions) | 28,644,066 bytes CSV，SHA256与HF LFS一致 | revision `f0f1642c872cb3fe346c1805b06c7f72900255f7`；SHA256 `31c2a13416120f9603574c0e6ad3a0455700472e7034fd89edda3d04f140158e` |

所有下载URL/字节/hash见`artifact/evidence/shared-environment-audit-20260908-v28/downloads.json`。原始文件在data同名目录，审计脚本`audit_data.py`与`statistics.json`在artifact同名目录。代码仓库LICENSE与HF卡片标记GPL-3.0，不据此推导所有原始诉状具有同一许可。未执行作者notebook、未调用模型。

实际CSV：3,000行、3,000唯一ID；1,523 win、1,477 lose；只有`id,target_text,verdict`三列。2,997种唯一文本，四个空输入ID为13731、282064、29352、262400。空输入之外的文本唯一；未见相同文本异标签。按空白切词min0/median1191.5/max7137，非模型tokens。公开包不等于论文全部约10.8K案例，不将其总量或标签细分统计套到这3,000条上。

## 为什么不符合当前任务

原论文Table1明确将Settled归win，将Uncontested Dismissal与Motion to Dismiss归lose；其全论文样本中和解5,234条、无争议驳回4,544条。前者是双方结束争议的结果，不是法院对实体要件成立的独立认定。全文Table1计数和§4.3二分汇总还存在两条差额，本文不调和为新的计数；本轮公开样本计数直接来自CSV。

论文§4.2说明通过正则抽取诉状事实和主张并清洗。因此发布的`target_text`不能称为完整诉状及附件。抽样319755含居家护理员工自2017年任职、每周超过40小时但仍按普通小时工资支付的主张，标签win。现有字段无法知道这一例的win来自和解还是实体判断，也不能把单方“non-exempt”主张当作已认定事实。

法律环境可以影响实体评价，但在此只能提出待建的新任务，不能把原win/lose换名成“依法应获胜”。公开文件没有细分结果、裁决正文、原始案号/法院/裁决日期等独立列；正文可能包含部分信息，尚无足够的全量可验证映射。没有下载一个通用长法规来填补此语义缺口。

## 三表：阴性候选的具体例子与构造边界

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 原任务：根据诉状预测最终win/lose | 3,000条诉状事实/主张摘录 | 未提供共享冻结policy或规范版本 | 未提供逐案细分终结方式/完整证据包 | 1,523 win / 1,477 lose，含和解映射，不能作为合规结论 |
| 拟议批任务：筛选依同版FLSA应获加班工资救济的请求；例319755 | 居家护理业务、原告自2017年任职、每周超过40小时、超时仍按直线工资支付的主张 | FLSA及适用豁免/雇佣关系/时效规则需要另建版本明确E，当前未取得 | 单方诉状摘录，不含已验证答辩/附件和完整事实认定 | 319755原标签win；实体规则gold未提供，不能转写为应获救济True |

| 类python的DAG | 具体数值 | 结论 |
|---|---|---|
| `scan(released_csv)` | 3,000条，4空输入 | 原始质量问题保留；空输入不可默认为lose |
| `resolve_law_version_and_case_outcome()` | 公开只有3列，细分结果未发布 | 无可验证的全量连接，不构造伪造的共享E任务 |
| `sem_map(predict_final_outcome).filter(win).count()` | 参考标签win=1,523 | 可做原预测问题，不等价于规范依赖的合规批任务 |
| `sem_map(apply_flsa).filter(relief_due).count()` | 输出总数未知 | 需要新gold；不得用原win标签评分实体规则正确率 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 原预测任务的319755参考为win，实际未运行；实体规范任务无已验证正确答案 | 固定抽取雇佣关系、工作周时长、工资计算与豁免主张；若执行法律任务须补齐同版E和相同证据；不能由win监督反推正确法则 | 不能预言更准确，也不能把事后和解原因补成既知事实 | ==核对输入是单方主张还是已认定事实==→==定位规范版本、豁免及缺失事实==→标记事实不足；不能借本案结局解释预测 | 条件性的`OvertimeEligibilityOperator(E_version, attributed_facts, employee_scope, exemptions, unpaid_hours, abstain)`仅是待建任务结构；不是从本轮轨迹学到的算子 |

本轮没有模型推理、冻结算子或独立确认；上述是比较设计边界。若未来获得逐案细分裁决及充分事实，才能重新审定；在此之前不纳入10湖清单，也不把缺证据造成的错误当成LOTUS能力不足。未新增源码/工程测试，脚本完成来源与结构审计。
