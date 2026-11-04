# 正式录用场景的启发式检索与裁决（2026-09-05）

本轮是来源与候选审计，不是新模型实验。正式录用以会议论文集、出版者页面及 camera-ready 为依据；论文录用、资产可得、同条件资源增益、Agent 优势四者分别判断。此前 AnomalyClaw 仅为预印本线索，不进入本轮正式录用推荐。

## 检索方法

按失败来源反向搜索，而不只搜“agent benchmark”：复杂规则的例外/优先级→规则推理；同一实体跨表→企业匹配；视觉计数/空间关系→逻辑异常；列名歧义→schema matching；量词/聚合→表格验证。再沿正式论文的实验、基线和数据仓库追踪真实文件。发现方、输入审计方、研究审计方分别搜寻并交叉质疑；协调方独立读取重点论文原表。

审计分工材料：[视觉发现](topconf-search-2026-09-05-discovery.md)、[实物输入](topconf-search-2026-09-05-input-audit.md)、[研究对照](topconf-search-2026-09-05-rigor.md)。各文档保留源码定位、版本、数据访问限度和降级理由。

## 优先一：RuleArena 的航空行李计费

- 正式出处：[ACL 2025 main long，550–572](https://aclanthology.org/2025.acl-long.27/)，[camera-ready](https://aclanthology.org/2025.acl-long.27.pdf)，[官方代码/数据](https://github.com/SkyRiver-2000/RuleArena)。
- 原任务：按公开规则计算旅客票价、行李与特殊需求费用。完整规则已提供给普通 LLM；错误包括超重/超大收费取最大值却误相加、遗漏豁免和计算错误。
- 可构造共享 DAG：scan 旅客记录 → sem_map 按同一冻结政策计费及规则依据 → project 明细 → sum 总费用。筛选超阈费用须预先冻结阈值，不伪称原生 Boolean 任务。
- 公开资源：规则文件、题目与生成/评分材料。基准共816题，航空300、NBA216、税务300；各场景须分成独立 family。规则来源真实，但问题为构造案例，不是实际旅客/纳税人业务日志。
- 原论文 Table 10：航空1-shot、同一 GPT-4o，Level 1 准确率 .32→.44，Level 2 .16→.33；Qwen72B .19→.42、.10→.26。增强方式为模型写 Python 后执行，论文所谓 oracle 指解释器的数学/逻辑执行，不是向模型返回 gold 规则解。
- 裁决：当前最贴近“详细规则+完整输入上仍有错误+固定程序可改善”。该消融只覆盖航空，不外推 NBA/税务；没有 LOTUS 实测、同预算 Data Agent 优势或单轨迹复用证据。
- 最小反证：同模型完整规则的直接调用、一次生成程序、可执行复核程序、有预算 Agent 四臂；若固定程序质量足够，承认其优势。严禁将数据生成器/答案函数作为公开工具。先核规则和 gold 一致性，再冻结开发及独立确认。

## 优先二：企业付款—发票匹配

- 正式出处：[Unveiling Challenges for LLMs in Enterprise Data Engineering，PVLDB 19(2):196–209](https://www.vldb.org/pvldb/vol19/p196-bodensohn.pdf)，DOI 10.14778/3773749.3773758。PVLDB 是正式同行评议出版渠道，卷期标注与会议举行年份应分开。
- 原任务：把银行到账记录匹配到未结发票，包括一对多/多对一、付款附言、客户别名、参考编号差错与金额差异。比同类型商品二元匹配更贴近关系运算与业务后果。
- 可构造 DAG：scan 支付 → 固定候选生成/公开关系 join → sem_map 候选发票集合与依据 → 验证集合约束 → 输出匹配关系及未核销金额。完整关系作为所有臂可访问输入；不能让基线缺关键客户表。
- 实物审计：公开 multiple-errors 数据包含15,521发票、12,332支付、10,000 gold匹配组。这里的组不是10,000个独立业务实体；切分须按支付/发票连通分量隔离。数据按企业特征构造并注入错误，不是披露的真实交易流水。源文件与获取记录见输入审计。
- 原论文 Table 6：Claude3.5 Sonnet，多表 .58 F1、相应平表 .86；GPT-4o .58、.64。这是输入表示/复杂度对照，不能称论文已测 Agent 自动 join 增益。原实验用2,000组合（790正、1,210负）；所有10,000组不是原论文每个模型的实际评测样本量。
- 裁决：批数据任务与下游关系最贴合；完整操作手册不是现成已证实资源。优先检验确定性多表组织、字符串/金额工具能否纠正具体匹配错误，并审计候选召回与容差规则是否有业务依据。
- 最小反证：固定 join+候选检索+金额约束程序与 Agent 使用同一公开表及工具。若差距仅来自提供平表，则主张限定为表示构造；不声称动态能力必要。

## 优先三：LOCO 工业装配逻辑异常

- 方法正式出处：[LogicAD，AAAI 2025 technical track，39(4):4129–4137](https://ojs.aaai.org/index.php/AAAI/article/view/32433)，[camera-ready](https://ojs.aaai.org/index.php/AAAI/article/download/32433/34588)。原 LOCO 数据论文是 IJCV 2022，不能改称 AAAI 数据集。
- 原任务与批化：同产品图像的数量/位置/装配异常；scan 图像 → sem_filter 满足明确异常谓词 → project ID → count。正常参考、裁剪、感知与规则比较有实际用途。
- 原论文 Table 3：guided CoT+ROI 的 AUROC60.4，加入 format embedding 后86.0；F1-max65.3→83.7。这是多模块固定方法的消融，不是 Agent 对直接 LLM 的公平预算比较。F1-max 还涉及最佳阈值，不能作为部署阈值下清单准确率。原表3和表5GPT-4o F1也不同，应保留原表语境。
- 裁决：图像与逻辑规则结合的候选；完整、独立来源的装配验收手册尚未闭合。需加入 [SALAD，ICCV2025正式论文](https://openaccess.thecvf.com/content/ICCV2025/papers/Fucka_SALAD_--_Semantics-Aware_Logical_Anomaly_Detection_ICCV_2025_paper.pdf) 等固定方法，不能只比直接VLM。
- 最小反证：工具必须真实读取图像进行感知，不读标注或 gold 选出的裁剪；各臂同产品规则/参考。若感知错误使规则不可用，不能靠标签工具制造Agent优势。

## 条件候选四：Magneto 的生物医学列映射

- 正式出处：[PVLDB18(8):2681–2694，2025](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)，[官方代码](https://github.com/VIDA-NYU/magneto-matcher)。
- 具体用例：把不同研究的患者/样本表映射到统一GDC字段；同一“年龄”可能对应诊断年龄、出生天数或索引年龄。共享任务为 source column → target field，并向下游统一表转换传播。
- 资源：公开表、目标schema与检索/重排方法；完整领域文档不是已验证的同资源增益。原方法还训练小模型，不可把整个系统收益说成同一LLM加文档。
- 关键攻击：原研究为实验省略GDC descriptions，部分gold是有限上下文下专家预期映射共识；补充真实文档可能改变预期答案。先解决目标语义、不可确定状态和gold一致性，再测文档增益。
- 裁决：真实数据来源有吸引力，环境有效性审计优先于运行；不能利用缺失必要字段定义制造静态失败。

## 方法证据与暂不进入主试验的候选

- [Chain-of-Table，ICLR2024正式论文](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f53fd88a4340063ecd258c0ae9948b40-Abstract-Conference.html)：表格选择、分组、排序、聚合的执行支持事实核验。原表1同GPT3.5 TabFact直接70.45→80.20，但Binder已有79.17；包含29个手工demo和部分操作8次采样，不能称单轨迹/同预算增益。适合固定推理工具路线，但异质TabFact/QA不能自动成为同谓词批次。先统计固定比较/聚合family，原方法本身是强对照。
- STAR/VideoTool，NeurIPS2025 main：真实视频工具可作为方法证据，异质视频QA尚未形成共享业务谓词；详见发现方正式链接和表格。
- OralGPT-Plus，CVPR2026：具体牙齿识别/定位与镜像工具，但训练、评分尺度、完整数据发布有边界；不将连续judge分数写成准确率。
- Ano-NAViLa，ICCV2025：真实病理与知识词库，但训练资源/词表版本和工具冻结问题尚未闭合。
- BLINK-Twice，NeurIPS2025 Datasets and Benchmarks：单独标明track；含编辑构造对抗例，不等于真实业务输入分布。
- SemBench，PVLDB正式：输入审计发现movie Q10自然语言“逐评论打分取均值”与gold_sql读取audienceScore不等价；仅此个案，不推断全库错误率。ecommerce上LOTUS强表现保留为阴性线索，不为目标筛掉。
- CaRL-EM，ACL2026 main：正式录用确认；是学习控制器强近邻，不是一条轨迹提取。审计记录部分表格均值不一致和训练成本，不直接复用摘要宏观提升。
- TabVer属TACL期刊；ACL展示不改成ACL main。AnomalyClaw及Inducing Reasoning Primitives from Agent Traces在本轮仅作未确认录用的研究线索。

## 总体裁决与本次验证边界

优先推进航空规则计费与付款—发票匹配的输入契约/小开发实验；工业装配作为视觉备选；GDC先做语义与gold审计。这是检索后建议，不修改现行已冻结实验计划，不宣称已经构造运行新的workload。

本轮没有证实“现代LOTUS在这些任务上差、Data Agent稳定更好、单轨迹提取保持优势”三连结论。正式论文提供的是值得复核的错误机制、可用资产和局部效果证据。新实验必须钉住模型、传统LOTUS版本/模式、完整输入、可访问资源和总预算，并纳入固定程序与无轨迹Coding Agent。源题与公开答案审计属于开发暴露，不能直接用作未经查看的确认样本。
