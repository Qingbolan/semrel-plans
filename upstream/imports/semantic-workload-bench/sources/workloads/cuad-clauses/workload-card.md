# CUAD clauses — BUILT / DEVELOPMENT PILOT

身份：CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review，NeurIPS2021；官方 https://github.com/TheAtticusProject/cuad 。510合同、41条款类别；有专家span标注和类别说明。发布目录声明数据CC BY4.0；原文件、模型权重及版本需独立锁定，已按 `environments/contracts/sources.lock.json` 获取官方数据。

先复现全部类别抽取：scan完整合同→sem_map条款类别及文本span→生成审查清单→按类别汇总。抽取结果不等于风险判断、法律效力或返修式处置。默认系统获得完整必要输入及相同类别定义。

源gold为专家类别/span。后续若只取某类复杂条款或转sem_filter，必须新建任务版本与映射核验，不能继承41类别任务的质量差距。本文不提供未核验实例ID；已有论文50合同实验与全量510合同区分。

环境候选：原全文及可取得PDF、章节/引用索引、类别说明、搜索/上下文读取/抽取结果核验工具。金标准span、答案和从gold生成的关键上下文禁止公开。PDF不是本轮已验证的视觉任务。

DocETL v3 §5.1以条款类型+span Jaccard>0.15评分；先复现该指标，再报告对更严格匹配的敏感性。按合同和模板近重复分组，不能将同合同41项当41独立文档。目标难点为漏抽取、定义/例外关联与跨段覆盖；是否当前模型仍失败待测。

本轮已从官方test 102合同按固定哈希选择8条开发pilot并构造完整公开/私有快照。source commit、文件hash和选择规则见源锁；模型配置、比较臂和停止规则见 `docs/heterogeneous-gap-pilot.md`。实际运行/评分以 `report.md` 和 `runs/cuad-gap-pilot-v1/` 收据为准。使用新的精确类别、一对一匹配scorer，与DocETL表中F1不可直接比较；尚无独立确认或单轨迹提取。

本轮终态：PILOT_SCORED_NOT_VALIDATED，未通过Agent主指标优势筛选；完整数值及任务有效性边界见根目录docs/pilot-results-2026-09-05.md。

Actual Codex CLI same-model development result: span F1@Jaccard>0.15 **0.5023**, coverage7/8 with shared initial timeout; exact-quote failures0, category relation counts unchanged from static. [Evidence and limits](../../docs/codex-cli-results-2026-09-05.md).

新增专家标注历史条件：H8旧合同/328类别案例，R8新合同，固定DAG与真实Codex各有/无H对照。[固定DAG与实测](../../docs/contract-history-results-2026-09-05.md)；任务仍为全部41类别span抽取和分类汇总。历史有局部修正，但未形成预设质量优势，不作为单轨迹成果。
