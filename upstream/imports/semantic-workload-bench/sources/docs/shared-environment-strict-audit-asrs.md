# ASRS人为因素分类：公开代码表不是复杂判定手册，Reject

下载并读取Jonk等[原论文](https://arxiv.org/pdf/2301.05663)数据/分类/评测章节，9页；[完整作者仓库](https://github.com/AviationNLP/nlp_aviation_safety)commit `21b850e7c0609442ddb9e52b2addaba7271ef301`、9文件，实际只有README、MIT LICENSE、结果图与.gitignore，没有对应数据或执行源码。完整仓库不等于完整实验交付。

同时下载NASA官方2024年4月[16页编码表](https://asrs.arc.nasa.gov/docs/dbol/ASRS_CodingTaxonomy.pdf)、[14页缩写表](https://asrs.arc.nasa.gov/docs/dbol/ASRS_Abbreviations.pdf)及2024-08-07更新的[159页疲劳报告集](https://asrs.arc.nasa.gov/docs/rpsts/acr_fatg.pdf)，实际50个唯一ACN。哈希/字节见[来源收据](../artifact/evidence/shared-environment-strict-asrs/source.json)。报告集按疲劳主题预选，不能当原论文随机split，也不能把50个主题筛选正例当自然均衡批。

## 表1：入场审计与十问

| 项 | 证据与限制 |
|---|---|
| A q/输出 | 对叙事返回12类人为因素的多标签集合；可固定。原数据Other/Unknown是类别，不是运行失败ABSTAIN。 |
| B E | 当前取得编码字段表+缩写字典。编码表第12页列12标签，但没有完整定义、边界和反例；不等于复杂标注手册。2024表晚于论文，不能认定是原标注版本。 |
| C gold/20 | 论文称每份报告经两名NASA分析员处理，独立于被测模型。20哈希抽样取得标签与叙事，但没有完整标签判定依据可定位，完整C通过0。 |
| D 完整E固定不足 | 未证。12类固定语义分类+缩写归一是强对照；不能因为旧BERT质量低就认定必须探索。 |
| E K/触发 | 疲劳、沟通、情境意识等需要语义解释，但12标签不是执行K。未取得轨迹、语义路由/家族共享证据。 |
| F N/真实性 | 真实自愿报告。论文列50755/2672/5937合59364，但称85%/5%/10%，其中2672/59364约4.50%，比例与计数不完全一致；不修补作者split。当前本地只有另一时期50条预选报告。 |
| G 充分性/泄漏 | PDF同置Narrative、Human Factors、Synopsis、Assessments与事件代码；被测输入不能整份PDF直接发送，须去标签/分析员概要。每报告可能多Person和多Narrative，标签并集会改变任务粒度。匿名实体分组未核。 |
| H 获取 | 原论文、全作者库、官方环境候选和50记录已下载；原论文全数据/划分未发布在库。本库MIT不自动覆盖NASA原报告；第三方资料权利仍需独立核查。 |
| Agent探索 | 缩写释义、标签定义与人物/时序；当前E没有完整标签定义供探索，不能用自造判定规则补齐。 |
| 超出普通分类吗 | 未证明；目前更接近共享标签schema的条件分类。没有HSCodeComp式复杂法源导航证据。 |
| Verdict | **Reject当前目标**：未取得复杂且必要的共享判定环境，C/D/E未闭合。不能以真实报告多或PDF总页数大替代E证据。 |

## 表2：Query × 数据湖

| Query | 数据湖数据1 | 数据湖数据2 | gold |
|---|---|---|---|
| 为叙事选择人为因素集合 | 官方报告PDF中Narrative及必要Person关联 | 编码表第12页Human Factors、缩写表 | Person下Human Factors字段；不能未经论证跨人合并 |
| 把叙事内航空缩写展开 | Narrative原文 | 14页缩写字典 | 公开记录没有独立展开gold，不能另计合格任务 |

## 表3：DAG

| 类Python的DAG | 类型/E/判定边界 |
|---|---|
| `rows = parse_reports(pdf)` | 普通解析；分离Person、Narrative与private标签 |
| `text = expand_abbreviations(rows, E.dictionary)` | 固定查表，歧义需语义消解；不是按家族探索的直接证据 |
| `labels = sem_map(text, E.label_definitions)` | 关键语义多标签分类；完整定义未取得，默认公开输入充分性未成立 |
| `score(labels, private_human_factors)` | 独立评分；不能将标签并集代理人物级gold |

## 表4：四路推演（未执行）

| 臂 | 预期结果边界 | 预期过程 | operator |
|---|---|---|---|
| LOTUS任务only | 可能识别明示疲劳，完整标签准确率未知 | 叙事→12类判定 | 固定多标签分类 |
| LOTUS完整E | 编码表仅列选项，不能弥补定义缺失 | 缩写查表→固定分类 | dictionary+classifier |
| 逐例Data Agent | 不保证重现分析员标签 | ==查缩写==→==查标签边界但定义缺失==→有界分类/ABSTAIN | 相同固定工具链；不能自造gold规则 |
| 批Data Agent | 未测质量/摊销 | ==一次构造缩写索引==→批量分类 | E-only预处理；家族库尚无依据 |

ρ_E缩写表/标签列表加载；ρ_P每份报告语义分类；ρ_G未知；ρ_R人物、时序、叙事中的具体错误。K、比例、质量、成本均未测。论文ASRS低性能与其猜测的标注一致性不足，不是同资源现代LOTUS失败收据。

## 实际例子与抽样边界

ACN2093166：机长报告在ROA目视进近下降时收到地形告警，随后爬升；叙事提及疲劳排班及虽已口头简报却未执行公司下降限制。Person字段六标签为Communication Breakdown、Fatigue、Human-Machine Interface、Situational Awareness、Training / Qualification、Distraction。实际标签可读取，但代码表仅列这些名称，不能据此逐一证明六标签必要。公司机场说明/进近材料也没有作为共享E取得；不得把此例改成公司政策违规任务。

[20条样例索引](../artifact/evidence/shared-environment-strict-asrs/sample20.json)按SHA256("asrs-strict-v1"+NUL+ACN)取前20。收据的human_factors仅为整份报告出现值的审计并集，不是已构造的人物级评测gold。报告开头Synopsis与后文详细记录会重复ACN，解析只保留含Narrative的50段。无模型、作者脚本或新确认split执行。
