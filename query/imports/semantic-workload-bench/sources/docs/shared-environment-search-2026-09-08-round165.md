# 增量165：MedProcNER镜像转换与引号补证

复用164原论文、完整官方repo和镜像，不计新湖，仍8/15。本轮实质解决11个span mismatch的表面原因，但没有解决原始gold数量、长规范和版本绑定。

下载镜像方法[SynCABEL原论文v3](https://arxiv.org/pdf/2601.19667v3)，8,058,819 bytes，SHA256 `1e842d07f0b6d35b8d73eebbfe2763d10e90bd11affe7e7499d167278c4e25c6`。[作者仓库](https://github.com/Aremaki/SynCABEL)主树commit `7d3329e08f3632b673e938767983c1344664b8d1`全部69个文件取得；recursive clone的arboEL子模块URL返回Not Found，锁定39319f0287e45885922704b9462cdf88e68133ee未取得。因此称主树完整，不称递归依赖完整。没有执行上游安装/训练代码。逐文件哈希与审计脚本在artifact/evidence/shared-environment-audit-20260908-v165，原件ignored data同版本目录。

## 转换与数据证据

`prepare_corpus.py`读取data/SPACCC/Normalization下train/test/test_simple/test_ner TSV；`syncabel/utils.py:26`先去重，再按文档分组，缺对应文本文件则跳过，把TSV实体字符串/跨度/代码直接封装BigBio，没有校验字符串等于原文切片。当前主树data仅__init__.py，并没有这些上游TSV。因此当前代码不能单独复现HF original_data内容，也不能证明减少6209个procedure是哪个过滤步骤所致。

164报告的11处不匹配，本轮逐个核对：**10条用标准库csv.reader解码后与原跨度完全一致；1条仅将弯双引号换成直双引号即一致**。本轮不修改原件，不将字符串修复视为临床标签复核。它说明11处是表面序列化/引号问题，不应笼统写成11个错误操作定位。

SynCABEL论文Table1报告合并SPACCC 1000文档、27799mentions；164镜像三类型合计32222，不仅procedure与原MedProcNER不一致，连镜像方法论文总量也不相同。可能存在筛选或版本差异，尚未得到转换收据，不能自行归因。论文中合成SynthSPACCC属于训练增强，本轮读取的是human original_data，不把合成训练集当真实病例。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 从病例识别操作并映射代码 | 164已下载1000病例镜像 | 长标注规范仍未取得 | 原始SNOMED术语与版本未冻结 | 8475procedure；11表面字符串差异已解释，标签来源数量未闭合 |
| 将预测代码生成文档索引 | 同一病例文本 | 同一规范与术语 | groupby文档的固定DAG | 仍需与官方原始index TSV一致性审计，不能以镜像派生并集冒充原index |
| 具体序列化例 | es-S1130-05582008000600006-1，2450:2475 | 原文含 `se deja la boca "abierta"` | 镜像字符串含外层引号和双引号转义 | csv解码后切片一致；只解释输入/标注表示，不判断临床语义 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(entities).compare(surface,text[offset])` | 8475procedure→11不等 | 审计侧仅读gold，不作为模型资源 |
| `diagnose(csv_decode,quote_fold)` | 10 CSV解码精确+1弯引号替换精确 | 不更改原文件；不是新增语义算子或Agent能力 |
| `reports.sem_map(procedures,E).sem_map(codes,terminology)` | 当前8475与原论文14684仍不同 | 默认完整gold尚不具备 |
| `groupby(doc).collect_unique(code)` | 1000文档 | 原生index标签待核验 |

以下方法预期未执行，资源/缓存/工具对齐，保留E-only与Coding Agent比较。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 原病例上的规范procedure跨度与代码，实际质量未知 | 固定语义抽取、词表候选及上下文判别 | 相同目标，质量未知 | ==查规范的操作范围、复合实体规则与术语映射==→输出 | `GuidelineRuleSet→SpanExtractor→CodeResolver→Index` |
| 表面引号转换不需语义推理 | 明确数据格式的一次性解析 | 同样采用确定解析，不要求Agent修数据 | ==仅在开发构造时确认序列化约定== | `FormatParser`是构造职责，不计作学到的语义能力 |

下一步仍须原始发布和完整E；当前来源保留待核验而非合格。无模型/prompt/训练/种子/token费用预算/推理并发缓存/测试套件/正式快照/score/commit。pyarrow25与标准库只做数据审计；不会因下载成功或字符串一致就声称环境有效性成立。
