# 增量157：WikiEvents完整原始发布已下载；缺任务绑定的长规范

新来源为NAACL2021 WikiEvents，不是同名Wikipedia Current Events知识图谱。状态`SOURCE_ACQUIRED_NATIVE_AUDITED_ENVIRONMENT_PENDING`，仍8/15。没有将模板集合的规模冒充复杂长环境。

## 来源与下载

[原论文](https://aclanthology.org/2021.naacl-main.69.pdf)：734056 bytes，SHA256 `4d87666bde11692894956f770448991aba350083d9da41216692c5b5e7b9b775`。

[作者完整gen-arg仓库](https://github.com/raspberryice/gen-arg/tree/253e0889b2377e0f7084cb406cf5d4142ee8a365)：commit `253e0889b2377e0f7084cb406cf5d4142ee8a365`，ZIP447784 bytes、43成员CRC通过，SHA256 `b589ed2799fc36a802a32946d90ea5215b7764d6b114a0ec77e4bc04dd9a350f`。

作者README指向S3发布。成功列举并下载wikievents/下全部9个非空对象：train/dev/test.jsonl、对应_info.jsonl及3个coref文件，共28455412 bytes，所有大小与S3清单一致。原件位于`data/shared-environment-audit-20260908-v157/`，下载哈希见`artifact/evidence/shared-environment-audit-20260908-v157/downloads.json`和`data-downloads.json`。不包含同S3的模型checkpoint，亦未声称下载整个S3桶。完整代码repo与完整wikievents数据前缀已取得。

## 本次原生观察

| 原生split | 文档 | tokens | 实体 | 事件 | 论元 |
| --- | ---: | ---: | ---: | ---: | ---: |
| train | 206 | 162603 | 28296 | 3241 | 4542 |
| dev | 20 | 12875 | 2256 | 345 | 428 |
| test | 20 | 14240 | 2673 | 365 | 566 |

合计246文档3951事件5536论元。doc ID跨split无重叠，不等于同事件新闻/近重复/训练污染隔离。实体与触发token范围、论元entity_id引用检查无失败；仅验证索引，不声称原文token拼接逐字节还原。

普通与informative版本246篇text/tokens完全相同；按发布顺序对事件字典比较1713项变化。尚未核对所有变化原因/事件排序一致性，不能将1713直接称“成功消歧数”。coref文件已全部下载，但本轮未审计簇引用及most-informative绑定。两个任务是同一湖的不同视图。

仓库event_role_KAIROS.json有51类，字段为event_id/template/i-label/keywords/roles/role_types，模板合计685空白词；没有详细definition字段或独立长标注手册。论文说采用KAIROS的67类三级本体，当前数据观察50类59种role。直接比对发现17个事件的类型键不在该JSON，以及31条论元role不在对应类型roles（其中包括类型键缺失的连带错误）。例如发布Contact.RequestCommand.Broadcast，但文件只有Contact.RequestCommand.Unspecified；Justice.InvestigateCrime.Unspecified的Observer/ObservedEntity不在当前roles。未发现src内显式相关别名，不能自行映射后声称原规范吻合。

公开LDC KAIROS较新发布不等于WikiEvents的2021标注规范，不能挂接2025/2026文档证明版本绑定。[LDC2025T07](https://catalog.ldc.upenn.edu/LDC2025T07)仍有单独数据许可，本轮未购买或下载其受限完整数据。原文许可、WikiEvents发布许可与代码license须分别确认。

## 三表与具体例

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 缺口 |
| --- | --- | --- | --- | --- |
| 将新闻伤害事件转成受害者清单 | 246原生新闻文档与tokens | 现有事件角色模板，长KAIROS规范未取得 | 可显式给定触发及事件type作为上游任务 | 全源3951事件5536论元；不是5536独立文档 |
| 将代词/简称论元转成最具信息量的实体提及 | 相同新闻全文 | 论文中的informative任务说明与角色约束 | 同文上下文；coref gold不能默认作模型工具 | _info版本已下载，簇及替换范围尚未核验 |
| 按角色聚合新闻中的人员/组织清单 | 预测论元与公开来源ID | 固定任务类型与role约束 | 同资源程序均可用全文和固定检索 | 需先解决本体键不匹配；不能将别名猜测当gold |

实际原生例`scenario_en_kairos_65-E2`：trigger injured，类型Life.Injure.Unspecified，Victim为Terry Duffield（实体T13）；普通和informative版本此例相同。它只是说明可追溯原生字段，不是长环境必要性反例或Agent优势案例。

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(documents).join(given_event_triggers)` | 246→3951事件 | 明确上游给定触发/type；不能当端到端识别 |
| `events.sem_map(extract_arguments,E,document)` | 目标5536原生论元 | E目前是短模板集合，长规范条件未满足 |
| `arguments.filter(role=='Victim').project(entity)` | 例E2→Terry Duffield | 同名跨文档去重需要新实体契约，不凭字符串自动认人 |
| `arguments.sem_map(most_informative_mention,E,document)` | 两视图相同246文档；1713事件字典变化待解释 | coref/目标信息量定义需独立核验，不能用private簇直接给答案 |

以下全部未执行模型，仅写目标/可行流程。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 例E2输出Victim=Terry Duffield，实际未测 | 固定语义抽取填充同一角色模板，确定性投影 | 相同目标，不预设优势 | ==读取Life.Injure角色约束、确认触发与全文指称==→论元输出 | `EventContext→RoleBinder→TypedArguments`；只靠模板生成可能已足够，必须纳入E-only基线 |
| informative例仍输出Terry Duffield | 同文检索/共指推断，禁止读取当前gold簇 | 相同目标 | ==查同文完整实体提及，核对信息量选择原则==→替换或保留 | `MentionResolver→CanonicalMentionSelector`；规则和评价仍待核验 |
| 类型键缺失不能自动按当前ontology拒绝正确gold | 先在构造侧冻结本体映射，执行侧同资源 | 相同限制 | ==检查公开类型契约==，不凭模型补成官方规则 | schema校验失败属于来源问题；不能当Agent能力失败或胜利 |

证据脚本audit.py/audit.json/examples.json在v157 evidence目录；examples包含gold只供开发审计。没有长规范绑定证据，本轮不升级。下一步可追查作者本体来源/版本，若仍只有短模板则转新源。无模型/prompt/种子/费用/推理预算/训练/测试套件/正式快照/评分/commit。
