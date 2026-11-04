# 第二十一增量：BSARD法律咨询来源核验（不列入合格湖）

已下载[ACL 2022原论文](https://aclanthology.org/2022.acl-long.468.pdf)、[完整作者仓库](https://github.com/maastrichtlawtech/bsard) commit `ff41f43b8cbf696fee7489cf188b8379dfdfd49c`，32blob Git哈希全部匹配；完整非synthetic数据来自[作者HF](https://huggingface.co/datasets/maastrichtlawtech/bsard) revision `f3ca6a396a47c4a3afd26b766b5abc0a56bb4205`。原始材料`data/shared-environment-audit-20260908-v21/`，脚本/统计/开发例/收据`artifact/evidence/shared-environment-audit-20260908-v21/`。仓库ZIP2,779,744bytes；articles.csv30,103,920bytes。未下载可选synthetic问题和训练负样本，不计入真实问题数量；未执行作者代码。源码MIT，数据CC BY-NC-SA4.0，不能混用许可。

**不通过原因是任务结构，而非文件不完整**：原论文§3.1说明问题是法律援助机构从真实来信归纳的匿名典型问题；gold是专家提供的相关法条引用。数据可以支持真实来源的法条检索，但没有每个咨询问题的yes/no法律结论。22,633条候选法条的规模也不等于每次判断必须理解一个长policy。不能将检索相关性标签冒充资格决定或判决。

实际统计：886train+222test=1108问题；6845条gold引用边，涉及1612个法条，全部ID可连接；单问题gold法条数min1/median2/max109。总法规文本3,093,212空白分词，单条中位77词。CSV中code字段34个不同字符串，论文描述32个法典；未核实差异来自命名还是版本，故不能声称已冻结论文原始32法典版本。train/test问题字符串无精确重叠不等于实体隔离。

## 三张表：仅解释已验证的检索任务，不补造决策任务

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 批量找出每个法律咨询问题的相关法条 | 冻结CSV法规库22633行；是候选法规关系，不自动等于长共享判断规则 | 1108专家整理的匿名典型问题；不同生活法律问题，不是一个固定福利资格任务 | 法条带reference/code/book等层级元数据 | 6845条question→article引用；没有独立批准/拒绝标签 |
| 开发例id1102：雇员在怀孕期间，能否拒绝加班或夜班？ | 全库输入，禁止只给gold选中的10条 | 问题字段+extra_description“Pendant la grossesse”，上下文不能漏 | 劳动相关条文可由固定/动态检索查出 | article_ids为22225–22234，共10条；**无yes/no gold** |

| 类python的DAG | 具体数值 | 能评价什么 |
|---|---|---|
| `scan(questions).join(extra_description)` | 1108条；开发例的怀孕条件来自独立上下文字段 | 上下文完整性 |
| `sem_join(articles,predicate=relevant).group_by(question_id)`或固定`retrieve+rereank` | 22633候选；穷举为25077364个配对，不是25077364个人工独立决策 | 法条检索 |
| `project(article_ids).score(relevance_gold)` | 6845已标注引用；未标注不自动证明绝对不相关 | recall/MAP等原任务检索质量 |
| `sem_map(answer_eligibility).sem_filter(approved)` | 无相应decision gold | **不可据此报告审批准确率** |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 开发例检索目标为22225–22234；未实测，不预言全召回 | 把怀孕上下文并入问题，固定词法/向量候选检索与语义复排；同样可读法规层级 | 相同检索目标，不虚构法律结论或性能差距 | ==识别劳动/怀孕/夜班与加班主题==→==检索相应规则并沿公开交叉引用查上下文==→返回法条ID | `StatuteRetriever(index_hash, context_parser, candidate_retriever, reranker)`；它是检索算子，**尚非用户所要求的长policy决策算子** |

为原法律决策任务补标答案、锁定固定资格谓词及适用法规版本，属于新增标注/任务构造工作，不是原数据已经提供。本轮保留否定证据，不将本路线或其翻译版本计入十个可行湖。未调用LLM，无方法实测或独立确认。
