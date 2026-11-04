# Increment76：AAEC范围冲突、prompt解码及基础检查视图

仍5/15；本轮构造397作文基础检查视图，尚未独立验证，不计入合格湖。完整下载证据见round75。

## 本次发现

五处扩展join冲突均是end比基础多1：essay098/114/182/248/337。基础span恰好在responsibl/educatio/governmen/environmen/communicatio后截断，扩展结束到完整单词。保存冲突两版，不自行将扩展变成基础gold。为开发检查排除这5篇，明确属于已接触gold的质量清理，不能称独立确认或按纯公开字段抽样。

prompts.csv不是UTF-8：唯一高字节为0xCA(36次)、0xD5(6次)，Mac Roman解释为NBSP/右单引号，CP1252解释为Ê/Õ而在语境中不通。采用明确记录的Mac Roman推断，403行=表头+402唯一essay；原始字节保留，不宣称作者声明过编码。先前UTF-8尝试失败及冲突打印因额外空tab失败均保留工具记录，随后修正读取并取得完整审计收据。

基础手册明确claims到majorclaim不画显式边，用claim的For/Against属性表达。不能把supports/attacks当全图所有边，也不能用常识补进不存在的gold。

本地读取许可：2.1允许学术研究；2.2/4限制再分发、仅允许研究报告有限摘录。构造只在本地忽略目录，交付获取/构造脚本；不将原始语料随代码发布。未联系作者或签署任何额外协议。

## 三张表

| Query | 数据湖数据1：共享E | 数据湖数据2：items | 数据湖数据3：private gold |
|---|---|---|---|
| 按AAEC规范抽取成分、关系和claim stance | 原31页11171word指南 | 397作文全文+写作题目；题目Mac Roman解码有明确推断收据 | 6007成分、3781关系、1486stances |
| 语义类型扩展（待构造） | 11页扩展规范+适用基础规范 | 同源湖；5边界冲突两版不合并 | 原6089类型，已下载；不称本轮实现 |

| 类python的DAG | 具体数值 | 下游目标 |
|---|---|---|
| `scan(essays,prompts).sem_map(parse_argument_graph,E)` | 397doc→740MajorClaim1486Claim3781Premise | 每篇成分与原生结构 |
| `graphs.explode(relations).filter(type=='attacks')` | 3564supports+217attacks | attack连接清单；不是217独立作文 |
| `graphs.explode(claims).filter(stance=='Against')` | 1212For+274Against | 相对主立场的claim清单；For/Against不等于支持/攻击关系标签 |

开发例essay001的T3[591:714]为Claim/For，T4[716:851]为Premise，R1=T4 supports T3；T1[503:575]为MajorClaim。已源审查，不是模型预测。

| 预期LOTUS关键算子结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 例T4→T3/supports且T3/For；实际未知 | 全文+prompt+同E sem_map，程序检查span/边/stance；允许同资源固定检索及编译 | 相同gold目标；实际未知 | ==查成分、嵌套支持与stance规则==；==对照全文主立场定位当前claim==；输出校验 | `argument_graph(text,prompt,policy)`→spans/types→relations/stance→校验→ABSTAIN或结果 |

E-only编译、Coding Agent及固定程序不可省略。不能用基础缺最后字符的标注瑕疵证明LLM语义失败，也不能预设Agent更准确。

## 构造与未完成

产物`data/shared-environment-audit-20260908-v76/inspection-v1`；脚本/收据`artifact/evidence/shared-environment-audit-20260908-v76/`。402assets包括397公开文档、完整协议、任务及private映射/gold/排除清单。未执行独立验证，状态INSPECTION_DEVELOPMENT_NOT_QUALIFIED。

本轮12gram文本筛查未检出额外手册/论文重叠，不能等同无示例泄漏，尤其图示中的文字需额外检查。接下来独立验证字段、全部源gold和stance/图契约，审计手册图示，核验规范实际依赖，再决定资格。无模型运行、无独立确认或环境价值结论。
