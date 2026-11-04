# 第三十三增量：PLAT真实附加税争议与共享检索环境缺口

**累计仍1/10；PLAT为待核候选，不计入严格合格清单。** 原论文、完整作者仓库和韩英各100条二元判定数据已下载。真实判例及专家复核标签有依据；但论文所用100判例＋4,042法条的检索环境未在本次发布仓库中取得，无法核实固定版本、历史/当前案件隔离及必要输入。

## 下载证据

| 来源 | 实际取得 |
|---|---|
| [原论文](https://arxiv.org/abs/2503.03444) | 当前PDF25页、1,666,050 bytes，完整下载并提取正文；不将2025首发日期等同当前修订内容 |
| [作者完整仓库](https://github.com/lbox-kr/plat) | commit `f40c5374ce24184741ee618e45aca141c2c7149e`，6blob SHA1逐项通过、ZIP CRC通过且完整解压 |
| [韩文二元数据](https://huggingface.co/datasets/sma1-rmarud/plat-kor-mc) | revision `2bdf6af364c4619dd1859cbe653e509e47e75460`，全部100条 |
| [英文二元数据](https://huggingface.co/datasets/sma1-rmarud/plat-eng-mc) | revision `0fab935525e9cc9c40537244b41ead5cc83b2cd5`，全部100条，同源翻译而非新湖 |

收据/URL/大小/SHA256见`artifact/evidence/shared-environment-audit-20260908-v33/downloads.json`，原始文件在data同名目录；HF卡片声明CC-BY-NC-SA4.0，不能由此推定商用LBOX整个检索库可重新分发。未下载其他题型，也没有将它们算作新cases。

原论文§3.2说明从LBOX约2.8k候选判例中构造100例，o3先抽取事实/主张，再由税务专业人员检查信息充分性、答案泄漏、幻觉及标签合法性，每例约30–40分钟。这里的模型参与是文书构造，不等于真实案件合成；但发布的是整理后的事实摘要，非全部原诉状/原裁判文书。

实际两语言均100唯一case_no，50 lawfulness=True、50False。英文公开候选输入case_info+facts+claims按空白切词327/494/1010（min/median/max）；韩文160/255/539是空白分词数量，不可与英文模型token直接比。数据含reasoning、decision、lawfulness三列，必须私有。case_no前缀存在法院名称，不能把前四字符全当裁判日期。

## 核心缺口

论文报告RAG检索池含100判例和4,042法条，而当前小型repo以eval.py、README和探索notebook为主；已下载二元表没有独立版本化法条库。不能将同一表的当前reasoning/decision拼成公共知识库，也不能仅凭“4,042法条”声称实际获得长共享E或无泄漏。论文未在已核段落说明这100判例与评测100例的隔离关系，本轮保留未知，不认定已发生泄漏。

文章主要涉及“正当理由”免除附加税，需要判例解释，不只Article48一句规则。样例2011guhap2638还涉及地方税、企业危机、延期与减免申请期限；不能把所有案例简化为同一短法条的形式蕴涵。当前100同任务真实案例可以支持开发研究，但还不足以证明用户要求的长共享环境工作负载已就绪。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 批量判断附加税或拒绝减免处分是否合法，重点审查正当理由 | 所需法条＋历史判例解释池；论文称4,042法条＋100判例，实际完整环境未取得 | 100个真实判例派生的事实/主张摘要 | 当事人身份、税种、延期及减免程序；需保留法律适用版本 | 专家复核50合法/50不合法；当前法院reasoning/decision必须私有 |
| 2011guhap2638：造船公司获企业税延期，却未另申请居民税延期；争议拒绝减免是否合法 | 地方税减免、企业严重危机及申请期限等规则尚需公开版本化来源 | 公司及税务机关相反主张：公司称获工作人员指引，机关否认并主张逾期申请 | 事实主张的归属不可当成全部已认定事实 | 作者整理的法院结论撤销拒绝减免，lawfulness=False；不是“所有税额取消” |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(korean_cases).select(case_info,facts,claims)` | 100条，韩英同源不翻倍 | 当前三列公开候选，仍需独立泄漏审核 |
| `load(frozen_statutes_and_prior_cases)` | 作者描述4,042＋100，下载缺失 | 无法核验与当前gold隔离，不能拿私有reasoning补足 |
| `sem_map(penalty_legality,E).sem_filter(not_lawful)` | 参考50False | 实际未运行，不是构造后全量可用收据 |
| `project(case_id).count()` | 参考50，实际未知 | 三题型仍100源案件，非300独立cases |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 2011guhap2638参考False；当前缺完整公开E，实际未运行 | 同一E固定检索税种、延期、减免程序与正当理由；归属事实抽取后按规则判定；允许共享检索缓存 | 同参考，不预言更准 | ==识别争议为拒绝减免而非直接税额计算==→==核对地方税规则与申请时点==→==查企业危机/合理信赖的历史解释==→输出合法性/ABSTAIN，不能检索本案法院答案 | `PenaltyLegalityOperator(E_version, tax_type, challenged_disposition, attributed_facts, justifiable_reason_tests, procedural_tests, abstain)`；先补独立共享E再比较E-only、固定程序、Coding Agent与轨迹提取 |

无模型调用/作者程序执行/源码修改/新工程测试。研究者读取的首例属于开发曝光。当前问题是公开环境可追溯性，不是必须先证明Agent胜出；故不以作者模型分数决定湖是否可行。
