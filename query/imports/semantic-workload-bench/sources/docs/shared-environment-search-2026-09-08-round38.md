# 第三十八增量：SemiHS-Bench半导体产品归类

**仍1/10；来源已下载但可行性尚未证实。** 本轮发现有真实产品、专家标签和共享裁定库的SemiHS-Bench。完整仓库取得，原论文普通下载403，完整冻结HS2022规范未取得。没有把“原论文尚未下载”写成已满足用户要求。

| 来源 | 本次核验 |
|---|---|
| [作者仓库](https://github.com/cti-iel/SemiHS-Bench) | commit `8f2c4074a9f124d6a294d04a534777f437c9e487`；141blob SHA1验证、ZIP CRC通过；包括完整数据和构造代码，未执行作者程序 |
| [作者声明对应论文DOI](https://doi.org/10.1145/3799682.3840202) | ACM PDF下载403，未取得；接受状态与出处来自README/CITATION，不冒充独立核验 |
| train/eval | 实读900/900条；73个HS6分类；多种输入tier不是不同案例或不同数据湖 |
| reference_corpus | 889条：CROSS400、EBTI389、日本海关100；属于共享历史裁定，不自动等同于完整规范 |
| 来源与标签 | eval为catalog582/BOL318；作者声明领域专家验证，原始catalog/提单全档不随库提供，本次未逐案对上游核对 |

先查的另一个HS-BENCH（Right Code, Wrong Reasons）OpenReview PDF也403，仓库未定位，不与本数据集混淆。未下载搜索结果中标为私有的HF镜像；使用作者公开GitHub发布源。GitHub数据声明CC BY-SA4.0，代码MIT，上游裁定及原始材料权利须分别看LICENSE-DATA。

本次审计eval的tier2_classifiable：yes582、partial172、no146；confidence为high525、medium372、low3。不能把稀疏到不可识别产品的输入失败当作LOTUS能力缺陷。train/eval存在4种完全一致tier2_minimal对象；tier1文本跨split完全相同0条。这是具体重叠证据，尚非完整实体/近重复审计。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在冻结HS2022规则下，将半导体供应链产品归入HS6 | 73行taxonomy及HS6描述已取得；完整HS2022章注/部注/解释规则尚未构造 | 900eval产品，catalog582/BOL318；900train可作开发但需实体隔离 | 889条跨法域历史参考裁定；不能按当前gold的reference_ruling_ids预选后假装自主检索 | hs6_label、justification_text、boundary_note、confidence、reference IDs、candidate金标位置等全部私有 |
| v2.0.eval.0001，混合气体X50S：约4%氢、其余氮 | 混合物归类所需适用章注/规则待核验，不能只看含有氢就套纯氢条目 | 原始BOL字段写MIXTURE OF GASES；tier1为专家复核的扩展用途描述，非原始提单全文 | 库中给定3条EBTI参考ID是标注侧关联，公开系统应获得全库而非答案选中的三条 | 发布gold280410、confidence high、tier2 partial；本次不独立认可或修改该金标。bol_metadata.declared_hs也不能泄露给系统 |

| 类python的DAG | 具体数值 | 当前边界 |
|---|---|---|
| `scan(eval).allowlist(public_product_fields)` | 900条 | 未构造正式公开快照；整条JSON不能给模型 |
| `resolve_product(tier1_or_tier2, public_catalog)` | 582yes/172partial/146no是作者tier2标记 | 两种输入条件分别报告，不能混合计优势 |
| `retrieve(all_reference_rulings).apply(frozen_hs_rules)` | 889条、3种来源；完整共享规范未取得 | 全库固定检索与Agent都可用；当前评测同源裁定重叠仍需审计 |
| `sem_map(hs6).sem_filter(hs6 == target).project(id).count()` | 73分类；选中数未测 | 原任务是sem_map分类，目标类别筛选为下游投影，不能暗改gold |
| `group_by_source_entity().split()` | tier2完全相同跨split4种，tier1相同0 | 字符串去重不证明实体独立 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例发布参考280410，实际未运行且混合气规则未独立核验；证据不足时应ABSTAIN | 固定识别成分/用途→检索规则和全裁定库→比较候选条目与排除条件→输出代码及证据，可用共享缓存 | 同一参考与证据条件，不能预言正确率或优势 | ==核验产品是混合气还是纯元素==→==查混合物适用规则及历史裁定是否可比==→==检查法域/版本与用途差异==→有据给代码，否则ABSTAIN | `HS6Operator(E_version, product_identity, composition, rule_path, precedent_retrieval, exclusions, sufficiency, abstain)`；比较固定检索、仅E编译、Coding Agent、整批Agent与单轨迹产物，不用私有boundary_note代替学习 |

本轮没有模型实验或真实提取算子。保留这条后续核验路线：它具有所需批量与公开标签，但还缺论文、完整冻结规范、源实体隔离和关键混合物例的独立依据。原始资产data/shared-environment-audit-20260908-v38；脚本、来源哈希、下载失败收据和实测统计artifact/evidence/shared-environment-audit-20260908-v38。
