# SemiHS-Bench：已取得数据/仓库，尚未完成资格审计

HF revision `6247f52c1f8443f5e3f9def6c9a939c9c619b615`，完整17文件5,461,128 bytes。官方GitHub commit `8f2c4074a9f124d6a294d04a534777f437c9e487`完整ZIP1,329,998 bytes。原论文未找到可下载版本；不计Strong、不追加正式38个候选。精确哈希见artifact/evidence/shared-environment-strict-semihs/。

| 条件 | 本次核验 |
|---|---|
| A/F | 固定HS6分类；实际900train+900eval。官方称来自目录/BOL，需进一步审计源实体隔离 |
| B/C | 889裁定、taxonomy和HS6描述已取得；尚无完整长规则环境及20例闭合证据 |
| D | open prompt明确使用模型自身知识，taxonomy只用于评分且不展示。现有差距不能证明完整E固定方法不足 |
| E | 25个difficulty tags是预定义混淆边界，不能直接作为学到的执行家族K |
| G | Tier1模型起草专家审核；Tier2原始稀疏输入。reference_ruling_ids按当前gold挑相似案例，不可直接提供给执行系统 |
| H | 数据与代码已下载，论文未取得；HF README写private/embargo，但API private=false且GitHub公开，发布说明不一致待核验。数据许可CC BY-SA 4.0；不外发原始材料 |

| Query | 数据湖1 | 数据湖2 | 数据湖3 |
|---|---|---|---|
| 对每件商品输出HS6代码 | 900eval原始/描述输入 | 889历史裁定（需全库检索而非gold选引用） | HS2022 taxonomy/说明；完整规则仍待核对 |
| 类Python DAG | scan → sem_map(classify) → project(id,code) | retrieve → compare | apply nomenclature |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 未测、未知 | 完整相同输入+固定检索/规则程序 | 未测、未知 | ==查明部件身份、核查规则边界、比较适用历史案例== → 分类/UNKNOWN | 待20例及真实轨迹核验，不预设动态分支 |

| 比较臂 | 原作者证据边界 |
|---|---|
| task-only | open要求own knowledge；不是完整E基线 |
| static-full-E | 尚未核验相应实验 |
| per-case Agent | 有provider-native web条件，未核验预算/同资源 |
| batch Agent | 未核验批内共享执行 |

下一步：取得论文、检查construction中的标签和边界生成来源，按预先确定规则审计20条eval，不将按gold挑选引用作为公开模型资源。未执行作者代码或模型。

来源：https://huggingface.co/datasets/MIL-HAL/SemiHS-Bench 和 https://github.com/cti-iel/SemiHS-Bench 。


## 固定20例与引用充分性初审

抽样：eval全部900条按SHA256("semihs20-v1" + NUL + frozen_id)排序取前20，记录sample20.json，未因疑点替换。20条描述、标签及解释已读；引用ID全部能在本地裁定库找到。这是定位完成，不是完整C20验证。reference-audit.json记录每例引用数量及非空解释数。

全889裁定中280条rationale_excerpt为空、392条url为空。空URL不等于原裁定不存在；非空解释也不等于充分。初步细读4条裁定暴露以下可核对缺口：

| 样本 | gold | 本地引用与实际缺口 |
|---|---|---|
| #13 eval.0002，约5%氢混合气 | 280410 | EBTI-DE-DE18254/15-1写chemisch einheitlichen Wasserstoff（化学单一氢）；没有解释该混合物为何同类。其他引用尚待逐项验证，不直接宣判gold错 |
| #12 eval.0298，DC电源/控制器子系统 | 848620 | H293625讨论特定RF发生器，档案摘录结尾被截断；需要功能、部件与整机规则的适用解释 |
| #3 eval.0263，CMP系统 | 848610 | N240976本地只有IonScan Basic System标题及空解释，不能独立证明CMP归类 |
| #20 eval.0308，wafer grinder控制电脑部件 | 848640 | N007092本地只有wafer handler标题、解释为空；比较对象和功能不同，尚不足以证明同代码 |

