# AFD 删除讨论：大批真实结果已核验，严格任务 Reject

原始任务是讨论结果预测；把它改成“按共享政策独立判定文章应否删除”需要补原条目、历史政策和来源，不能直接继承预测gold。它有类似HSCodeComp的语义主题差异，但没有可核验的执行家族；当前更接近讨论分类，K未知。

## 表1 入场审计

| 数据湖 | 原论文/仓库 | E | x与N | 固定q / gold | C / D / E / G | 获取 / Verdict |
|---|---|---|---|---|---|---|
| Wikipedia AfD 2005–2018 | [26页CSCW原论文](https://www.cs.cmu.edu/~awb/papers/2019_Mayfield_CSCW.pdf)，[完整作者库](https://github.com/emayfield/AFD_Decision_Corpus)，commit e184673699fb2577c8369a1f18adb903d0b57e63 | taxonomy.txt 47499bytes/3112行，别名与分类目录；完整事前政策正文/历史版本未取得 | Cornell镜像383918讨论、3295340发言；0孤立关联、0无发言讨论 | 给定冻结讨论前缀预测关闭结果；人工社区关闭结果、程序标准化标签；不是独立规范正确性gold | C20关联检查完成、完整支持0；D多数票强对照未排除；K未知；G外部来源/修订历史欠缺，outcome字段直接泄漏 | 原论文与全repo、401810632bytes镜像已下载CRC通过；政策与实验split未齐，Reject |

镜像原始计数不同于论文抽取402440/分析369592，转换差异未闭合，不混用。论文37政策/44指南/71essay及2111aliases是论文统计，不当成本地完整政策。仓库GPL3；Wikipedia原始文字权利需单独核对，仓库许可不覆盖全部外链。镜像源与哈希见[source receipt](../artifact/evidence/shared-environment-strict-afd/source-progress.json)。ZIP SHA256 7a87283e217ad4da6e69688a0205da517f0765f76a7fd402009016d2b3b35035。

## 表2 Query × 数据湖

| Query | 数据湖1：utterances.jsonl | 数据湖2：conversations.json | 数据湖3：taxonomy.txt |
|---|---|---|---|
| q1 预测关闭动作标签集合 | 截止时间前的text/timestamp；可选择明确允许的投票label | 383918条，article_title可公开；outcome_label/raw_label/rationale等必须私有 | 政策引用别名，不是完整E |
| q2 按完整政策判定是否应删除 | 当前缺文章历史全文和封存的外部证据 | 原关闭动作不能自动作为独立合规gold | 缺历史全文，因此不可构造可回答任务 |

q1可重复，信息不足应ABSTAIN；no-consensus是源语义结果而非ABSTAIN。其他候选q没有独立gold，不人为扩成2–5任务。

## 表3 类Python DAG

| 类Python的DAG | 具体数值/语义边界 |
|---|---|
| `scan(383918 conversations)` | 普通算子，ID关联3295340发言 |
| `x = project_public(cutoff(utterances))` | 普通时间截断和字段allowlist；关闭理由禁止进入 |
| `stance = sem_map(text)` | 语义算子；若允许原vote标签需给所有臂同资源 |
| `features = aggregate(stance, time)` | 固定普通程序；撤票/重复/编辑仍需契约 |
| `prediction = sem_map(features, discussion, allowed_E)` | 决定预测；当前仅taxonomy，不可声称完整政策判断 |
| `score(prediction, private_outcome)` | 普通评分；标准化混合动作不能未经验证变成二分类 |

## 表4 方法预期（全部未执行）

| LOTUS关键操作预期结果 | LOTUS执行过程 | Data Agent预期结果 | Data Agent过程，==探索== | 预期operator结构 |
|---|---|---|---|---|
| 100154443的源gold为keep；未预测模型会输出keep | 语义抽取两个村名/来源主张→固定检索→预测 | 同资源不能补出人口普查原件；优势未知 | ==检查GEOLAND引用和实体冲突==→发现外链未封存→预测或ABSTAIN | `entity_resolution→source_check→policy_compare→outcome`；仅设计，未提取 |

| 四路臂 | 预期过程/风险 |
|---|---|
| 任务only静态 | 文本/立场分类；可能已很强，不是环境依赖证据 |
| 完整E静态 | 完整历史E未获得，该臂不可执行；taxonomy全量可放入或索引但不能冒充政策全文 |
| 逐记录Agent | ==查别名/政策定位==→比对主张；缺失原件不会被探索自动修复 |
| 批Agent | 可共享别名索引与政策定位缓存；没有证据其收益来自语义家族而非普通预处理 |

ρ_E=别名索引；ρ_P=截断/立场提取/投票汇总；ρ_G候选=地理实体、人物/作者、组织、列表合并，但仅主题而非测得执行家族；ρ_R=具体来源可信度/实体/编辑演变。比例与K均未测，不以政策数或标签数估计K。

原论文§4.1：非平票讨论中管理员94.8%遵循多数票；加入语言的模型相对仅gold投票特征无显著提升。这是论文完整讨论结果，非本次运行，不能外推到提名时刻。强固定基线必须保留立场提取、投票与时间聚合、固定规则/检索。当前未证明超越普通分类、RAG或缓存。

## 20个独立讨论审查

按SHA256(`afd-strict-v1`+NUL+conversation_id)排序取20，合计158发言。读取gold、提名、引用和贡献节选；长文本未做逐字完整审读，不能称20完整C。证据[样本](../artifact/evidence/shared-environment-strict-afd/sample20.json)、[审查收据](../artifact/evidence/shared-environment-strict-afd/sample20-audit.json)、[全量统计](../artifact/evidence/shared-environment-strict-afd/corpus-counts.json)。

| ID | gold | 观察与缺口 |
|---|---|---|
| 100371610 | delete | 仅提名一条；最终soft delete与两次relist来自私有理由，原文/流程历史未完整冻结。 |
| 100408864 | keep | 非英语来源与旅游指南可信度、地理显著性；外部新闻和条目原文缺失。 |
| 100314999 | delete | 来源独立性、宣传与电影重定向争议；外部参考/修订历史缺失。 |
| 100121853 | no-consensus | 音乐显著性与媒体覆盖争议；真实no-consensus不是不显著性判定。 |
| 100115215 | delete | 氏族目录与GNG，引用其他AfD；该先例和实际来源未封存。 |
| 100013486 | keep | 无参考不等于不显著，BEFORE流程被引用；条目及显著性证据缺失。 |
| 100088892 | delete redirect | 蓝色染毛/历史皮毛词义分歧与撤票；delete redirect不能强映射简单delete；外部书籍/报刊缺失。 |
| 100132519 | delete | 管理员理由为空；只有投票及Google搜索主张，无法定位完整政策依据。 |
| 100379181 | other | gold other，原理由是恢复消歧义并重定向；规范化标签丢失动作细节。 |
| 100415175 | delete | 软件来源独立性与搜索无结果；搜索结果及公司条目缺失。 |
| 100256868 | delete | 公司显著性，Google无显著覆盖主张未附封存证据。 |
| 100078178 | delete | 运动员职业联赛与GNG；Soccerway外部资料，未封存且涉及不同球员。 |
| 100154443 | keep | 两村实体混淆经人口普查纠正；Google Maps/存档/条目版本缺失。 |
| 100385256 | no-consensus | 作者出版来源争议；no-consensus default keep；关闭理由属于gold不能做公开E。 |
| 100169527 | delete | 家谱组织独立来源，ORG/GNG规则只有引用分类，来源缺失。 |
| 100108817 | delete speedy | 仅一提名；私有理由A1速删，原条目上下文缺失。 |
| 100397054 | delete | 手册/教程排除；微软文档与原条目缺失。 |
| 100337447 | delete | 列表范围、合并和版权历史保留；条目在讨论中变化，来源与时间截断须冻结。 |
| 100244495 | delete | 学者GNG/PROF/TOOSOON；论文影响与可靠覆盖仅参与者主张。 |
| 100107741 | delete | 作者显著性/单一事件/隐私；条目反复编辑，来源及历史版本缺失。 |

真实例子100154443：提名认为无法定位村庄，讨论先将Khosalipur认作Khosalpur，后据人口普查纠正为两个村；gold=keep，引用GEOLAND。当前库保存这些主张及外链，没有相关人口普查内容与冻结政策条文，因此不能给出完整E短引并声称依据闭合。

无模型运行、无作者脚本执行、无实验split构造；未新增可运行workload。源码master checkout不等于论文cscw_checkpoint复现实验。
