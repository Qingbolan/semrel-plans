# Increment75：Argument Annotated Essays完整来源及双层标签核验

新候选AAEC，暂不加入合格列表，仍5/15。已下载基础原论文、基础完整官方发布包、扩展原论文及完整扩展作者仓库；本轮完成全量正文/基础span和关系端点核验，以及扩展标签精确join审计。未构造public/private视图或运行模型。

## 下载与规范

- [基础原论文](https://aclanthology.org/J17-3005.pdf)630918bytes，SHA256 `8a8850c9cb1d0939fdd9a7f000e13562f1c7b662b7b5f578b24a8649602729d6`。
- [大学官方基础发布记录](https://tudatalib.ulb.tu-darmstadt.de/items/9177c48c-8bd5-4881-9cb4-0632b5941464)：浏览工具返回403，但正常HTTP下载返回公开Angular应用页面。读取页面公开config定位其官方/server API，列出ORIGINAL/CC-LICENSE并完整下载，未登录或绕过访问权限。
- 完整`ArgumentAnnotatedEssays-2.0.zip`2064482bytes、15entries、CRC通过，SHA256 `7d592ccdebfcce580b2d3d9bb53c93da691cbb3ac2741e8d403a7d1599e60de7`。嵌套`brat-project-final.zip`1623entries、CRC通过，含macOS元文件；实际essay*.txt是402篇，不能把压缩包entry数当文档数。license独立下载60877bytes。README说明包括正文/标注、prompts、split、guideline，均已取得；这是完整数据发布包，不冒称完整作者模型实现。
- 实读基础`guideline.pdf`：**31页、11171words、1515230bytes**，SHA256 `07070281aaf4164304740083f0f24092d1e7dcc7ee423d0ac70bafc614790dc4`。具体为major claim/claim/premise、结构关系及标注步骤，不是只提供标签名。还需核验其中多少规范对所选具体任务必要。
- [语义类型扩展原论文](https://aclanthology.org/2023.argmining-1.8.pdf)552002bytes，SHA256 `e11a1d44e97cd20793d42b50b0e6a5a6e6158f441adc551a78e65c525ec18610`。
- [完整扩展作者仓库](https://github.com/discourse-lab/arg-essays-semantic-types/tree/0dce719cc23905a33752233440e7527b595179c6)，commit `0dce719cc23905a33752233440e7527b595179c6`，ZIP229766bytes/5entries，4Gitblobs精确核验，CRC通过。该仓库本身只有ID/类型/span，不含原始正文，不能单独当完整输入。扩展指南只有11页，不能单独冒充31页长E，也不把扩展算第二湖。

## 全量实际检查

402正文，6089成分：MajorClaim751、Claim1506、Premise3832。基础所有span文字匹配，supports3613、attacks219的端点均存在。1506 stance：For1228、Against278。尚未全量验证stance对象、图语义及许可条件。

扩展6089rows覆盖402doc；policy344、value1502、common_ground1774、hypothetical_instance917、real_example717、statistics400、fact411、other2、testimony22。与基础(docID,start,end)有5条不匹配，例如essay098/value/858:915、essay114/testimony/1119:1384。不能仅因两者同为6089就说一一对应；也不能用近似匹配静默修补。基础任务并无这些span错误，须分开处理。

## 三张表

| Query | 数据湖数据1：E | 数据湖数据2：真实items | 数据湖数据3：private gold |
|---|---|---|---|
| 按AAEC规范抽取论证成分、支持/攻击结构及claim相对主立场的方向，生成论证清单 | 基础31页11171词指南 | 402真实学习者作文及各自写作prompt；prompt是item特定输入，共享的是标注规范 | 6089成分、3832关系、1506 stance |
| 为论证成分增加语义类型以比较论证方式（待join解决） | 同湖基础规范＋11页扩展规范 | 同作文；是否给定成分边界需要显式冻结annotation-given或end-to-end任务 | 6089语义类型，5精确join冲突未解决 |

| 类python的DAG | 具体数值 | 下游目标 |
|---|---|---|
| `scan(essays,prompts).sem_map(parse_argument_graph,E).project(components,relations,stances)` | 402doc；751MajorClaim1506Claim3832Premise | 每篇可核对的论证结构；不是一般文本主题分类 |
| `graphs.explode(relations).filter(type=='attacks').groupby(essay_id)` | 源219attack连接 | 包含反驳连接的作文/连接清单；独立作文数待构造统计，不能直接说219篇 |
| `components.sem_map(semantic_type,E_extension).groupby(type)` | 源6089rows，5join冲突 | 类型分布；不能把基础gold边界只给Agent而不给静态方法 |

开发例essay001的prompt是学生应学习竞争还是合作。基础T1[503:575]为MajorClaim，T3[591:714]为Claim，T4[716:851]为Premise；R1为T4 supports T3，T3 Stance=For。扩展给T1=policy、T3=value、T4=common_ground。这里只转述已读取源gold，未执行任何模型。

| 预期LOTUS关键算子结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 例中T4→T3/supports，T3=Claim/For；实际待测 | 作文+prompt+完整必要E固定sem_map→span/端点/枚举验证→关系投影；允许同资源检索与共享编译 | 相同gold目标；实际未知 | ==查claim/premise及支持/攻击边界规则==；==核对全文主立场和当前成分的层级作用==；生成图并校验 | `argument_graph(text,prompt,policy)`→成分span→结构/stance→验证→输出/ABSTAIN |
| 例中T1=policy、T3=value、T4=common_ground；实际待测 | 冻结输入条件后固定语义类型sem_map；明确是否给定成分边界 | 相同目标；未预设更优 | ==查语义类型定义与疑难界限==；==核对该成分语境及基础功能==；类型校验 | `semantic_type(component,context,compiled_E)`；不能读取当前gold类型作为工具 |

同资源E-only编译、Coding Agent、固定工具程序均为必需强对照。长手册仅为来源条件，不证明静态LLM不足或轨迹学习必要。

## 后续与产物

`artifact/evidence/shared-environment-audit-20260908-v75/`保存download.py、download_base.py、audit.py及收据；完整来源`data/shared-environment-audit-20260908-v75/`。全部下载进程正常结束。未运行作者代码。后续核验31页具体规则与真实边界、5处扩展冲突、原prompt编码/完整性、许可、手册/论文示例重叠与作者实体分组，再构造公开输入/private gold。当前不计入合格15湖，也无模型效果结论。
