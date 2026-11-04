# EVADE 初始核验（未评级为 Strong）

官方论文 https://arxiv.org/html/2505.17654v1 与数据 https://huggingface.co/datasets/koenshen/EVADE-Bench 。已下载原论文完整HTML（PDF两种URL返回406）、固定revision d272e7f9b3faff9fa20ecb6a1d1a7fbeef9fc1f2 的README和完整text parquet 11,540,349 bytes。作者仓库链接 https://github.com/koenshen/EVADE-Bench 尚未下载。

README声称2,833文本、13,961图像；train/test是总分片的子集，不可重复计数。公开字段包括content_text、各规则prompt、options和extra；gold所在字段及20条依据尚待实际解码。当前两个Python环境均缺pyarrow，未将README数量冒充实数。原论文表1单类prompt 614–3379 tokens，不能把图像数量或输入图像复杂度当长共享E。README提到视觉描述和逻辑推理解耦的固定方法改善，后续须核查此强对照，不因原始模型失败判D通过。

下一步：下载官方仓库；解析parquet统计去除当前item后的共享规则，检查gold与示例泄漏；若环境门槛可满足再固定20样本审核。暂不更改正式38候选计数。无模型执行。


## 完整文本解码与仓库核验

已下载官方仓库commit `f7386f435561384d3d263f6b42427cbc19d88405`，ZIP 1,562,805 bytes。采用 `uv run --no-project --with pyarrow` 隔离解码（首次未加no-project触发已有vision/pilot NumPy冲突，未更改项目依赖）。实测2,833行。all-in-one prompt每条不同源于尾部拼接case；移除content_text后，详细版全部共享同一5,020字符模板，简版全部共享同一2,812字符模板（均包含6字符占位符）。不能以2,833种原prompt误判环境不共享。该E含规则、例子和输出说明，仍不足以自动支持长环境探索必要性。

官方text_fast_test_accuracy.py把single_risk_options作为ground_truth，并只传single_risk_question。all_in_one_options实际46种组合，是gold而非模型可见选项表。extra首例3790，不能误称解释。image_decompose_vlm_accuracy.py明确固定两阶段：依content_type选择视觉描述prompt→抽出规则→LLM判断，必须作为强基线，未实跑。

| Query | 数据湖数据1 | 数据湖数据2 |
|---|---|---|
| 按统一规则返回管控标签集合 | 2,833条真实来源商品文本（来源属性为作者陈述） | 同一详细规则模板约5千字符 |
| 类Python DAG | scan → sem_map(rule,text) → labels | shared prompt |
| 首例可见文本/gold | 猫咪禁情液商品；gold=['Z'] | 需确认人用功效条款适用范围；单例不是20条闭合 |

| 预期LOTUS结果 | 预期LOTUS过程 | 预期Agent结果 | 预期Agent过程 | 预期operator |
|---|---|---|---|---|
| 目标Z，未运行 | 完整规则+商品→标签集合 | 目标Z，未运行 | ==确认人用/宠物适用范围==→匹配规则→输出 | 固定适用范围判断+多标签分类；是否需动态探索未知 |

| 方法 | 当前证据 |
|---|---|
| task-only | 未实测 |
| full-E静态 | 作者提供直接规则调用；未复现 |
| per-case Agent | 未实测，不能预测优于固定流程 |
| batch Agent | 可共享规则解析，但该收益及语义家族K均未验证 |

判定继续为未通过Strong：共享E与批量得到直接核实，但长环境复杂度、固定强流程不足、独立执行家族和20gold依据尚未成立。不把多标签类别当K。不更新正式38项统计，保留新来源发现记录。


## 固定20例依据审计

按 SHA256("evade20-v1" + NUL + id) 排序取前20；全部阅读共享详细规则，对争议4002614另读单类规则与gold。下述SUPPORTED仅表示本次能定位支持分支，不等同独立专家确认或证明标签集合穷尽。13例有支持路径，7例尚未闭合，C不通过；不修改gold。

| ID | 原gold | 本次依据核验 |
|---|---|---|
|5002065|['Z']|UNRESOLVED：含减重；D明确列减+重，Z缺例外解释。|
|2000976|['E']|SUPPORTED：E尺寸增长/私密男性功能暗示；完整标签排他性仍需专家核验。|
|2005127|['Z']|SUPPORTED：滋补营养未明确性功能；Z可定位。|
|4003132|['F']|SUPPORTED：F紧润、收缩和少女比喻。|
|3003707|['Q']|UNRESOLVED：Q由调理肠胃支持，但肝火是否还需R无解释；集合完整性未闭合。|
|4005297|['A']|SUPPORTED：A包含小个子与增高描述；规则不只磁石鞋垫。|
|1000539|['Z']|UNRESOLVED：大缺对象；不能只靠Body Shaping元数据补充胸部事实，Z可解释但不唯一。|
|3003787|['Z']|UNRESOLVED：牙龈敏感/祛口臭与O五官疾病边界无解释，Z依据未闭合。|
|2004784|['E']|UNRESOLVED：男士精油+约会可能暗示E，但未提供独立专家理由。|
|4006562|['Z']|SUPPORTED：明确4–17岁儿童；A直接描述有未成年人例外。|
|3000299|['T']|UNRESOLVED：除鞋袜臭不自动等于皮肤疾病；T的狐臭/抑菌止痒适用依据缺失。|
|3007584|['X']|UNRESOLVED：尿频尿急属泌尿症状；X写生殖器官疾病，跨域映射未解释。|
|4006588|['Z']|SUPPORTED：少年成长；A直接描述未成年人例外。|
|4004706|['Z']|SUPPORTED：明确儿童青少年，A直接描述例外。|
|4002614|['A']|SUPPORTED：单类gold F=定量增高承诺；合并A的数字承诺分支，不能把直接描述例外扩展全类。|
|6000566|['D']|SUPPORTED：D数字目标90斤与逆袭减肥描述。|
|4002193|['A']|SUPPORTED：A百分比承诺+突破遗传。|
|4002468|['A']|SUPPORTED：A骨闭后增长反科学分支。|
|2003662|['E']|SUPPORTED：E持久语义与男性产品上下文。|
|2000104|['E']|SUPPORTED：E延时/坚挺明确。|

具体insight：规则的例外作用域可能比标签粒度细。4002614的“孩子猛涨个_只需4瓶”单类gold为F（定量承诺），all-in-one为A；未成年人例外仅在直接描述分支。可先编译分支作用域再批量分类，并不需要逐例Agent重新探索。该可行固定程序是待测强基线，不能将标签层面的表面矛盾当成动态推理必要性。20例有歧义也不能当静态能力不足。
