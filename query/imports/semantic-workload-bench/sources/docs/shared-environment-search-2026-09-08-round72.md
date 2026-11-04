# Increment72：GUM规范补全与原生话语图审计

仍4/10；本轮完成来源补全与原生图结构核验，不提前将GUM标为合格。原论文/完整仓库下载证据见[round71](shared-environment-search-2026-09-08-round71.md)。

## 本次新增证据

1. 从[GUM作者站点](https://gucorpling.org/gum/RSTDT-tagging-ref-manual.pdf)下载完整Carlson–Marcu RST-DT手册：87页582747bytes，SHA256 `b53a69ec63e05efc85ffc16612500130f7d3cc8c8764f2b775f52bb1225486a0`。GUM官方规范明确它适用于不与GUM规则冲突的情形，尤其分段；不是87页一律优先。§2分段8634words，跨PDF2–31页，按§2到§3标题精确截取。
2. GUM规范要求先读Mann–Thompson1988；从[RST研究站点](https://www.sfu.ca/rst/05bibliographies/bibs/Mann_Thompson_1988.pdf)取得1202177bytes，SHA256 `20e689aa8cfabb8b87d6ce426937638e8441e7d29a9db701e7ecbf27c7d80335`。不把整个参考文献合集的总页数冒充必需E长度。
3. 作者wiki话语规范的11张内嵌示例图全部下载并记录bytes/SHA256。去UI保留`template slot=contents`内HTML。Tesseract对11图做OCR，为后续案例重叠审计提供输入；OCR不是人工确认，尚未执行完整筛除及视觉复核。
4. 当前257非Reddit文档的原生RS4全量检查：257root、33007EDU、30372group、1290secondary edge；节点唯一、每图单根、主树无环、parent/secondary/signal来源端点存在、关系名在本图inventory、signal token范围合法，**0结构错误**。不等于语义正确或独立确认。
5. Primary parent edges63122含23584个`span`和3609个`same-unit`；去掉这两类结构连接后35929条。归因attribution-positive1967+negative106=2073；explanation-evidence976；contingency-condition582。此为原生图边计数，非去重后的现实事件，也不是文档数。
6. eRST论文§4.1.1说明模型预标后五名标注者人工纠正DM及其关系，增加secondary edges；§4.1非DM signals采用半自动方法，§4.1后续仅在部分文档上做完整人工纠正实验。**不能把所有signal当独立人工gold**。源文件的status=gold也不能代替逐层来源验证。初始候选可聚焦主树/secondary关系，不把非DM辅助signal冒充标准答案。

## 更新三表

| Query | 数据湖数据1：环境E | 数据湖数据2：真实items | 数据湖数据3：私有gold目标 |
|---|---|---|---|
| 按GUM/eRST构建每篇话语图，输出归因/证据/条件关系 | 作者GUM话语规范＋适用的RST-DT分段规则＋原理论/新版eRST定义；包括11图 | 257非Reddit文档；4文档跨层字符差异仍待构造时明确处理 | 原生主树、secondary关系；非DM signal不默认作为人工gold |
| 按GUM构建实体与信息状态/共指图 | 作者实体规范，见round71 | 同257文档；不能另算数据湖 | 原生WebAnno字段；完整typed edge解析仍待完成 |

| 类python的DAG | 本次具体源数值 | 下游意义 |
|---|---|---|
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(label.startswith('attribution'))` | 257文档；归因连接2073=1967positive+106negative | 来源与被归因内容的层级连接清单；parent节点可能是多EDU的group，不能只保存单句ID |
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(label == 'explanation-evidence')` | 同257文档，976连接 | 按规范提取证据/主张单元连接；不是新增独立任务或湖的计数依据 |

具体源例子仍采用已开发暴露的`GUM_news_sensitive`：EDU4“who gave it to the CBC today .”经`elaboration-attribute`指向EDU3；标题为organization-heading。这说明输出不仅是标签分类，还需识别单位范围和正确层级parent。不能用该例直接证明Agent优势。

| 预期LOTUS关键语义算子结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 目标EDU4→EDU3/elaboration-attribute；实际未知 | 完整必要文本/版式及同一规范sem_map，随后确定性图验证与关系投影；同样允许固定检索、缓存 | 相同gold目标；实际未知 | ==查关系定义、分段和嵌套attachment规则==；==核对parent是单EDU还是group==；构图并校验 | `parse(text, structure, compiled_policy)`→单位范围→主树→次边→节点/无环/枚举校验→查询投影；失败ABSTAIN |

这是设计预期，无模型运行。结构校验只能发现引用错误，不能替代语义gold评分；同一E一次编译、Coding Agent、固定工具程序均应保留为强对照。

## 产物、边界与下一步

下载在`data/shared-environment-audit-20260908-v72/`，审计脚本/收据在`artifact/evidence/shared-environment-audit-20260908-v72/`。`audit_graphs.py`实际全量执行，`graph-audit-private.json`保存分类计数与零结构错误结果。没有运行作者代码或修改source。

仍需：筛查文本及示例图中的开发重叠；提供保留公开版式而无summary/sentence-type/实体/EDU gold的输入；处理4篇跨层差异；冻结规范优先级和实际必需范围；构造manifest与源对等验证；独立划分及环境价值实验。作者规范允许在ANNIS中查看先例，不代表可把当前评测gold作为工具挂载；若使用历史实例，需要单独划分H并对全部方法公平开放。
