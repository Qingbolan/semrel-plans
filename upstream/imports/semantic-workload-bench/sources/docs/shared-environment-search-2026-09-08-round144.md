# 第144轮：拉脱维亚公共采购合规数据全发布包核验

仍8/15。本轮为新真实监管来源，尚不计入合格湖：批量规模、外部证据和完整法规版本未闭合。上一轮143有原件与标签统计，属于进展。

下载[作者原始研究论文 Retrieval-Augmented Generation for Procurement Validation](https://www.scitepress.org/Papers/2026/142494/142494.pdf)，ICAART2026，8页198854bytes，SHA256 `a304ef9a3db08aa2cba99a985bbb60304071cfefea1e3602084233cf5b95e10c`。它是使用该数据并报告RAG验证的作者论文；不混称另一篇标题为Dataset and Baseline Implementation的论文也已下载。后者本轮仅搜索定位。

[CLARIN-LV作者数据仓库](https://repository.clarin.lv/repository/xmlui/handle/20.500.12574/135)的两个README和全部dev/test ZIP均已下载，官方4个MD5逐项相同；dev1929183bytes/48members、test8753304bytes/94members、CRC全部通过并解压。没有找到本项目独立源码仓库，不能将论文引用的LangChain/LlamaIndex仓库算作作者代码已取得。CC-BY-NC-SA4.0，仓库发布日期2025-08-27。原始字节在data/shared-environment-audit-20260908-v144/，下载URL/sha256/md5在artifact/evidence/shared-environment-audit-20260908-v144/。

来源确实是CFCA专家评估的30真实采购项目，原始采购文件及合同草案，而非模型生成病例。dev10项目11文档，test20项目27文档；共30DOCX+8PDF。30INI配置到源文件/答案文件的绑定全部存在，30DOCX的word/document.xml全部XML解析成功；未把8PDF已下载说成逐页语义已核验。

两split questions.yaml SHA256相同：`a9fe751eda243449382966b890344508c5f261d7b14ab04e6fbccefde2e3a5d6`。BaseLoader保留问题编号及Latvian字符串，避免小数编号解析为浮点、或yes/no转换影响。改写清单实际157个节点，150个带question、55个带question0，29个带check外部核查标记，64个引用PIL/MK107/MK13法规；文本含键/标签合计6863正则词，不全是政策内容。官方描述168questions与该文件157nodes不一致，不能默默沿用168乘30作为实查数量。

30份答案均157节点、无重复nr。主answer合计4500字段：jā2597、nē114、n/a1716、?73；前置answer0合计1650字段：jā546、nē1061、n/a10、?33。主问题和前置条件是同一项目相关判断，不是6150独立case。?是该项目采用的另一版检查清单没有这一题，属于缺标/版本差异；n/a是语义不适用，不是FALSE或执行ABSTAIN。论文另用X表示上游缺上下文导致后续无法回答，不能混入上述gold类型。

共享检查清单版本S.7.1.-PL-21（09.12.2019）有明确来源，但完整历史法规、外部平台记录未包含在下载包。check可指采购计划、IUB、EIS等，README明确这些题不能仅凭采购文本/合同回答。不能用当前平台状态或随意新法规回填历史gold，更不能只给不完整输入然后宣称LOTUS能力不足。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| Q1 批量检查不分标段是否有合理说明 | dev10/test20真实项目文件、部分附合同草案 | 统一questions.yaml；第4题先问是否只有一个标段，再检查未拆分理由 | MK107第196条引用；完整适用历史法规尚未下载 | KND-2020_20第4题answer0=nē，answer=n/a，即前置不成立、后续不适用 |
| Q2 核对采购数据与批准计划是否一致 | 同一项目文件 | 第1题要求变化不影响程序选择/合同价格 | check=KPVISIP；批准采购计划未随包提供 | KND-2020_20第1题jā，输入充分性未证明，不能直接要求模型复作 |
| Q3 检查特定采购程序是否有合法适用理由 | 同一项目文件 | 第2题程序适用前置条件 | PIL第8条第6、7款引用，完整法规待取得 | KND-2020_20第2题answer0=nē、answer=n/a |

| 类python的DAG | 具体数值 / 中间状态 | 下游gold边界 |
| --- | --- | --- |
| `projects.sem_map(check_applicability, checklist).sem_map(check_rule,E)` | 30项目；第4题示例前置No→n/a | 前置No应按固定分支跳过后续，不需Agent动态发明流程 |
| `.filter(answer=='nē').project(project,check_id)` | 全主answer114个nē（跨题汇总，不是114独立项目） | 需保留n/a、?和ABSTAIN，不能压成统一否定 |
| `projects.join(approved_plans).sem_map(compare_plan,E)` | 30项目配置完整，但外部计划未提供 | 必要输入缺失，当前不运行或评分此DAG |

以下均未运行模型；样例输出是作者gold语义，不保证模型准确率。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| KND第4题目标前置No、结果n/a；未测 | 固定sem_map判定标段→条件分支→需要时查法规/说明；相同工具与缓存 | 相同目标；未测且不预言更好 | ==读取第4题适用条件与MK107引用==→检索项目标段→前置否则输出n/a | `ConditionalProcurementCheck(check_id,project,E)`；条件DAG已在公开清单中，不能当轨迹新发现 |
| 第1题goldYes，但现有输入缺批准计划 | 固定检索发现缺必要记录→ABSTAIN，不当No | 同样不能从未提供计划作决定 | ==确认check=KPVISIP所需计划及历史版本==→记录资源缺失 | `PlanConsistencyCheck(project,approved_plan)`依赖缺失，不生成假算子补答案 |

资源齐备后比较固定RAG/Coding Agent/E-only编译/整批Agent与单次轨迹冻结，同一工具和预算；不能以缺法规或缺计划造成基线失败。这里的30项目有真实监管意义，但在每个固定检查下N=30且独立测试20，数量和适用规则版本不足以满足当前大批量标准。本轮不因30×150得到4500就宣称满足目标。

下一证据需求：固定可由公开材料回答的任务范围；取得准确法规版本、引用段以及必要外部记录；解释168与157差异和?版本关系；核验答案与具体源段；确认是否有更多同条件独立项目。没有扩大宣布合格，没有新快照/模型/评分/commit。
