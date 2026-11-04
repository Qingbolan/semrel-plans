# 第147轮：GIST候选审核任务的多对一关系与原PDF核验

仍8/15，GIST不重复计数且未qualified。上一轮是下载/原页/版本审计的实质进展。本轮在共享指南下载仍超时期间，完成另一条必要链：原始抽取候选到最终gold的关系验证。

原论文和完整作者仓库已在[第146轮](shared-environment-search-2026-09-08-round146.md)下载及锁定，本轮复用commit `003f412f43af5ea2495d462b9460f1b50a95bc8c`，不重复下载。5个[Zenodo v4文件](https://zenodo.org/records/15124118)本轮移除download参数后均read timeout，收据downloads.json；无活跃下载句柄，不持续空轮等待该站。

新增[作者数据所指AIXTRON2020原始报告](https://www.aixtron.com/investoren/publikationen/2020/en/Sustainability%20Report%202020.pdf)4697666bytes，SHA256 `52032fb6727f7caded0136aeaa6d3e0a001094e4fea119dd9b92510ae1b255a9`。PDF第48、51页已渲染并视觉读取，分别对应印刷47、50页。原件在data/shared-environment-audit-20260908-v147，脚本和收据在artifact/evidence/shared-environment-audit-20260908-v147。

## 关系求证

实际annotation_dataset_updated.csv有5667行，对应5631个merge_id，最新gold有5631个唯一merge_id。5598个ID对应1候选，30个对应2候选，3个对应3候选；33个多行组没有任何整行完全重复组。全部5667候选均能按ID找到gold，且年份/scope一致，报告名匹配gold当前名或旧名；没有孤儿。这个检查证明锁定两文件的关系绑定，不证明所有候选拥有独立最终正确/错误标签。

同名公司复合键直接join仅覆盖4507个gold；换成company_name_old覆盖5585个，剩余46个是名称迁移条件不同（Uniper规范化和旧Vital名称），不是丢失记录。可行构造应以验证过的merge_id连接，同时保留源候选行号和报告实体。不要依赖未核对的公司名重写，也不要将字典覆盖后的单行称一对一连接。

5667候选中553行llm_value非NA，57行标为non_exp_manually_added_record=TRUE。后者来自人工补充，不能作为无泄漏的原LLM候选输入；如构造审核任务，输入allowlist应过滤人工添加并保留真实LLM字段，所有专家判断、纠正值、原因、gold页文本均在private侧。本轮未建快照。

初始诊断曾使用字典观测键覆盖率；发现重复后改为保留所有行的分组版本，当前join_audit.py与join-audit.json是最终审计。没有使用覆盖后的计数作为候选gold统计，没有改上游CSV。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按公司整体Scope1总量口径，审核2019年排放抽取候选并纠正 | AIXTRON2020完整报告，PDF48/51页 | 同一报告/年/scope的两候选：42.8 tonnes，170.8 tonnes；源行index218/219 | 共享指南尚未取得，不能宣称复杂E；论文公开四项口径仅是目前可读规则 | merge_id220最终170.8 tonnes of CO2 equivalents，印刷页50 |
| 汇总正确候选对应的公司年scope值 | 5667原候选行，含57人工添加行 | 5631个目标槽位关系 | gold包含作者修订；原始阶段原因不必等于最终原因 | 553行原字段非NA不等于553个合格值；第一轮644非空gold不等于逐候选标签数 |

| 类python的DAG | 具体数值 | 语义与上下游边界 |
| --- | --- | --- |
| `original_candidates.sem_map(review_and_correct,report,E).groupby(target).resolve()` | 样例42.8→纠正170.8；170.8→保留170.8 | 42.8是公司车辆局部排放，新计算口径的2019列；170.8为2019 Scope1总量。纠正是按最终值派生的期望，不冒充独立原因gold |
| `reports.sem_map(extract_totals,E).explode().project(year,scope,value,unit)` | AIXTRON2019/Scope1=170.8；2020/Scope1=322.84（后者本轮原PDF观察，未另核CSV） | gold页50是印刷页，不可直接调用PDF索引50；工具必须声明页码类型 |
| `join(candidates,gold,on=merge_id,validate='many_to_one')` | 5667→5631目标；33多候选ID，36额外候选行，0孤儿/年月scope报告绑定失败 | 这是构造侧关系诊断，运行器不得执行gold join。不能用当前gold选页当公开检索 |

以下LOTUS/Agent均未运行，不能声称质量差距。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 目标将42.8纠正为170.8，实际输出未知 | 固定检索原报告总量/Scope1段落，读取表格标题与组织范围，再按E判断；可使用相同页面工具 | 同一目标170.8，不预设更准 | ==核对共享口径要求总量而非子类别==→==从车辆表标题识别局部覆盖，再查总排放段落==→输出170.8和证据 | `EmissionCandidateReviewer(candidate,report,E)->status,corrected_value,unit,evidence`；候选行身份与目标身份分离，不写死220/页50 |
| 两候选解析到同一目标，不重复计算两次排放 | 固定程序允许批内报告缓存，保留多候选后去重/解决冲突 | 同样只产生一个目标170.8 | ==核对候选共享目标与重复提及==→确定性分组 | `review -> resolve_target -> normalize_unit`；固定DAG中语义审核重要，分组算术不冒充新语义能力 |

第一位非专家对170.8候选留有irrelevant/not absolute原因，而最终专家讨论值为170.8。因此不能直接将所有非专家原因字段当最终错误原因gold。42.8的两非专家原因均为not related to whole company，原页的公司车辆表支持局部总量解释；仍需指南精确口径与最终原因定义。

## 结论

本轮新增证据证明GIST支持更具体的候选审核构造，但共享规范复杂度、正式发布版关系、全报告访问和许可仍欠账，不增加合格数。不将共享E换成长输入报告，不将大量scope-year槽位当大量独立报告。下一轮转向新的独立可下载来源；GIST保留待站点恢复后补齐指南，避免反复失败下载成为唯一活动。无模型/API预算、无默认运行快照、无正式评分、无测试套件或commit。本轮原报告和gold样例属于开发暴露。
