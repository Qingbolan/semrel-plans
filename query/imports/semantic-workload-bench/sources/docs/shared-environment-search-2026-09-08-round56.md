# 第56增量：CRAFT完整仓库、协议与概念层核验

本轮新增独立候选，合格仍2/10。未把CRAFT的多个本体模块或不同版本算多个湖。任务候选是全文概念索引，关键节点sem_map输出跨度和本体ID；也可另立明确mention-given归一化任务，但本轮未用这种改写增加批规模。

## 下载与实读

- 原论文[Concept annotation in the CRAFT corpus](https://doi.org/10.1186/1471-2105-13-161)：20页738315bytes，已完整下载。
- [作者完整仓库](https://github.com/lhunter-lab/CRAFT)，commit `2abe82b8bb8089448b84937d5f61d8c218011322`，ZIP175100750bytes/3152条目，CRC通过；递归Git tree非截断，3078blob逐个Git对象SHA1匹配。完整源码仅静态读取，未运行作者脚本。
- [概念标注原指南](https://bionlp-corpora.sourceforge.net/CRAFT/guidelines/CRAFT_concept_annotation_guidelines.pdf)：47页11972326bytes，2010-03-14。网页工具因大小无法打开，但本地完整下载及pdftotext成功。
- 当前README描述v5.0.0，97篇全文；原论文对应旧版，不能把旧文统计直接当当前仓库结果。
- CHEBI+extensions实读97XML、17163提及、57不连续跨度；跨度范围全合法，单跨度文字与原文一致。嵌套OBO ZIP CRC通过，54703350bytes、58627直接Term。
- 73种gold类别无直接OBO条目。README明确这些是CHEBI角色的平行物质类，CHEBI_EXT数字对应CHEBI数字；按此规则全可解析。不是73个缺失答案，也不能忽略扩展含义直接当原角色同义。
- 指南明确引用46篇源文章作示例。精确PMID检查只说明这些已暴露，不保证其余51篇无近重复或其他污染。

所有资产位于data/shared-environment-audit-20260908-v56；下载脚本、哈希、Git核验与全量统计位于artifact/evidence/shared-environment-audit-20260908-v56。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 为每篇全文生成CHEBI概念索引，保留出现位置 | 同一47页跨度/语义匹配协议 | 当前冻结CHEBI+extensions本体及公开角色扩展定义 | 97篇完整文本及原NXML | 17163人工提及→跨度+本体ID；不能将XML标注或按gold生成的候选集给模型 |
| 实读开发例PMID11319941 | 最近语义匹配及边界规则，具体推导尚待逐条核 | CHEBI:64276定义glutaraldehyde；CHEBI:15355定义acetylcholine | glutaraldehyde[27019:27033]、cholinergic[16658:16669] | 分别64276、15355；后者表面词不等于本体名称，当前未实证需要多轮Agent |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `docs=scan(full_text)` | 97个源文档；不是17163篇独立文档 |
| `mentions=sem_map(docs, protocol, ontology)` | gold17163提及，57不连续；可全文处理或公开分段后聚合，但不能擅自将切片数当独立样本量 |
| `validate_and_resolve(mentions, extension_rules)` | 73种平行角色类通过作者公开规则可解析；无需读取逐实例gold |
| `index=groupby(doc_id).collect(concept_id, spans)` | 可评分概念集合及位置；本轮未构造独立下游gold或运行模型 |

| 预期关键语义算子直接交给LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 例目标glutaraldehyde→64276、cholinergic→15355；准确性未知 | 固定本体检索/重排与sem_map，允许相同全文、跨度验证和缓存 | 同一目标，未预设收益 | ==检索候选定义；查修饰词与不连续跨度规则；核对角色/物质扩展语义；检查全文上下文==→概念提及 | 本体索引→上下文候选→定义匹配→跨度组合→扩展转换→结果验证；尚未从轨迹生成 |

待核：47页旧指南与当前扩展规范的完整适用边界；示例隔离后实际批规模和实体级划分；真实实例的规则依赖；public/private构造及默认可执行输入。不直接挂载unused_classes文件，因为其包含标注集未使用类别信息，应先区分任务定义与gold统计。作者许可为annotations CC BY3.0，原文和本体仍需分别确认，未新增许可证。无模型、独立确认、环境消融、优势或成本结论，新工程测试0。
