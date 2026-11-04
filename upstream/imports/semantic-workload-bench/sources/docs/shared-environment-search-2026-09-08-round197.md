# 增量197：AMR全量解析与短规则边界

复用196原论文、完整规范仓库和语料镜像。以Python3.12.7、PENMAN1.3.1实际解析全部1562图并调用penman.models.amr.model.errors：0解码失败、0通用model约束错误；10670instances、10457edges、829attributes，其中322个负极性属性分布于307图。此检查不验证谓词sense库存、每个ARG角色是否对应正确frameset、人工gold是否正确或官方镜像一致性。

安装仅在忽略目录data/shared-environment-audit-20260908-v197/deps，不修改项目依赖；.venv无pip的初次命令失败，改用已存在uv pip --target完成安装。可复现脚本与完整逐图计数在artifact/evidence/shared-environment-audit-20260908-v197/audit.py/json。

规范Negation至Questions之前仅328空白分词（含代码例子）。示例lpp_1943.5解析后负概念确为chew-01。完整AMR可能需要整个14k词规范与角色库，但将任务缩成否定抽取后不能继续以完整规范篇幅证明长E。本次依README下载官方AMR Dictionary返回HTTP403，已记录downloads.json；没有以替代词典无声明填补版本。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 句子→完整AMR→事件参与者索引 | 1562句1部文学作品，镜像源 | 完整规范14404词；官方词典403，frame版本未齐 | 同句上下文、明确公开检索资源 | 1562原生图可解析，语义及官方版本未确认 |
| 句子→否定作用范围→否定行为清单 | 同句 | 否定章节328词；不能冒称长E | 预测图后程序投影 | 322负属性/307图，例chew-01 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(sentences).sem_map(amr_parse,E).validate().project_events()` | 1562解析成功；10670概念10457边829属性 | 本轮parse读取gold做构造审计，不是模型预测成绩 |
| `predicted_graphs.filter_attribute(polarity='-').project(concept)` | gold派生322项；不是322独立文档 | 短规范充分性待测，不能预设动态探索优势 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| lpp5负概念chew-01；实际模型结果未知 | 句子＋328词规范固定调用；完整图任务另补角色库 | 同目标，实际未知 | ==查否定与模态作用域== → 输出结构 → 公共PENMAN检查 | `ScopeResolver + GraphValidator` |
| 全部规范图，实际未知 | 同资源固定检索frameset后解析，允许批共享缓存 | 同目标 | ==查词义/ARG定义和构式规则== → 图生成 → 检查 | `FrameLookup + AMRParser`，外部版本仍待绑定 |

==是可观察查阅。全量gold解析成功不是LOTUS或Agent得分，未运行任何模型、性能或成本实验。仍11/15开发可构造；下一步转新来源，保留AMR框架资源/来源绑定及文学单来源限制。不以缩短任务后更容易通过的否定分类替代原长E目标。
