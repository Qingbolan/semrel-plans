# Codex CLI 同模型实测结果：2026-09-05

已按用户要求执行真实 Codex CLI 0.151.0，沿用此前同一服务的 `gpt-5.4`。CUAD、BioDEX 各一个完整批次，每批8条，CLI均正常退出，没有新增模型请求失败。结果没有通过主指标优势筛选。

| 指标 | 原静态流程 | 固定复核 | 原受限工具循环 | Codex CLI |
|---|---:|---:|---:|---:|
| CUAD span F1，Jaccard >0.15 | 0.5079 | 0.5318 | 0.5275 | **0.5023** |
| CUAD span F1，Jaccard >0.5 | 0.3953 | 0.4113 | 0.4231 | 0.3890 |
| CUAD coverage | 7/8 | 7/8 | 7/8 | 7/8 |
| BioDEX RP@10 | 0.3643 | 0.3643 | 0.3589 | **0.3393** |
| BioDEX RP@5 | 0.4000 | 0.4000 | 0.4250 | 0.3500 |
| BioDEX RP@25 | 0.4286 | 0.4286 | 0.4375 | 0.3929 |
| BioDEX coverage | 8/8 | 8/8 | 8/8 | 8/8 |

原 `data-agent` 文件名保留历史身份，指Python受限工具复核循环，不是Codex。本轮才是stock Codex CLI原生模型/工具循环。所有数据都是已经评分的开发记录；这些结果不能证明总体能力边界，也不能视为独立确认。

## 实际行为与质量变化

CUAD：Codex执行23条shell命令，4次完成的文件修改事件，调用既有公开工具8次，并生成 `repair_predictions.py`。它修复了初始引用中的空白、断行及边界问题，使不匹配原文的引用从21条降至0。它没有改变任何合同的类别集合，关系TP/FP/FN仍为100/22/26、类别聚合计数误差仍为30。合同 `6859a73163e8bf450ce312cd` 的一条 `Parties` 引用被删除，span F1从该记录的原分数下降0.0450；其余7条主指标相同。引用合法性改进没有补回漏抽类别。

BioDEX：Codex执行22条shell命令，3次完成的文件修改事件，生成 `build_predictions.py`。它直接用Python读取/检索完整文章与24,369项术语JSON，未调用包装的向量检索或其他公开工具，所以新增embedding调用为0；这不等于没有使用环境资源。引用不匹配从6条降至0，目录外术语从1条降至0。但预测标签数由43降至30，关系TP/FP/FN从14/29/20变为11/19/23，macro-F1由0.3361降至0.3019，标签计数总误差由45降至40。误报减少的同时，正确标签也被删去。

BioDEX唯一RP@10下降的文章为 `1d5f77272a1270f7bae16b6d`：初始4标签被全部删除，该记录RP@10下降0.2。Codex按原提示将其视为非患者药物不良反应；原pilot已发现这一患者ADR口径与released gold事件范围存在不对齐风险。当前结果不能用来宣称其医学判断错误或静态方法能力不足。其余7篇RP@10不变，不代表标签集合完全相同。正确目录名、原文证据、事件范围、gold标签一致性是不同指标。

两个生成脚本均含当前record ID和逐实例修正/答案，是本次batch执行产物，不是自动提取的可复用算子。未在新实例运行它们，也没有将其包装成B5结果。

## 配对与成本

| Codex 相对对照 | 平均主指标差 | 改善/退步文档 | 描述性配对bootstrap 95%区间 |
|---|---:|---:|---:|
| CUAD vs 静态 | −0.0056 | 0/1 | [−0.0169, 0.0000] |
| CUAD vs 固定复核 | −0.0295 | 1/5 | [−0.0538, −0.0065] |
| BioDEX vs 静态 | −0.0250 | 0/1 | [−0.0750, 0.0000] |
| BioDEX vs 固定复核 | −0.0250 | 0/1 | [−0.0750, 0.0000] |

8条的开发筛选未通过“相对两个对照均+0.05且至少3条改善”的冻结条件。区间沿用seed20260905、10,000次文档级配对bootstrap；不是独立群体显著性或患者分组确认。

