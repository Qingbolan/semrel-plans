# 第三十五增量：HateModerate政策审核来源核验

**累计1/10；HateModerate不计入严格合格清单。** 本轮已取得原论文和完整作者仓库。其非仇恨数据全部来自DynaHate、GPT及人工编写；主要上游DynaHate本身是标注员动态构造的对抗数据。删除GPT行不能得到真实平台内容批次。仓库政策描述合计837词，也没有证实一个长共享政策环境是逐条判断的必要输入。

## 原始材料及实测

| 材料 | 本次核验 |
|---|---|
| [HateModerate原论文](https://aclanthology.org/2024.findings-naacl.172/) | PDF20页、953,671 bytes；已下载，SHA256见收据 |
| [完整作者仓库](https://github.com/stevens-textmining/HateModerate) | commit `3acc336e0e690dd4d7d9918fa6e885f67c48ddae`；ZIP16,214,501 bytes，59个Git blob全部SHA1一致、ZIP CRC通过 |
| `postprocess/all_examples_hate.csv` | 4,796行，4,535种句子 |
| `postprocess/all_examples_nonhate.csv` | 2,906行，2,262种句子；两个人工valid字段均1有2,286行，这些字段表示所指定非仇恨类别是否匹配，不是独立真实平台审核结果 |
| `original/cate2guidelines.csv` | 41条；description合计837词；每条最短6、中位19、最长50词 |
| [DynaHate上游原研究](https://aclanthology.org/2021.acl-long.132/) | 训练过的标注员分轮生成和标记内容，并含扰动；不能等同于自然用户帖子。上游原论文PDF也已下载，330,480 bytes，SHA256见upstream-download.json；未下载上游仓库，不称其为新的完整复现。上游仅用于来源追踪，不另计一个数据湖 |

原论文写7,704条、非仇恨2,908条；冻结仓库实读总计7,702条、非仇恨2,906条。独特非仇恨句子也相差2。论文来源统计DynaHate5,174/GPT1,385，仓库合计5,165/1,392，存在版本差异；尚未解释，不填补虚构行。CSV实际为制表符分隔，审计脚本已按TSV解析。

| 来源 | hateful行 | nonhate行 |
|---|---:|---:|
| DynaHate | 2,850 | 2,315 |
| GPT | 813 | 579 |
| manual | 258 | 12 |
| HateCheck | 457 | 0 |
| 其他来源合计 | 418 | 0 |

其他来源含真实社交语料候选，但本轮未逐项建立原帖、完整上下文、政策版本和独立决策的对应链。不能把它们自动称为真实、长E依赖的完整二分类工作负载。仓库没有明确许可文件的情况下，下载与研究审计不自动获得再发布授权；本轮未外发原数据。

## 三表：具体开发例及未运行的方法预期

以下是排除依据的审计示例，不是推荐的合格数据湖。句子来源与隐藏类别说明必须分开；不向被测系统暴露`guideline`、`type_name`、votes或valid字段。人工生成的数据可以用于控制实验，但不满足本次真实案例要求。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按同一套Facebook仇恨内容规则判断每条内容是否违规 | 41条短政策描述，共837词；不是已核验的长政策手册 | 7,702个句子—政策条目，句子可能重复，不等于7,702独立真实帖子 | 没有完整对话线程、代词指代对象及对应历史政策版本 | hateful文件及标注投票、nonhate文件和类别验证；不是平台执法记录 |
| nonhate example_id=1：`they are a cancer to the world!` | 需要判断攻击对象是否是受保护群体，再检查疾病比喻相关条件 | 来源DynaHate，原索引7498；这是构造样本 | 句子中的“they”没有在该句内明确指代；不能用私有类别补公开上下文 | 发布为nonhate；隐藏类别是针对非受保护实体的贬损，两个人工valid及GPT valid均1。仅凭孤立句子不能保证该标签可恢复 |

| 类python的DAG | 具体数值 | 证据与执行边界 |
|---|---|---|
| `scan(hate, nonhate).separate_private_annotations()` | 4,796+2,906=7,702行 | 仅完成源读取与统计，未发布模型快照 |
| `group_by_source_entity().split()` | hateful4,535种句子、nonhate2,262种句子 | 两个集合的去重数不能简单相加作为独立实体总数；还需扰动家族隔离 |
| `bind_policy(E).resolve_target(public_context)` | E描述837词；示例1缺明确指代 | 如果必要证据缺失，返回ABSTAIN，不读取隐藏type_name猜答案 |
| `sem_filter(violates_policy).project(id).count()` | 模型输出、选中数均未测 | 不以发布标签直接充执行结果 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例1的发布参考为nonhate；孤立输入不足时应ABSTAIN。未运行，不能预言实际输出 | 固定提取攻击对象与受保护属性，读取同一规则，应用比喻/例外条件；缺上下文则中止，可共享规则缓存 | 同样不应从缺失指代强推nonhate；没有证据保证Agent优于固定过程 | ==检查指代能否从公开句子/线程恢复==→==检索受保护对象定义与相关例外==→仅在上下文充分时判定，否则ABSTAIN；不能探索私有类别补答案 | `ModerationOperator(policy_version, resolve_target, protected_group, attack_type, exceptions, evidence_sufficiency, abstain)`；需要比较仅E编译、固定检索、Coding Agent及整批Agent，不能假定轨迹提取有优势 |

本轮未执行作者代码或任何模型；表中过程是待测设计，没有准确率、tokens或摊销收益结果。这个案例揭示的实际问题是公开输入与人工构造意图不一致，而非静态LOTUS能力不足。原资产位于`data/shared-environment-audit-20260908-v35/`，脚本、来源收据与统计位于`artifact/evidence/shared-environment-audit-20260908-v35/`。
