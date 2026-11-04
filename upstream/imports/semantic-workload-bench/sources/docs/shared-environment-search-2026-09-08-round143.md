# 第143轮：MAUD原论文、两个完整仓库及原生标签核验

仍8/15，MAUD为待定来源，不计合格。上一轮142产生原始数据审计证据，属于进展。本轮发现MAUD具备真实并购协议、多种批量审查问题与人工标签，但关键共享标注手册尚未取得。

实际下载[EMNLP原论文](https://aclanthology.org/2023.emnlp-main.1019/)293751bytes，SHA256 `aa83b7630aee3ca0ab69b498985e1a35998bee3aa87f57d5d418446c77959955`；[完整主仓库](https://github.com/TheAtticusProject/maud)commit `4640316078dcd370debb877f350c39a28b181ffe`，ZIP33141392bytes、40members、CRC通过，SHA256 `afd7bbe556aa411bc8f787dd74d62db7b0a02f259d2dd3978a7e07e2e393daf5`；内附data.zip161members也CRC通过并完整解压，含152合同。

另下载[完整抽取仓库](https://github.com/The-Atticus-Project/maud-extraction)commit `89cc5f6ce210268f170aa019ea204ed4e608c604`，ZIP26054537bytes、13members、CRC通过，SHA256 `42482fde076947bed76f3540f4ceb19852a36c7a0424720983c2d2f8e0e565ce`。它是同一湖的抽取视图，不是第二个湖。README明确旧论文抽取baseline存在训练bug；本轮未运行或复述其性能作为可比结果。

来源路径：data/shared-environment-audit-20260908-v143/；URL、commit、下载收据和审计结果在artifact/evidence/shared-environment-audit-20260908-v143/。

主仓库发布实际39231行：train25827/dev6753/test6651；main20623、abridged14928、rare_answers3680。rare_answers由专家最小改写原文以获得稀有答案，不能算真实合同新增案例；abridged不算新增独立合同。main有152合同、144个question+subquestion组合（不是论文92原始问题），每个contract/question/subquestion仅一行；91个组合覆盖全部152合同，其余覆盖10–151合同。train/dev/test的main均涉及152合同，两两实体交集均152；这个split不能证明跨合同泛化，不默默重划分。

抽取视图实际train120docs/2640QA/6311spans，dev16/352/885，test16/352/767，合计152docs/3344QA/7963spans；逐span上下文切片精确相等，0越界/表面不符（以切片校验）。未做与main全文版本/合同ID映射、同源CUAD重叠、近重复或专家手册例子泄漏审计。这些只证明源字段可读与offset一致，非独立确认。

原论文A.12说明标注人员接受70–100小时培训并阅读手册，团队共识与律师复核；不能把培训小时数等同已公开共享E。早期论文搜索命中248页手册并称准备公开，但本轮没有取得那份完整手册。主repo的Google Drive索引已实际下载，显示contracts、README、datasheet及三个CSV，未见手册；HF只核对文件清单，未另下载重复数据。官网“Labeling Handbook”明确是CUAD商业合同手册，其完整内容需购买；这不是MAUD手册，不替代、不购买、不联系作者。

[作者MAUD页面](https://www.atticusprojectai.org/maud/)支持真实来源和人工标签，[官网手册页面](https://www.atticusprojectai.org/labeling-handbook/)支持其CUAD范围。不能仅凭“248页曾存在”声称已得到长E。代码/数据许可需分开，官网MAUD数据标CC-BY4.0，未推断手册和代码自动同许可。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| Q1 批量提取并购对价类型，筛出全现金收购 | 152合同全文，包含修订文本 | 应有MAUD共享标注手册：未取得 | main中人工选定条款文本只可明确作为given-span对照；全文任务不偷渡gold选段 | contract41 Type of Consideration=All Cash；原段每股70美元，修订改75美元 |
| Q2 找出每份合同的关键交易条款，供Q1等审查复用 | 同批全文，抽取视图152文档 | 22 deal point types；详细共享标注标准缺失 | 抽取问题为固定22类别族 | 3344QA、7963span，源offset表面校验全通过；不等于完整规则已公开 |
| Q3 分类MAE、终止权等其他deal points并汇总 | 同一main来源 | 144个question+subquestion组合，不能当144新湖 | 需独立标签映射/规范/实体划分 | 原始main20623标签可核验，但本轮未逐类冻结可执行契约 |

| 类python的DAG | 具体数值 / 中间输出 | 下游及限制 |
| --- | --- | --- |
| `contracts.sem_map(extract_deal_points,E).explode(spans)` | 152→3344QA目标→7963goldspan | 22类别抽取，需全文与分类来源映射审计 |
| `deal_points.sem_map(classify_consideration,E).filter(answer=='All Cash')` | contract41→All Cash；条款含70→75修订 | 全文流程与给定gold段流程必须分开；每股75不是本轮独立金额gold |
| `.project(contract_id).count()` | 对价类型组合最多152合同 | 未计算完整筛选数或运行模型，不填虚构清单指标 |

以下是预期方法设计，未运行LOTUS/Data Agent，不预测优势。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| contract41目标All Cash，实际输出未测 | 固定检索对价及修订条款→sem_map按类别判断→投影；可用相同缓存和工具 | 同目标，不能预言更准 | ==检索对价条款和修订关系==→核对现金/股票形式；70→75不改变All Cash→输出依据 | `ConsiderationClassifier(contract,definitions)->type,evidence`；若只有这个简单问题，长手册必要性弱 |
| 22类别抽取目标为原span，实际输出未测 | 固定分类目录+全文分块/检索→sem_map→span合并/校验 | 同目标；复杂性本身不是优势证据 | ==读取类别边界与交叉引用规则==；详细规范当前缺失，不能从private span猜规则 | `DealPointExtractor(text,E)->typed_spans`；规则未齐，不称已提取operator |

固定程序、Coding Agent、仅E编译及整批Agent均须同资源对照。需进一步取得MAUD完整规范，证明具体跨条款任务的E依赖，完成main/extraction来源映射与实体隔离，才可计入构造合格。当前不建公开快照、不修标签、不运行baseline/模型/正式scorer、不commit。不是因下载失败全面受阻；下一增量可继续手册公开路径或新的独立来源。
