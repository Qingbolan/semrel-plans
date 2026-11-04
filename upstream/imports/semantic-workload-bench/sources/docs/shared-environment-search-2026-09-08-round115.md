# 第115轮：STAC 原生图与作者评分路径不等价

本轮是上一轮候选的核验增量，不是新增数据湖。累计仍为7/15，STAC仍待定。上一轮产生新数据包，属于有证据的进展。

## 下载与源码证据

原论文和完整语料/46页指南已在111轮下载。本轮另完整下载作者的三个源码仓库，ZIP全部CRC通过，无依赖安装、无模型执行。

| 仓库 | commit | bytes / ZIP members | SHA256 |
| --- | --- | --- | --- |
| educe | `3c1e2987d5c04e23ed012f41fe3a8ce5010bdbc9` | 3266588 / 584 | `86e17fe17b75b7178d0dd25865d098dc1d2edf663d97a73854ebe2fd00f361e8` |
| irit-stac | `ec36fac93d26101ba1014db5540483a182472918` | 185185 / 119 | `1322af80d193c537151f4333b4eef6d3776cbd97c6a898ed7a1c24d25c825c1c` |
| attelo | `717b1df21fc0dd1eb5d78e6d8018005759577fa5` | 251955 / 153 | `c4ef5cc8fe92733ea5107bd6e590d2a15cedfb7e5ee3c00e3e1b704b99dd7278` |

来源：[原论文](https://aclanthology.org/L16-1432/)、[Educe](https://github.com/irit-melodi/educe)、[IRIT STAC](https://github.com/irit-melodi/irit-stac)、[Attelo](https://github.com/irit-melodi/attelo)。ZIP包含所锁commit的完整工作树，不是完整Git历史；仓库版本不宣称与2016论文运行版本相同。

源码定位：Educe `educe/stac/graph.py:167` 的 `strip_cdus` 支持head/broadcast/custom；`learning/features.py:1410` 在未设置ignore_cdus时执行转换。Attelo `attelo/score.py:105` 的 `score_edges` 将预测转换为端点对到单标签的字典，重复端点会覆盖标签。它不提供我们所需的递归CDU结构匹配。没有把其他RST constituent评分误认为STAC原生图评分。

## 本次实际计数与具体错误

对114轮inspection-v2只读审计：944对话、1111 CDU、9732关系；30 CDU直接含另一个CDU，2132关系涉及CDU（227条两端都是CDU），688问答边和96澄清边涉及CDU。递归、无序的直接成员签名无重复、无环。28组端点各有多个不同标签，无同标签重复。例record_0149的e35→e40同时是Acknowledgement和Comment；单标签字典会丢失其中一个。

不能把CDU摊成叶节点、转换成head、或丢掉第二标签后仍称原生完整图gold。此结论来自已下载代码和实际数据形状；没有运行作者历史训练/评分全流程。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 为协作对话检索每个问题及完整回应范围 | 944段公开对话，给定EDU切分、说话人和turn_no | 同一46页作者规范；§4.2定义多EDU回应，§4.1区分问答、追问和澄清 | record_0083：e0询问用羊换木头；e1答yup；Nancy同一轮说e2 sorry、e3 dont have wood | 包含e0→c0 Question_answer_pair，c0={e2,e3}；不能只取e3冒充相同结构 |
| 汇总需要澄清的对话连接 | 同一批对话 | 同一规范对Clarification_question和Q_Elab的区分 | 不提供人工addressee、CDU成员或关系 | 378条Clarification_question，其中96条触及CDU；属于同一解析任务的另一查询视图，不算新湖 |

| 类python的DAG | 具体数值 | 关键中间结果 | 下游gold |
| --- | --- | --- | --- |
| `dialogues.sem_map(parse_graph,E).explode(edges).filter(type=='Question_answer_pair').project(question,response)` | 944→9732原生关系→2359问答边 | 预测CDU及多标签有向边；688条问答涉及CDU | 回应端点保留结构；record_0083含e0→{e2,e3} |
| `dialogues.sem_map(parse_graph,E).explode(edges).filter(type=='Clarification_question').count()` | 944段；378条目标边 | 96条目标边涉及CDU，不是全按独立EDU分类 | 378为本开发包精确gold计数，不是预测结果 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；正确目标是e0→CDU{e2,e3}，不预设一定失败 | 同E sem_map生成图→公开结构校验→固定多标签关系过滤；允许共享计划和缓存 | 未执行；正确目标相同，优势未知 | ==查§4.2完整回应范围规则== → ==结合Nancy同一轮两段确定回应边界== → 输出CDU和问答关系→结构校验 | `parse_graph(edus,speakers,turns,E_version)`输出递归CDU和关系三元组集合；CDU以递归成员结构对齐，不按任意c0名称匹配；无效输出ABSTAIN |

上述流程是可观察操作设计，不是私人思维链或已提取代码。固定工具程序、Coding Agent、E-only编译、整批Agent都应取得相同公开输入；没有从复杂图结构直接推断Agent必要。

## 结论和剩余边界

共享规范确实规定具体关系和复合范围，而不仅是标签名字；但46页包含分段、其他标注层和Glozz操作，不能全计为当前解析任务必需长上下文。复杂E相较短规则是否必要仍未测量。完整指南例子语义重叠审计也未完成。原生多标签/CDU评分需显式定义，不能套用已检查的单标签函数。

本轮不把STAC计入7个可构造湖之外。下一增量优先寻找其他独立候选；STAC的未决问题已具体化，不重复做无关文件校验。现有7个亦仅为来源/构造开发资格，未证明科学VALIDATED或Agent收益。

产物：`artifact/evidence/shared-environment-audit-20260908-v115/{downloads.json,audit.py,audit.json,multilabel-pairs.json}`；完整源码位于`data/shared-environment-audit-20260908-v115/`。复跑只读诊断：`python3 artifact/evidence/shared-environment-audit-20260908-v115/audit.py`。无训练/评分、无新增单元测试、无commit。
