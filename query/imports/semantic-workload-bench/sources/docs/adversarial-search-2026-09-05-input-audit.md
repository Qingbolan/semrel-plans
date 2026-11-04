# 对抗搜索：输入真实性与构造可行性审计

日期：2026-09-05，Asia/Singapore。角色：输入/构造攻击方。本次仅阅读官方网页、固定版本源码、JSON和公开样例；没有下载图像/权重、运行模型或构造新评测集。已读 git status、AGENTS、SPEC、research-context、environment-validity、evaluation-protocol、近期 report 和 MMAD 审计；共享工作区原有未跟踪内容全部保留。本文的“存活”指值得下一步低成本反证，不表示已证明 Agent 或资源增益。

## 裁决

| 候选 | 当前裁决 | 决定理由 | 最便宜的下一步反证 |
|---|---|---|---|
| AnomalyClaw 衍生 LOCO/SDNET 子任务 | 条件存活，不能沿用发布结果作为干净比较 | 有实际像素工具及共享图像判断，但默认工具代码含 test 标签条件统计，部分发布调用可达；SDNET 源照片划分未隔离 | 从独立源组重建小开发集；去掉 test 校准提示；比较完整图像输入的直接调用、固定工具链、Agent |
| MMAD/LOCO 单产品 | 条件存活 | 真图像/异常标签/正常参考可形成固定筛选；完整逻辑规则和知识来源仍有缺口 | 先逐规则核对正常训练材料与任务标签，真实图像工具必须不读人工 JSON |
| TrialGPT | 条件存活，语义与固定分解路线 | 病例叙述、试验条件、相关性标签公开；需要核对病例来源及同一 trial 的可用判断量 | 固定一个 trial，审计全部必需事实和 UNKNOWN，再比较整条判定与事实抽取→逐条件判定→聚合 |
| DABstep 费用适用性 | 降级为规则编译/执行候选 | 资源完整，但 payments 明确合成，输入大部分已结构化；逐支付 gold 不随任务级答案自动存在 | 用文档独立写两份解释/判定器，查边界和空列表，先证明语义规则可唯一执行 |
| GuideBench | 降级为规则遵循开发控制 | 存在共享规则子集；实际 math 数据中发现参考解与禁止叠加规则冲突 | 小规则集穷举合法组合并与 gold 独立核对，先估歧义/错标而非测模型 |
| UNDERWRITE 公开样本 | 暂停可运行环境构造 | 发布的是多模型轨迹，未发现独立指南/SQL资产；不能用当前测试工具回包重建环境 | 先找到完整版本化指南/数据库/执行器；拿不到则只做轨迹结构研究 |
| MedGUIDE | 降级为合成指南控制 | 数据 `path` 直接包含正确终点；完整树需另外取得，不能从当前测试路径拼成“外部知识” | 取得独立完整树，按树/路径划分，屏蔽 path、答案、生成/评分元数据后复测 |
| FinQA | 保留待统计，不立即构造 | 有原文表格和程序 gold，但样本含 gold-selected model_input；同运算不等于同业务语义 | 按明确金融指标统计独立报告数，审计完整公开输入，不提供 gold_inds/model_input |

## 1. 新候选 AnomalyClaw：实际代码揭示的边界

