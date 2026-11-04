# 第124轮：VetClaims新25案开发检查包构造完成

7/15保持；这次构造不代表晋级或科学VALIDATED。复用120轮原论文与完整作者源ccb98b19525e，新查作者提交历史。

## 作者版本线索

[作者仓库](https://github.com/LLTLab/VetClaims-JSON)历史显示：2019-06-07加入角色协议；2020-08-27提交65841572187fe8a3d711f4491b6718af08b9f13e的消息为加入2019秋季25份新判决。它支持同作者后续队列来源，不直接证明使用六协议的精确版本和所有裁决约定相同。README仍主要解释旧50份。commits.json保留实际API结果，未从年份直接推断独立确认。

## 已构造内容

新目录data/shared-environment-audit-20260908-v124/inspection-v1：25case、2665行、35个清单资产。public含作者原句、内嵌原文上下文、六协议原PDF、19节点规则树及任务限制。private含独立角色gold和来源映射。逐行公开ID由case序号+数组位置生成，不使用角色或易重复的源sentID。规则树仅保留label/operation/nodes，移除ruleID，不含病例真值；六协议尚含需核验的例子。

保留原始标注句字节语义（JSON重新序列化），没有自动改写123轮的拼写/排版差异。任务明确给定作者句子切分与选择，不能称原始全文端到端解析。原判决的裁决内容是本角色识别任务的合法输入，不是患者获赔预测任务。

独立verify.py检查35个资产哈希/大小及完整文件集合；2665行与源句、源角色gold、源上下文逐项一致；public字段allowlist通过；树19节点。该验证没有证明协议例子无泄漏、许可、OS隔离、模型质量或复杂E必要性。未实现该包的模型runner/scorer；它是可审查输入包而非已完成benchmark。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 检索事实认定句 | public/cases中25案2665行，句子与未标注全文 | public/environment六PDF共39页 | 清理后的共享19节点规则树 | private/gold.json角色；Finding188 |
| 按案检索证据评价推理 | 同批案例 | Reasoning/Finding/Evidence协议 | 来源差异保留于作者句子，所有方法输入相同 | Reasoning227；两查询共享一次角色分类结果 |

| 类python的DAG | 具体数值 | 输出契约 | 下游gold |
| --- | --- | --- | --- |
| `cases.rows.sem_map(role,context,E19).filter(role=='FindingSentence').project(record_id)` | 25案2665行→源目标188 | 六类角色；record_id按数组位置无答案生成 | 188源统计，未执行预测 |
| `cases.rows.sem_map(role,context,E19).filter(role=='ReasoningSentence').groupby(case_id).count()` | 源目标227 | 同输出固定聚合 | 227总量，独立配对评分待实现 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未运行；船舶记录证明力例目标ReasoningSentence | 固定同资源角色分类→过滤；允许固定阶段和共享缓存 | 未运行；目标相同，优势未知 | ==读取六角色边界及共享规则树== → ==核对句子在上下文中的推理功能== → 输出角色 | `SentenceRole(author_sentence,context,E19,protocol_hash)`；提取必须单独提供真实轨迹，本轮没有提取结果 |

下一步不是重复源校验，而是协议例子/队列关系核验与环境必要性审查。单独39页长度或35资产校验通过都不足以加入可行名单。固定程序/E-only编译/Coding Agent可取得同一public资料。

复跑构造需不存在的目标目录；build.py目前默认路径已存在，重复执行会拒绝，须显式改为新路径；verify.py只读构造包并另写本轮验证收据。代码/收据位于artifact/evidence/shared-environment-audit-20260908-v124/{build.py,verify.py,build-receipt.json,verify-receipt.json,commits.json}。没有模型调用、新单元测试或commit；来源gold已开发暴露。目录分离不是安全沙箱。


125轮计数纠正：六协议总正则词数为18685，早先18785是加总错误；其中Part I为6807、Part II为11878，前者仍含行内例子。
