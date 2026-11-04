# 第116轮：Leaf Clinical Trials（LCT）新候选，原始发布与当前仓库存在差异

状态：待定，不计入可行名单；累计7/15。没有将1,006个不同试验误称为同一protocol下的1,006名患者。本候选依据用户允许的sem_map范围，研究共享标注规范下的批量条件语义抽取。它不是患者批准/拒绝数据。

## 实际取得的材料

[原论文](https://www.nature.com/articles/s41597-022-01521-0)的作者预印本PDF（arXiv2207.13757，19页）已下载；三个完整作者仓库ZIP取得且CRC通过。另完整git clone规范Wiki，commit `656ae3e826bf5f20904eaf9944df8e84a3b5f75b`，59个Markdown文件、7408正则词（包含导航/性能页/链接，不全是必需规范）。Wiki嵌入远程图像并未随git克隆取得，不能称完整视觉规范已离线获得。

| 来源 | commit/版本 | bytes | SHA256 |
| --- | --- | --- | --- |
| https://api.github.com/repos/uw-bionlp/leaf-corpora | 461288aeba8b37fabd43bd7c55f0e1cb1bb10b9e | 3221490 | d9bc6eea1cb239976c1d36f2164c1d4a8828851fdb157d84f7185f6d8e65d57f |
| https://api.github.com/repos/uw-bionlp/clinical-trials-gov-data | 62d54af08ba52e8196e664fcec01122a4d4e38ab | 7604957 | 0672a36779d4e4a80c85050609243c593f10ace82e0450f87ca789dbd8f5f1fa |
| https://api.github.com/repos/uw-bionlp/clinical-trials-gov-annotation | 1d90d8d13aa23e2820fa39306c6fb581901f3512 | 588 | ee92e399e815c1fdc3b6325493cd0064be50f44fb1392a558b64b211ec23eb72 |
| https://arxiv.org/pdf/2207.13757 | 原论文预印本 | 919648 | f1deb2f8ef5b9d1a5ec2e6b12f6dc2d9b640031e6e90ff116374bc930af6c1a1 |

论文指定[Figshare原始发布](https://doi.org/10.6084/m9.figshare.17209610)的完整lct_corpus.tar.gz也已下载：1,331,799 bytes，2034成员；作者MD5核对通过，SHA256 `fa875243c14295adf6b5c431e1998c1b074ee010c9787a3bf2e30cd0fe075211`。元数据声明CC BY4.0，当前leaf-corpora仓库有MIT文件；分别记录，不将MIT自动外推到所有上游材料。

## 原始数据核验

当前leaf-corpora的leaf_clinical_trials：1006份文本、56067文本span、27966事件、12471属性、10410显式R关系。事件内部角色同样承载关系，不能只数R行声称关系总量。50种span类型；本次范围/逐字surface/引用检查全部通过，无不连续span。两组文本完全重复：NCT03929458/NCT03925753、NCT03867032/NCT03867058，故1004份唯一文本；未自动排除或生成确认split。

原Figshare：1006份，56093 spans、27990事件、12479属性、10422 R关系。与当前仓库1006/1006文本字节一致，但只有963份标注字节一致，43份不同。差异未解释，不能混合两个版本的gold，也不能将字节差异全部认定为语义改标。

原论文报告513份人工起始标注、493份模型预标注后人工修正；不是纯模型silver，也不是所有样本从零双人标注。论文还举例用UMLS解决概念边界，历史资源和完整规范输入条件待核验。当前检查未验证属性值语义、角色合法性、事件环、全量源版本语义等价或指南例子泄漏。

## 具体任务表（候选，非资格确认）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 把各试验条件编译成可审查的数值/时间约束结构 | 同一批1006份真实ClinicalTrials.gov条件文本（1004唯一文本） | 共享LCT规范Wiki，Eq-Comparison、数值单位/时间单位、过去/未来等规则 | NCT03860038：文本位置25–28为Age，29–33为≥ 18 | Age事件→Numeric-Filter→Eq-Comparison；Operator=GTEQ；Value文本18；这是结构gold，非患者入组gold |
| 为条件审查检索例外、否定及条件依赖 | 同一批完整条件文本 | Exception/Negation/If-Then等共同规范 | 规范明确逗号隐含Or不标注，只有显式or/and-or连接才标注Or | 当前原生标签含If-Then259、Or4157、Negates932（另有带数字的重复角色，须保留）；不是完整逻辑推论gold |

| 类python的DAG | 具体数值 | 关键中间操作 | 已有下游gold/边界 |
| --- | --- | --- | --- |
| `trials.sem_map(extract_lct_graph,E).explode(numeric_constraints).project(span,operator,value,unit)` | 1006输入；5297个Eq-Comparison span；1962个精确名Numeric-Filter角色 | 输出原生span、事件、属性和角色，再固定投影 | 示例Age≥18对应GTEQ/18；所有数值约束的完整投影尚未构造，不把5297当有效SQL数量 |
| `trials.sem_map(extract_lct_graph,E).explode(relations).filter(type=='If-Then').project(source,target)` | 当前图259个If-Then | 语义解析→固定类型过滤 | 可对原生边评分；没有公开真实患者表或SQL执行结果gold |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未运行；简单Age≥18正确目标为GTEQ、18，不能靠此例证明复杂E必要 | 同规范sem_map解析完整条件→校验偏移/角色→固定投影；允许共享缓存 | 未运行；应产出同样结构，优势未知 | ==查比较操作及单位规则== → ==区分数值过滤与时间范围== → 生成原生结构→校验 | `LCTGraph(text,E_version)`保留event/attribute/repeated-role，版本冻结；结构投影单独声明，不直接生成无gold的患者决定 |
| 未运行；对隐含Or应遵守标注规范而非补出所有逻辑连接 | 规范给出显式连接约束，可被固定程序/E-only编译使用 | 未运行；同一规范下不得擅自补边 | ==读取Commas-that-mean-Or约定== → 输出显式边 | 名义角色与重复参数明确映射；不预设轨迹学习胜于E-only或Coding Agent |

## 判定与下一步

共享规范有真实任务特定约定，数据量和gold形式值得继续。但7408词总Wiki不等于7408词必要规则；年龄例本身可由短规则完成。下一步核验43份标注差异、Wiki缺失规范页/图片和例子重叠、事件角色与属性完整性，再决定能否加入可构造名单。LCT与同仓库LLF不计为两个独立湖；未启动LLF实验。

本轮产物在`artifact/evidence/shared-environment-audit-20260908-v116/`：downloads.json、release.json、figshare-metadata.json、audit.py/audit.json、example.json、release-parity.json。raw在同名data目录。可复跑当前语料诊断：`python3 artifact/evidence/shared-environment-audit-20260908-v116/audit.py`。无模型调用、无新增单元测试、无commit；源码获取/静态检查不等于模型质量验证。
