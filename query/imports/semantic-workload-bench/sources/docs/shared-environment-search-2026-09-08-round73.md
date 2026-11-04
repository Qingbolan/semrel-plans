# Increment73：GUM公开输入/private原生图开发视图

本轮实建并独立校验247文档的GUM开发检查视图；仍未计入已合格湖，保持4/15。来源见round71–72，完整作者仓库commit `22fdf87f9c71c96bcc771461d06e689b1f90020d`；原论文/规范均已下载。未运行LOTUS/Data Agent。

## 构造

从275个GUM文档按固定规则排除18个Reddit正文缺失文档、4个XML/RS4 token不同文档、6个公开规范/原论文/示例图OCR长文本重叠文档，三个集合本次不重叠，剩247。GENTLE不纳入，不另算湖。重叠规则为英数小写12gram且至少65字符；OCR与此规则不是无污染证明。

公开每篇只有匿名ID、source tokens、选定结构标签的token范围（head/p/list/item/table/row/cell/caption/figure/quote/sp/lg/l）。源tokenization和结构标记明确给定；不含摘要、s_type、POS、entity、EDU边界、target关系或signal。简化结构不等于原始网页或图像完整可见，必须进一步核验具体影响，当前不宣称默认输入已充分。

私有保存原生RS4节点、EDU的0-based半开token范围、group与parent/relname，以及secondary edges；非DM自动/半自动signal不用于gold。公开规范保留GUM规则HTML及11图、RST-DT§2分段、Mann–Thompson1988与eRST论文。全文参考资料的总页数不等于任务必需E长度；规则优先GUM，不能调用ANNIS读取当前评测gold。

## 用户要求的三表

| Query | 数据湖数据1：共享E | 数据湖数据2：items | 数据湖数据3：private gold |
|---|---|---|---|
| 构建GUM/eRST话语图并提取归因、证据、条件连接 | GUM规范/11图、适用分段规范及RST/eRST定义 | 247真实文档的245991source tokens及简化结构 | 31584EDUs、29033groups、1244secondary edges |
| 同湖实体/信息状态/共指任务 | 作者实体规范已下载 | 同源湖；本视图暂不包含其任务契约 | 原WebAnno在完整源仓库；完整解析/构造未完成，不能称本轮实现 |

| 类python的DAG | 本次构造具体数值 | 下游gold目标 |
|---|---|---|
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_attribution)` | 247doc → primary positive1861+negative101 | 1962归因连接，包含group层级连接，不是1962独立文档 |
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_evidence)` | 同247doc | 932条explanation-evidence连接；标签投影变体不另算湖 |
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_condition)` | 同247doc | 546条contingency-condition连接 |

真实例子沿用开发暴露的GUM_news_sensitive：其EDU4“who gave it to the CBC today .”经elaboration-attribute指向EDU3。完整树必须同时表示标题、group及其他连接，不能把这句独立判断当整篇图gold。

| 预期LOTUS关键算子结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 目标包含EDU4→EDU3/elaboration-attribute；实际未测 | tokens/结构＋相同E固定sem_map输出图；确定性图校验及关系投影；允许共享缓存/固定检索 | 相同目标；实际未测 | ==查attribute、分段及group attachment规则==；==对照文档结构定位单元与父节点==；生成并校验图 | `parse(tokens,structure,E)`→EDU ranges→primary tree→secondary edges→validation→projection；预算失败ABSTAIN |

需同资源E-only一次编译、Coding Agent与固定工具程序对照。不得预设LOTUS失败、Agent成功，也不能把graph verifier当语义正确性证明。

## 实际验证与剩余缺口

产物：`data/shared-environment-audit-20260908-v73/inspection-v1/`。脚本/收据：`artifact/evidence/shared-environment-audit-20260908-v73/`。

`verify_inspection.py`独立于builder读取源：266asset精确集合/bytes/SHA256、247唯一ID、公开字段allowlist、XML tokens逐条相等、全部31584EDU有序完整覆盖且文字一致、原生节点属性及1244secondary逐条对等，PASS。结构标记范围合法性检查通过，尚未逐项验证完整可见版式与多模态输入充分性。不提供预测或研究效果结论。

下一步：检查简化结构遗漏的实际语义依赖，尤其figure/speaker/版式；核验当前规范与源版本的具体适用关系；完成实体图另一任务视图。独立实体划分、精确规范必要性消融、模型执行与成本均未完成。当前检查视图状态INSPECTION_DEVELOPMENT_NOT_QUALIFIED，不升级VALIDATED。
