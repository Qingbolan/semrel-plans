# 第118轮：LCT规范冲突核验，暂停晋级

本轮复用116轮下载的原论文、完整作者仓库/原发布包和完整Wiki Git历史；来源哈希不变。上轮实测版本差异属于进展。当前7/15维持，LCT仍为待定候选，不在可行名单。

## 新证据

Wiki commit656ae3e的Modifier.md把chronic列为Modifier的状态示例；但当前leaf-corpora中，surface严格等于chronic（忽略大小写）的166个span全为Acuteness，acute91个也均为Acuteness。此统计只涉及完整独立span，不覆盖所有包含该词的短语。

具体：NCT03861312“Non-Specific Chronic Neck Pain”中的Chronic[149,156)是Acuteness。当前annotation.conf允许Acuteness-Type-Value=acute|chronic，故不是标签未定义。但Wiki没有对应Acuteness说明页；公开[Acuteness链接](https://github.com/uw-bionlp/clinical-trials-gov-annotation/wiki/Acuteness)实际重定向首页。[Recency链接](https://github.com/uw-bionlp/clinical-trials-gov-annotation/wiki/Recency)也重定向首页。已克隆全部Git历史中的文件名未发现Acuteness/Recency/Medication/Equality-Comparison/Relation.md；这不证明作者私有或其他站点从未存在相应说明。

部分规则能在其他页找到，例如Eq-Comparison.md包含Temporal-Recency定义、Drug.md包含药物定义，所以不把所有断链等同于全部规则缺失。真正待定的是规范冲突的优先级和完整规范冻结，而非简单补链接。

原论文Methods明确标注员使用UMLS浏览器查不清楚的概念，并在组合span裁决例中用UMLS概念存在性决定边界。当前未得到确切历史版本，不可把任意当代词表替换进去后称完全复现。模型常识也不能自动当作锁定环境。

## 请求的三表（诊断候选，不是新增可行湖）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 抽取条件的病程修饰及所修饰的事件 | 1006真实条件文本 | 共享Wiki的Modifier页面把chronic作Modifier例 | 当前annotation.conf定义Acuteness=acute/chronic；缺独立说明页 | NCT03861312 Chronic[149,156)→Acuteness；不得用当前gold倒写公开规范 |
| 抽取完整医学概念边界 | 同批文本 | 原论文提到使用UMLS查词和合并概念 | 历史UMLS版本尚未取得 | 117轮back pain原/现版本边界不同；尚无统一版本契约 |

| 类python的DAG | 具体数值 | 关键输出 | 下游gold边界 |
| --- | --- | --- | --- |
| `trials.sem_map(extract_graph,E).explode(spans).filter(type=='Acuteness')` | 当前272个Acuteness span；其中完整chronic166、acute91 | 保留原文偏移及角色，不把全部修饰词自动归类 | 272为源gold统计；未建立可运行public快照或模型成绩 |
| `trials.sem_map(extract_graph,E).project(concept_spans)` | 1006输入；原/现43份标注文件不同 | 规范版本与优先级需先固定 | 不能因Wiki遵循结果与当前gold不一致便宣称静态质量差距 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；Wiki与配置的优先级未冻结时结果无唯一预期 | 同E语义调用→公开schema校验；校验能查合法标签但不能解决chronic规范冲突 | 未执行；不预设Agent能正确选版本 | ==核对Modifier例与Acuteness配置== → ==记录规范冲突== → 按预先冻结契约处理；不能查private答案决定 | `extract_graph(text,E_version,precedence)`；优先级缺失不是由训练gold自动填补的分支 |

两方法必须同资源比较。当前不需要追加推理实验来证明这个已发现的输入契约缺口；也不因此否定LCT作为普通信息抽取数据集的用途。长共享环境必要性和单轨迹提取价值仍未成立。

证据：artifact/evidence/shared-environment-audit-20260908-v118/norm-audit.json；执行记录包含只读扫描与Git历史命令。无新下载/构造、无模型调用、无新增单元测试或commit。下一轮转向其他独立候选，LCT待取得完整一致规范后再恢复，避免不断检查文件而不改善资格证据。
