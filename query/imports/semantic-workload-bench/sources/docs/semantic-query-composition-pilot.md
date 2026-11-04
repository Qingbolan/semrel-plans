# 从现有semantic operator query归并任务：开发pilot v1

2026-09-08，按用户新路线实施：survey/benchmark定位场景→核数据/原query/基线→按任务含义归并→构造公开数据湖→隔离Codex重复执行→保存query、operator候选和可观察轨迹。来源发现与重复运行用于开发，不预设Agent优于静态或进入单轨迹提取。

## 首个执行簇：电影口碑复核表

来源SemBench commit `c814e3807e72d4cf876b852b17e77f3cc94575c2`。原Movie Q2选正向影评、Q3计数、Q4算比例、Q8按正负分组，共享同一影评情感判定。新请求：“为本批电影生成口碑复核表：列出指定影评中的所有正向review ID，给出正/负数量及正向比例。”电影和指定影评集合参数化；Q2的任选五条改为完整正向清单，明确是派生query而非原题逐字复现。原Q9评分和Q10排名不并入，二分类gold不足以证明细粒度评分或排名。

作者发布sf_2000含2,000行，构造前实际核出135个重复reviewId，各出现两次且全部字段完全相同。公开湖按完整相同记录去重为1,865条影评，保留全文和电影ID/标题关系；冲突重复立即拒绝。新任务统计唯一影评，明确不同于原表bag计数，不将改后的数值与论文原规模结果混比。原scoreSentiment、reviewState、originalScore、reviewUrl、电影audienceScore/tomatoMeter不进入公开资源；原LOTUS谓词只读取reviewText，所以所有方法使用同样语义输入。原gold是作者源表的scoreSentiment，非本轮新标注或已独立审定的情感真值；保留“clearly positive”与二分类标签的可能边界差异。

选择规则在模型运行前冻结：按可用影评数量选前三电影，以movie ID打破并列；每电影按SHA256(seed+NUL+reviewId)取12条，seed=`sembench-composition-development-v1`，共36条目标、3条电影级任务记录。其余影评可留在湖中，明确不计入本批结果。这不是完整电影口碑统计，也不是原论文规模复现。构造已查看源标签，所有运行均属开发；重复3次是同数据随机执行，不是3个独立确认批次。

## 冻结执行与比较范围

- 传统LOTUS：按作者requirements使用lotus-ai1.1.3 wheel，独立解包到data目录，不改既有依赖；关闭cascade/cache，用原Q3的sem_filter prompt，再固定计算清单/数量/比例。该流程复用源算子，但参数化并合并了多道query，属于派生流程对照。
- Codex：复用本仓WorkspaceAgent和CodexContainer，原生CLI0.151.0。3次新上下文执行相同公开快照，每次最多8个模型请求、600秒；容器无网络、输入只读，无仓库/宿主home/密钥/private挂载。允许批内共享代码、计划与缓存；不要求每影评重新规划。
- 共用既有.env服务的gpt-5.4请求别名，温度0、reasoning none；实际官方snapshot身份未知。原LOTUS库通过记录适配器访问Chat Completions，Codex走Responses，接口和系统prompt不同，非预算对齐因果比较。静态每影评一调用，共36次；Codex按整批执行，预算不同须披露。无自动任务重试。每臂内部串行；静态与Agent两臂可同时运行，实际最多两个并发模型请求。
- 记录源hash、任务/公开manifest、实际模型返回名、prompt、每次工具/命令及输出、错误/终止、tokens和wall-clock；不收集私有思维链。金额未知不填0。现有容器镜像ID在各run记录；不将构造侧gold或作者答案JSON递归挂入公开输入。
- 评分在冻结输出后由evaluator读取private gold：review清单precision/recall/F1、计数误差、比例误差、电影级完整结果一致性、coverage/ABSTAIN，以及3次重复输出一致性。语义正确性与内部算术一致性分开，不让错误标签通过自洽检查变成正确。

