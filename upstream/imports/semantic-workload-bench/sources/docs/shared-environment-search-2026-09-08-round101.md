# Increment101 — SciDTB开发检查包：302摘要、4201篇章节点

仍7/15，未升级SciDTB资格。本轮复用round100已完整下载的原论文、完整作者repo与87页RST参考手册，不重复下载。[原论文](https://aclanthology.org/P18-2071/)、[作者仓库](https://github.com/PKU-TANGENT/SciDTB)。

实际进展：官方dev/test的306份独立EDU输入与gold/second_annotate共612次文本对比，仅P14-1129文件末尾多空行。剔除空白行、去每行首尾空白后全部一致；保留分词及<S>标记，不声称原论文未分词原文。两份标注原始带标签边一致dev1338/2133、test1318/2118；head一致1720/2133、1699/2118。这包含未完整节点的原始分母，仅是发布版本之间的一致性，不是模型得分或人类准确率。

构造inspection-v1：302摘要、4201节点、308个manifest资产。排除3篇主gold正文parent=-1；另排除D14-1010，其原文与论文Figure1两段12词/65字符以上重叠，直接看到原论文例图文字。此筛查不证明其余无短语/改写泄漏。主gold未修补；secondary原件全部私有保留，包括P16-1163的不完整节点，不能把它用于完整树确认评分。构造/排除均为开发用途。

public只含record_id、给定EDU的id/text、两份参考PDF及明确标为INSPECTION_ONLY的task.json。private含主关系树、第二标注、源ID与split映射、排除原因。独立verify.py检查全部308资产集合/字节哈希及302篇4201主节点与原生文本/标签精确投影一致，公开记录allowlist通过。这里的manifest是独立审计包格式，不是仓库core Snapshot，也无OS隔离或模型执行。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按SciDTB规则批量构建摘要篇章树，再索引评价性结果 | 开发检查包302摘要、4201个给定EDU | 87页RST参考手册及6页SciDTB论文改写；适用映射尚未冻结 | 给定EDU顺序、分词、<S>标记；不含parent/relation | 官方主gold树4201节点，第二人工标注独立保留 |
| P14-1095训练讲解：实验报告行为与研究结果谁为head | EDU15实验表明；EDU16FactChecker准确率更高 | SciDTB覆盖attribution方向：被归属的结果内容为head | 16个EDU整篇上下文；此训练例不在302篇包中 | 15→16 attribution；16→1 evaluation（round100原件） |
| 对两份参考标注比较 | 原始306篇官方EDU | 同一任务与节点编号 | 两份人工标注，只在评估侧读取 | dev1338/2133、test1318/2118带标签边一致；不可挑选更利于某模型的参考 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `read(edus).sem_map(parse_tree,E).validate_tree()` | 302摘要→4201节点的目标树结构 | 原生主gold投影；未执行推理 |
| `trees.explode().filter(relation='evaluation').project(edu_text)` | 示例返回EDU16内容 | 人工关系派生清单，非新标注的应用价值gold |
| `verify_manifest().compare_public_and_private_with_source()` | 308资产、302文档、4201节点PASS | 只验证构造，不证明语义质量/长E必要性 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 训练例目标15→16 attribution、16→1 evaluation；实际未知 | 同参考规则＋给定EDU，固定sem_map、结构校验、固定预算复核 | 相同目标 | ==查SciDTB对RST方向规则的覆盖==→判读整篇→生成树→校验 | `versioned_rules→head_selection→relation_label→tree_validation→evaluation_projection`，仅拟议，未从轨迹生成 |
| 302篇输出可评分树或ABSTAIN，具体质量未知 | 可预索引/缓存适用规则；不可读private | 同样可共享探索和批计划，不强迫逐篇重新规划 | ==定位类别定义与覆盖规则==→批内复用→在疑难项查询允许资源 | 候选规则索引＋类型约束＋证据判读；需E-only编译/CodingAgent对照 |

未完成项：87页手册含分割、新闻特有类别和附录，给定EDU后不能计入分割成本；SciDTB关系细分及direction规则只能按论文明确覆盖，不能猜测完整映射后冒充作者规范。完整适用E长度/复杂性、跨数据湖论文重叠、短示例近重复及独立确认尚未建立。第二标注的一致性约63%要求预先冻结评分规则，不能把争议当Agent优势。未进行模型/成本实验，不计第8湖。

产物：data/shared-environment-audit-20260908-v101/inspection-v1；artifact/evidence/shared-environment-audit-20260908-v101/{audit.py,audit.json,build.py,build.json,verify.py,verify.json,example.json}。新构造目录不可覆盖；同路径重跑build明确拒绝。
