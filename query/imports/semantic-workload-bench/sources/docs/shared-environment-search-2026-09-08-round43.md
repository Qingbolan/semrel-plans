# 第四十三增量：PANORAMA输入版本与多重驳回依据

**累计仍1/10。** 本轮复用已下载的原论文、完整作者仓库、完整8,143行源表、2,884行测试和524页MPEP2100，不重复下载。确切commit/hash见[第30轮](shared-environment-search-2026-09-08-round30.md)，旧ALLOW冲突见[第31轮](shared-environment-search-2026-09-08-round31.md)。本轮没有把启发式抽取覆盖为新gold。

## 新核验

1. 2,884条测试context.claims与对应源表initialClaims逐项完全一致。原论文§2.2.1及附录说明initialClaims取自首次Non-Final Rejection前，而非任意最初提交稿。故此前“initial一词可能意味着错误时点”的疑问有了来源解释；仍非逐案对USPTO提交记录的独立字节验证。
2. 全量读取已保存的原始CTNF状态跨度，并仅在rejected紧接明确35USC条款时抽取依据。发布102的834条中353条命中102、14条同时命中102/103、467条未匹配；发布103的1,453条中751条命中103、702条未匹配；发布ALLOW的597条仍有1条命中102、6条命中103、590条未匹配。未匹配是规则覆盖不足，不能当无驳回；这些统计不是准确率或修复gold数量。
3. 14个双依据候选来自2申请：14923954的13个claims，以及14111727的claim6。已经读取两份源文中的相应完整段落。作者转换器在`convert2bench_noc4pc.py`第338–353行选择第一个非空sectionCode作为唯一answer_code，同时拼接多条reason；它不保存完整法律依据集合。
4. 不能把14条全称为新错误。14923954的103依据来自Jaczynski书章和Flottweg2009资料，测试prior_art_specifications仅提供专利US8557297，没有这两份非专利文献。若任务只针对给定对比专利，保留102可能符合限定范围；若任务要复现完整审查依据，输入和gold都需扩展。14111727/6的两类依据则均来自同一Shin专利，必须明确单码优先规则或改为集合。

## 具体规则依赖

14111727，NANOWIRE SENSOR HAVING NANOWIRE OF NETWORK STRUCTURE，claim6。源审查正文：Shin记载纳米线50nm及重复间隔0.3–0.7倍，对应15–35nm；申请claim范围10nm–1µm。审查员引用MPEP2144.05及相关先例，认定重叠范围构成prima facie obviousness，并列103依据；同一文书此前还把claims1–7及9–12列为102(e)驳回。**这是源审查依据，不是本轮独立专利法律重审**；区间相交是数值事实，是否足以驳回仍依赖规则、反驳及具体特征，不能编译成所有重叠范围一律驳回。

14923954的103依赖Jaczynski的2008书章和Flottweg2009资料，原文涉及图、分离路径与离心机结构；本轮未取得这两份资料。不能把CTNF的审查员解释公开给模型当作原始对比文献。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 根据固定规范，批量判断claims相对于允许对比文献的102/103依据 | 已下载MPEP2100 Rev07.2022共524页；各案实际版本绑定仍待完成 | 2,884测试项/164申请，全部context.claims与源initialClaims相同 | 对比专利含审查员预选段落；完整说明书/图纸及非专利材料未全部补齐 | 原三分类及原CTNF独立保存；7个ALLOW直接冲突，14个双依据待明确范围 |
| 14111727/claim6，纳米线间隔 | MPEP2144.05重叠范围规则；不得只用算术代替完整判断 | 10nm–1µm目标区间及依赖claims | Shin US20130337567；50nm×[0.3,0.7]=[15,35]nm；源版本/图表完整性待继续核 | 发布102，原文同时102(e)/103(a)；不是已运行结果 |
| 14923954/claim1，甲壳类磷脂分离 | pre-AIA102(e)/103(a)，同一法律判断任务 | 相应初始claim与依赖链 | 发布输入只有US8557297；103还需Jaczynski与Flottweg资料，当前欠缺 | 对完整源依据为102+103；限定给定专利的任务不能直接借用缺失NPL的103 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(test).join(initial_claims)` | 2,884/2,884文本数组精确一致 | 来源转换一致性，不是原USPTO文档版本全量验证 |
| `sem_map(claim_features).join(prior_art_features)` | 示例区间[10,1000]nm与[15,35]nm | 单位换算可确定；特征是否逐一对应仍需语义判断 |
| `sem_map(applicable_grounds,E,features,prior_art)` | 14项源文双依据候选 | 输出集合或按明确任务规则单码，不能由source reasons顺序暗中决定语义 |
| `sem_filter(any(ground in {102,103})).project(id).count()` | 全库可靠修复gold计数尚未产生 | 已知局部事实不替代全批准确gold；执行失败单独ABSTAIN |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 纳米线例完整源参考含102/103；原三分类参考102。未运行，二者不混用评分 | 固定依赖展开→特征和量纲抽取→区间计算→读取同E范围规则和例外→输出允许依据；可共享规则缓存与固定复核 | 同一任务定义下同一参考，不预言更准确 | ==确认pre-AIA与claim依赖==→==核对Shin原文/图及范围单位==→==查MPEP2144.05的适用和反驳条件==→输出依据及证据；不能从本案CTNF获取答案 | `PatentGroundsOperator(E_version, claim_dependencies, prior_art_scope, feature_map, range_reasoning, anticipation, obviousness, evidence_gaps, abstain)`；同E编译、Coding Agent、固定工具、批Agent均需比较 |

本轮明确下一步构造要求：先冻结“给定对比专利”或“完整审查资料”的证据范围，再定义单码/依据集合及程序状态；需要补齐的NPL/图纸不能以专家解释代替。暂未建立修复快照或新确认集。脚本与私有诊断在`artifact/evidence/shared-environment-audit-20260908-v43/`；两份源审查实例保留在`data/...-v43/`，不挂载给被测系统。

未新下载、未调用模型、未执行作者程序、新工程测试0。使用既有audit-venv的pyarrow读取数据；session6888已正常结束。
