# RegBench：合成场景路线Reject

当前未入场，不增加计数。[项目仓库](https://github.com/regbench/regbench)与[官网源码](https://github.com/regbench/regbench.github.io)已完整clone，commit/数量/字节见收据；没有执行任何作者代码。官网页面抓取失败后读取官网源码，`app/page.tsx:82`论文链接为href=#、PLACEHOLDER: Read the Paper；CITATION作者Anonymous。不能据README的NeurIPS2026字样声称已发表或已读原论文。

本地数据dnv499、basel281、pilot47，共827。字段包括question_text、required_facts、source_section、scenario_parameters、annotator_grounding、tested_pattern、leak_check。真实工作流与生成来源尚待脚本核验，不能把scenario直接叫真实案件。

| Query | DNV首行F500_0001 | Basel首行B_T0_0150 |
|---|---|---|
| 原问题 | 12t轴载、两载荷面、单轮、0.35g，计算胎压及海上甲板设计压力并判断简化方法 | 380亿美元银行控股公司，判断资本要求适用性及计算种类 |
| 发布required_facts | 约464.8kN/m²及627.5kN/m²等 | 适用性和资本类别，完整字段见收据 |
| 任务关系 | 一条多输出设计计算题 | 另一类法规适用题；不能与前列合并成同一q |

数据既有数值输入也有交叉引用链，但source_section/chain/annotator_grounding为评测或构造元数据，不能不经协议放进系统输入。README称DNV正文不随包重分发，需要注册下载；Basel正文也需提供镜像。现有论文缺失、E镜像未取得、C0/20。

下一步按原顺序审查生成脚本、审核独立性和原论文可获取性，完成边界判定再转下个候选。不能仅凭深层chain宣布存在1≪K≪N：固定图遍历+语义事实计算也可以走不同节点。四路方法质量与ρ/K均未知。

[下载及完整首行收据](../artifact/evidence/shared-environment-strict-regbench/source.json)。该文件包含gold，只供构造审查，不挂载模型公开环境。

## 构造与基线源码核验后的判定

**Reject：F真实案件不满足，原论文与完整E仍缺。** 历史待审段保留，以下为当前结论。`generate_500_v6.py:273–315`读取采样链的起点、终点及中间规则，再调用LLM生成问题；`generate_basel_v7.py`提示模型编写具体银行场景，同时输出required_facts、correct及expected_derivation。因此模型参与构造输入和参考，不是独立自然案件裁决。

`docs/CALIBRATION.md`区分fact-level-blind审核与显示v5d标记的anchored审核；不得否认存在盲审，也不得把部分审核扩成827条全量模型无关gold。374审查项是作者报告的审核切片合计，未独立重算，不能当本轮C20。

**README/代码冲突：** README将run_chainrag_baseline.py称作oracle-chain，但当前脚本上下文函数使用question_text做BM25检索，然后从检索文本正则追踪一跳引用；gold required_facts在judge函数中使用。不能据README把这段上下文生成代码叫oracle。是否对应论文实际运行仍缺论文及收据，未执行此脚本。

| A固定任务 | B共享E | C20 | D静态不足 | E/K | F真实批 | G独立性/泄漏 | H获取 |
|---|---|---|---|---|---|---|---|
| 多种计算/适用问题，未抽出数百同q | 两法规域正文镜像未取得 | 0完整 | 未建立；已有固定一跳检索代码，未对齐比较 | 深度tier非执行家族K | 合成场景，失败 | 模型生成参考+分层人审；chain/gold不得进answerer | 两完整repo827行已下，论文占位、正文缺 |

| 类Python DAG | 普通/语义边界 |
|---|---|
| `index=BM25(E.sections)` | E-only普通预处理 |
| `anchors=retrieve(index,x.question)` | 固定检索 |
| `refs=follow_regex(anchors,max_hops=1)` | 固定结构导航，读取不同节点也可同程序 |
| `answer=sem_map(apply_rules,x,anchors+refs)` | 核心语义判断及数值事实解释 |
| `check=grade(answer,private.required_facts)` | 私有评价，不能反向驱动预测 |

| 方法 | 首条DNV数值题预期 | 过程 | operator候选 |
|---|---|---|---|
| LOTUS仅题目 | 源参考464.8/627.5，不保证无E可得 | 单次答题 | 无充分依据 |
| LOTUS完整E及固定检索 | 未实测；参考数值为目标 | 检索公式/默认值→语义变量映射→普通计算 | `retrieve→bind_variables→calculate` |
| 逐条Agent | 同一目标，未证明更准 | ==查单轮、胎压缺省与海上公式==→变量映射→计算 | 同固定模板可实现 |
| 批Agent | 可共享公式索引，额外收益未知 | ==建立公式/适用条件索引==→批量语义路由→计算 | ρE索引、ρP抽取计算、ρG公式家族假说、ρR个案；比例/K未知 |

十问边界：q不统一、E版本正文缺、x合成且数量见前表、y构造有人机混合、C0、D未证、K未知、共享/独有步骤如上；字段隔离未建快照，不足状态未冻结；尚不能区别于固定多跳RAG与规则求值。需要原论文不意味着在已知硬失败后继续伪造20个真实案例；本来源保留阴性结论，不计Strong。
