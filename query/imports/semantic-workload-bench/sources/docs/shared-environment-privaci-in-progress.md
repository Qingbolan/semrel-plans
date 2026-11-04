# PrivaCI-Bench 原件审查

[原论文](https://aclanthology.org/2025.acl-long.518/)与[官方完整仓库](https://github.com/HKUST-KnowComp/PrivaCI-Bench)已下载；commitcb49d187095062bfff554121d4fa31440a32578e。下载SHA见[来源收据](../artifact/evidence/shared-environment-strict-privaci/source-progress.json)，实际Arrow读取见[计数与源哈希](../artifact/evidence/shared-environment-strict-privaci/arrow-counts.json)。进行中，不计Strong。

| Query | 数据湖数据1 | 数据湖数据2 | gold边界 |
|---|---|---|---|
| 判断案例在GDPR下permit/prohibit/not applicable | GDPR/data*.arrow 3137行case_content | GDPR规范树与角色/属性知识库 | 2462prohibit、675permit；允许来源为政策和合成，需核独立性 |
| 同类HIPAA任务 | HIPAA214行 | HIPAA规范与辅助KB | 20prohibit/87permit/107not applicable，论文正文所列19/86/106不一致 |
| AIAct任务 | AI_ACT3000行 | AIAct树 | 971/1029/1000，原文说明全部合成，不是现实案件批 |
| ACLU相关法律任务 | ACLU69行 | 原作者未解析对应法源 | 58prohibit/11permit；首例是诉讼进行中的amicus说明，不自动是终局判决 |

| 类Python DAG | 语义 |
|---|---|
| `scan(case_content) -> sem_map(CI_roles,attributes,purpose)` | 公开输入不能包含人工/模型标好的CI参数 |
| `ground(CI,KB) -> retrieve(law) -> sem_map(compliance)` | 语义角色归一和规则适用；固定检索流程尚未排除 |
| `evaluate(pred,private_norm_type)` | 必须先核norm_type来源与粒度；not applicable不是执行ABSTAIN |

| 方法 | 预期过程 | 结果/复用边界 |
|---|---|---|
| LOTUS任务only | 直接case_content分类 | 原DP；结果并非本次实测 |
| LOTUS完整E/固定检索 | CI抽取→固定KB匹配/检索→判断 | 原论文naive RAG失败不足以排除强固定方法 |
| 逐记录Agent | ==核主体角色、例外和法律范围==→决策 | 缺失法源/独立gold不能靠Agent补成已验证 |
| 批Agent | ==共享法规与角色索引==→逐条适用 | rho_E/rho_P可复用；rho_G/rho_R及K未测 |

原DP+CI与DP+CI+LAW使用标注CI参数、适用规则，是annotation-given条件，不可当普通资源对齐对照。必须保留源实体/来源划分；3137篇类文本未证明3137独立事件。原数据没有来源URL字段的子集仍需外部映射，不能把文章号定位替代gold必要且充分依据。

实际首条GDPR为MPIL未加密密码及未记录/上报泄露；标注Article32/33/34，但当前文本的通知条件是否充分仍未核。首条ACLU是Nijeer Parks案法庭之友陈述，处于反对summary judgment阶段，不能解释为法院最终确认违法。未完成20条审查，不升级。


## 固定20条GDPR实质审查

[逐条样本、条文映射与缺口](../artifact/evidence/shared-environment-strict-privaci/gdpr-sample20-review.json)：按原行号SHA排序，20条不重抽。共享KB实际679行，条文ID可定位，但不等于gold充分性成立。第7/16/18等permit文本缺合法性充分事实；第20的violated_articles含33，背景却说按33报告，未给迟报等事实。Article32安全措施与Article33通知应分开，不能由其中一项失败推定两项都违反。本文不修改gold，也不把无同意简单等同违法（Article6有其他依据）。

已读库内Article6(1)、7(1)、7(3)、33(1)对应文本；第2/10允许文本直接断言compliant，存在答案措辞线索。当前20是内容/条文局部审计，原裁决与来源映射仍缺，不能升级C20。


## 当前判定：Reject；相关强固定基线已取得

C20完整依据、G独立真实标签闭合与D/E均未达到，固定样本还存在标签/事实缺口。因此当前公开组合判Reject，不是证明无法从原始案件重建新任务。原始法规/知识库可作为资源，但不能替代缺失事实。

相关[ContextLens原论文](https://aclanthology.org/2026.acl-long.294/)与[完整官方库](https://github.com/HKUST-KnowComp/ContextLens)已下载，见[来源收据](../artifact/evidence/shared-environment-strict-contextlens/source.json)。论文§3–4复用PrivaCI GDPR628/AIAct600测试集，不增加独立数据湖。它预分四层规则、固定语义问答、优先级聚合，并用多重图执行AIAct检查器；这是需要纳入的强固定方法，而非新Agent必要性证据。此处没有运行模型或复现性能。
