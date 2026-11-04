# 增量173：Thai Discourse Treebank 原件与共享规范

新来源待核验，仍9/15。先查LST20发现作者加载说明要求登录取得完整语料，没有绕过登录或取得该全包。转向在LST20新闻上新增篇章关系人工标注的Thai Discourse Treebank（TDTB）：作者公开了原文token和标注。两者源文章重叠，不会作为两个独立湖计算。

## 已下载并读取

- [TDTB原论文](https://aclanthology.org/2024.tacl-1.34.pdf)：4950793 bytes，SHA256 `8d4bad45ff26b66eda701b7f115ee9de8480df509b7676021c64dbe597741ac7`。
- [完整作者仓库](https://github.com/nlp-chula/thai-discourse-treebank)：commit `226b2f898c7044345fcabec7d449f4d7da29b5d1`，583个tracked文件，全部取得并哈希登记。
- [LST20原报告/指南](https://arxiv.org/pdf/2008.05055)：28页，786427 bytes，SHA256 `7dfa19879ee0d0aa89a60e6eb56fd302d885ebf38358a2bca9ef677f8c1f5f5c`。它定义基础标注，不能自动当TDTB篇章语义规范。
- [官方PDTB3手册](https://catalog.ldc.upenn.edu/docs/LDC2019T05/PDTB3-Annotation-Manual.pdf)：81页、29840个空白分词，507859 bytes，SHA256 `15f12df435ae03670f11fd3f2bf547cd603038111810a5e0376f02c708e17756`。

原件在`data/shared-environment-audit-20260908-v173/`；逐文件下载哈希及统计在`artifact/evidence/shared-environment-audit-20260908-v173/{downloads.json,audit.json}`。首次git ls-files按行解析碰到macOS `Icon\r`的quoted路径导致哈希脚本失败，改用`git ls-files -z`后全部成功，无源文件改写。

TDTB论文和data/th-tdtb/README明确采用PDTB3意义层级；论文§3–4描述Thai语言特性和新增Expansion.GenExpansion。81页手册需要与这些改动共同构成E，不能只给英文手册就声称规则完整。论文称逐连接词详细说明随库提供，但当前583文件只有TSV、CoNLL-U、rels、tok、txt、README及macOS文件，没有独立指南PDF/连接词说明文件；其是否已包含于某数据文件及完整规则闭包待核验。

## 原生规模及已发现边界

`without_args`实际384个TSV、464171个token行、18374个非N意义标签行；`with_args`180个TSV、298347个token行、11753个非N意义标签行。两个目录交集180个文档ID，并集384。根README说without_args为204篇，实际目录含全384；应理解为只有204篇缺完整argument层，不能把180+384相加。

with_args均9列，without_args均8列。非N行数量当前按token数统计，尚未合并多token/discontinuous connective。派生DISRPT README报告10868关系，与11753非N行不是同一单位，待核验转换。README说明依存边为自动解析结果，不是人工gold。

源新闻分词等基础标注和篇章标注应按任务分开：given-token任务可显式给token；如果预测论元边界则不能公开arg1/arg2字段。语义分类任务如给定人工连接词/论元要明示annotation-given。原句法列也不能全部递归塞入模型上下文。仓库没有独立LICENSE文件，本轮未证实语料许可；论文CC-BY4.0不能扩展成新闻原文许可。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 给定连接词位置，逐篇输出篇章关系意义及论元 | 384篇真实新闻token；其中180篇有论元标注 | 81页PDTB3手册+TDTB论文的Thai修改；详细规则闭包待核验 | 28页LST20基础标注规范；可选显式给定分句信息 | 18374非N标签行；180篇中另有arg1/arg2 token映射 |
| 具体T00784的token3459“ก็”是哪种关系？ | 原句内token3448–3457描述听者不理解而发生冲突；token3460“อันตราย”（危险）；中文为辅助释义，原Thai为输入依据 | Cause.Result及Arg1/Arg2方向约定 | token索引 | `Contingency.Cause.Result`；Arg1=3448…3457，Arg2=3460，来自原始最后一列 |
| 形成新闻因果关系清单及每篇数量 | 预测的意义和论元表 | 固定选择Cause关系并保留方向 | doc ID | gold派生清单，未全量构造；不是独立因果真实性标注 |

| 类python的DAG | 具体数值 / 输出 | 边界 |
| --- | --- | --- |
| `scan(news).join(given_connectives).sem_map(sense,E).project(doc,token,sense)` | 384源文档；18374非N行在合并连接词之前 | source token粒度与关系实例粒度不能混用 |
| `selected_docs.sem_map(argument_spans,E).join(senses)` | 180篇；例3459→Arg1[3448..3457],Arg2[3460] | 两个语义步骤有原生gold；统一实例结构尚待验证 |
| `relations.filter(is_Cause).project(arg1,arg2).groupby(doc).count()` | 示例应保留1条Cause.Result | 方向决定清单语义；模型和全量派生评分未执行 |

以下为未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标为Cause.Result及对应论元；实际未知 | sem_map读Thai上下文和同一规范；允许固定章节检索 | 相同正确目标，无优势预设 | ==查连接词的语义歧义、Cause方向及论元绑定规则==→输出 | `ConnectiveContext → SenseLabeler → ArgumentBinder → RelationRow` |
| 对该例产生有方向的因果关系行 | 按冻结层级与方向规则投影 | 同一关系行 | ==开发时确认源字段与目标实例单位==→固定聚合 | 检索缓存+结构化论元/意义接口；目录映射不是学到的语义操作 |
| E-only编译可能与轨迹提取相当 | 从完整规范直接生成检索计划/类别约束，再同资源执行 | 一次真实轨迹能否帮助尚待测 | ==记录实际读取规则及可观察中间输出==→提取→冻结 | 当前只列预期结构，未生成或运行学得operator |

下一步：解析连接词链接和论元字段，核验180篇与派生10868关系的映射，补完整Thai规则及许可证据，再决定是否登记开发可行。无LLM/训练/模型prompt实验/种子/token预算/推理并发缓存、安装、测试套件、正式快照或commit；下载进程均exit0。
