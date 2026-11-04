# CliniCARE-Bench 严格入场核验

**Reject（当前发布对本目标），不等于研究任务无价值。** 结构上比简单线索分类更接近HSCodeComp：时间锚点、证据来源、合理例外需要语义判断。但每固定任务仅30例、标签模型参与产生、精确病例未获得，不能进入Strong。新搜索由保险理赔转入相邻的临床规范审计；它不是实际保险公司赔付决定。

本轮实际重新下载[原论文](https://arxiv.org/abs/2608.07796)，浅克隆[完整官方仓库](https://github.com/scaleapi/clinicare)全部当前树215文件，commit `bbce780bc0dab07aae584f4dbc097601916b0905`，与旧37轮相同。PDF979,077bytes、52页；pdftotext有PDF字典警告，§4.4–4.5与数据访问文字可读，未宣称全文视觉核验。[收据](../artifact/evidence/shared-environment-strict-clinicare/source.json)。本轮实际读§4.2、4.4–4.5、DATA_ACCESS.md、scenario-06-sepsis-bundle/scenario.toml，统计目录及manifest；没有执行作者程序或读取患者数据。

## 表1 入场审计

| 数据湖 | 论文/仓库 | E组成规模 | x/N | q | gold | C抽样 | D完整E静态不足 | 分支/K | G/H | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| CliniCARE/SEP-1审计 | 上述原文/固定commit | 67项policy manifest，16份随库MD；其余获取配方；不能将67都视为已下载 | 论文30患者病例/场景，25场景共750；本地病例0 | 同一规则下bundle是否按时完成或有合理理由 | 三模型裁定；不是750例独立人工gold | 0/20，受控cohort和病历未取得，不能伪造 | 跨表与时间锚点是真实需求，但固定检索+语义列+分支程序尚未被排除 | 时间起点/实际给药/合理理由为可能家族；K未测，4标签≠4家族 | 无full750.csv；MIMIC及cohort需凭证，代码MIT不替代第三方许可 | Reject：F、gold独立性；C/G/H未闭合；D/E未证明 |

A：单scenario固定q成立；B：共享policy成立，但版本转换需本地封存，论文语料不能逐字节重建。C：未得病例，不能完成20例定位。D：长E、跨表、多跳不自动排除固定程序。E：潜在语义分支，未测K。F：30而非750，且有意平衡的回顾性样本，不是自然分布。G：原规范混合外部指南、一般临床知识、benchmark-specific operational choice，不能假定只读指南足够。H：原文/完整代码可得，精确病例与gold未取得。

## gold来源的新核验

原论文§4.4：750例中556例三模型一致、183例2比1、11例三种不同意见，最后一类交临床人员直接裁定。§4.5：临床校准为75例单评与每场景1例的双评子集；临床人员阅读模型提供的证据报告，而非独立重新检索病历。作者明确承认这一校准并非完全独立。这里的independent指模型相互独立运行，不能换成用户要求的“独立于任何模型产生的gold”。

同节标明规则来自三类：外部指南、既有临床知识、benchmark操作选择。DATA_ACCESS.md说明construction只能重建silver，精确published labels只能从受控cohort取得。本轮未拿到其中任何真实患者的gold，不以模板占位符冒充具体病例。

## 表2 Query×数据湖

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 私有gold |
|---|---|---|---|---|
| 按冻结规则逐例审核SEP-1完成/例外，输出四类决定 | corpus_manifest.csv及相关指南MD/PDF；当前只部分落地 | hosp/emar实际给药、labevents乳酸、microbiologyevents培养、icu/chartevents | ED edstays/triage及Note出院叙述，用于时间锚点与转院信息 | full750.csv的scenario_id/params_json/expected_label；该q30例，未取得 |
| 汇总YES病例清单与数量 | 同E | 同30例 | 普通project/count；不是第二个独立语义任务 | 未知，不能从全库标签分布推算 |

一页人类标注表：case_id字符串；verdict为YES/NO/缺数据不确定/医学歧义不确定；anchor为时间与来源；applicable_elements为适用要素；evidence为记录定位；justification为缺项或超时的公开理由。执行失败独立ABSTAIN。阈值/适用范围须用冻结benchmark契约，不作为临床建议。

## 表3 DAG

| 类Python DAG | 类型 | 具体输入/数值 |
|---|---|---|
| `R = scan(cohort).where(scenario_id == 'sepsis-bundle')` | 普通 | 论文N=30，本地不可执行 |
| `facts = join(edstays, emar, labs, cultures, notes)` | 普通检索/join | 关联subject_id/hadm_id，不能拿orders冒充实际给药 |
| `episode = sem_map(resolve_care_origin, facts)` | 语义，主要依赖x | 是否转入、早期时间是否在记录中 |
| `rules = compile(frozen_policy_and_operational_contract)` | E-only | 阈值、时间窗、例外定义共享 |
| `checks = compute_windows(episode, facts, rules)` | 普通数值+固定分支 | 模板3h/6h，不是所有病例自动适用全部项 |
| `y = sem_map(adjudicate_justification, checks, notes, E)` | 语义，决定最终标签 | 区分缺数据、合理理由和医学歧义 |
| `project(filter(y == YES), case_id); count()` | 普通 | 正确数量未知，无真实预测 |

## 表4 四路推演

全部为待测试方法，不是执行收据。没有具体患者输入，因此不预言某条YES/NO。

| 臂 | 预期结果 | 预期过程 | 可能operator结构 |
|---|---|---|---|
| LOTUS任务表only | 规则细节与病历输入不足时不能可靠复现 | 需先固定检索病历，单次sem_map判定；不能以不给必要病历制造失败 | 通用四类审计提示 |
| LOTUS完整E | 可能与Agent一样好；未测 | E-only编译→同资源固定检索→语义提取时间锚点/理由→数值窗口检查→判定 | EpisodeResolver+RuleGraph+EvidenceSchema |
| 逐记录Data Agent | 同目标，缺院外记录时仍应不确定 | ==定位适用规范==→==检查转院叙述及病程起点==→==检索实际给药而非医嘱==→==判断缺项理由== | 有预算的证据检索、时间计算、理由判断、终止语义 |
| 批处理Data Agent | 可能摊销规范解析；质量和成本未知 | ==一次封存规则==→==按早期语义列分组转入/本院起病==→逐例取证并复用检查程序 | 共享规则/索引+组内流程；不能读gold分组 |

ρ_E是规范解释/索引；ρ_P是时间与给药检查公共程序；ρ_G可能是转院起点不明、重复起点、临床例外等家族；ρ_R是个案证据解释。没有可访问轨迹，比例与K均未知。转入路径可能由结构字段或叙述语义预测；不能仅凭不同取证位置声称静态程序不足。

## 十问与交付边界

1. q/输出：见一页表，四类事实决定，ABSTAIN独立。
2. E：共享67项目录，只16份随库；其余未下载，本地转换非原实验字节冻结。
3. x/N：真实MIMIC来源患者，固定q30例；本轮零患者读取。
4. y：模型共识及临床校准，不满足全量模型独立gold。
5. C：0/20；没有实例，缺证据就是未确认。
6. D：多表检索必要不代表Agent必要，强固定程序比较缺失。
7. E/K：语义家族有结构可能，未测，不将25任务/4标签作K。
8. 探索：时间锚点、实施证据、适用性/例外；共享和个案步骤如表。
9. G：病例无公开输入；隐藏operational criteria不得混作模型预知gold。完整契约若不同于指南，要明确公开，不可隐含。
10. 非RAG/缓存：尚不能排除固定检索、语义事实表加规则程序。

本路线已有明确入场失败，不等待凭证而停止整个目标，也不发起联系或受控访问申请。没有20条样本就保留0/20；这份卡是有依据的淘汰审计，非已完成全部正向验证。下一候选继续其他领域，当前不列Top5。
