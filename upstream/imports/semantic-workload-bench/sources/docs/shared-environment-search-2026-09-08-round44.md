# 第四十四增量：EUIPO商标异议真实标签存在，但公开仓库缺输入

**不计入合格列表，累计1/10。** 本轮新检索商标混淆争议，实际下载原论文和完整作者仓库，读取全部CSV；不是沿用搜索摘要计数。

| 资产 | 下载核验 |
|---|---|
| [ICAIL2023原论文](https://orbi.uliege.be/bitstream/2268/322890/1/ICAIL2023.pdf) | A Quantitative Evaluation of Trademark Search Engines’ Performances through Large-Scale Statistical Analysis；8页；原PDF已下载并pdftotext实读 |
| [完整作者仓库](https://github.com/thovdamm/ICAIL23-Evaluation-Trademark-Search-Engines) | commit `a20ffe7dc7efcd5f35126b4c62a1e79168a1ea8e`；仅1个blob，即results.csv，Git SHA1及ZIP CRC通过 |
| results.csv | 实际8,126行/8,126唯一decision_ID；LOC原值+4,287、-2,057、+ -1,781、空1；不是8,126个二分类任务 |

原论文第3页明确：公开列表和搜索性能，但不公开判决和具体搜索结果，作者给出的原因涉及其研究所依据的文本与数据挖掘使用范围。这是作者对发布范围的说明，本轮不作法律解释或联系作者。仓库没有商标图像、双方商标ID、商品/服务描述、事实正文或规则PDF；holder_ID不是双方商标内容。没有许可证文件，不能将仓库公开可见解释为无限再发布许可。

论文原任务是搜索引擎能否召回争议对方商标，不是混淆可能性裁决复作。研究甚至把未认定混淆的争议对方也用于召回评价。因此搜索命中排名不能充当混淆决策gold。CSV的+ -具体细分和商品范围需要原判决解释，不能擅自合并为TRUE或FALSE。

另检索确认官方EUIPO指南有整体评估、商品/服务相似性、视觉/语音/概念比较及相关公众注意程度等规则。由于本源核心case输入未公开，本轮未下载长指南来装饰空输入；不能声称具备长E。2014/2020/2021/2022指南版本也不能不加区分地套于2016–2022所有案件。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 逐对商标及商品/服务，在冻结指南下判断混淆可能性 | 长指南尚未下载/绑定 | 8,126个判决ID、日期、holder_ID；商标实际输入未取得 | 商品、服务、相关公众和两方图像缺失；不能用搜索排名填充 | +4,287/-2,057/+ -1,781/空1；仅原字段，未逐案核对 |
| decision2813874，17-01-2018 | 规则版本未核验 | holder716400，没有双方图像和事实 | 六个搜索字段均Err；Err是检索问题，不是法律否定结论 | 原LOC为+，本轮不能根据缺输入复作 |
| decision3052070，28-05-2019 | 同上 | holder430886；EUIPO对方商标排名2、申请方排名1 | 排名不说明哪类商品构成混淆 | 原LOC为+ -；需原判决拆分范围，不能映射单一Boolean |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `scan(results).join(decision_assets)` | 8,126唯一ID | 判决/图像/商品资产没有随库提供，join尚未完成 |
| `sem_map(confusion_by_goods,E,marks,goods,public)` | 1,781混合LOC项需要明确输出单位 | 输入缺失，不能运行完整必要输入基线 |
| `sem_filter(confusion).project(case,goods).count()` | 可靠下游gold数量未知 | 不用4,287或6,068冒充已核实可执行任务计数 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 在现有缺输入条件下不能给可靠实体判断；未运行 | 资产join→固定相似性、商品范围与相关公众抽取→整体评估；必须先取得实际输入 | 同样缺输入，不能假设Agent能凭空补齐 | ==核验资产是否齐全==→==确认混合结果对应的商品范围==→==读同版本整体评估规则==→材料充分才判断，缺失则ABSTAIN | `TrademarkConfusionOperator(E_version, marks, goods_scope, public_attention, distinctiveness, global_assessment, abstain)`；这只是候选接口，不是已生成算子 |

下载脚本、SHA256、完整仓库核验和实读统计在`artifact/evidence/shared-environment-audit-20260908-v44/`；原资产在`data/...-v44/`。session92170正常结束；未运行作者程序、模型或新工程测试（0）。该来源当前不是可行湖，继续寻找其他独立来源或可公开补全的核心case材料。
