# 固定 DAG 语义质量候选：发现方及交叉质询

日期：2026-09-05，Asia/Singapore。范围：一轮官方资料检索、轻量 JSON 检查和三方交叉质询；未下载图像包、运行模型、安装模型或执行作者程序。本文是候选发现证据，不是新 benchmark 构造或质量实测。当前 CUAD/BioDEX/PCB 阴性边界维持。先检查 git status 并读 AGENTS、SPEC、context、environment-validity、evaluation-protocol、README、artifact-guide、report 近期条目；共享现有文件保留。账本由协调方统一追加。

## 筛选结论

优先进行输入审计的两条是 **SDNET2018 裂纹筛选**和 **LOCO 单产品装配一致性**。前者有新的真实来源及直接模型失败线索；后者有固定分解改善的论文线索。但新发现的 AnomalyClaw 公布实现包含测试集条件的专家选择及分数提示，**不能将其原表称为干净的资源/Agent 增益证据**。保留环境候选，不沿用其测试缓存、校准或切分。

第三条为 **TrialGPT 的固定试验初筛**，仅在同一试验具有足够独立患者标签时进入开发。它是合成病例背景下的规则分解研究，不是已证实的真实临床输入环境。

| 候选 family | 具体共享任务与固定外层 DAG | 直接判断错误机制；可执行资源 | 当前处置 |
|---|---|---|---|
| SDNET2018 | 对同一种混凝土表面批图判断是否含可见裂纹；scan → sem_filter(crack) → IDs/count | 阴影、接缝、划痕与细裂纹混淆；原图裁剪、纹理/边缘程序、独立冻结视觉专家、正常参考 | 优先输入审计；不得扩成结构安全等级 |
| LOCO / MMAD-LOCO | 固定一个产品，如早餐盒，按完整共同装配规则筛选异常；scan → sem_map(组件/数量/位置) → rule check → IDs/count | 感知计数、左右区域、替代项与组合约束；真实 ROI、组件感知、完整规格、固定规则程序 | 优先规则及感知输入审计；与既有暴露 LOCO 按源图去重 |
| TrialGPT | 固定一临床试验，按完整患者摘要判断初筛资格；scan patients → criterion sem_map → logical aggregation → shortlist | 否定、时间范围、缺失事实与多条件；完整试验条件、标准化单位/日期计算、逐条件固定分解 | 条件保留；先数独立患者，不用75k pair冒充样本 |
| DABstep 费用适用 | 固定费用规范，批交易匹配适用费则并聚合；scan → join merchant → sem_map(rule applicability) → calculate → sum | 条件和通配、merchant/transaction字段混淆；manual/fees/关系表及规则编译器 | 降级为规则环境；数据 synthetic，解释冲突与行级 gold 未解决 |
| FinQA 同指标 family | 同一业务指标跨报告抽取操作数，算指标并排序/聚合；scan → sem_map(operands) → calculator → aggregate | 表头、年份、范围与单位绑定错误；完整发布 text/table、计算器、历史人工程序 | 暂缓；没有本轮证据证明足量同业务指标样本 |
| GuideBench 同规则价格 family | 固定一套优惠规则，对批购物场景计算适用优惠；scan → sem_map(applicability) → deterministic total → aggregate | 例外、叠加限制、作用域；完整 Guidelines 与规则求值器 | 小型合成逻辑诊断；gold一致性待审，非真实业务场景证明 |
| V*Bench 属性视觉搜索 | 固定目标属性抽取子任务；scan image → sem_map(attribute) → filter/count | 高分辨图局部目标不可见；真实定位/裁剪/搜索 | 工具单元诊断；191异质QA未证明同任务批量 |

以上 DAG 是本研究提议，不声称原 benchmark 已发布这些批处理查询。资源不是缺省必需规则的替代品：全部比较臂都应获得完整必要图像/试验条件/业务规则；工具带来的计算与组织收益另测。

## 1. SDNET2018：新物理输入线索与反证

