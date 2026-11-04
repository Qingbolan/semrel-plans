# 第107轮：ChEMU-Ref 原论文、完整仓库及原生关系核验

结论：SOURCE_ACQUIRED_AND_AUDITED，尚未计入合格湖，仍7/15。本轮提供新的真实数据候选与可重跑证据，不宣称模型能力优势。

## 下载与来源

- [ChEMU-Ref原论文](https://biaoyanf.github.io/files/papers/eacl2021-chemu-ref.pdf)，EACL2021，540787 bytes，SHA256 f2bb7196d19dc262ee9b3d4aa00ebe6a849c3f3a37b73454a34f639e7b8f34a5。
- [完整作者仓库](https://github.com/biaoyanf/ChEMU-Ref/tree/b5b5a54c7f80d70e53c2b8aeab47f2f3329d39fc)，ZIP2065921 bytes、35成员、30Git blobs，全部Git对象哈希匹配，CRC通过。包含完整公开train/dev及代码；没有test原始标注，不等于下载了1500条最终全语料。
- [完整作者标注指南](https://biaoyanf.github.io/files/papers/chemu-ref-dataset.pdf)：28页、10640正则词、425016 bytes，SHA256 e87ba21047bf5bad3b9dfe57d0415ed30557e4c77fc9c0baa11b34404146d861。
- 同时下载2020作者网站完整repo，commit443dd0f39b9cbe95a423e7131c9d3d45ce9ee45a，13成员、1677920 bytes；2020综述4996666 bytes。这些仅补充同家族来源，不另计独立湖。
- [Mendeley作者发布页](https://data.mendeley.com/datasets/r28xxr6p92/1)列CC BY4.0，搜索索引显示sample ZIP及指南。实际文件API/HTML下载HTTP403；当前chemu.au/2021/主页可读取，但data入口重定向后404。未获取原始全量BRAT，未注册账号或运行上游代码。

## 实际数据审计

900训练+225开发=1125条记录，159364 tokens、5769句、16039关系：Coreference3243、Transformed600、Reaction-associated4072、Work-up7709、Contained415。

所有已填写区间均满足0≤start≤end<token_count（闭区间）。但69个关系端点是空数组，涉及35条记录；不能将空端点解释为否定或已验证隐含论元。有1632个端点包含多个区间，须保留不连续结构。doc_key无重复；0110/0532的token序列完全相同。未核验专利ID分组，1125片段不等于1125独立专利。

指南与数据进行小写正则词12-gram、至少65字符的匹配，12条记录命中。这里只是泄漏候选，化学长名称本身可能产生匹配，尚未逐一判定。不能据此宣称已隔离指南示例。

## 按要求的三张表

本轮以完整token化片段为输入，预测带跨度的关系图；不提供gold选出的mention列表。其下游是按关系类型检索实验阶段来源，可用原生边构造派生gold；不是实际化学收率或实验成功率预测。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量抽取物质指代及来源关系，找出经后处理得到的产物与直接来源 | 作者发布的1125条token化专利实验片段 | 28页共同规范：跨度、复合提及、数量、状态变化及5类关系 | 全部句子上下文；暂没有专利ID到全文的映射，不能暗加全文知识 | 16039条有向关系，包含不连续span；69空端点待处置 |
| 具体记录0516：产物白色晶体来自哪个后处理前对象？ | 混合两份异丙醇溶液后得到沉淀，随后过滤、干燥，得到8.56g产物，原文报告85%yield | 指南§4.3要求将分离/纯化所得对象与其直接来源建立Work-up关系 | token71–72为Precipitated crystals；89–102是带8.56g/85%描述的产物；104–106为a white crystal | Work-up(89–102 → 71–72)；Coreference(104–106 → 89–102)，另有产物→标题名的Coreference |
| 具体记录1153：两次mixture是否直接同一实体？ | 前一次The mixture位于40–41；经历50°C/12小时处理，后一次the reaction mixture位于72–74 | §4.1把状态已变化但成分相关的对象标为Transformed，不能一律Coreference | 文本仍使用mixture，但规则要求参考中间步骤 | Transformed(72–74 → 40–41)。此记录另有一个Work-up空端点，故仅作开发诊断，不当完整可评记录 |

关系数组方向以作者README和实际JSON为准：先anaphor、后antecedent。指南例子展示顺序可能不同，不能按展示次序直接构造JSON。

| 类python的DAG | 具体输入数值 | 语义中间输出 | 下游可核对目标 |
| --- | --- | --- | --- |
| `snippets.sem_map(resolve_material_relations,E).explode(edges).filter(type=='Work-up').project(anaphor,antecedent)` | 1125条原始片段；本轮未排除35空端点记录 | 0516产物→沉淀的Work-up边 | 0516原生Work-up边数1；全原始发布Work-up7709条，包含缺端点问题，不直接作为合格评分分母 |
| `snippets.sem_map(resolve_material_relations,E).explode(edges).groupby(type).count()` | 5类、16039条原始关系 | 同一关系图复用到类型计数/阶段检索 | 0516分布Coreference2、Reaction-associated3、Work-up1，其余0；不是推理执行结果 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 0516正确目标包含产物→沉淀Work-up和白色晶体→产物Coreference；预测未知 | 固定sem_map提供同一完整E及token片段，输出结构化span/关系；允许固定章节检索、校验和缓存 | 同一正确目标，不能预设更高准确率 | ==检查指南中的跨度、Coreference与Work-up区分== → ==追踪混合、过滤、干燥前后的物质对象== → 输出有向边及公开证据位置 | `ResolveMaterialRelations(tokens,E_version)`：跨度解析→物质状态/来源图→规则分类→格式/引用校验；保留不连续span、ABSTAIN；不读取gold |
| 1153诊断边正确目标Transformed，不是Coreference | 固定规则/章节检索也可检查两处mixture之间的处理步骤 | 同一正确目标；本轮未执行 | ==定位§4.1状态变化规则== → ==读取两处mixture之间的处理过程== → 输出Transformed | 可冻结任务规则与步骤提取程序；不能把“mixture一律Transformed”写死，是否需要执行经验仍待对照 |

这些均为拟议方法结构和gold期望，不是LOTUS/Agent实测。需要同资源固定程序、Coding Agent、无轨迹E-only编译、整批Agent与单轨迹冻结算子比较；共享预处理/缓存均允许并完整计费。

## 后续具体门槛

获取或核对原始BRAT，确定69空端点是否转换损失；如不可恢复，明确排除35源记录并保留原始坏例。审计12个指南重叠及专利级来源隔离，冻结公开token输入/私有原生图映射，并独立验证。28页规范含实质跨章节规则，比仅短标签说明更接近长E任务，但实测环境增益和单轨迹价值仍未建立。

产物：data/shared-environment-audit-20260908-v107/；artifact/evidence/shared-environment-audit-20260908-v107/{downloads.json,ref-downloads.json,audit.py,audit.json,secondary-audit.json}。无模型调用、无源码功能修改、无新增单元测试、无commit。
