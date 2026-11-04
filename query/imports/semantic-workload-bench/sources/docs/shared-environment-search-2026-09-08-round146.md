# 第146轮：GIST企业排放披露，真实报告与修订gold核验

状态：新增独立候选，未qualified，仍8/15。上一轮完整仓库与规则输入诊断有实质证据进展。本轮下载原论文、完整作者仓库，并取得一份真实报告核验数值；共享指南暂未下载成功，不将报告长度当共享E长度。

## 来源与下载

- [原论文](https://www.nature.com/articles/s41597-025-05664-8)：Scientific Data 2025，9页PDF2774839bytes，SHA256 `be5298221feb99086b7402fc2ecdc0f12e066021608f0990ce9b92f1a9275834`。
- [完整作者仓库](https://github.com/soda-lmu/gist-data-descriptor)：commit `003f412f43af5ea2495d462b9460f1b50a95bc8c`，ZIP8964804bytes、480members、CRC通过，SHA256 `bba7aea04363bae4e57ea5d2ebe5ba607cf78700298df5f0807f4db997be6a17`。含422个XLSX、20个CSV及R分析代码；XLSX数量不是独立报告数。
- [Zenodo v4发布页](https://zenodo.org/records/15124118)列两个指南、两个codebook和datasets.zip。本次API及5个文件均HTTP504，未取得发布zip/指南，不冒称与仓库CSV同版。下一轮可重试实际文件；不需要用户授权，也不是全局阻塞。
- 仓库给定CubeSmart旧URL返回403；[另一公开报告URL](https://s205.q4cdn.com/638877794/files/doc_financials/2021/ar/2021-CubeSmart-Sustainability-Report-Final.pdf)下载17103744bytes。第19个PDF页（印刷P18）已渲染视觉核验。两URL字节相同性未知；替代来源明确留档，未更改源数据。
- 原件在`data/shared-environment-audit-20260908-v146/`；可重跑audit.py及audit.json、sample.json在`artifact/evidence/shared-environment-audit-20260908-v146/`。下载错误见原件目录download-results.json。论文CC-BY4.0；数据及企业报告的具体再分发许可仍待核验，不把论文许可外推。

## 实际数据与版本问题

四份仓库gold文件逐行读取，company_name/report_year/merge_id复合键均无重复。gold_standard.csv为5644行、139报告、132公司、643非空数值；gold_standard_revised.csv为5631行、645非空值；带ISIN未最终修订版亦5631行645值；gold_standard_with_ISINs_edited_revised.csv为5631行、139报告、130规范化公司名、644非空值、531非空页面文本。每版139个URL。公司名归一化计数不是企业实体审计。

论文报告5646行，与上述实际文件均不同；没有默默修复。最终修订版4987行value为NA，不等于4987个独立真实负例。每报告约40个scope-year槽位，不能把5631行当5631份报告。页面文本是gold定位的页面，不能直接作为默认检索输入或把这些531行当无需全文的无泄漏批次。

作者manual_correction_gold_standard.R记录删除NA重复项、CubeSmart误复制数值和Lundin scope修订。代码阅读未执行R流水线。原报告P18列顺序为2021/2020/2019，Scope2数值23918/25276/27984；与最终修订gold相符。gold附带文本开头却为2020 2021，后面才出现2019，证明文本线性化确实损伤列对齐。只核验这份报告，不外推139份正确。

## 用户要求的三张表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按统一排放口径提取每公司每年各scope总排放 | 139个真实报告URL；本轮取得CubeSmart全文 | 共享标注指南：已定位，下载504；论文说明公司整体、绝对值、scope及总量条件 | PDF表格布局/单位；需全报告检索，不能gold选页 | 最终修订CSV5631行644非空值；CubeSmart2021/2020/2019的2lb分别23918/25276/27984 MTCO2e |
| 判断待核查抽取是否符合统一口径并修正 | 原LLM提取及报告 | 同一指南与错误类型codebook，尚未取得 | 人工阶段原XLSX/中间CSV已下载，但未逐行闭合 | 不能直接将中间非专家判断视为最终错误原因gold；此第二任务待核验 |
| 从合格排放序列计算变化量 | 上一任务输出 | 明确同公司/同scope/同单位/两年都存在 | 不跨公司/不混market与location | 2021相对2020：23918−25276=−1358 MTCO2e；由两个人工值确定性派生，不是额外专家趋势标签 |

| 类python的DAG | 具体数值 | 中间及下游边界 |
| --- | --- | --- |
| `reports.sem_map(extract_scope_year_values,E).explode().normalize_units()` | 全库139报告；最终修订644非空值 | 必须携带年份/口径/单位/证据；NA不自动转0 |
| `values.filter(scope=='2lb').join(previous_year).map(delta)` | CubeSmart2021=23918、2020=25276，delta=-1358 | 不把Scope1+2总额30354误取为Scope2；不把2020和2021列对调 |
| `candidates.sem_map(review,E).filter(valid).project(corrected_value)` | 已有人工多阶段记录但本轮未核验全量join和优先级 | 不能现在报告审核准确率或七种最终错误原因gold数量 |

以下模型行为均为待测设计，只有CSV统计和PDF核对实际执行。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 目标2021/2lb=23918，实际模型输出未测 | 全报告固定检索→读取原PDF表格/布局→按E抽取→验证单位年份；若只给破损线性文本存在错列风险，不能据此断言LOTUS失败 | 同一目标23918，无优势结论 | ==读取共享口径，确认未显式指定的Scope2怎样归类==→==发现文本年份排列与原表不一致，调用页面查看工具==→按列抽取23918 | `ScopeYearExtractor(E_version,report)->list[year,scope,value,unit,evidence,status]`；规则归类、布局恢复、绝对/强度区分、未知/失败分离 |
| 目标变化量-1358 | 与Agent同资源完成上游语义步骤；后续join/减法确定性执行 | 同一目标-1358 | ==核对组织边界和两年单位一致==→调用相同join/减法工具 | 提取算子后接固定`ComparableSeriesJoin`和`delta`；算术不是另一个学习语义任务 |

固定流程必须拥有同样的页面查看、表格解析、检索、缓存及预算。E-only编译、Coding Agent、整批Agent均应纳入；不能强制LOTUS消费损坏文本、只让Agent看PDF制造质量差距。

## 当前结论与下一步

真实报告/人工修订gold/有用抽取DAG已获得具体证据，但本轮没有完整共享指南、全报告可访问性和版本闭合，不能计入第9个。优先补齐Zenodo两指南和发布gold，测量实际规范长度、解析口径规则，并检查发布版与仓库修订版关系。若规范只是少量条件，应保留为长文档抽取候选，不能靠额外挂载整本GHGP把E人为变长。无模型调用、无实验划分、无默认公开快照、无正式评分或训练；本轮gold查看属于开发暴露。
