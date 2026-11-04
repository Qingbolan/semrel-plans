# 第十二增量：ILSI / LeSICiN 的原始来源与标签审计

2026-09-08，Asia/Singapore。严格通过数仍0/10。本文为排除/待核账本，不将未通过候选列为可行数据湖。

## 下载和核验范围

[原论文](https://arxiv.org/abs/2112.14731)PDF已下载，523,932 bytes。[作者完整仓库](https://github.com/Law-AI/LeSICiN)锁定commit `612dc7bd2d579292c70dd6c6d457858f49ac3075`，ZIP18,726 bytes，14个Git blob全部一致。没有执行作者代码。

[作者Zenodo6053791](https://zenodo.org/records/6053791)完整下载并通过元数据MD5的文件包括dev.jsonl（85,261,365 bytes）、secs.jsonl、label_vocab.json、schemas.json、type_map.json、label_tree.json、citation_network.json。未下载模型权重/2.25GB向量。train/test下载主动停止，保留为`.partial`；它们不参与本轮统计。完整作者仓库与完整数据集是两件事，本轮不声称全量数据已下载。

原资产：`data/shared-environment-audit-20260908-v12/`。[下载收据](../artifact/evidence/shared-environment-audit-20260908-v12/download-receipts.json)、[可复算脚本](../artifact/evidence/shared-environment-audit-20260908-v12/audit_data.py)、[统计](../artifact/evidence/shared-environment-audit-20260908-v12/statistics.json)。

## 数据实际是什么

论文描述从Indian Kanoon的最高法院与六个高等法院裁判中，用分类器抽取Facts（论文报告该抽取器Facts F1为0.839），以原判决引用的IPC条款为标签。不是人工逐条重标事实充分性或罪责。论文称66,090条案例，列出的分割数又为42,884/10,203/13,043；本轮实际完整dev文件是**10,200条**。先前进度消息提到的10,203是论文数，应以本次文件计数为准。

共享发布环境只有100条高频IPC条款，46,219 bytes、7,050空白分词；不是完整500余条IPC，也没有完整版本/生效日期匹配证明。把更长IPC另行附加，不能自动证明发布gold已对应那一版本。

完整dev实测：10,200个不同ID、39,923条gold引用边；所有gold均存在于100条目录。10,153个不同精确文本，即47条相对唯一文本数的冗余。8,824条出现`section(s)+编号`；7,688条至少有一个显式编号与本条gold匹配（75.37%）。2,884条命中宽松的appeal/petition→dismissed/allowed模式。

正则只匹配紧邻的第一个编号，未穷尽并列/变体引用；命中可能是历史审级或诉讼请求，不全等于当前结论泄漏。它证明输入常带直接标签线索，需要语义审计，不能单凭此比率断言全部数据无效。

## 具体原例交叉核验

开发记录`1000139`，[对应原判决](https://indiankanoon.org/doc/1000139/)是2008-09-10的Inspector Of Police, Tamil Nadu v Muthusamy & Anr。工具网页可读；直接HTTP下载403，因此未伪称保存原HTML。

公开输入保留：一审依据IPC302及34定罪、高院无罪、最高院认为证据不足以干预高院，并有上诉驳回结语。发布gold只有`Section 34 in The Indian Penal Code`。原网页正文同时出现302和34，但只给34建立法条链接。这支持“标签可能受网页链接抽取覆盖影响”的推断，未证明作者对所有记录采用相同抽取逻辑。

因此：把gold缺302解释为“302不相关”，或把gold含34解释为“34罪责成立”，都没有依据。该例实际维持无罪，标签仍含34。详见[开发例子](../artifact/evidence/shared-environment-audit-20260908-v12/development-example.json)，含private gold，只用于构造审计。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 原任务：预测每份Facts对应的IPC引用集合 | E：100条高频IPC文本，7,050词 | R：本轮完整dev10,200条自动抽取Facts | 层级图；训练引用网络必须另设允许历史监督边界，不可挂载当前gold边 | 39,923条dev引用边；不等于穷尽的适用/违反标签 |
| 对1000139，是否输出“第34条被引用” | 第34条共同意图规则 | 文本本身出现Section34 | 完整原判决可作构造溯源；不可提供给预裁决系统 | TRUE，可通过文本抽取命中，未证明需长E |
| 对1000139，是否认定共同犯罪成立 | 需完整适用法律、证据与审级任务约定 | 发布输入包含终局结语 | 现有引用目录不足以定义判决任务 | 无此gold，不能把引用TRUE变成有罪TRUE |

## 类Python DAG

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `E = load(secs, label_tree)` | 100条，7,050词 | 已核来源；不冒充完整刑法 |
| `R = scan(dev).project(id, text)` | 10,200条 | 原文件混存labels，构造必须allowlist分离 |
| `mentions = extract_section_numbers(R)` | 8,824条有显式编号 | 本轮正则检查；是强抽取控制，不是语义算子学习 |
| `pred = sem_map(R, E, predict_cited_sections)` | 每行多标签集合 | 未运行；不改成定罪判定 |
| `selected = sem_filter(pred, contains(section34))` | 实例gold目标TRUE | 未运行；只能评价引用集合成员 |
| `score(private_links, pred)` | 39,923条dev边 | 未评分；缺引用不是严格负例法律判断 |

## 多种方法预期表

全部为未实测预期。不能把论文本身的神经模型指标当LOTUS或Data Agent结果。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 1000139的34成员目标TRUE；预测302也合理但可能被原gold罚 | 文本引用抽取→标准化到目录→集合；无需预设每行读取全部E | 同样可能给{302,34}；不能声称更准 | ==核正文302/34与任务“引用”定义==→==分辨当前与历史审级==→输出 | `CitationExtractor → Normalize → Deduplicate`；可能只是抽取控制 |
| 若改问定罪，原标签不能评分 | 必须另建任务与gold，不能沿用引用gold | 应指出标签语义不支持；不是Agent收益 | ==检查引用是否等于裁决认定==→拒绝偷换任务 | 任务语义校验；不能从一条示范发明新法律标签 |
| 对无显式引用的行，固定检索可能足够 | 同E检索→候选法条匹配→证据检查，允许缓存/分支 | 有界探索是否改善未知 | ==查相关条款条件与例外==→==检查事实是否足够==→输出或ABSTAIN | 参数化法条检索与条件检查；必须对照E-only编译和Coding Agent |

## 决定

本轮不计通过：原gold支持引用预测，不支持完整的适用性/责任判断；共享法条为短选集；自动Facts抽取残留裁决和编号线索已获具体原例及批量证据。单纯加完整法律文本并删除显式编号，仍未修复gold语义，不能这么构造“合格”任务。

未运行模型、无新专家标注、无新增工程测试（0），仅下载完整性、结构统计与原例交叉核验。论文分割计数与文件不一致保留；许可与跨split实体重叠未完成。目标仍为至少10个严格求证的可行湖，继续寻找独立来源，不用本轮排除项补数。
