# HICRIC / IMR appeals：严格入场审查

判定：**Reject 当前完整裁定 workload**；结果预测任务本身成立。更接近异质规则导航的候选，但尚无 HSCodeComp 式闭合环境和家族证据，不将题材复杂当执行复杂。

## 表1：入场审计

| 数据湖 | 原论文/仓库 | E及规模 | x与N / q | gold | C依据 | D静态不足 | E家族 | G可回答性 | H下载 / Verdict |
|---|---|---|---|---|---|---|---|---|---|
| HICRIC | [原论文19页](https://drive.google.com/file/d/1vsu0Ns6R6AeTX4-Hf2OdYqRvHD4yNm4y/view)；[完整官方仓库](https://github.com/TPAFS/hicric) | 论文8311文档/419m词/2.83GB；本次实际下载并打开regulatory-guidance全分区1110行；不是已下载全部E | 实际train64067/test9920，共73987背景摘要；固定q预测外部复核维持/推翻 | decision是真实复核结果；sufficiency_id为模型伪标签；背景模型抽取 | hash抽20已保存，完整E依据闭合认证0；非20条已证明不可回答 | 没有同资源full-E/固定检索/预编译强基线不足证据 | K未知；7种原始appeal_type字符串不是7种执行家族 | 论文明确描述不足以裁定；full_text有结论；缺保单/版本/管辖关系键 | PDF、完整repo、全两split、925人工背景标注、1110环境文档已下；全E未下；Reject |

A固定预测任务通过，严格依法裁定q与预测q不同。B存在真实共享知识库，但最小充分裁定环境未建立。C未通过。D/E未确认。F有真实大批，但跨保险/州/年份且单一保单下N未统计。G失败。H代码Apache2.0、HF数据CC-BY-SA4.0；第三方原材料权利需逐源核对，不能用代码许可覆盖。

原论文§5挑战明确讨论管辖、法律、保险合同、完整医疗史和医学文献缺失；§8列出未收录州计划及managed-care contracts。语料规模不能补齐未公开的个案事实。原文PDF§5.6.4写74007输入；实际发布73987，差20原因未确认。HTML版本与PDF有数字差异；本卡以本次文件统计为准。人工span发布925条，论文描述1000条，差异未解释。README8310与论文8311不一致，未实算全部语料。

## 表2：Query × 具体数据湖资产

| Query | 数据1：test parquet `text` | 数据2：规则parquet `text,tags,source_url,date_accessed` | 数据3：私有gold `decision,sufficiency_id,full_text` |
|---|---|---|---|
| q1 预测外部复核结果，输出Upheld/Overturned；预测证据不足另报UNKNOWN | test第0行：67岁男性，2019-01-02至03住院申请；无血流不稳、肾衰、严重梗阻或败血症 | 1110份监管文本；未找到该例适用保单及版本的直接映射 | Upheld；sufficiency_id=1不表示规则证据闭合；full_text为事后解释 |
| q2 按适用保单及医疗必要性规则裁定，输出Upheld/Overturned/UNKNOWN | 同一真实病例 | 当前不能确认充分E；不可拿任意临床指南代替该保险的规则 | 原裁决是候选gold，但未认证可由公开E+x复现；不是可运行严格任务 |
| q3 判断摘要是否足够预测，输出0/1 | 全73987摘要 | 环境依赖未证明 | sufficiency_id是伪标签，不能冒充独立人工gold，因此不纳入 |

具体第二例：train第0行38岁跨性别男性、gender dysphoria、医生建议body contouring，申请15839-22及15877×12；gold Overturned。审查员全文引用WPATH并说明医疗必要性，但该引用与结论属于事后材料，不可原样给系统。不能据此声称两例都已闭合到E。

实际打开的E首文为HHS-OIG General Compliance Program Guidance；其开头说明为自愿、非约束性指引。它确为环境资产，却不能据标签kb推断其足以裁定上述两例。原始文本的空格丢失也应在后续解析质量审计处理。

## 表3：类Python DAG

| DAG步骤 | 具体值及语义边界 |
|---|---|
| `rows = scan(test).project(['text'])` 普通 | 9920行；排除decision/full_text/sufficiency_id；appeal_type是否可用须另冻结协议 |
| `facts = sem_map(rows, extract_case_facts)` 语义 | 年龄67、住院2019-01-02/03等；不得补出保单/州/完整医疗史 |
| `rules = retrieve(E, facts, version_scope)` 普通检索+语义适用性判定 | version_scope缺失；明确UNKNOWN，不能默认当前规则 |
| `y = sem_map(facts, rules, adjudicate)` 关键语义算子 | 若改做严格裁定，证据缺口应UNKNOWN；发布gold仍Upheld，二者不应混称模型错误 |
| `selected = sem_filter(y == 'Overturned'); count(selected)` 普通过滤/聚合 | published test二类gold4576推翻、5344维持；排除不足伪标签后的论文三类统计不同 |

## 表4：四路推演（未执行，gold不是实测输出）

| 臂 | 预期执行结果与边界 | 预期执行过程 | 候选operator结构 |
|---|---|---|---|
| LOTUS静态，仅任务+摘要 | q1目标第0例Upheld，但预测未知；q2合理输出可能UNKNOWN | 单次语义预测/分类 | 固定prompt分类器，是强必要对照 |
| LOTUS静态+完整E | 未下载完整E；没有预测质量值。大E不能单次完整塞入不证明固定检索不足 | 事前按州/险种/日期索引→检索→一次语义判定；完整上下文臂须报告真实上限 | 固定索引+事实提取+规则适用性检查 |
| 逐记录Data Agent | 无已测优势；无法通过工具恢复未公开合同和病历 | ==查保单/时间/险种范围==→==查医学规则及例外==→核对病例→缺证据UNKNOWN | `resolve_scope → retrieve_policy → evaluate_necessity → evidence_gate`；仅设计假设 |
| 批处理Data Agent | 可共享检索和规则解析，收益未知 | ==一次建环境索引==→==按早期语义事实选择规则家族==→逐案事实核对 | 版本化规则缓存+参数化判定；不能缓存训练/测试裁决全文作为E |

ρE为环境解析/索引，ρP为每案事实及范围检查，ρG可能为住院必要性/疗法试验性等共用规则，ρR为个案临床证据；四者比例及K均未测。训练/测试划分论文按来源和结果分层随机，不等于患者/实体隔离。二类与伪标签合成三类不应混报。固定RAG、规则预处理和条件分类均未被排除，因此不能回答“为什么一定需要经验提取”。

## 证据和验证

本次资产位于`data/shared-environment-strict-hicric/`；完整commit、大小和SHA256见[来源收据](../artifact/evidence/shared-environment-strict-hicric/source.json)，[实际字段统计](../artifact/evidence/shared-environment-strict-hicric/data-audit.json)，[20条原始抽样](../artifact/evidence/shared-environment-strict-hicric/sample20.json)，[实际环境首文](../artifact/evidence/shared-environment-strict-hicric/environment-sample.json)。抽样含gold仅供审计，不是public输入。未运行作者代码、模型、基线或成本实验；未构造新split，未完成20条必要性/充分性证据链。
