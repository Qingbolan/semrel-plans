# 第117轮：LCT版本差异与内部环，尚不晋级

本轮只读检查已下载的原Figshare发布和当前作者仓库。来源/commit/hash见116轮卡与downloads.json。上一轮取得新源和初步差异，属于进展。本轮未下载新论文或仓库，复用已完整取得的材料。

## 实测结果

1006份文本仍一致。963份标注字节一致。对文本span、事件、关系、属性做忽略实例ID/行顺序的递归结构比较：962份结构一致，42份确定不同，2份因事件引用环不能按此签名比较。2个环样本中1份字节相同、1份字节不同。因此43份字节差异包含42份已确认结构变化及1份有环的变更样本，不是43份都已完成递归比较。重复角色后缀保留；此签名不是临床语义等价判定。

原版与当前版都存在两处event-role环：

- NCT03921892：Family-Member E13→Has E17→Negates E13。
- NCT03865524：Negation E21→Negates E56→Asserted E21。

这是内部标注图，不是外层批处理DAG。不能因内部有环直接声称固定DAG不可执行，也不能在SQL编译前未经声明把图递归摊成树。没有自动删边或修复gold。

一个确定的版本变化：NCT03865784旧版分别标Observation“pain”[99,103)和Modifier“back”[94,98)，新版改为Observation/Observation-Name“back pain”[94,103)，删除对应Modifier节点；“lumbar injury”也由分开改为合并。两种版本的span评分将不同。论文描述曾用UMLS判断组合短语是否一个概念，但尚无证据证明这次具体改动使用哪个UMLS版本，不能自行补成作者解释。

Wiki内部相对链接核验发现relation、recency、medication、equality-comparison、acuteness五种目标文件不存在。部分可能是改名/旧链接（已有Eq-Comparison.md），只证明链接不完整，不证明全部规则缺失。图像示例仍未完整核验。`Names.md`只写不要标名字，不能把该文件名误当作所有Condition-Name规则。任务相关规则覆盖仍待核验。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 为试验条件产生可复核概念及约束图 | 1006真实条件文本 | 共享LCT规范；原论文提到组合概念边界裁决使用UMLS | NCT03865784里的back pain、lumbar injury | 原版pain+back Modifier；新版back pain合并。冻结版本前无唯一评分契约 |
| 检索否定条件所约束的对象 | 同批文本 | Negation、Assertion、Family-Member规范 | NCT03865524两事件互指 | 原生环应保留到诊断，不通过删除一边伪造tree gold |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold边界 |
| --- | --- | --- | --- |
| `trials.sem_map(extract_graph,E).project(concept_spans)` | 1006输入；原56093 spans/现56067 | 必须固定一个版本；42份确定结构变化 | back pain例原/现偏移不同；未构造冻结投影 |
| `trials.sem_map(extract_graph,E).validate_graph().project(negation_scope)` | 两版本均2个event-role环 | graph validation输出诊断；不自动树化 | 可保留原生关系评分，生成可执行SQL还需明确语义；不能把环当ABSTAIN gold |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未运行；新版目标back pain[94,103)，旧版目标不同 | 同资源sem_map→版本化跨度/关系校验→固定投影 | 未运行；必须服从同一版本，不宣称更准 | ==核对允许的组合概念边界规则== → ==检查当前规范版本== → 输出结构及引用 | `extract_graph(text,E_version)`保留多层图；source-version固定；不读取当前gold决定版本 |
| 未运行；内部环可由公开程序检测 | 图解析→固定visited-set/SCC诊断，不能无界递归 | 未运行；同一工具也可检测 | ==检查图输出的结构约束== → 保留诊断并遵循冻结任务输出契约 | 图和SQL编译分开；未实现可执行患者查询，不称自动提取成果 |

以上只是候选任务契约及预期，未执行LOTUS/Data Agent。相同环境应提供给固定工具、Coding Agent和E-only编译；复杂结构不证明动态Agent优势。

累计7/15不变。下一步核验规范实际输入完整性和图像示例，或切换其他独立候选；没有满足长E必要性前不晋级。保留版本差异，不把42份改标静默混进统一gold。

产物：`artifact/evidence/shared-environment-audit-20260908-v117/version_audit.py`、`version-audit.json`、`graph-and-guide.json`。可重跑版本比较：`python3 artifact/evidence/shared-environment-audit-20260908-v117/version_audit.py`。图/链接扫描本轮命令保留在执行记录，尚未独立脚本化。没有新数据split、模型调用、单元测试或commit；gold已阅属于开发。
