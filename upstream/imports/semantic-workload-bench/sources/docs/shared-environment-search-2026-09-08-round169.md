# 增量169：UCCA评分完成及来源字符串纠正

复用166–168全部原件，不计新湖，仍8/15。上一168是评分进展与真实运行等待。本轮先poll原session96797，没有重启；进程最终退出0。一次macOS sample尝试时原进程刚结束，返回进程不存在；随后从原session取得正式完成输出。

## 已完成结果与修正

367 passages全量官方XML解析及labeled self-score、normalize=False完成，244.854秒、0异常、0自比匹配差异。参考/预测分别解析的同一原图，此结果只证明评分链路可用，不是模型准确率。官方yield计分单位合计primary174261、remote8268、implicit1546，与原始边数不是同一单位。

passage20删除共享Pitt的A/remote边：remote19匹配/20参考，recall0.950、F1约0.974；primary与implicit仍全匹配。normalize=False有356个primary计分单位，True有347个；同一删除边效果保留。由此确认该例下关键中间边影响图评分，但未证明下游清单/聚合质量或LLM能力。

**修正166–168的来源表述**：27是metadata原始来源字符串数，不能直接称27独立文章。去掉Wikipedia前缀、可选连字符与空格后得到26个名字；Paul McCartney的两个空格版本合并。没有纠正Maria Carey等拼写，也没有做真实实体归并。规范化后train/dev共享Angelina Jolie、Maria Carey、Paul McCartney三项，test与二者仍无交集。train22/dev4/test3来源数量各自不变。

52条R/remote分布40passages、17原始来源字符串（规范化16来源）。若整篇排除这些已暴露冲突来源，只剩92passages、10来源名；这不是实际冻结的清洗集，更不证明剩余全部符合规范。git最近版本记录有一般validation fixes，但搜索commit message没有找到解释R/remote的迁移说明；不能由此断言历史不存在任何讨论。

所有新审计结果见artifact/evidence/shared-environment-audit-20260908-v169/audit.json；评分原收据保存在v168/self-score.json和remote-deletion-probe.json。来源与图原件未改，未安装新依赖。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 逐段生成Scene/Participant图及共享关系 | 367passages，26规范化来源名 | 37页随库v2指南 | 官方labeled图评分；必须固定normalize开关 | 原生9765A/remote；不能用8268全部remote计分单位替换此数量 |
| 具体passage20第二Scene共享Pitt | 原文省略主语 | remote参与者定义 | 删除该边的受控预测副本 | reference20个remote yield单位，删除后19匹配 |
| 按源文章划分开发/确认 | metadata原始字符串及明确前缀处理规则 | 固定划分文件 | train/dev共享3来源、test3来源无交集 | 不是按段独立的确认；没有新分割或gold调参 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `parse(reference).score(parse(reference))` | 367/367可运行；244.854秒 | 自比工程诊断，无模型质量结论 |
| `delete_shared_A().score(reference)` | remote19/20，P/R/F1=1/.95/.974 | 单个开发例因果探针，不代表一般下游增益 |
| `normalize_source_name().groupby(source)` | 27原始字符串→26名字 | 只做前缀空格处理，不声称近重复/实体审计 |
| `sem_map(parse,E).project(scene_participants).aggregate()` | 目标仍规范图及下游表 | 完整投影/数据一致性未验证，不用评分器绿色代替 |

以下仍为未执行的LLM方法预期，固定程序、Coding Agent、E-only编译与Agent同资源比较。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确保留共享参与者可避免本例remote召回损失，实际模型未知 | 固定场景识别与参与者共享解析 | 相同目标，未证明更好 | ==检查第二场景缺省主语与remote规则==→图输出 | `SceneParser→SharedParticipantResolver→Graph/SceneTable` |
| 冻结图规范与评分版本后再报告质量 | 固定完整输入、统一normalize、labeled评分 | 同样契约 | ==只在开发阶段确认规范和评分对象一致==→冻结后执行 | `VersionedTask→Parser→Projection→PrivateEvaluator`；版本管理不是学到的语义能力 |

本轮关闭上轮真实运行等待，补充来源纠正和评分差异。不追加模型实验或将UCCA升级为可行湖。下一轮可返回其他原始公开来源；UCCA的26来源规模、E/gold一致性和示例暴露仍是具体缺口。无模型/prompt/训练/种子/token费用预算/推理并发缓存/测试套件/正式快照/commit。