本次没有更改gold，也没有声称四例错误；下一步需完整规则及原裁定，评估其余引用能否补全。20例完全闭合数仍未建立，不能把程序找到引用当作通过。原论文仍未取得。构造代码初步定位了专家状态与证据计数检查，但未将未读完整代码输出解释为已验证监督来源。


## 官方原裁定恢复：摘录缺口与规则适用仍须分开

本轮通过CROSS网站实际main.js中公开的`/api/ruling/{id}`接口下载H293625、N240976、N007092完整正文。入口从官方页面脚本读取，不猜测私有接口；原网页部分403/只有页面框架不等于正文不可获取。保留原始响应于忽略数据目录，另生成去除临时下载URL的内容文件及独立哈希收据official-rulings.json。

- H293625：正文明确RF Generator自身构成机器，并依据Section XVI Note2(a)、GRI1/6归入8486.20；不能直接以其代码证明普通DC控制/电源子系统同类。需核查其功能与sole/principal-use条件。
- N240976：实际商品是离子束减薄晶圆的IonScan Basic System，2013年归8486.10。恢复了标题外的工艺事实，但仍需比较CMP样本是在制造晶圆还是器件加工阶段，以及其他引用与规则。
- N007092：同一Phoenix wafer handler给出2006年8428.90.0010与2007年8486.40.0030，说明历史代码必须做版本对齐；功能为搬运且无制造/测试功能，不能直接证明grinder控制电脑部件标签。
- #13三个本地氢气参考全部补读：德国记录化学单一氢；斯洛伐克记录分别99%氢、94%氢含5.9%甲烷。三条均未直接解释本样本约5%氢混合气的归类。保留疑点，不修改gold，不声称已依据完整法规证明标签错误。

本轮完成3份原始参考恢复；仍不是20例完整gold验证，无模型或算子执行，无Strong升级。下一步需要结合HS2022完整规则与其余引用审查，而不是将“已下载正文”当作通过。


## HS2022第28章及verified字段语义

已从WCO官方2022目录实际链接下载第28章完整PDF，277295 bytes，SHA256 918741c8aa72d3163791fcbe644050127262b0842dd75dd1dcfdd5bfd6fa7766。Note1限定化学单一元素/化合物并列出杂质、溶液及必要保存/运输添加等条件。#13输入是约5%氢混合物，剩余组成及具体Note1例外条件未充分给出。因此目前不能仅凭“氢”或三条高纯氢参考推出其gold；也不指定替代代码，因为相关事实和完整跨章判断尚缺。

构造源码`ingest_bol.py`第405行附近明确hs_verification只是申报代码HS4前缀一致性sanity check；`auxiliary_enricher.py::_bol_hs_verified`做相同前缀检查。故本例`hs_verified=true`不能当作独立专家逐案确认凭证。它不否定作者另有专家审核，但需要另行取得审核记录/来源，不能由字段名推断。

本轮新增官方版本规则证据与标签字段语义核验，未改gold。原论文、20例完全闭合、完整E固定方法不足与语义家族证据仍未成立。


## E条款核验：25类不是独立执行家族证据

完整读取`boundary_detector.py`与`difficulty_tagger.py`。`detect_boundaries`先读hs6_label，再从candidate_set减去gold得到干扰代码；sibling_split按gold与干扰代码是否落入配置簇判定。cross_family按gold所在侧、另一侧干扰代码或关键词判定；关键词文本包含tier1_description及justification_text。`compose_boundary_note`按标签拼接配置中的固定句子。

因此25标签具有gold辅助的诊断分组语义，不能证明从公开输入发现了25个需要不同推理程序的家族，也不能直接作为模型路由输入。`infer_classification_driver`也是解释文本/描述上的关键词启发式，不是人工观察执行轨迹；`tier2_classifiable`亦有MPN/产品词/规格启发式，字段名本身不能视为专家事实。

本路线当前决策：暂不为升格Strong继续机械扩展裁定下载。已有明确未满足项：原论文未取得；固定20例中存在公开事实/规则适用未闭合；D缺完整同资源固定对照；E现有标签不能作家族证据。保留候选数据资产供今后新增证据核验，既不以未知判定数据无价值，也不以候选数满足Strong目标。
