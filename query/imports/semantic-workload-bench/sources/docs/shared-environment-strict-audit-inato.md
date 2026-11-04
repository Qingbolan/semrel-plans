# Inato多模态试验筛查：公开实验材料Reject

原论文[Callies等，Communications Medicine 2025](https://www.nature.com/articles/s43856-025-01256-0)，9页1366795bytes，已下载并读方法、真实队列、数据/代码可用性；[完整作者仓库](https://github.com/inato/ai_trial_eligibility_assessment)commit `95c9a72d2ab7e0b0e5416811bab4ec21a4bc213a`、335文件已下载。原件哈希见[来源收据](../artifact/evidence/shared-environment-strict-inato/source-progress.json)。本轮没有运行作者代码；用AST字面解析条件字典、CSV读取输出。

## 表1 入场审计

| 项 | 直接证据/结论 |
|---|---|
| A固定q | 按固定条件判断患者是否满足，可固定；原n2c2是13条件而非同一完整试验 |
| B共享E | 公开raw13条件176空白词，refined13条件407词；真实36试验标准被论文明确列为NDA不可分享。长患者病历属于x，不是共享E |
| C20 | 输出表覆盖20患者，但原患者输入未取得；0/20完整支持，不把模型rationale当原病历 |
| D | 仓库本身为固定topK检索+条件评估；论文全环境下强固定不足未建立 |
| E | 日期/数值/病史等语义步骤可能不同；13条件不是执行K；无已核实家族复用 |
| F | 论文真实485患者36trial650criteria7021标签不是本地数据；本地聚合输出3380行仅20患者260唯一配对，重复配置不扩N |
| G | is_met为参考、is_met_predicted/rationale为模型输出，不能输入反推；真实标签含人工条件审核与患者级结论启发式推导，不能全称独立条件标注 |
| H | 原论文及全repo已取得；数据目录只有假sample.xml，README明确fake，开头Lorem ipsum；未见根LICENSE，权利范围未确认；原真实E/病历未获得 |
| Verdict | Reject当前公开材料；它更接近短条件上的固定检索判断，非已证实HSCodeComp式语义执行家族 |

论文Data availability称n2c2门户截至2025-10-08暂停新申请，这是论文日期限定陈述，不推断当前门户状态。不能因此说n2c2永不开放；即使获得该数据，13条短条件仍不自动满足复杂共享E。

## 表2 Query × 数据湖

| Query | 数据湖1：条件字典 | 数据湖2：患者资料 | 数据湖3：结果CSV |
|---|---|---|---|
| 每患者判断HBA1C条件 | raw定义为任一HbA1c在6.5–9.5% | 真实病历未提供；fake sample不算真实病例 | patient365/HBA1C，is_met=True；预测亦True，但后者不是独立gold |
| 每患者判断MI_6MOS | raw定义MI in past6months | 时间锚及真实原文未提供 | 结果存在不代表可重做事实日期核验 |
| 真实trial整体资格 | 36trial标准未发布 | 485患者为论文报告 | 7021条件标签不能当485个完整协议独立裁决 |

输出建议保留MET/NOT_MET/UNKNOWN与执行ABSTAIN，但原二元n2c2标签不含独立UNKNOWN，不能自行补标后称同一任务。

## 表3 类Python DAG

| 类PythonDAG | 普通/语义与数据边界 |
|---|---|
| `criteria=load(raw_or_refined)` | 普通，13短条件；版本必须冻结 |
| `pages=render(patient_text); index=embed(pages)` | 普通预处理/模型嵌入，患者局部而非共享环境；源输入缺失 |
| `images=retrieve(index,criterion,guidelines,top_k)` | 固定检索，可共享条件查询 |
| `result=sem_map(criterion,images)` | 核心语义判断决定参考比较 |
| `score(result,private_is_met)` | 普通评分；不可用rationale补源证据 |

## 表4 四路方法推演，均未执行

| 方法 | 预期结果边界 | 预期过程 | operator |
|---|---|---|---|
| LOTUS任务only | HBA1C患者365源标签True，原病历缺失，不能预测实际输出 | 固定字段判断需完整病例 | 尚不可执行 |
| LOTUS完整E | 13条件可整段或固定索引；不证明需要Agent | 条件+同病历→固定检索→判断 | `retrieve→value_time_extract→compare` |
| 逐患者Agent | 同输入缺口，无可承诺优势 | ==读条件/检索指南==→==找HbA1c及日期==→判断/UNKNOWN | 与固定流程可相同 |
| 批Agent | 可共享条件拆分及查询，不证明家族收益 | ==一次预处理条件==→批患者检索与判定 | 条件索引+固定语义列 |

ρ_E条件解析/检索指南；ρ_P固定取页/评估；ρ_G数字阈值、相对时间、病史等假说但未观测；ρ_R个例事实。比例/K未知。条件不同或topK参数不同不是K；模型rationale不等于可观察工具执行家族。

真实输出样例365/HBA1C：模型rationale声称某日期病历中患者自报HbA1c低于7%；不能从该生成文本验证6.5下界或原始记录真实性。本卡不判该源gold错误，只说明证据不能由预测自证。20患者原件缺失，因此不编造20逐条C表。

[输出字段/计数](../artifact/evidence/shared-environment-strict-inato/output-schema-audit.json)：37CSV；聚合all_results3380行、20患者、13条件、260唯一配对；269PNG分布于results_aggregated252与results_by_configuration17，未当病历图像。无新模型结果、无public/private快照、无新确认split。