| 费用计量 | CUAD Codex | BioDEX Codex |
|---|---:|---:|
| 新增模型请求 | 21 | 16 |
| 新增input tokens | 904,941 | 599,648 |
| 新增output tokens | 7,957 | 11,452 |
| 含原共享静态结果的模型tokens | 1,194,890 | 896,341 |
| 含共享初始的模型请求 | 29 | 32 |
| CLI批次wall-clock（秒） | 618.83 | 627.85 |
| 新增embedding tokens | 0 | 0 |

CUAD/BioDEX分别有5/2条非零退出shell命令，均由Codex在同次执行中修正并保留在轨迹中，开销未删除。所有最终CLI正常退出。

本轮任务新增37次模型请求、1,523,998 tokens，无缺失usage；另有原生Responses连通测试175 tokens、Codex执行测试2次请求10,869 tokens，总新增已知1,535,042 tokens。实际金额未知。CUAD standalone还包含原静态一次超时的未知usage，该失败仍计入coverage分母。BioDEX standalone另含历史术语预处理133,247与初始查询1,001 embedding tokens，共134,248。

服务报告CUAD/BioDEX分别558,592/509,527 cached input tokens；无客户端响应回放。尽管请求reasoning effort为none，服务仍分别报告2,481/5,224 reasoning tokens，只保留数量，不保存私人推理内容。两个家族并发运行，每家族为一个串行CLI请求流；容器启动和文件转发开销包含在wall-clock，镜像构建另存setup收据，没有做受控延迟实验或CPU-seconds测量。

## 配置与解释边界

沿用旧public快照、任务提示、初始结果和scorer；原CUAD初始超时按所有review臂的规则传播，因此7条实际复核、1条ABSTAIN。BioDEX的旧口径问题没有只为Codex修改。Codex在无网络Docker中可读公开文件、编写/执行代码、共享批计划及计算，没有仓库、私有gold、密钥或宿主Docker socket。隔离实测全部通过。

模型请求和返回均为gpt-5.4；仍是代理别名，不能独立验证权重快照。Codex用Responses，旧流程用Chat Completions；固定temperature0/reasoning none/maxoutput12000，但原生系统提示、批次上下文、可执行代码、预算不同，不能称严格等预算因果比较。stock CLI自动安装自己的内置system skills；没有导入用户skills、历史会话或项目指令，也没有观察到调用内置skills。所有私有gold评分都在CLI退出后进行。

Frozen [设计](codex-cli-pilot.md)保持不变。其“无plugins/user/project instructions”指未导入用户扩展；原生内置system skills为本次观察补充。原生SSE透传时排除reasoning项并缓冲到请求完成，故不是生产网络时延基准。没有同预算B3、完整DocETL或资源消融。这轮证据说明当前任务/环境下Codex能做程序化检查，但没有显示更高主任务质量；不进入单轨迹提取阶段。

## 产物与复现

- [CUAD比较v2](../runs/cuad-codex-cli-v1/comparison-v2.json)、[预测](../runs/cuad-codex-cli-v1/predictions.json)、[CLI轨迹](../runs/cuad-codex-cli-v1/cli-events.jsonl)、[生成脚本](../runs/cuad-codex-cli-v1/work/repair_predictions.py)。
- [BioDEX比较v2](../runs/biodex-codex-cli-v1/comparison-v2.json)、[预测](../runs/biodex-codex-cli-v1/predictions.json)、[CLI轨迹](../runs/biodex-codex-cli-v1/cli-events.jsonl)、[生成脚本](../runs/biodex-codex-cli-v1/work/build_predictions.py)。
- 每个run下保留prompt、inputs及hash、launch-source、call-NNN.json、隔离检查、run/metrics和原始生成文件；mailbox仅作临时传输。旧comparison.json保留，v2仅将CLI内置skills脚本从“Agent生成代码”列表排除，分数/成本不变。
- [复现脚本](../artifact/reproduce-codex-pilot.sh)：已具备旧快照与static run、安装pilot依赖的环境下，`SWB_CODEX_OUTPUT=/absolute/unused/path bash artifact/reproduce-codex-pilot.sh`。脚本使用PATH中的python；本次用`.venv/bin/python`。镜像构建后必须联网调模型的仅是宿主broker，Agent容器运行时始终无网络。
- 工程验证24项离线测试通过，Docker隔离和真实shell执行通过；没有独立团队复现或研究有效性认证。
