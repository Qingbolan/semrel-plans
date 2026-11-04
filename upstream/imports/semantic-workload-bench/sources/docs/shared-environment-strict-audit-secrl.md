# SecRL / ExCyTIn-Bench — Reject

[原论文](https://arxiv.org/abs/2507.14201)及[完整官方仓库](https://github.com/microsoft/SecRL)已下载。commit a1b234f7a846133f08b7b5e1614c5c63b96f3b5c，432文件，ZIP138724069bytes。[来源哈希](../artifact/evidence/shared-environment-strict-secrl/source.json)。代码MIT，未执行作者代码或攻击行为。

| 条件 | 直接证据 | 判定 |
|---|---|---|
| F | 论文§3：模拟八条攻击链，良性背景亦模拟；每条独立tenant episode | 不能称天然真实case批 |
| A/G | 从事件图的起止节点用LLM生成QA与solution | 多个不同问题，不是同一个固定语义q；不是独立人工逐casegold |
| C | QA带start/end alerts/entities与shortest path | 这是构造/评分信息，不应作为公开探索资源；20人工gold闭合0 |
| B | 论文介绍59表，构造正文写57表；数据需另建/下载SQL环境 | 本轮仓库未发现.db/.sqlite；不声称完整环境已取得 |
| E/D | 图路径有结构复用；一部分question自带实体线索 | 不能由路径数或模型生成题量推导语义家族K；固定查询替代未排除 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 样例：找可疑进程对应的账户名 | incident38 QA上下文指定host、notepad进程及PID | 需要SQL日志/事件关系；非本轮已下载完整可执行环境 | answer=nathans、solution及gold路径，私有评分资源 |
| 类python的DAG | `scan(questions)`，问题各异 | `agent_sql_search(context, question, E)` | `compare(answer, private_gold)`；不等于同q的天然批 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 样例目标nathans，未运行LOTUS | 抽取给定进程/主机条件，固定SQL关联账户，需先核验真实表 | 未运行Agent，不能预设正确 | ==检查表schema，定位进程关联与账户字段==，再查询验证 | `resolve_process -> join_user -> project(account)`；结构路径可固定，非已自动提取算子 |

| 具体下载核验 | 完成 | 限制 |
|---|---|---|
| 文件 | secgym/questions含80个JSON、5个MD；逐文件记录数已保存 | 不将多个模型/版本/split相加成独立N |
| 样例 | 实际打开o1/v0/test/incident38首个完整问题/答案/路径 | 未对原SQL证据闭合，不称真实专家裁决 |
| 模型输出 | 仓库含历史实验日志 | 本轮未将其当作可复现实测或读取私人思维链以解释模型决策 |

[问题文件清单](../artifact/evidence/shared-environment-strict-secrl/question-files.json)。保留为SQL调查机制参考，不进入Strong候选。
