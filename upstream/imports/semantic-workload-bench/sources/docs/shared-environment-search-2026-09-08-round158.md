# 增量158：MuLMS完整仓库与原生XMI，4篇与SOFC重叠

状态`SOURCE_ACQUIRED_NATIVE_AUDITED_PROTOCOL_BINDING_PENDING`，仍8/15。没有将MuLMS-AZ、MuLMS实体/关系层拆成不同数据湖。

## 下载证据

[原WIESP2023论文](https://aclanthology.org/2023.wiesp-1.11.pdf)588414 bytes，SHA256 `914246e51f712b1636a37c3336e8b56a975016c09d74d9bab552976b9d05e9ad`。

[作者仓库](https://github.com/boschresearch/mulms-wiesp2023)通过`git clone --recurse-submodules`完整克隆，主commit `d1dff6aa2fe17fcf8a6d5d7c579b27789034a9c6`，作者锁定AZ子模块 `0007fba8e9d4e6804b2f02d26a3899e9856c0599`。原生50篇XMI和metadata已随子模块取得，不是仅下载代码空壳。HF元信息也已读取，但未下载其parquet派生视图，不能声称完成HF全部下载。

主仓库`annotation guidelines/MuLMS_Guidelines.pdf`，15页1329496 bytes，文本4455空白词，SHA256 `a973228f6130036fdce702f3b7b3b5f6b18835a14604c765dc425b1058717b55`。首页July25,2024；CHANGELOG说明2024-07-26新增指南。其晚于2023原论文，不自动意味着不适用，但本轮未取得逐版本映射证据。PDF只抽取文本/页数，未作图形关系逐图验证。

原件在`data/shared-environment-audit-20260908-v158/`，哈希和可重跑audit.py、audit.json、documents.json、source-overlap.json在`artifact/evidence/shared-environment-audit-20260908-v158/`。

## 本次核验

50 XMI原文共1824096字符、49733实体、22639关系，实体偏移范围与关系端点ID检查无失败。这只是原生范围/引用检查，不证明Java UTF16与Python字符索引在所有非BMP字符上等价，也不证明原PDF抽取准确。

实体包含MAT15793、MEASUREMENT2248、QUAL_MEAS1498、PROPERTY3970、VALUE4934等，另有IMPLICIT_*类别。关系包含measuresProperty2178、propertyValue2108、conditionProperty1856、sameMeas616等；另3条RelationType缺失、1条property_value、1条sameMeasurement。别名是否被官方转换器规范化未查明，不能自动修补源gold。

主指南明确提及15篇doc名称。SOFC metadata实际tab分隔，MuLMS metadata为comma分隔；首次按逗号读SOFC得到错误列结构，检查header后修正并assert45个DOI。精确casefold/strip DOI交集4篇：sofc_01/02/03/04。不能声称这4篇独立于SOFC，是否剩余案例足够及排除后的gold统计未冻结。

metadata split为train1/2/4/5各7、train3为8、dev7、test7。7篇官方test并非大独立确认集。原文本许可metadata包含CC-BY，但代码与指南许可边界仍需分别核对；未发布或提交原文。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 缺口 |
| --- | --- | --- | --- | --- |
| 为材料文献搜索提取测量属性—数值对 | 50篇XMI原文本 | 15页测量/实体/关系规范，2024版待绑定 | 正式测量、定性测量、隐含实体规则与全文上下文 | 2178 measuresProperty、2108 propertyValue原边；不是自动完整数值表 |
| 区分测量条件与测量结果 | 相同文档及实体上下文 | conditionProperty与propertyValue定义 | 原生单位、区间、条件与仪器信息 | 1856 conditionProperty；需解决别名和空类型及任务范围 |
| 合并同测量的分散描述 | 同一文档各测量提及 | sameMeas与隐含实体规范 | 公共全文，当前gold边不可给模型 | 616 sameMeas；完整性/闭包未核验，不能称独立聚类gold |

实际原生例electrolysis_01：propertyValue连接`band gap`到`between 1.15 and 1.25 eV`，另`solar-to-hydrogen (STH)`到`13%`、`Transmittance`到`between 10% and 78%`。该文已在指南中提及，仅开发展示；不能把三种属性数值误归到同一测量或同一材料。

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(documents).sem_map(extract_typed_entities,E)` | 全原生目标49733实体、50文档 | 实体含隐含类别，offset检查不是完整语义正确性 |
| `entities.sem_map(link_measurement_roles,E,document)` | 原生22639边，包括3空类型 | 需先冻结公开上游/独立gold，未调用模型 |
| `links.filter(type=='propertyValue').project(property,value)` | 2108原生边；例band gap→1.15–1.25eV | 保留范围与单位，不投影成一个点值 |
| `measurement_graph.join(conditions).collect()` | conditionProperty1856 | 不自动笛卡尔连接所有属性；需原生路径证据与隐含节点契约 |

以下为未执行的方法预期，无性能/成本预测。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| band gap与1.15–1.25eV成对，实际未测 | 固定sem_map用同规范区分属性、数值与条件，再绑定关系 | 相同目标，不预言优势 | ==查propertyValue/conditionProperty规则及原文语境==→有类型边→保留范围 | `EntityExtractor→MeasurementRoleBinder→RangePreservingProjection`；真实提取未实现 |
| 分散测量信息只按合法关系合并 | 同工具检索全文，固定图流程也可实现 | 同样要求源证据 | ==查sameMeas与隐含实体适用范围==→关系输出 | 独立节点/关系契约，缺失不能猜；需与E-only编译比较 |

本轮没有将该湖升级：指南版本绑定、短规则充分性、已知示例/跨SOFC重叠以及关系别名仍未闭合。原论文和完整递归仓库已取得，下一轮若能定位官方loader实际转换可进一步求证，否则转新源。无模型/prompt/训练/种子/token费用预算/测试套件/正式快照/评分/commit。