核验 [固定 commit](https://github.com/jam-cc/AnomalyClaw/tree/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6)。[DATA.md](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/DATA.md)说明发布 manifests、检索索引、专家分数缓存、Agent 输出；原图从上游取得，D6/D7 检索索引没有随版本冻结。缓存模型预测本身不等于人工 gold，但当前实现不是对任意新图可执行的完整专家服务。

[agent_tools_v8.py](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/benchmark/scripts/agent_tools_v8.py#L85)有明确问题：

- 85–87 行注释将专家选择的 AUROC 来源标为 v2 manifest 与 `subspacead_test.json` 的交集。119–128 行把范围提示标为 v2 test cache，包含 `normal_median`、`anomaly_median`。132–140 和 345–355 行把这些统计作为工具观察交给模型。当前默认代码路径存在明确测试标签校准风险；它不等于逐图直接读 label，源码存在也不证明所有发布运行用过，不能推定所有分数均失效。
- `tool_expert_score` 用 item ID 读取已缓存预测和 top patches；新增记录没有缓存即返回 unavailable。重建环境须从真实像素运行相同专家，保留训练、参考、校准来源与预处理成本。
- 329–330 行将 `1-AUROC` 解释为被标记项中误报比例，统计含义错误；该提示不应照搬。
- 1069–1106 行 `tool_domain_knowledge` 只是再次调用文本 LLM，没有查询独立手册。不能把多一次模型回答称为文档资源收益。
- 裁剪、图像差分、FFT 等确实处理像素；`component_counter` 数的是专家热图连通块，不是识别螺丝等实体的可靠计数器。工具名不是任务语义证明。

[D7 manifest](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/benchmark/manifests_v2/D7_remote_sensing_manifest.json)实际 158 行，20 calibration /40 dev /98 test；query 为 image2，ref 为同场景 image1。[builder](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/benchmark/scripts/build_manifest.py#L497)以 `mask.max()>0` 构造建筑变化标签。前时相是必要输入，直接 LOTUS 必须也拿到两图；变化不自动代表损坏或灾害。旧 builder 域编号与发布 manifest 不同，不能未经映射就认定脚本可精确重建。

[D6 manifest](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/benchmark/manifests_v2/D6_infrastructure_manifest.json)实际 180 行，20/40/120，未发现 query 自身进入其 refs，也未发现 test query 进入任意 refs。但按文件名连字符前缀这个待上游确认的母图代理，dev/test 重叠 13 组、calibration/test 9 组。发现方独立以 `(category,prefix)` 重算一致。[SDNET2018 官方来源](https://digitalcommons.usu.edu/all_datasets/48/)确实由母照片裁成 patches；新确认须按母照片隔离。

实际可达复核：`agent_v12.py` 第36行导入v8、第237行调用其dispatcher；v8 registry映射expert，第1164行调用。三份D3发布JSON中，Qwen有6次expert调用，3次`obs_keys`含`range_hint`与`domain_auroc`，另3次为unavailable；Seed有2次、其中1次含上述字段；GPT5.5 D3没有expert调用。发布history仅存字段名而非完整观察数值，不能逐值确认当时payload与当前源码一致；尤其不能据此把GPT5.5 D3增益归因于这一风险路径。计数只使用可观察工具名和字段元数据，未在本文保存内部推理文本。

发现方接受以上攻击，将新开发校准和真实专家执行列为门槛。Root 独立重算 D3 三个发布结果，每个都有 120 个 usable、无 error；因此不能笼统宣称该子域优势由删失败制造。算术可复核不解除测试校准与固定工具强对照问题。

## 2. 手册环境核验

### UNDERWRITE

读取 [HF 文件树](https://huggingface.co/datasets/snorkelai/Multi-Turn-Insurance-Underwriting/tree/main)及 data 子目录、完整数据卡。可见资产为轨迹 parquet、卡片、示意图片，未见独立 SQL 或完整核保指南。卡片明确 `company task id` 可跨模型比较，因此 380 条不是 380 独立企业；`correct` 为 LLM-as-judge 结果。信息有合成与公开来源，非真实核保工作日志。使用历史轨迹可以研究工具行为，但不能从当前 R 的轨迹回包中提取规则，再声称外部环境帮助判断 R。当前结论是资源缺口，不是证明资源不存在于任何其他位置。

### GuideBench

锁定 [commit 78c5bfa42facee34db31e4ba03ad2c3b5a04bbbc](https://github.com/Dlxxx/GuideBench/tree/78c5bfa42facee34db31e4ba03ad2c3b5a04bbbc)。直接 JSON 解析：`price_tasks.json` 442 条、47 个精确 Guidelines 集，最大共享组18；`math_tasks.json` 52 条、14组，最大5。因此“每题规则完全不同、无法批处理”的绝对攻击不成立，但可用同环境批规模有限。

[math_tasks.json](https://github.com/Dlxxx/GuideBench/blob/78c5bfa42facee34db31e4ba03ad2c3b5a04bbbc/data/math_tasks.json)零起始第27项，答案695：rule44禁止与固定金额券叠加，rule11也禁止与满减叠加，ReferenceAnalysis却在使用满350减90后再减25。部分规则彼此方向不一致，解释还涉及跨商品/订单作用域。这里报告明确冲突线索，不另造正确答案，也不推广为全库错误。

SHA256：math `8e74181768cd2c466e81eefc338fbbdd0a466ef5528a600feb4e0574a0f858ab`；price `525c565f76012ab9c8164909364a368e47ecd0e36bd03afed4f238d6f9cd9f4d`。独立规则解释和 gold 审计先于模型能力判断。

### DABstep

实际读取 [manual.md](https://huggingface.co/datasets/adyen/DABstep/blob/main/data/context/manual.md)、[payments-readme.md](https://huggingface.co/datasets/adyen/DABstep/blob/main/data/context/payments-readme.md)、fees、merchant JSON及 tasks目录。payments 明确 synthetic；merchant 包含已有 account_type、MCC、capture_delay，fee包含枚举、范围、布尔与公式，主要挑战可能是把文本规则编译为确定性程序，而非逐行开放语义判断。

manual 只明示 null 通配，fees 中有大量空列表，须核验其语义；fraud ratio文字方向与百分比例的通常解释需消歧。这些是低成本审计点，未运行支付数据判定，不宣称全部记录不可计算。既有主任务答案不能自动提供每条支付适用规则的独立 gold。固定程序若显著改善直接调用仍符合用户本次筛选意图；后续单轨迹贡献必须对比无轨迹一次 Coding Agent。

读取时文件 SHA256：manual `bb7f4ca6fdc759af1f480702b3a3b12e17e9293b0d38a1dbfbbc8ffc1e572d2c`；payments-readme `8754b92d0b3127856ff72266ea482995d2a1f6a34d0a12732f7c26f527f2c4a5`；fees `9a833666ae9be5a8e756dd1fe076c72e7c502d64161315ffa8fee9e5bf2599dc`；merchant `f158e834de27ee8407e99d9c32da690357981d2770958fd302a9bb79ced83581`。这是 main 文件字节记录，尚非完整快照锁。

### MedGUIDE

读取[论文方法](https://arxiv.org/html/2505.11613v1)、[HF文件树](https://huggingface.co/datasets/MedGUIDE/MedGUIDE-MCQA-8K/tree/main)及 datasets-server 首行实际字段。公开 `path` 包含分支条件和正确叶节点，`answer_text/answer` 明示答案；另有生成模型及质量分。公开执行只能提供经过 allowlist 的病例/选项等，不能递归挂载全行。论文由指南路径生成病例，不是独立真实病例；知识加入后改善首先是树执行/合成一致性证据。HF根目录仅卡片与parquet，尚未核验完整55棵树是否可独立获取及使用，不能从当前测试路径反推“无泄漏手册”。

## 3. 发现方提出的补充候选

[TrialGPT 固定版本](https://github.com/ncbi-nlp/TrialGPT/tree/1b3242cd50c153a9c324661d4a0bd94fc68a4226)可见 queries、qrels、检索结果和部分 corpus。已读取 TREC2021 原始病例样例：包含真实临床叙述风格和去识别日期标记，来源必须按子集分别核验，不能把所有来源一概说成真实患者或全合成。病人×试验为相关组合，不是每个组合都独立；也不能将未标注组合当不符合。先固定 trial/疾病范围，检查足够的病例判断与必要事实。

[FinQA 固定版本](https://github.com/czyssrs/FinQA/tree/0f16e2867befa6840783e58be38c9efb9229d742)开发第一条实际含 pre_text、post_text、table、qa 和多个 retrieved 字段。qa 包含 program、gold_inds、ann_table_rows、model_input，示例 model_input 含正确证据行；均不能直接当无标签公开输入。外层可为同金融指标提取→计算→聚合，但必须先统计语义相同的指标家族及独立公司/报告量。仅同为 divide 不成立共享业务任务。

## 验证与限度

本次标准库网络读取与 JSON/Counter/哈希解析成功；一次按根目录读取 `agent_tools_v8.py` 返回404，随后依据真实文件树改读 benchmark/scripts 位置成功。无软件测试（0）、模型调用、种子/推理预算/并发/缓存配置或金额；均不适用。外部源码只读取未执行。本文没有证明任何本地质量提升、资源因果或单轨迹迁移结果；最终 ledger 由 root 统一追加，不与其并发修改 report。
