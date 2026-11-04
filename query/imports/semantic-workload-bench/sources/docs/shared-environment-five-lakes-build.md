# 五个 Partial 的数据湖与批 Query 构造

本次按已有 Movie/DataSpace 的 `public/lake + records.json + task.json` 方式，实际构造五个冻结开发快照。主入口是 [collection.json](../data/shared-environment-five-lakes-v2/collection.json)，注册目录是 [五湖目录](../workloads/shared-environment-five.json)。每湖有一个固定语义任务 Q1，以及共用其输出的筛选 Q2、聚合 Q3、未完成清单 Q4：**5 个主任务、20 个 query 定义，不是20个独立数据集或执行家族。**

| 数据湖 | 任务记录 / 来源分组 | 共享环境 | 固定 Q1 | Q2 / Q3 的具体用途 | 状态 |
| --- | --- | --- | --- | --- | --- |
| [STARD](../workloads/stard-batch/workload-card.md) | 1543咨询 / 1543咨询ID | 55348法条 | 返回相关法条ID排序 | 指定法条关联咨询；每条法条覆盖的咨询数 | 开发检索构造 |
| [AnnoCTR](../workloads/annoctr-batch/workload-card.md) | 3348给定提及 / 112报告；湖共120报告 | 1266实体定义，其中578技术 | 指定提及→技术ID，保留子技术粒度 | 技术相关提及清单；给定提及的报告级归并 | 条件正例链接；保留源类型冲突 |
| [CodiEsp](../workloads/codiesp-batch/workload-card.md) | 1000报告 / 936论文前缀代理 | 87170操作代码、四册2018书、任务指南 | 返回P操作代码排序 | 指定编码提及报告；每代码报告数 | 原标签复现开发用途 |
| [HSCodeComp](../workloads/hscodecomp-batch/workload-card.md) | 632商品 / 632商品ID | 35950税则行、29932编码、4429页PDF | 返回一个10位HTS码 | 参数化前缀商品清单；编码分布 | 缺输入诊断用途 |
| [UDRP](../workloads/udrp-batch/workload-card.md) | 1572裁决前分析片段 / 1572案 | 152页Overview 3.0 | 回顾性预测救济/驳回 | 驳回复核清单；决定计数 | **仅供审查，泄漏与事实缺口未解决** |

以上来源分组不是已验证的独立实体划分。不跨湖混算独立N，不增加候选、Partial或Strong数量。新的审查工作可能继续改变总候选数，本构造不覆盖全局判定状态。

## 快照与查询布局

每项 `data/shared-environment-five-lakes-v2/<dataset>/` 包含：

```text
public/
  records.json          # 全量任务关系；无原gold字段
  task.json             # 默认Q1及输出契约
  queries.json          # Q1–Q4、参数、DAG、任务边界
  lake/
    catalog.jsonl       # E侧标签定义，不含记录-label关联
    texts/              # 适用时：完整报告/病例/前分析案文
    resources/          # 逐项白名单复制的原件与全文衍生物
    README.md
  manifest.json
private/
  gold.json             # record_id、原标签集合
  source-map.json       # 原ID/划分/源实体代理；不暴露给模型
  source-lock.json      # 版本、路径、SHA、角色
  gold-outside-catalog.json
  audits/              # 已有标签冲突/残余泄漏证据，适用时
  construction.json
  manifest.json
```

AnnoCTR 另有 `reports.jsonl`、`entity-definitions.jsonl`；HS 另有保留无编号父节点的 `hts-tree.jsonl` 与原JSON。CodiEsp 的原X操作证据和UDRP正式命令分别保存在private附表。public目录分离本身不是OS隔离；运行模型应沿用已有 `WorkspaceAgent` 的public-only容器，不能挂载整个仓库或源锁。

Q1返回既有执行器使用的 `record_id, status, value`。`value` 是去重、有序的字符串label列表，HS和UDRP成功时恰一个元素；集合任务允许完成的空列表。`ABSTAIN`必须为null并带非空reason。原数据没有独立UNKNOWN标注，本版不新增事实UNKNOWN类别。因输入不足无法完成时保留具体原因，不把它计成负例或删除出分母。

