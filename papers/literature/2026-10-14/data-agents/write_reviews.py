from pathlib import Path
import json
root=Path(__file__).parent
reviews={
'2402.17453':('DS-Agent- Automated Data Science by Empowering Large Language Models with Case-Based Reasoning-ICML-2024','ICML',2024,'2402.17453v2',[
'''DS-Agent 面向“给定训练数据和评价目标，自动构建可运行且有效的预测模型”。核心是两阶段案例推理：开发阶段利用 Kaggle 经验迭代；部署阶段迁移成功代码。阅读范围为正文 §1–6、算法与任务形式定义、实验表及附录任务说明。这里的图是 agent 规划/代码执行流程，不能自动当作关系语义算子 DAG。''',
'''出发点是模型生成的实验计划往往缺乏领域经验，运行反馈又很贵。§1–2 将 Kaggle 经验作为可检索案例，避免通过额外参数训练学习每个任务。具体需求是重复处理同分布的分类/回归任务时，先承担探索成本，再复用成功实现。''',
'''§3 将任务定义为描述、训练集、验证集、测试集和评价指标。开发循环依次检索、按执行反馈重排、复用案例制定计划、生成/调试代码、保留有效结果；部署阶段只取最相似的成功任务与代码，直接适配。两阶段的输入知识不同：前者为人类经验，后者为已执行的 agent 代码。''',
'''贡献在于把反馈接入案例选择和计划修订，并明确区分探索和低成本部署。§4.2.2 去掉 ReviseRank 或整个 CBR 都使结果下降；§4.3.2 多放案例反而会干扰单例适配。分析：这些结果支持“针对当前任务选对可执行先例”，没有证明任意新领域都能直接迁移。''',
'''§4.1：30 个任务，文本、时间序列、表格三种输入，分类与回归两类目标；12 个开发任务、18 个部署任务。数据输入为各任务的 train/valid/test，环境知识是 Kaggle 人类经验库与成功代码库。不能将30任务写成一批30行输入；论文没有统一输入记录 batch size。原始自然语言指令应从官方 benchmark 配置逐条提取，本次不将本文概括写入 query JSON。''',
'''场景是数据科学团队面对新预测任务，希望 agent 产出训练与预测代码。执行路径：读取任务描述和数据划分→检索相似项目→训练与验证→结合错误或指标修订→保留实现→对下一任务直接适配。需要区分用户数据与方法的案例记忆；案例库不是模型预测的输入特征。依据 §3、Figure 3。''',
'''§4/Figure 4：GPT-4 在12个开发任务的重复实验中达到100%模型构建成功率；成功并不等于最佳预测精度。Table 1 另报任务指标排名。Figure 5：18个部署任务的一次运行成功率，GPT-4约99%、GPT-3.5为85%；Table 4 的 GPT-4 成本由开发$1.60降到部署$0.135/次。开发5次、部署10次随机重复，均非batch规模。可复现时须保留任务划分、案例库版本、模型和迭代预算。''']),
'2409.07703':('DSBench- How Far Are Data Science Agents from Becoming Data Science Experts-arXiv-2024','arXiv',2024,'2409.07703v2',[
'''DSBench 同时评测数据分析与预测建模。已阅读 v2 正文 §1–5、Tables 1–7 和任务输入/指标定义；该版本分析任务来源写作 ModelOff。应保持版本信息，不能把不同摘要版本中平台称呼混在一起。此处是 benchmark 论文，不是创造了全部底层数据的原始研究。''',
'''§1 指出现有短代码补全任务难以反映长业务描述、多个表和图像共同出现的分析需求。其具体场景是一份财务案例带工作簿和多道问题，或一项 Kaggle 竞赛带训练/预测数据及提交规范。''',
'''§2.1 输入为案例介绍 I、文件集合 D 和问题 Q，输出答案；§2.2 输入为竞赛说明、训练/测试数据及示例提交，输出预测提交文件。分析以答案语义比较评分；建模既检查能否产出有效文件，又评价预测质量。二者不能共用一个“代码运行成功”指标。''',
'''贡献是把完整问题上下文、数据文件和工具执行纳入同一评测，并用 RPG 处理不同建模指标。分析：RPG 要按§2.2公式解释为相对于基线/上界的归一化表现；不能仅因名字含 Gap 就认定越低越好。版本正文摘要与Table 6的最优数值不一致，引用具体实验应保留模型和表号。''',
'''466个分析问题来自38个 ModelOff challenge；Table 2给出31个Excel文件、69个sheet和5张图片。74个建模任务来自筛选后的Kaggle竞赛，原训练数据按8:2重划分。输入列应逐任务列出文件和表列；共享案例介绍/字典属于环境上下文。466是问题数、69是sheet数，均不是记录batch size。本文未提供统一batch参数。''',
'''财务分析用例可先读取案例介绍，再在多个工作表定位目标数据、计算问题答案；预测任务读取字段说明、训练集和测试集，输出与sample submission相同格式的预测。工具可用Python或Excel，benchmark本身不限制唯一解法。上述是§2的场景释义，不是可登记为原文的query。''',
'''Table 4：AutoGen/GPT-4o分析任务准确率34.12%，按challenge平均为26.72%；两种平均口径不同。Table 6：GPT-4模型构建成功87.84%、RPG45.52；GPT-4o为71.62%与34.74。人类分析结果仅抽10个challenge，建模代码结果覆盖22个竞赛，不能写成全部540题的人类上界。Fig.5显示分析任务长上下文更难，Fig.6的建模成功率没有同样明显趋势。''']),
'2410.05080':('ScienceAgentBench- Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery-ICLR-2025','ICLR',2025,'2410.05080v2',[
'''ScienceAgentBench 将论文中的具体科研数据任务转为生成独立 Python 程序的评测。阅读 v2 正文 §1–5、Tables 1–3、评价和人工rubric分析；正式发表信息另由官方仓库确认 ICLR 2025。阅读版本的实验数值不替代2026 verified split的结果。''',
'''§1 的问题是：不能仅凭 agent 能写一篇研究报告，就断言它能独立完成科学研究。需要先验证加载数据、处理数据、建模、分析、画图等可执行子任务。用户对象是希望节省编程时间、但仍能验证产物的科学家。''',
'''§2.1 一条任务包括任务指令、数据目录及内容预览、可选专家知识、参考程序。系统必须输出可独立运行的Python文件。§2.2 从44篇同行评议论文提取任务，经过专家和标注者复核，最终102条；这些是基准作者改编的任务，不能标成原论文逐字查询。''',
'''贡献是任务真实性验证、输出执行判定和细粒度rubric结合。数据重划分、移除部分测试点及隐藏测试标签用于抑制直接复述或读取答案。分析：rubric来自参考实现，可能低估等效替代算法；§4.2作者也讨论了这一点。通过执行仅是VER，达成目标才是SR。''',
'''输入包含细胞图片、分子、地图和EEG等异构数据。任务的目录预览帮助定位文件；可选领域知识是环境上下文，不能放入硬件栏。Table 1原文示例：“Train a multitask model on the Clintox dataset to predict a drug’s toxicity and FDA approval status.” 对应输入为Clintox数据，输出模型预测，成功阈值ROC-AUC≥0.77。未逐条获取数据文件前，不编造列名或记录数。''',
'''同一框架可处理药物毒性预测、睡眠IMU数据端点计算和多伦多消防站覆盖图。后两者分别需要时间序列和空间数据，评价产物不同，不能统一当成文本分类。§2.3设置依赖环境并执行程序；这属于运行条件，与问题所需的专家知识分开记录。''',
'''Table 3以每题3次独立尝试中按SR/VER/CBS/成本顺序选最佳结果。Claude-3.5-Sonnet self-debug无专家知识SR32.4%、有知识34.3%，对应每任务API费用$0.057/$0.061；o1另列，不应略去后称其为所有模型最优。三次尝试不是输入batch。专家知识有时降低可执行率但提高成功率。当前官方仓库已发布2026 verified数据，复现实验须锁定版本。''']),
'2402.18679':('Data Interpreter- An LLM Agent For Data Science-ACL Findings-2025','ACL Findings',2025,'2402.18679v4',[
'''Data Interpreter 用任务图与动作图处理多阶段数据科学问题。已阅读 v4 正文 §1–5、Algorithm 1、Figures 2–5与Tables 1–4；发表版本为ACL Findings 2025。不能把2024预印本日期误写为2024 ACL发表。''',
'''动机是任务间存在依赖，执行后数据和错误会改变后续步骤。一次性生成全部代码难以持续修正。具体需求包括读表、清洗、建模、计算混淆矩阵及可视化串联时，在失败处修订且复用已完成的中间结果。依据§1、§3.1。''',
'''§3将高层问题分为任务图，每个任务再展开为可编程动作节点；动作同时包含工具调用和普通Python逻辑。Algorithm 1执行节点、检查结果、重试，随后更新任务状态。§3.2按拓扑顺序比较新旧任务描述的共同前缀，保留未变化的成功部分并重做分叉后的工作。''',
'''贡献是两个粒度的执行反馈：动作代码修复和任务图修订；工具以代码组合进入上下文。Table 4显示在4个ML任务上的综合得分从纯代码执行0.37、加入图修订0.85、再加入节点生成0.94。分析：任务DAG是规划结构，若要映射semantic operators需另核实每节点输入输出与语义，不能把所有Python操作叫semantic operator。''',
'''§4.1覆盖InfiAgent-DABench的257题/52 CSV、Kaggle ML任务、20个开放任务和MATH子集。结构化输入为CSV或训练/测试表，开放任务也涉及网页、图像和账号状态。具体列名、路径应从每题发布文件取得。论文不存在贯穿所有任务的记录batch size；工具top-k及调试上限不是batch。''',
'''Figure 2的分类与可视化流程要求前一阶段产生的预测结果可供后续混淆矩阵与绘图使用；失败后动作生成器利用执行反馈改写代码。图像处理、网页模仿和邮件回复则需不同的输入资源和可用工具，不能用一个“数据环境无”覆盖全部。''',
'''Table 1：GPT-4o版本准确率94.93%，相对无agent的75.92%增加19.01个百分点；“25%”是相对增幅。GPT-4-0613版本73.55%，低于对应无agent78.99%，作者归因上下文容量。Table 2综合分0.95、API成本$0.84；Table 3开放任务完成率0.97、$0.41。不同任务集的综合分、完成率、准确率不可合并为一个成功率。''']),
'2609.24137':('Data Agents- Agentic Data Systems-arXiv-2026','arXiv',2026,'2609.24137v1',[
'''本文将data agent定位为覆盖数据组织、语义算子、计划编排、反馈、记忆和主动适应的数据系统。已阅读v1正文§1–8、Algorithm 1与实验Tables III–VII。它与semantic operator研究直接相交，但主动发现任务的完整能力仍被§7列为开放问题。''',
'''§1从销售额下降场景出发：仅计算汇总不足以解释原因，还需要评论、外部证据和数据语义。跨源场景要求agent先发现相关数据，再组合关系计算与语义分析，而不是每个新领域重新手写流水线。''',
'''§2建立语义目录和向量索引；规划器组合SQL、关系算子、semantic filter/join/group/extract以及API。§4通过类型与签名检查、多候选输出比较、合成样本检查和Pipeline2NL一致性反馈修订计划。§3用带版本边的记忆管理插入、更新、失效、检索和合并，保留冲突历史。''',
'''贡献是数据组织—计划—验证—记忆的整体集成，§6消融针对语义组织、反馈与记忆。分析：一致性检查能发现偏差，但多个候选或LLM生成的样本答案一致并不构成语义正确性证明；不能把这些流程记作原始gold。§7明确更强的自主发起/闭环能力仍未完成。''',
'''§2原文示例：“Which product experienced the largest decline in sales, and why?” 输入为销售表与评论，环境含语义目录、索引和历史知识；SQL先定位下降产品，语义过滤负评，再抽取/分组原因。该例没有给出具体列schema或公开文件路径，因此不编造可执行query JSON。§5-A明确记录合批、级联和共享前缀KV复用，但未给统一batch size。''',
'''销售诊断是关系聚合与文本证据联动的具体场景；DABstep测试跨文档/表格分析，Spider 2.0-Lite测试不同引擎上的SQL。记忆复用的数据集知识不等于输入业务记录；处理一个查询时能读取哪些表、文档、目录与历史工作流，应分栏描述。''',
'''§6称以Qwen3为骨干、DABstep validated split与Spider 2.0-Lite 547题评测。Table III给出easy94.44%、hard50.79%；Table IV执行准确率44.50%。Table V为2.8对6.5分钟、5.1对7.4分钟；基线分别不同，不能相互混用。Tables VI–VII是按查询类别的token费用证据，非实测batch吞吐。消融支持组件作用，但公开配置、具体Qwen3版本和数据切分仍需代码确认。'''])}
files=['README.md','出发点分析.md','解决的问题分析.md','Novelty分析.md','workload分析.md','usecase分析.md','benchmark分析.md']
cat=json.loads((root/'catalog.json').read_text())
cat=[p for p in cat if p['url'].split('/')[-1] not in ['2405.15793','2402.10890','2605.12493','2605.08904','2307.06551']]
for p in cat:
 id=p['url'].split('/')[-1]
 if id not in reviews:continue
 folder,venue,year,version,sections=reviews[id];target=root/'reviews'/folder;target.mkdir(parents=True,exist_ok=True)
 for file,body in zip(files,sections):
  title=p['title'] if file=='README.md' else file[:-3]
  (target/file).write_text('# '+title+'\n\n[论文原文](https://arxiv.org/html/'+version+')\n\n'+body+'\n')
 p.update(venue=venue,year=year,reading_status='full_text_reviewed',review_folder=str(target),reading_scope='正文方法、任务定义、实验表与局限；选读相关附录。未复现实验，未遍历每条发布任务。',review_version=version,evidence=[p['url'],'https://arxiv.org/html/'+version],reviewed_on='2026-10-14')
(root/'catalog.json').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
print(len(cat),'papers;',len(reviews),'reviews')
