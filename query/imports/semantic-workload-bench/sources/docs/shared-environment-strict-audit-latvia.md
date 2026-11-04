# 拉脱维亚采购验证：严格入场Reject

原始8页论文与CLARIN-LV完整dev/test发布包已经下载，本轮重新计算SHA256并实际打开清单、20份test答案以及论文方法部分。[原论文](https://www.scitepress.org/Papers/2026/142494/142494.pdf)、[官方数据仓库](https://repository.clarin.lv/repository/xmlui/handle/20.500.12574/135)、[原下载与全量统计](shared-environment-search-2026-09-08-round144.md)、[本轮可复算审查](../artifact/evidence/shared-environment-strict-latvia/audit.json)。未找到作者独立代码库；不把第三方RAG框架称作者仓库。许可CC-BY-NC-SA4.0。

| 入场条件 | 核验结论 |
|---|---|
| A | 固定第4项检查可以重复；150题不能自动当一个统一Boolean任务 |
| B | 共享questions.yaml及法规引用；项目采购文件属于x，不属于共享E |
| C | 本轮20答案到第4项规则键定位，完整事实+历史法规闭合0/20；不称20/20通过 |
| D | 论文明确question0前置判定和固定跳过流程；未证明同资源强固定程序不足 |
| E | 单一检查的适用/理由分支已写进清单，未测中间执行家族K；跨不同题不能作K |
| F | 30真实项目，dev10/test20；不满足数百；4500主答案不是4500独立项目 |
| G | 部分check需KPVISIP/IUB等外部记录，未随包；?表示另一版无该题，不是事实未知 |
| H | 原论文198854bytes、devZIP1929183/testZIP8753304bytes均已取得；完整历史法规未取得 |

结论 **Reject当前严格目标**。有真实专家判断，但规模及证据闭合不满足。它有语义理由判断，仍可能被“固定适用性判断→固定检索→理由分类”覆盖，未证明HSCodeComp式中间家族结构。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | gold |
|---|---|---|---|---|
| 第4项：单标段是否有客观不拆分理由 | questions.yaml nr4，MK107 §196引用 | 30项目DOCX/PDF采购文件 | 完整历史法规未取得 | 测试20：9Yes、2No、9不适用 |
| 第1项：与批准采购计划是否一致 | nr1，check=KPVISIP | 同项目文件 | 批准计划未随包 | 有专家答案但当前输入不闭合 |

| 类Python DAG | 类型/依据 |
|---|---|
| `R=scan(project_files)` | 普通；N30，test20 |
| `a=sem_map(single_lot, R)` | 语义；决定适用性 |
| `y=NA if not a else sem_map(objective_justification,R,E)` | 固定分支+语义判断；不能把缺证据当No |
| `project(filter(y==No),project_id); count()` | 普通；test源No2，预测未知 |

| 臂 | 预期结果/过程 | operator结构 |
|---|---|---|
| LOTUS任务only | 无完整适用标准无法可靠复作；未测 | 通用理由分类 |
| LOTUS完整E | 可能充分，未测；固定前置判断、同工具检索与理由判定 | Applicability→Justification→Decision |
| 逐记录Agent | ==确认前置及历史条款==→==定位标段和理由==→判定；无实测 | 相同固定分支也能表达 |
| 批Agent | ==一次解析清单==→逐项目取证；收益未知 | 共享规则+逐条证据抽取 |

ρ_E：清单解释；ρ_P：同一前置与理由检查；ρ_G：单/多标段路径已在清单，未证明额外语义家族；ρ_R：个案理由理解。比例及K未知。缺法规/计划不会因Agent探索而自动获得。

## 20份真实答案的规则键定位

全test20份，不按标签选取；已开发暴露。每条均对应同一`questions/questions.yaml` nr4→MK107 chapter196，但未逐份审读采购全文，不能当条件C的完整核验。

| 项目 | 前置answer0 | 主answer |
|---|---|---|
| APP_DI_20202ERAF_AK | nē | nē |
| DND_20206 | jā | jā |
| EDI_20203AK | jā | jā |
| IKVD_20213_ESF_SAM | nē | n/a |
| IP2020_01_ERAF | nē | n/a |
| IeM_IC_201913 | nē | n/a |
| KNP-2022_15 | jā | jā |
| KP-2020_016A-KF | jā | jā |
| LNP-2019_76 | nē | n/a |
| LNP-2020_37ERAF | jā | jā |
| LU-2020_49_ERAF | nē | n/a |
| MNP 202121_ERAF | jā | jā |
| PND_2019_15-ERAF | jā | jā |
| RTK 2019_12 | nē | n/a |
| SND 202015-ERAF | nē | n/a |
| SNP_202001 | jā | jā |
| SNP_202067 | jā | jā |
| VND_20201 | nē | n/a |
| VNP_2023057AK | nē | n/a |
| VeA_202012ERAF | jā | nē |

全30份答案扩查发现5处局部组合为answer0=No而answer=No，集中在4、37.4、40.9项；对应位置见JSON。这与论文介绍的前置No→n/a流程存在需解释差异。未查明是版本转换、字段含义或标注问题，不修改gold，也不声称5个专家错误。

具体例APP_DI_20202ERAF_AK，第4题前置No、主No。按论文流程生成的程序将给n/a，与发布答案不一致。这是**契约/标签一致性问题，不是静态模型语义失败**，也不能用Agent迎合该行gold特例。

十问：q与输出为第4项Yes/No/NA，不足UNKNOWN、执行ABSTAIN；E为共享清单/应有历史法规；x30项目；y为CFCA专家；C仅20规则键定位；D固定流程替代未排除；E/K未测；探索为适用规则与项目事实；G有外部输入/版本缺口；没有排除条件分类或工作流缓存。原文、数据、样例均存在，但不满足严格入场；不增加Strong数。
