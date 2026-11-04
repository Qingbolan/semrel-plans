# UDRP严格审计：Partial，非Strong

原论文、完整843037756bytes作者归档、152页官方共享E及1572公开案文已在历史22–26轮下载。此次复用原字节，不重复下载；[原下载与版本证据](shared-environment-search-2026-09-08-round26.md)。[原论文](https://astrolavos.gatech.edu/articles/Manuscript_UDRP_final.pdf)、[作者完整归档](https://doi.org/10.5281/zenodo.16954717)、[官方Overview](https://www.wipo.int/amc/en/docs/2023_overview3.pdf)。本轮实际读取private标签、两案裁决片段、1287公开输入、E目录及相关术语位置；没有声称20案全文法律复核。

| 入场项 | 实测证据/缺口 |
|---|---|
| A | 按统一UDRP规则预测公开记载案件是否获救济，固定q成立 |
| B | 152页共享解释/政策；不等于每案需要全文 |
| C | 20确定性样本已提取引用线索，完整事实—条款必要/充分审查0/20；引用数字非通过收据 |
| D | 完整E固定检索/事实列/规则图不足未证明 |
| E | 有合理使用、恶意时间、被动持有等家族假设；K未实测，不用标签比例推断K |
| F | 1572真实单域名裁决的回顾性静态切片；1513获救济/59驳回 |
| G | 裁决作者已筛选事实，原诉状未给；1287另行查询内容未封存，语义泄漏及实体划分未闭合 |
| H | 原文/完整发布/E可得；软件许可不等于全部裁决和指引再发布授权 |

**Partial**。不同规则判断实际存在，但是否坍缩为可复用语义执行家族、是否超出固定程序，仍无直接证据。常量获救济准确率1513/1572=96.2468%，驳回类recall=0；这是标签算术sanity，不是LLM实验。标签偏斜说明只报accuracy会误导，不能单独证明“路径不分叉”。

| Query | 数据湖数据1 | 数据湖数据2 | 私有gold |
|---|---|---|---|
| 对每案判断是否应获转移/撤销救济 | public-v2/environment.pdf | cases/*.txt，§1–§5记载事实/主张/程序 | gold-extraction-v2.jsonl，正式决定提取的粗标签 |
| 返回获救济ID清单与数量 | 同E | 同1572案 | 1513；普通投影不是第二个独立语义任务 |

一页任务列：id；decision=RELIEF_GRANTED/DENIED/UNKNOWN；attributed_facts；rule_refs；status=OK/ABSTAIN。UNKNOWN为证据不足，非DENIED；该扩展尚无独立标注，不可擅改原gold。public-only输入不含当前裁决分析，分析只用于构造审查。

| 类Python DAG | 类型/条件 |
|---|---|
| `facts=sem_map(extract_attributed_facts,cases)` | 语义：事实与主张归属、时间、使用方式 |
| `rules=retrieve(frozen_E,facts)` | 固定检索也允许分支/多跳 |
| `elements=sem_map(apply_elements_and_exceptions,facts,rules)` | 语义，决定三要件；可合法早停 |
| `decision=combine(elements); project/filter/count` | 固定组合与普通下游；过程缺失不等于否定事实 |

| 臂 | 预期执行结果/过程 | operator |
|---|---|---|
| LOTUS任务only | 未测；常量可获96.25%但漏全部驳回 | 通用判定提示不构成充分对照 |
| LOTUS完整E | 同目标；可能足够，未测 | E-only规则图+固定检索+语义事实表+要件检查 |
| 逐记录Agent | ==查适用规则==→==核对时间/事实归属==→==识别例外==；缺未封存材料仍无法确保正确 | UDRPReliefOperator，含适用性和证据不足 |
| 批Agent | ==一次解析E==→==按早期语义列路由规则==→逐案查证；成本未知 | 共享规则/索引，家族结构待测 |

ρ_E为规则索引/解析；ρ_P为三要件与证据归属；ρ_G可能为合理使用/注册时间/被动持有；ρ_R为个案证据。无轨迹比例、无K估计，不以20条引用集合的数量替代。来源裁决中的分支不能直接当作Agent自动发现的分支。

## 20样本线索清单

按SHA256(`strict-udrp-v1`+NUL+source_case)排序取20，未分层筛gold，19获救济/1驳回。数字抽取自private分析，包含Overview版本号3.0等噪声，不是已验证的条款映射，也不能给模型作路由。完整线索和复算脚本见[审计JSON](../artifact/evidence/shared-environment-strict-udrp/audit.json)。

| case | gold | 分析词数 |
|---|---|---:|
| D2024-2226 | RELIEF_GRANTED | 1081 |
| D2024-0001 | RELIEF_GRANTED | 1559 |
| D2024-0092 | RELIEF_GRANTED | 1435 |
| D2024-1422 | RELIEF_GRANTED | 1126 |
| D2024-2048 | RELIEF_GRANTED | 1224 |
| D2024-1482 | RELIEF_GRANTED | 1212 |
| D2024-1234 | RELIEF_GRANTED | 1399 |
| D2024-0418 | RELIEF_GRANTED | 979 |
| D2024-0487 | RELIEF_GRANTED | 791 |
| D2024-1630 | RELIEF_GRANTED | 1014 |
| D2024-1526 | RELIEF_GRANTED | 638 |
| D2024-0192 | RELIEF_GRANTED | 947 |
| D2024-0099 | RELIEF_GRANTED | 1252 |
| D2024-1067 | RELIEF_GRANTED | 1391 |
| D2024-1287 | DENIED | 2299 |
| D2024-2102 | RELIEF_GRANTED | 840 |
| D2024-0547 | RELIEF_GRANTED | 984 |
| D2024-1481 | RELIEF_GRANTED | 1646 |
| D2024-0693 | RELIEF_GRANTED | 1590 |
| D2024-1633 | RELIEF_GRANTED | 907 |

## 两个定点观察

D2024-1633：裁决讨论维修服务网站及Oki Data合理使用条件，引用Overview2.8.1；是否限定原告商品、是否准确披露关系会影响判断。这里说明语义分支存在，不证明固定检索不足。

D2024-1287：原分析说明为评估域名命名模式另行使用Google/Forebears搜索，并引用Overview4.8。public-v2案文2183词，未出现这两个工具名，且未附其查询收据。词名缺失本身不证明所有相关事实缺失；直接未封存的查询结果使证据世界闭合仍未确认。源gold为DENIED，不能凭近期广告链接直接推出注册时恶意。

十问：q/状态见一页表；E长且共享；x为回顾性裁决摘要切片；y为正式决定粗化；C未完成20闭合；D强固定臂不足未证；E家族有假设K未知；探索涉及规则/事实归属；G外部调查与事实选择未决；当前尚不能排除固定RAG/工作流缓存。旧限定Strong只说明任务结构，不适用本次目标。


## 增量：本案外部调查与规则授权分开

全1572分析宽泛词面扫描命中101案；其中47案含research/Internet search/Google/Archive/4.8等进一步线索。它们含程序语言、当事人调查和假设句，不能称101或47案实际自行调查。定点阅读确认下列20案有本案调查动作表述。抽样按可见动作选取，非随机样本、非全量外部调查比例。

| case | 已见实际调查 | gold粗类 |
|---|---|---|
| D2024-0031 | 独立搜索确认行业声誉，并查到招聘诈骗报告 | RELIEF_GRANTED |
| D2024-0199 | Internet Archive核实历史事实 | RELIEF_GRANTED |
| D2024-0237 | Google查询alpha finance发现第三方业务 | DENIED |
| D2024-0264 | Zetland搜索发现词典/地名/第三方商标使用 | DENIED |
| D2024-0303 | 公开搜索引擎确认个人活动报道 | RELIEF_GRANTED |
| D2024-0353 | 查询sunlife official/thailand确认业务存在 | RELIEF_GRANTED |
| D2024-0372 | Archive调查未确认声称的连续持有，另查缩写使用 | RELIEF_GRANTED |
| D2024-0376 | Internet搜索确认行业声誉 | RELIEF_GRANTED |
| D2024-0387 | 发现P.I.F.F.杂志及社交账户 | DENIED |
| D2024-0499 | allelou查询返回与原告无关结果 | DENIED |
| D2024-0666 | 异地且限时Google查询Waterland验证双方说法 | DENIED |
| D2024-0717 | 访问Web Archive对比2016网站 | RELIEF_GRANTED |
| D2024-0740 | Internet搜索核验2020年声誉 | RELIEF_GRANTED |
| D2024-0838 | 搜索商标并查看业务历史 | RELIEF_GRANTED |
| D2024-1287 | Google/Forebears核验词义、姓氏及命名模式 | DENIED |
| D2024-1678 | 从新西兰搜索macif比较地域可见性 | RELIEF_GRANTED |
| D2024-1900 | Companies House及注册号核实公司存在 | RELIEF_GRANTED |
| D2024-1934 | 搜索LinkedIn及姓氏核验注册人名称可能性 | DENIED |
| D2024-1994 | boost casino搜索检验关联及独特性 | RELIEF_GRANTED |
| D2024-2085 | 从Princeton查询Phoenix Insurance，原告未入前十 | DENIED |

[结构化审查](../artifact/evidence/shared-environment-strict-udrp/research-audit.json)。这些是评测侧裁决分析里的动作，不是被测Agent轨迹，不可提供给模型提示当前案件分支。不得按是否有此动作筛确认集，再宣称自然分布无偏。

可复用的是调查问题类型，如声誉核验、历史网页、第三方同名、身份注册；查询内容与时点属于个案证据。历史搜索不能用今天的实时结果替代。调查“发生过”也不意味着去掉它就一定改变标签，需与公开事实逐案对照或重新独立裁定。C的完整20条闭合仍未完成，D/E亦未通过，维持Partial。