[上游大学数据页](https://digitalcommons.usu.edu/all_datasets/48/)给出 230 幅相机原图、256×256 分块以及 crack/no-crack 人工标签，56,092 块并不是56,092独立场景。图像来自桥面、墙和路面；[数据论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6247444/)展示了阴影、污渍、接缝、孔洞等干扰。公开下载包约516 MB，本轮未下载；官方许可为 CC BY 4.0。裂纹有无是已标注语义，严重度、承载安全、维修行动均无相应 gold。

新线索来自 [AnomalyClaw Table 1](https://arxiv.org/html/2605.10397v1)：SDNET 域的 Direct→融合Agent AUROC 为 GPT-5.5 .573→.778、Seed2.0-lite .445→.706、Qwen3.5-VL-27B .580→.672；固定 AnomalyVFM .798，超过这三项 Agent。故即使数字被独立复现，也只支持“直接判断存在可改善空间”，不证明动态策略不可替代。D6 平均模型调用约2.83/3.08/3.02次，预算未对齐单调用。

输入攻击方核查作者 `agent_tools_v8.py`：`EXPERT_POLICY` 按 v2 test cache AUROC选专家，`EXPERT_RANGE_HINTS` 含 test cache 的 normal/anomaly median 并可回传模型。必须删除整条测试条件资源路径，不能仅隐藏字段名。专家权重可以作为候选，但需从原始允许图像重新计算，使用开发集决定选择与校准。工具固定调用、无工具重复推理、同预算 Agent 必须比较。

本方从 GitHub API 锁定 AnomalyClaw commit `1a0c4b4e8e25d8a231f694b264a6669925b6d0b6`，用标准库 urllib/json/hashlib读取 D6 manifest：180行，calibration20/dev40/test120；test deck41/wall38/pavement41。SHA256 `e9d1cf0c96a838a63ad6cc0d037846bbe5735f23e5b1a6e89df693fee58f22ab`。以(category,文件名首个连字符前缀)作母图代理，calibration-test重叠9组，dev-test13组。此代理仍需原README核对，不能宣布已做实体隔离；它已足以否定“文件路径不同就独立”的假设。

最小重建：核对母图ID → 按母图分组 → 新匿名public路径 → 保留上游图块标签于private → 重算正常参考及允许工具 → dev冻结阈值 → 新母图测试。不能把裂纹检测成本包装为工业人工验收手册收益；该路线主要测试感知工具，而非长手册。

## 2. LOCO：固定推理可保留，弱比较不能沿用

[官方 LOCO](https://www.mvtec.com/research-teaching/datasets/mvtec-loco-ad)具有产品图像、正常训练参考与异常区域 gold；研究使用需遵守 CC BY-NC-SA 4.0。不能将结构异常与逻辑异常混成“完整规则违例”而不核对标签。MMAD 多题与 LOCO 原图有重叠，是同源资源而非第二个独立 family。类别级 `domain_knowledge.json` 不是完整验收SOP，其规则欠账和来源不确定仍见既有 MMAD 审计。

[LogicAD 原论文](https://arxiv.org/html/2501.01767v1) Table3提供固定流程线索：Guided CoT 48.5 AUROC，加ROI 60.4，再加格式嵌入86.0；逻辑证明路径报告F1-max83.3。其使用手工类别规范/提示和一次正常图；这不是从一条Agent轨迹学得规范。无模块行23.4是论文特定表示流水线消融，不能称现代LOTUS直接异常分类准确率。必须同供完整规范比较直接判断、结构化感知+规则执行、Coding Agent和自适应感知。

AnomalyClaw D3是5种产品混合，120个test样本，其中早餐盒22、连接器23、果汁瓶23、图钉21、螺丝袋31。Manifest SHA256 `376259d231c5b9e9f02b0d8cec795deb1729bc9a4af74173434b12a100516472`。它的域平均不是任何一种产品的可靠收益。按原始产品扩展/重新分组，核查真实感知工具，禁止读取同名人工组件JSON（历史 LogiCode 问题）。复杂知识与感知错误必须分开消融。

## 3. TrialGPT：真实试验文本、合成患者及强固定流程

[官方代码与数据](https://github.com/ncbi-nlp/TrialGPT)和[论文](https://arxiv.org/abs/2307.15051)给出检索→逐条件匹配→聚合排序流程、183合成患者、超过75k试验关联判断及1,015医生逐条件标注。87.3%逐条件准确率是现有 TrialGPT 结果，不是与同模型直接调用的增量。具体试验正文是必要规则，绝不能不给静态方法。原始用途以一患者检索多试验为主；改为固定试验跨患者需要先统计该试验已有独立judgments，未评判pair不能当负例。缺失事实须保留未知/不足证据，而非推断不合格。

构造成本是标签覆盖与对象变换核验、试验版本冻结、患者实体split、逐条件与trial gold关系核对。无需先造医学Agent平台。若固定分解已接近专家而直接现代模型也足够好，该候选不满足当前质量差距目标。

## 4. 三个文本候选为何暂不推进

**DABstep：**[官方目录](https://huggingface.co/datasets/adyen/DABstep/tree/main/data/context)有 manual、fee规则、交易和商户关系；[manual](https://huggingface.co/datasets/adyen/DABstep/blob/main/data/context/manual.md)定义规则匹配，不能省略。[官方介绍](https://huggingface.co/blog/dabstep)的早期整体难度数字不是同一fee family的直接LLM对照。输入攻击方已读 payments-readme，声明 synthetic；还发现 null 与 [] 通配语义、fraud ratio文字与例子的疑似冲突。本轮未独立解决这些冲突，未获得独立逐交易fee gold。先验证规范能否唯一编译以及现有答案一致性，失败即停；不创造自己规则+自己gold作为真实业务正确性证据。

**FinQA：**[官方代码](https://github.com/czyssrs/FinQA)、[原论文](https://aclanthology.org/2021.emnlp-main.300/)公开 text/table、专家问题、答案与程序；它可提供真正的操作数及计算步骤 gold，但同程序形状不等于同业务指标。未统计足量同 metric、同口径、不同报告样本，因此本轮不进入构造。尤其要将语义操作数选错与算术执行错误分开；程序执行提升不能全归因语义Agent。

**GuideBench：**[官方库](https://github.com/Dlxxx/GuideBench)、[ACL论文](https://aclanthology.org/2025.acl-long.557/)提供指南与答案。攻击方实际检查价格442条，最多18条共享完全相同指南，因此不是绝对无法合批，但样本很小；README参考解有疑似违反自身叠加禁令，需审计gold。即便修复，仍是合成规则诊断，不自动成为真实企业定价环境。UNDERWRITE完整资料未公开核验，仅轨迹记录，故未列入可落地前七项。

## 5. V*Bench：作为感知机制诊断

[官方仓库](https://github.com/penghao-wu/vstar)公开高分辨率视觉搜索实现与benchmark入口。191题的异质目标不能直接充作固定共享谓词。可先用真实图片验证定位/裁剪是否从像素产生所需属性，但需重新证明同任务family及足够独立原图，不能把任意视觉QA按一个`sem_map(answer question)`包装为目标批任务。公开代码中用于视觉搜索评估的target_bbox参数还应与实际工具路径隔离，避免评价侧定位gold进入推理。

## 对抗后的可反驳假设

1. SDNET：同源实体隔离、同完整图像输入下，允许公开视觉工具的固定/Agent路径能改善固定阈值的裂纹清单质量。若只AUROC变好而F1/清单不改善，或优势随无泄漏重建消失，则不通过。
2. LOCO：完整装配规则与正常参考同供时，真实结构化感知与规则执行比直接异常判别更可靠。若只提供人工标注组件才有效，则退为annotation-given诊断；若完整规则下直接模型已足够好，则不通过。
3. 两者均不预设动态Agent优于固定流程；若固定流程收益可复现，它是强基线和可能提取产物。只有后续真实单次轨迹→自动提取→新实体独立执行成功，才支持本项目单轨迹主张。

工程测试0，模型调用0，图像下载0；没有质量/成本/独立确认结果。当前只有元数据源码审计与外部论文转述。未commit、push或外发本地材料。
