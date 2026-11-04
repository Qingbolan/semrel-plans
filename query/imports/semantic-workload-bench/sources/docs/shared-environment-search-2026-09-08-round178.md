# 增量178：UAV-HFACS航空事件候选的输入与gold缺口

新领域候选，暂不加入合格清单，仍9/15。完整作者仓库已下载；原论文身份已定位，但PDF请求403，未取得论文原件，不能说用户要求的下载闭环已完成。

## 来源与实际取得材料

- [原论文页面](https://www.mdpi.com/2504-446X/9/10/704)：UAV Accident Forensics via HFACS-LLM Reasoning: Low-Altitude Safety Insights，Drones2025，DOI10.3390/drones9100704。搜索返回的原站内容明确链接下述仓库；PDF下载403、随后HTML读取429，保留失败，没有绕过访问限制。
- [完整作者仓库](https://github.com/YukeyYan/UAV-Accident-Forensics-HFACS-LLM)：commit `e281194dfc2b10cb341db913dd52b0000a8d6232`，62 tracked文件。含200行CSV、YAML知识、附录、代码及来源纠正说明。
- [NASA ASRS编码分类表](https://asrs.arc.nasa.gov/docs/dbol/ASRS_CodingTaxonomy.pdf)：已下载16页。**ASRS taxonomy不是HFACS8.0手册**，不能把它充作该任务的完整共享E。
- 原件目录`data/shared-environment-audit-20260908-v178/`；全部下载文件哈希与源行统计在`artifact/evidence/shared-environment-audit-20260908-v178/{downloads.json,audit.json}`。

## 已核验缺口

CSV实有200行、200唯一acn、62列、18个Present标签列，即3600个标签单元。全部200行`model=gpt-4.1-mini`，`method=OPENAI + YAML + FewShot`。README称专家标注，但这些模型来源字段需要原始独立标注/人工复核收据来解释；本轮未发现逐标注者表与裁决记录。**不据此断言不存在专家复核，也不将这些标签直接作为独立人工gold。**

182行narrative长度恰为300字符，其余18行更短。示例879418在单词片段“another l”处结束；这支持存在截断风险，但尚未取得原ASRS完整记录逐字核对，也未找到裁剪实现。analysis_summary与逐标签Explanation包含判断及可能超出公开叙述的细节，不能填回模型输入弥补缺文，否则泄漏当前答案。

来源说明存在冲突：根README仍称ASRS，DATASET_CORRECTION_NOTICE要求改为多个航空安全数据库。不能把所有acn自动当成已验证的NASA来源键。论文原站搜索内容称由ASRS筛选586篇；其与公开200篇的抽取和标注关系待原论文及来源锁验证。仓库代码MIT/数据说明CC BY4.0不自动覆盖未核对的原事件材料。

## 三表（候选诊断，不计合格湖）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 按HFACS批量标注无人机事件的人因类别 | 200条事件CSV，182条叙述长度300字符 | HFACS-UAV YAML和附录；完整8.0规范未取得/绑定 | 原始报告来源键与完整记录未核验 | 18类3600单元；模型字段与专家声明的关系未核清 |
| 879418是否涉及违规/监督因素 | 公布叙述：UAV飞行测试完成后积累时数，末尾截断；synopsis提到非合格人员占座 | 分类定义与证据充分性规则需完整提供 | analysis_summary只在private诊断，不作输入 | CSV有标签与解释，但本轮不将其升格为可用于确认的答案 |
| 汇总涉及各类因素的事件清单 | 预测18维标签表 | 固定阈值/Boolean计数 | 事件ID | 可由可靠gold派生，当前gold与输入未闭环 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(full_reports).sem_map(hfacs_codes,E).project(event_id,codes)` | 目标200事件×18类 | 公开CSV可能截断，完整输入尚未取得 |
| `codes.explode().groupby(code).collect(event_id)` | 3600待判断单元，不是3600独立事件 | 不用模型已有Explanation当独立监督 |
| `audit_source_and_annotation_provenance()` | 200/200同模型字段，182/200长度300 | 属构造核验，未执行模型性能实验 |

以下为未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 完整报告和规范下输出有证据的18维结果；当前不能预言具体正确值 | 固定规则检索与sem_map，同资源供给完整原文 | 同一目标，无优势预设 | ==查类别边界和报告证据，区分事实缺失与类别阴性==→结构化输出 | `ReportEvidence → TaxonomyRetriever → MultilabelCoder → EvidenceCheck` |
| 不应从截断文本推断确定不存在某因素 | 若冻结任务有UNKNOWN则按契约返回；不能默认为0 | 同样证据边界 | ==检查所需事实是否在允许材料中==→输出/升级 | 证据充分性检查须有明确定义，不能为Agent独占资源 |
| E-only编译或固定YAML规则是必要对照 | 从同一E构造程序并计共享成本 | 单轨迹提取额外价值待实测 | ==记录一次真实执行的公开动作与证据==→提取冻结 | 不能把现成手写YAML称为轨迹学得operator |

下一步如继续该源，先补原论文下载、原报告与独立标注证据；当前不适合马上构造比较实验。没有运行仓库代码、安装依赖、调用模型或访问任何论文内部系统。无训练/prompt实验/种子/token预算/推理并发缓存/正式快照/commit，0测试套件测试。clone及NASA PDF下载均完成；原论文失败已终止，不存在等待中的进程。
