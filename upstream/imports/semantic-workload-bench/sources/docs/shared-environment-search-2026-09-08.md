# 长共享环境 × 真实批量决策：增量核验 1

日期：2026-09-08，Asia/Singapore。当前通过全部条件的可用数据集：**0 个**。这是本轮检索结果，不是不存在性证明。本轮停止于原始文件核验和两个官方来源交叉检查，未构造 workload、调用实验模型或验证环境因果增益。

用户新增筛选条件：一个冻结的长 policy/protocol/document E；同一任务下大量真实 items；逐项、独立可核验 gold；判断实际依赖 E。30–100 页和千级 cases 是用户给出的目标规模示例，不将它们擅自定义成精确硬阈值。分别报告实际长度和每 E 的 N。全文案例很长不意味着共享 E 很长；全库 N 不意味着每 E 的 N。

## 本轮新增证据（均不作为可用推荐）

### 1. Systematic review：实查 CSMeD-FT 发布包

[作者仓库](https://github.com/WojciechKusa/systematic-review-datasets) commit `b30e9739939f52b1e799295138791f1fd5b002a5`。下载 33,521,286 bytes ZIP，直接解析 CSV/JSON，无解压执行。发布包含 `main_text`、`decision`、`reason_for_exclusion`，所以“现成 screening 数据只有摘要”不能泛化到该包。没有逐一重新下载论文 PDF 或验证全文解析质量。

本次全量分组统计：

| 发布 split | 全文行数 | review 数 | 每 review 中位数 | 最大 N |
|---|---:|---:|---:|---:|
| train | 2053 | 148 | 6 | 171 |
| dev | 644 | 36 | 10 | 125 |
| test | 636 | 29 | 12 | 133 |

最大组 `CD001431` 为171行（68 included/103 excluded），其 `criteria_text` 1,039个空白分词。test 最大组 `CD013274` 为133行（13/120），字段长5,726词；逐节检查发现混入 `Data collection and analysis` 2,107词、`Sampling of included studies` 1,856词，及事后发现/分析过程。四个 `Types of ...` 小节合计758词；这**不是完整必要规则长度**，日期、语言和抽样等限制还可能在其他节。原文还存在重复列表。因此不能直接将5,726词当作干净的事前复杂 protocol，也不能把整个 review abstract（含结果）交给模型。

[原论文](https://oro.open.ac.uk/102450/1/NeurIPS-2023-csmed-bridging-the-dataset-gap-in-automated-citation-screening-for-systematic-literature-reviews-Paper-Datasets_and_Benchmarks.pdf) §5说明通过开放全文 URL 获取子集，再用 GROBID 解析；并非原 review 完整检索池。原 split 名称保留仅为来源名称：本次构造侧查看了标签，未建立本项目独立确认集。

**判定：不通过当前完整门槛。** 已证实有真实全文和筛选标签，但未获得长事前 E 加千级全文批量。按原 review 找注册 protocol 和完整筛选日志是后续具体缺口，不靠拼接不同 reviews 放大 N。

### 2. 法规：实查 OmniCompliance 的 GDPR articles 文件

[作者仓库](https://github.com/HKUST-KnowComp/OmniCompliance-100K) commit `07c44ff5795229ce1f205acaf6018f7b4ce569d5`。下载一个 GDPR articles cases 文件及 rules 文件；**没有审计全库**。本文件实际2,703行、486种 `source_rule`；每条 rule 的样本中位数6、最多10。2,703不是已去重的独立案件数。标签1,449 VIOLATES/1,254 COMPLIES。作者规则文件是多粒度路径展开，有父子重复，不以文件字符量估计法规净长度。

这2,703行都只有8个字段：`example_name, example_background, process_and_outcome, source_rule, relation_to_rule, involved_parties, relevant_rules, dates`，没有逐条来源 URL 字段。标题已有 Fine 等裁决信号；背景可能已经带有违法结论。发布的标签针对各自的 source_rule，不能不经审计改成“是否违反整部 GDPR”的统一 gold。

[论文](https://arxiv.org/html/2603.13933v2)说明先按规则检索，再由 Grok 搜索 Agent 总结案件及结果，人评为抽样而非全量逐案裁决核验。本轮在文件前四行做两项定点交叉核查（非随机错误率估计）：

- `Microsoft Bing GDPR Fine by CNIL` 写2022年罚款150 million euros；[CNIL 官方2022年12月公告汇编](https://www.cnil.fr/sites/default/files/atoms/files/lettre_information_cnil_decembre_2022.html)写60 million euros。金额错误已证实，但单凭金额错误不推导 Boolean 标签错误。
- 首行 TikTok 案的 `source_rule` 是 Territorial scope，`relation_to_rule=VIOLATES`。对应[爱尔兰 DPC 官方裁决公告](https://www.dataprotection.ie/en/news-media/press-releases/DPC-announces-345-million-euro-fine-of-TikTok)列出的违规条款为5、24、25、12、13相关款项，并非第3条。至少说明“适用某条款”和“违反某条款”未可靠区分，不能直接认可 rule-level gold。

**判定：不通过 gold/可追溯性门槛。** 官方法规与真实裁决的来源路线值得继续追，但当前发布行不能直接成为可用 benchmark；需要回到原裁决、稳定案件ID、事实/裁决分离和统一判定语义。不能根据两个定点问题推断全库错误比例。

### 3. 临床试验：方向和真实性排除

[TREC 2022 官方任务说明](https://trec-cds.org/2022.html)明确是 patient-to-trials，患者 topics 为医务背景人员编写的 synthetic admission notes。因此不是同一长 protocol 对大量真实患者的筛选决策。将关系转置也不能增加真实患者或生成未标注 gold。本轮不下载其大试验库，不将其列为可用候选。

### 4. 保险：长条款和真实案件尚未同时核实

[InsLogicBench 原论文](https://aclanthology.org/2026.acl-long.1035.pdf) §4.1给出110份中文保单、平均10,103 tokens、总2,621 QA；§3说明通过逻辑真值分配和模型合成案例。总量除保单约23.8只是均值，不代表每 E 分布。其案例不满足本轮真实 cases 要求，因此排除。

[纽约 DFS 官方申诉索引](https://www.dfs.ny.gov/public-appeal/search)搜索索引确认提供真实 closed appeals 的摘要/结果与 references；直接打开返回403。本轮没有取得并审查原始 case，也没有证据证明很多案件共享同一完整版本保单。状态是未核实，不是肯定不存在。

[InsureBench 页面](https://www.insurebench.com/)本轮显示 launching soon、scores pending；未发现可验证发布包和每 E 分组统计。不将营销描述当数据交付。

## 下一增量的具体问题

只追两条证据缺口，不再按“screening/compliance”名称堆候选：

1. 从真实法规裁决的原始档案检查：同一版本法规下，能否获取大量去裁决泄漏的充分事实输入，及含无违规结论的独立 gold；不能把执法罚款库的所有行直接当平衡合规筛选集。
2. 从单个真实 review 反查注册 protocol 和完整全文筛选日志。需要同时统计事前相关规则净长度、可公开全文数量及原始决定/排除原因；不以事后分析章节制造长上下文。

环境依赖需另测完整 E、无 E、适用范围合理但规则不同的 E，以及 E-only 直接编译的固定程序。当前只有来源审计，没有任何实验支持 Agent 必要性或长上下文成本。不能用未运行的消融替代通过条件。

## 可复核产物

[来源及 SHA256](../artifact/evidence/shared-environment-audit-20260908/sources.json)、[实测统计](../artifact/evidence/shared-environment-audit-20260908/statistics.json)、[统计脚本](../artifact/evidence/shared-environment-audit-20260908/inspect.py)。源字节在 Git 忽略目录 `data/shared-environment-audit-20260908-v1`。复算：

```sh
python3 artifact/evidence/shared-environment-audit-20260908/inspect.py data/shared-environment-audit-20260908-v1
```

仅用于本地来源核验；上游内容再发布权利未逐项审核，不提交原文数据。无需修改现行运行器、SPEC或将实验状态升级。
