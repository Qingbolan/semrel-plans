# 第150轮：UMR英文完整文件去重与校验器兼容性

仍8/15，UMR不是新来源：第68轮已有原论文/完整仓库。本轮启动下载后通过历史卡核对到同版本，已完成的重复下载仅作字节复核，不计研究新增来源。真正新增证据是整文件候选范围、文本去重和公开校验器格式兼容性。

原论文[Building a Broad Infrastructure for Uniform Meaning Representations](https://aclanthology.org/2024.lrec-main.229.pdf)518912bytes，SHA256 `1fac9c3b0c5fdabc3f60d18450fed8ee0e1fef149093c82435d9034895163676`。完整[umr-data](https://github.com/umr4nlp/umr-data)commit ae46502fe27c7bf61978cb466dd2fc8312cb2ef8，59149442bytes7774ZIPmembersCRC通过；完整[umr-guidelines](https://github.com/umr4nlp/umr-guidelines)commit215f88e27528e0ebaa798caa2ba399b311642cb5，443430bytes26membersCRC通过。均与68相同版本；下载收据保留不覆盖历史。

新下载完整[UFAL umrtools](https://github.com/ufal/umrtools)commit4377bc4e84b6671d5ef7b0d605151a39780c8a36，163267bytes7membersCRC通过，SHA256dba36ef53cd6893fd42931213975b52bafafd0b32bc7e4982c19e265507d6626。此为公开校验工具，不冒称UMR数据作者统一最新规范。原件data/shared-environment-audit-20260908-v150；收据/审计脚本artifact/evidence/shared-environment-audit-20260908-v150。

## 比68新增的范围证据

以前的94英文文件“至少一个无type块”不能作为94完整人工文档。本轮要求文件所有块都无type：英文仅14文件468块；中文48文件976块；Arapaho5/406，Kukama2/105，Latin1/50，Navajo5/506，Portuguese1/96，Sanapana6/602；Czech0。无type仅是元数据筛选，不证明人工独立审核。

14英文文件的Words行序列原字节不同；逐行折叠空白后仅9组、259块。5对重复：0004/0580（141块）、0005/0007（29）、0006/0001（28）、0002/0231（2）、0003/0008（9）。最后一组2句为Lindsay午餐和下雨不浇花教学例，不能当两个真实案。其余0576/0577/0578/0579为短新闻片段，源实体独立性/当前gold人工来源仍需核验；不在此宣称8个独立真实案例已闭合。只比Words序列，不证明整图/对齐/注释版本相同。

共享guidelines.md第68轮已实际测得48221空白分词，标题UMR0.9/2022而当前数据3.0。长规范确实存在，但不能覆盖所有3.0人工/确定性/LLM转换差异。英文README有3226代词决策由LLM辅助，未逐块指明独立人工复核；不可把整个英文31534句作为人工gold。

校验器probe：系统Python缺regex；改用已有.venv依赖成功运行未改校验器。level2对0001返回452个Format错误，示例为trailing-whitespace和too-few-blocks。代码期待另一种分块结构，未完成3.0格式适配，因此这个结果不等于452个语义错误。未为通过检查删除/改写gold，不将该validator称已验证当前源。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold边界 |
| --- | --- | --- | --- | --- |
| 将新闻转换成事件、论元、时序和确信程度图，建立可查询事件索引 | 共享UMR长规范48221词但版本适配待核 | 完整新闻Words及允许的语言资源 | 图标注需private；句子图若给定须对所有方法明确同给 | 首例landslide/die/fear肯定，miss为partial-affirmative；不是人类确认每个失踪者死亡 |
| 给定句子图构造跨句模态索引 | 显式annotation-given句子图，不能隐含读取 | 仅模态相关规范子集 | 上下文包括消息来源与报道状态 | 只做模态不自动需要48K全规范；长期目标不能靠挂整本手册人为膨胀E |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `files.filter(all_blocks_unflagged).dedup(normalized_words)` | 英文584文件→14候选文件/468块→9文本组/259块 | 不能从无标记推出人工gold；5重复组不独立计数 |
| `documents.sem_map(to_umr,E).project(event_modal).filter(partial_affirmative)` | 首新闻miss为partial-affirmative目标 | 未执行模型/评分；图生成适用全部规范，单模态则须重测所需子集 |
| `validate_umr(source)` | 0001实际level2返回452Format错误 | 公开工具格式不兼容；不是模型失败、语义标注错或验证成功 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 目标miss为partial-affirmative，输出未测 | 同输入完整新闻，固定规范检索+图构造+引用检查；允许整批缓存 | 同目标，无优势结论 | ==区分fear事件与其不确定内容，核对模态范围和信息来源==→生成模态边 | `SemanticGraphBuilder(E_version)->nodes,edges,status`加`ModalIndex`；源框架/词汇资源依赖明确 |
| 若仅给定句子图做模态，相同目标 | 同句子图、相同工具，不能拿Agent额外gold图 | 同目标 | ==核对已给上游图范围，读取对应模态子规范==→生成下游关系 | 限定子任务的operator必须承认只需规范子集，不能全书成本论证 |

不将多语言各算一个数据湖，不将合成教学例、转换图或未发布占位当真实人工案例。此路线本轮不升级：英文完整真实人工批次不足，其他语言未完成来源/规范/许可绑定。下一轮不重复当前仓库下载，优先新的可下载长手册数据，或补已知候选的确切缺口。当前所有进程结束；无模型/种子/prompt/实验预算/测试套件/快照/正式评分/commit。一次源码校验器兼容性probe是工程诊断。语言许可沿用68分别核对，不统一外推。