候选算子为`classify_review_sentiment(text)`或`sem_filter(positive, review)`，外层ID选择、分组、计数、比例为确定性步骤。候选来自原任务语义；后续须与真实trace对齐。当前实例ID写死的Agent脚本只是运行产物，不是可复用算子。尚不执行B5提取或宣称摊销收益。

## 入口与产物

源材料：`data/semantic-query-discovery-20260908/`，其中checkout含gold，仅构造侧使用。公开任务：`data/sembench-movie-composition-v1/public/`，私有gold为同级private。构造入口：

```sh
PYTHONPATH=src .venv/bin/python artifact/semantic-query-discovery/prepare_movie.py
```

构造拒绝覆盖既有目标；本文件在模型请求前冻结，结果另行追加到研究账本/发现报告。来源数据许可与代码许可分别核验；本轮只本地实验，未发布原影评或向其他人发送。


模型调用前构造修正：首次“2,000个唯一ID”断言失败，尚未发布目标目录；审计确认135组完整相同重复，无冲突。随后按上述唯一影评协议重新构造，未按标签或预测删样。

## 新服务执行协议 v2（第二轮整批调用前冻结）

旧服务的36次静态请求与1次Codex请求均HTTP503，输出全部ABSTAIN；保留原目录。用户提供的新服务为OpenKey `/v1`。预检显示：gpt-5.4无渠道，gpt-5.4-mini过载；gpt-5.2 Chat Completions成功，返回模型名`openai/gpt-5.2`，但Responses接口404。因而新执行显式使用gpt-5.2与Chat接口，且设置该服务可接受的HTTP User-Agent。模型名称是服务声明，未独立验证底层身份。

LOTUS直接发Chat请求；原生Codex通过已安装LiteLLM的Responses/Chat格式转换访问同一模型。Codex CLI、公开输入、工具及任务循环不改，转换只负责消息与工具schema、返回事件格式；custom apply_patch用JSON content包装，原语法约束不再由API强制。转换前后请求、真实provider响应、token usage均保留；无自动Responses→Chat重试或模型切换。桥接缓冲完整回复后生成事件，不能以这些事件时间研究流式延迟。静态36次与Codex每批8次预算仍不同，最多两臂同时请求；金额保留服务usage字段，但未核对实际账单，不将provider cost当已付金额。

本轮目录前缀`runs/sembench-movie-openkey-`，公开manifest和query不变。预检目录`runs/sembench-openkey-*-preflight-v1`保存失败和成功的小请求。此变更是服务适配及开发流程验证，不与原模型结果合并为同条件比较。

## Agent预算开发修正 v3（重跑前冻结）

v2的Codex已真实执行目录、schema、JSON和CSV检查，但在8次模型请求后被预算拒绝，尚未输出结果；保留`agent-r1-v2`及全部费用，不把该失败判为情感分类错误。其工具还实际遇到`python`不存在，改用`python3`。依据执行预算失败、未依据private评分，v3将三个新上下文重复的模型请求上限统一为24，wall-clock仍600秒，其余任务/输入/模型/桥接/工具不变。静态36次流程继续按v2完成。v3是修订后的开发运行，不能把v2失败从工作账本或总试验成本删除。

## 完成状态

全部三次v3原生Codex执行已完成并私有评分，LOTUS32/36、Codex24/36、28/36、23/36；未显示Agent改善。本轮新增公共CLI参数支持显式--public，默认仍为冻结目录；重建快照得到相同public manifest。原始trace、失败和预算变更完整保留。完整来源、15簇登记、方法具体表和有效性限制见[指定登记仓库报告](../../Awesome-Sem-Filter-Bench/docs/semantic-operator-query-composition-2026-09-08.md)。

复现收据限制：本轮Agent旧run尚未记录宿主模块执行前hash；静态script hash在运行结束读取，期间新增过CLI选项，不能当执行起点源码指纹。当前已改为执行前记录，另保存[交付代码/依赖指纹](../artifact/evidence/semantic-query-discovery-20260908/code-and-dependencies.json)，明确不补造历史执行hash。原始输入、模型调用/返回、事件、预测及镜像收据保留；本次为开发trace采集，不宣称完整的独立复现实验认证。
