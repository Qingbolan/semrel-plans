# 第四十五增量：AcmGENTIC代码取得，真实评测数据发布地址404

**累计仍1/10。** 本轮检索变异功能证据任务，下载[原论文2604.00075v1](https://arxiv.org/pdf/2604.00075v1)，9页、1,491,748 bytes，以及[完整AcmGENTIC作者代码](https://github.com/AliSaadatV/AcmGENTIC)，commit `f6175e065e13570a8a139ad55e2a3478b51b5475`；21blob Git SHA1全部通过、ZIP CRC通过。

论文明确分开两个地址：benchmark数据是`AliSaadatV/LLM_func_exp_bench`，流水线代码是AcmGENTIC。前者web和GitHub API均404，未取得；后者完整下载，不能用它冒充已获得benchmark。首版下载脚本在404后解析None报TypeError，修正缺失响应检查后继续独立可获取代码仓库；保留两次失败收据，没有覆盖为成功。

## 实际数据边界

论文报告11,527个ClinGen变异，1,709带PS3/BS3；529个可下载PDF的variant-paper对，标准化后466对，另有1,058摘要（529正/529负）。**这些是论文计数，不是本次原数据实读。** 数据从curator汇总中由gpt-4.1-mini提取PMID和证据强度，需进一步核原始专家标注与逐论文分配。摘要负例由无PS3/BS3标注的变异所引用论文抽样，不能默认“无功能代码”等价于“摘要确无功能实验”。

完整代码仓库仅附两个变异的HTML/PDF模型报告（共4文件），没有466对的独立gold。示例报告名`2_162277580_C_A_GRCh38`、`4_186083346_C_T_GRCh38`是管线输出，不作为专家gold或独立后续批次。未执行作者代码，也未读取.env或调用外部模型。

论文明确所有benchmark结果用Direct模式，Agentic模式为扩展功能。因此其公布的模型性能不构成Agentic模式相对固定流程的实测优势。原论文还将variant-matching失败或不明确输出作为覆盖问题；只在成功匹配子集上算方向准确率不能替代全部466例端到端质量。

长共享规则尚未取得/版本绑定。不能把代码里PS3/BS3简述或短strength规则直接说成30页专家规范。该来源同样锚定ClinGen，若后续可用还需与CGBench按变异/论文/专家原记录去重，不能自动作为独立新湖。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在冻结功能证据规范下，对变异—论文对输出PS3/BS3方向与强度，再汇总供复核 | 长规范未下载、VCEP特化版本未绑定；代码有短规则 | 论文报告466对；实际数据仓库404，未下载 | 标准化变异ID、全文图表是必要输入，当前未取得该批数据 | 论文称ClinGen来源后由LLM结构化；逐对独立标签未取得 |
| 已发布演示`2_162277580_C_A_GRCh38` | 不能由演示输出反推合规规则 | 坐标只是报告标识，不能代替完整variant-paper输入 | HTML/PDF输出报告已随完整repo下载 | 不存在已验证专家gold；不能拿模型报告自评 |

| 类python的DAG | 具体数值 | 核验状态 |
|---|---|---|
| `scan(variant_paper_pairs).normalize_variant()` | 529→466（论文报告） | 63标准化排除的具体记录未取得 |
| `sem_map(match_variant,pdf,identifiers).sem_map(extract_assays)` | 466对；方向/强度/摘要 | 不是本次执行，中间matching缺全量独立gold |
| `sem_map(PS3_BS3,E,assays).sem_filter(meets_target).aggregate()` | 可靠选中数未知 | 应全批报告ABSTAIN/coverage，不能只给模型成功匹配子集指标 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标为方向/强度/证据JSON；具体样本正确值未取得，不能虚构 | 同等输入固定ID归一、全文/图表提取、实验与机制核对、规则判断；可以缓存同论文/规则 | 同schema；未运行，也没有论文Agentic比较可借用 | ==核对转录本与变异同一性==→==定位功能实验及对照==→==读取疾病机制及试验校准规则==→证据充分则输出，不足则ABSTAIN | `FunctionalEvidenceOperator(E_version, variant_aliases, assay_extractor, mechanism_match, calibration, direction_strength, abstain)`；必须对照E-only编译与固定工具流程 |

原资产data/shared-environment-audit-20260908-v45，下载/哈希/源码核验artifact/evidence同名目录。下载session28371失败后终止；修正运行34602正常完成，无活跃下载。新工程测试0、作者代码运行0、模型调用0；无新确认划分。此来源暂不计入，不能把有Agent代码等同于有合格数据湖。
