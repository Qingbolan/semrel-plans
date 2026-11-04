# TrialGPT 2.0 / NIH-TrialBench：严格来源核验

**Reject（当前公开材料）**。原论文是2026-09-01的[43页预印本](https://arxiv.org/abs/2609.01202)，不是2024 TrialGPT。已下载24418822字节原PDF并实际阅读Methods的系统、队列、评审设计及补充政策描述。完整下载[作者现有TrialGPT仓库](https://github.com/ncbi-nlp/TrialGPT)，HEAD仍为1b3242cd50c153a9c324661d4a0bd94fc68a4226，共24 tracked文件；它是旧数据发布，未含NIH-TrialBench或2.0专属目录。没有找到专属发布不等于证明任何地方都不存在。下载成功不能写成获得2.0病例。

## 入场审计

| A固定q | B共享E | C依据定位 | D完整E静态不足 | E家族 | F真实批 | G回答性/独立gold | H获取 | Verdict |
|---|---|---|---|---|---|---|---|---|
| 可定义患者→固定组合内试验推荐；资格与推荐不能混用 | 回顾队列各自固定trial corpus与policy；前瞻每周更新；非单一长protocol | 0/20，未取得新病例与标签 | 未确认；原系统已有固定检索和结构化评估 | 治疗线次/生物标志物等语义因素，K未知 | 公开benchmark126合成；真实NCI100患者×9试验，不是900患者 | 推荐还依赖临床优先级；最终共识包含辅助评分，不全是模型盲法标签 | 原PDF/旧完整repo已下；新数据、完整E、专属许可未取得 | Reject |

NIH-TrialBench Methods明确由24名研究者按目标试验编写126合成病例，共享1373候选试验，990配对被审；以上是论文数量，不是本地数据统计。临床回顾共288病例横跨五工作流，不能合并成同一个E；前瞻27例的E每周更新。NCI是最接近可审清单的真实子队列：100病例、9试验、900全审配对。但每个固定trial最多100病例，且未取得输入。

Methods pp19–20明确每对有一个先于辅助实验的独立盲法临床标签；另两位在交叉设计中分别有/无系统辅助。三者一致取共识，不一致第四人裁定。**不能说不存在独立人工标签，也不能把最终共识全部称作模型无关。** 其余多为模型选出的高推荐top10审查；未评配对不能当负例。作者也说明hit rate不是全库recall。

## Query × 数据湖

| Query | NIH-TrialBench | NCI真实队列 | 前瞻POTB |
|---|---|---|---|
| 患者→试验推荐清单 | 126合成vignette；目标trial；共享1373trial；原JSON未取得 | 100临床病例×9trial；原病例/标签未取得 | 27真实病例，339配对；每周快照未取得 |
| 固定trial→逐患者资格 | 反向N至多126且合成 | N=100；三类为Eligible/Subject-to-change ineligible/Definitely ineligible | N至多27，快照不同 |
| 决策语义 | Recommended/Eligible but Not Recommended/Ineligible | 三类是下一步筛查行动，不是最终入组 | 最终临床推荐，不是协议条件的纯布尔结果 |

没有可下载的真实逐例，不编造患者字段、条款和gold实例。论文讨论的误判片段不是完整数据行。

## 类Python DAG

```python
index = index_trials(E.corpus)                 # 普通共享预处理
for patient in cases:
    trials = retrieve(index, patient)          # 固定检索；小组合全遍历
    facts = sem_map(extract_clinical_facts, patient)
    assessments = sem_map(match, facts, trials, E.policy) # 决定语义输出
    ranking = sort(assessments, key=(fit, confidence))    # 普通排序
    emit(ranking)
```

该固定流程是必须保留的强baseline，不能把所查试验不同当作K种程序。病例资料、trial标准、推荐政策及医学知识的闭合仍需独立检查。

## 四路推演（未执行）

| 臂 | 结果预期边界 | 过程 |
|---|---|---|
| 传统LOTUS仅任务/病例 | 缺trial条件，无可依据的具体标签 | 直接推荐，不能作为有竞争力完整输入基线 |
| 传统LOTUS+完整E | 无证据证明固定流程不足 | 同资源索引→事实语义列→逐trial匹配→排序 |
| 逐记录Data Agent | 可能核对治疗线次；质量未知 | ==查候选trial标准及政策==→==核治疗背景/缺失项==→结构化评估 |
| 批Data Agent | 可能共享trial索引、固定条件；额外增益未知 | ==预建trial与条件索引==→按早期事实候选分组→==复用相关条件==→逐患者复核 |

可能operator为`extract_facts→retrieve_trials→match_criteria_and_policy→rank`，尚未提取。ρE为索引/条件解析，ρP为固定匹配排序，ρG为治疗线次/分子背景分支假说，ρR为个案临床判断；所有比例及K未知。政策可以env-only预处理，固定语义条件分类尚未被排除。

十问结论：q/输出见表；不足信息在原系统影响confidence而非自动不合格，不能自创UNKNOWN gold；E大小和版本必须按队列取得，不能拿1373项注册信息代替完整protocol；x/N与y标注来源如上；C0；D未知；E/K未知；探索拆分如上；G有隐私不可获取、临床背景及辅助标签问题；当前不能证明区别于固定RAG/条件评估。更接近固定条件评估路线，尚无HSCodeComp式中间执行家族实证。

[下载与观察收据](../artifact/evidence/shared-environment-strict-trialgpt2/source.json)。未运行作者代码、模型或临床实验；旧仓库LICENSE不能替新队列授权。当前版本停止正向20例审查，因为合成/规模与获取条件已不满足。
