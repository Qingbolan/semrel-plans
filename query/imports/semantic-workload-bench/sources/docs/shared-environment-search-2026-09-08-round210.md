# 增量210：PARSEME作者说明与法语扩展资源

仍12/15。本轮补下[1.1原论文](https://aclanthology.org/W18-4925.pdf)，445997bytes，SHA256 `554fc7c5ef8366d3ba0b6a0220e29830839cd628530f8bc3b4834866768aa064`；此前已下载1.2/1.3论文。本轮完整克隆[法语项目Wiki](https://gitlab.lis-lab.fr/PARSEME-FR/PARSEME-FR-public/-/wikis/home)，commit `0093ac356a326fe4e2be280175a7c71fea89bab0`，19个tracked文件。完整项目主仓库也成功取得，但只有README，不能把README所述corpora当成已下载数据。

原件在data/shared-environment-audit-20260908-v210，完整hash/克隆收据在[210证据目录](../artifact/evidence/shared-environment-audit-20260908-v210/)。没有认证、联系作者、发布或改写原文件。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 当前动词表达发现/分类 | 208视图20708句 | PARSEME1.1规范 | 法语Wiki明确将动词表达指回1.1 | 5639表达，MVC22的规则表述差异未闭合 |
| 扩展候选：非动词表达→类别与判定依据 | 尚未取得对应批量语料；主仓库只有README | Wiki中词汇、语义、形态句法等标准 | 原格式CRITERIA字段允许记录CRAN/ID/PRED/LEX等人工判定依据 | 目前只有格式说明，不能声称已获得批量依据gold |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `sentences.sem_map(find_and_type,E).explode()` | 当前开发视图20708句/5639表达 | 既有源结构已核验，模型未执行 |
| `nonverbal_items.sem_map(type_and_criteria,E)` | 19个Wiki源文件；语料数量未知 | 仅可行性线索，不能注册新任务或新湖 |
| `outputs.groupby(criterion).count()` | 类别/依据字段有官方格式定义，实际分布未知 | 必须先取得真实标注并验证覆盖率 |

当前具体源例沿用faire valoir[40,41]→MVC。扩展项目格式给出的`ADP|MWE|IRREG`表示介词性非动词表达、使用IRREG依据；这是作者格式示例，不是新下载语料的实测记录。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 当前例[40,41],MVC为gold目标，未实测 | 固定检索规范→映射→typed校验 | 同目标，未实测 | ==核对版本及MVC两段规则==→按预先冻结的冲突契约输出/ABSTAIN | 版本化规则索引与分类器；未提取 |
| 扩展任务的类别+依据集合，真实输出未知 | 固定标准索引→多标签映射→聚合 | 同目标，未实测 | ==查词汇/语义/形态句法依据及适用条件==→映射→聚合 | `CriteriaResolver + MultiLabelEmitter`，仅待数据验证的设计 |

1.1原论文结论明确提到MVC规范存在需改进之处。此说明支持保留审查缺口，但不是针对209所见两个问题的专门勘误，不能据此选定优先级。法语Wiki说明非动词表达是其扩展重点，动词表达仍采用外部1.1；因此不能将Wiki新规则直接覆盖原5639动词表达gold。

有价值的新线索是CRITERIA字段：格式说明其针对非动词表达由标注者填写，动词表达与命名实体此字段未指定。它可能支持依据级评价，但本轮尚未拿到承载这些字段的批量语料。后续查对应正式发布与论文；仍不计新湖。没有模型执行、资源必要性实验或独立确认。