每个源码构造器只负责本领域输入投影。共用 [SharedLakeBuilder](../src/semantic_workload_bench/shared_lakes.py) 管理源hash校验、暂存、封存和发布；共用 [BatchQueries](../src/semantic_workload_bench/shared_queries.py) 执行Q2–Q4。所有输出目录拒绝覆盖，失败清理本轮暂存。消费源文件必须与锁一致，构造不联网、自动补源或按gold筛选E。

## 复现

从本仓库根目录执行；构造用已有锁定原件，Python标准库即可。命令的输出目录必须尚不存在。

```sh
PYTHONPATH=src python3 -m semantic_workload_bench.shared_lakes build \
  --dataset all --output data/shared-environment-five-lakes-rebuild

PYTHONPATH=src python3 artifact/shared-lakes/verify.py \
  --collection data/shared-environment-five-lakes-rebuild \
  --receipt artifact/evidence/shared-environment-five-lakes-rebuild.json

PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_shared_lakes.py' -v
```

单湖构造将 `--dataset all` 改为 `stard / annoctr / codiesp / hscodecomp / udrp`，输出目录直接成为该湖的public/private父目录。源锁位于 `environments/<dataset>/sources.lock.json`，可用 `--root` 指定含锁、query及锁定data路径的仓库根目录。

Q1由语义系统产生 `predictions.json` 后，执行普通下游查询。例如STARD按法条705建立清单和聚合：

```sh
PYTHONPATH=src python3 -m semantic_workload_bench.shared_queries \
  --public data/shared-environment-five-lakes-v2/stard/public \
  --predictions /absolute/path/to/predictions.json \
  --target 705 --output runs/stard-query-composition-v1
```

输出 `results.json` 包含Q1输入预测、Q2清单和数量、Q3按标签与来源分组的统计、Q4未完成原因与coverage，另存输入/代码hash收据。同样支持 `T1140 / bn39 / 70 / DENIED` 四湖参数；这些是固定示例参数，不按新预测或gold挑选。未完成组标记 `is_complete=false`，不会用部分技术清单冒充整报告结果。

**新增命令没有实现或运行Q1的LOTUS基线、Agent推理或质量评分器。** Q1本轮交付为真实输入和可消费任务契约；Q2–Q4为可执行确定性步骤。原任务MAP、MRR、集合F1、证据质量及派生统计不能互相替代，`queries.json`中的指标是后续评分计划。

## 构造中实际发现并保留的问题

- **AnnoCTR**：旧3348计数按 `entity_type=TECHNIQUE` 且有ATT&CK链接得到。其中11条链接实际指向software，18条技术链接在冻结KG缺失，因此29条原gold不在578技术输出catalog内。全部原输入和标签保留，未静默重标或删样。private逐条记录；后续不能把这些不可达目标直接解释成模型语义失败。3348提及实际来自112报告；其余8报告仍完整进入湖，但不构成额外链接目标。
- **CodiEsp**：保留119份没有P标签的报告，空源集合不等于无临床操作。保留侧别/词义冲突及未排序X偏移原件，不把P任务扩展为已实施治疗判断，也不修改原标签。
- **HS**：保留平台原类别、完整属性和价格；不补图片、件价、汇率或外部历史裁定。原重复question替换为固定共享任务，hs_code仅private。
- **UDRP**：沿用原public-v2的69句去除记录，仍有既有4处残余词面标记和未完成语义泄漏审查；正式命令及其规则抽取标签隔离。注册的裁决query不能作为已准备好的预测评测使用。
- **STARD**：公开问题与全库法条，隔离match_id/name与相关法规；保留原train/dev映射，仅规范化库内字面换行。源相关性标签不保证完整回答充分性。

首次尝试以纯technique URL筛选时得到3337条，数量门槛拒绝发布；修正为保留原3348并记录11条冲突。第一次完整构造v1保留为开发产物；最终v2补入AnnoCTR全部120报告并更新说明。没有覆盖旧快照。

验证收据：[validation.json](../artifact/evidence/shared-environment-five-lakes-v2/validation.json)。逐湖校验公私manifest、ID关联、公开引用、标签字段隔离，重新构造并比较公私manifest完全一致。all-ABSTAIN检查仅为接口fixture，验证未完成行不会变成负例；没有模型输出或质量分数。局部测试覆盖篡改、覆盖保护、暂存清理、源类型冲突、无标签报告、未编号税则祖先、私有裁决隔离及下游统计。

构造成功不验证C–G、资源充分性、来源许可、Agent优势、执行家族K或完整经济成本；这些保持未知。
