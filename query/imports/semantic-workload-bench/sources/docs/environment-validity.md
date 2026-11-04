# Environment construction validity

This document is a research evidence ledger, not a claim that a packaged environment is scientifically valid.

| Dimension | Required evidence | Current PCB state |
|---|---|---|
| Task grounding | Source workflow, record unit, output use and added assumptions | Paired PCB defect inspection; downstream count is benchmark-defined; no repair claim |
| Source authenticity | Original commit, per-file URL/hash, license and transformation | Locked 24 pairs and labels; local imported bytes verified by builder |
| Construction correctness | Selection recipe, source-to-record map, no silent exclusions, immutable public assets | Deterministic inherited pilot selection; opaque IDs; labels mapped only in private |
| Input adequacy | Default can inspect tested image and return same predicate | Interface defined; no default VLM accuracy measured |
| Resource benefit | Paired tested-only vs tested+template vs tools, same model/records | NOT MEASURED |
| Gold validity | Existing independent labels plus mapping/ambiguity review | Class5 presence from original bbox labels; source annotations not independently reannotated |
| Leakage | Filename, gold crop, model training, reference and entity overlap audit | Runtime excludes label paths; group IDs retained privately; historical pilot exposure known |
| Downstream relevance | Intermediate gold replacement; list/count error change | Count scoring available; causal experiment NOT RUN |
| Representativeness | Population, sampling and workload distribution | 24 hash-selected test rows; synthetic-added defects; insufficient for production prevalence |
| Robustness | Alternate demos, board groups, resource counts and image conditions | NOT RUN |
| Reproducibility | Rebuild sources, validate hashes, run/score and regenerate figures | CLI and artifact script supplied; no independent-team reproduction yet |

## Resource-role map

Tested image: task input. Aligned clean template: legitimate assisting evidence. Class definition: intended target semantics. Geometric comparison code: an imperfect fixed baseline/tool implementation. Current evaluation bbox labels: evaluator-only truth. Approved, disjoint historical labels can be explicit environment supervision under the [history protocol](historical-experience.md). Adding a resource must name the error it can correct; an enlarged folder is not evidence of a better data lake.

The template baseline uses engineered pixel parameters, not manufacturing tolerances. Measurements should separately vary templates, alignment tools, domain descriptions and perception models. Missing resources or poor preprocessing must be classified as such, not attributed to static semantic expressiveness.

## Planned validity experiments

V1 same VLM with tested image only / paired template / paired template plus source-backed class explanation. V2 frozen geometric baseline versus that VLM; exposes an alternative mechanism, not a fair same-model dynamic claim. V3 all systems share tools and templates; compare fixed procedure, Coding Agent and batch-aware Agent. V4 replace step predictions with gold before fixed project/count to quantify error propagation. V5 vary batch size independently from lake size and label prevalence. V6 freeze new group-disjoint confirmation data before model development.

Save per-record paired outputs, prompt/model/tool versions, label distribution, abstentions, failure classes and confidence intervals. Reject a claimed environment benefit when it relies on test-label-derived resources. Negative findings remain publishable observations, not reasons to silently change the task.

## New candidate status (2026-09-05)

BioDEX and CUAD have published LOTUS comparison evidence. Both now have eight-record development snapshots and recorded common-model pilot runners; actual run/scoring outcomes are in report.md. Construction and execution do not establish a quality gap or resource benefit. Their resource cards list unverified acquisition, terminology/definition, gold and split obligations. Primary validity gate now includes reproducible static quality shortfall, same-environment Agent improvement and downstream consequences before extraction evaluation. PCB's successful fixed control does not pass this gate. See [candidate plan](accuracy-gap-candidates.md).

## Imported PCB observation and history extension (2026-09-05)

The table above describes the original local 24-record control. A separate 100-record experiment from Awesome-Sem-Filter-Bench is now preserved as [imported receipts](../artifact/evidence/pcb-native-lotus-20260905/provenance.json), not rerun here: native LOTUS image-only89%, paired91%, same-model tool Agent92%; 9 corrections/8 regressions, paired p=1.0; fixed program100%. Record-disjoint from the earlier79, but not board-group-disjoint, with artificial added defects and no production-disposition gold. It does not validate the Agent-improvement gate.

Two [historical correction cases](../environments/pcb/history/history-cases.json) now record inputs by source/hash, official human labels, system outputs and researcher-derived candidate lessons. These are post-hoc, both negative, development-side resources. Histories have not been mounted or experimentally compared. The known179 source IDs are excluded from future independent confirmation via an explicit exposure registry; entity/near-duplicate audits remain required. History curation provenance, temporal applicability, fixed-example/retrieval controls and new-batch quality are the next validity obligations, not completed evidence.

## Local pilot evidence boundary

Frozen designs: [CUAD](heterogeneous-gap-pilot.md), [BioDEX](biodex-gap-pilot.md); [operational notes](pilot-execution-notes.md). Public input completeness and byte integrity were checked; lexical/source-ID duplicate checks were performed. Resource causality, budget-matched superiority, proxy snapshot identity, annotation completeness and independent confirmation remain unestablished. Scoring is separate from model execution and does not set VALIDATED.

## Pathology development import

Current [pathology pilot](pathology-batch-pilot.md): 1,000 historical test patches and 32 train references checked against locked NPZ pixels and labels; exact pixel overlap with registered 10,000 training examples is zero. Patient isolation remains unverified. Fixed bootstrap CNN rerun accuracy0.457/macro-F1 0.3721, coverage1.0. Reference benefit, same-resource Agent improvement and clinical validity are untested. Original Vision checkout contains no recovered medical checkpoint.

本轮结果：[CUAD/BioDEX pilot](pilot-results-2026-09-05.md)均未通过主指标优势筛选。BioDEX全部gold术语在目录中，但部分gold在初始候选中仍被错误归一化/排除，且事件范围与提示存在对齐风险。资源存在、引用合法与任务正确性须分别验证；不得据低分认定静态能力边界。

实际Codex CLI同模型整批验证已完成：[结果](codex-cli-results-2026-09-05.md)。公开文件只读/私有路径缺失/无网络Docker边界经实测，模型请求37次均完成；主指标未改善，引用合法性改善不建立资源因果收益。两个生成脚本含当前实例修正，未作为冻结算子迁移。

新增[CUAD标注历史实验](contract-history-results-2026-09-05.md)已完成：H/R记录与发行主体代理隔离、近重复检查、public-only容器与五臂同源输入校验；固定请求除H数据外逐字相同。历史少量局部改正被退步抵消，未显示明显资源收益或Agent使用优势；仍非完整实体/训练独立确认。


## DataSpace fund workspace development control

[Protocol](dataspace-amortization-pilot.md): complete upstream archive SHA256 verified; task184 workspace imports19files/40,624,940bytes with private official reference. Entity transformation keeps SQLite/CSV/JSON, isolates manager groups and contains1/16/300records. Official374positive tuples match an independent public SQL audit. One trace-derived program executes299/300correct plus1ABSTAIN; handwritten fixedSQL300/300. Task-relevant resources are SQLite-only; no multimodal perception, resource ablation, training/near-duplicate independence or research-quality gate has been established.

## Semantic-query composition development control (2026-09-08)

[Protocol](semantic-query-composition-pilot.md): SemBench Movie Q2/Q3/Q4/Q8 share one review-sentiment relation. Source2,000 rows collapse135 exact duplicates to1,865 unique reviews; lake also includes116 movie rows. A frozen36-review/3-movie subset is exposed only as public text/IDs, with source sentiment/rating fields private. A second build produces identical public manifest. Native Codex runs in the verified public-only offline Docker container; the user-supplied Chat-only endpoint requires an explicit LiteLLM wire bridge. Static LOTUS32/36 versus Agent24/36,28/36,23/36 by source labels. No resource ablation, independent gold audit, entity-disjoint confirmation or frozen operator extraction. Mixed/negative-sounding snippets with positive source labels limit interpretation of classification disagreements. This is a pipeline/trace control and does not support an Agent or environmental advantage.


## 五个 Partial 的开发数据湖构造（2026-09-15）

[五湖交付](shared-environment-five-lakes-build.md)：STARD1543、AnnoCTR3348给定提及（112目标报告，湖120报告）、CodiEsp1000、HS632、UDRP1572。新增精确源锁、公私隔离、统一query契约及确定性下游执行。AnnoCTR11条源类型冲突加18条缺KG使29条gold不在技术输出目录；全部保留。UDRP残余泄漏/外部事实、CodiEsp标签冲突、HS缺输入不因封存消失。没有新确认划分、语义推理、质量评分或科学有效性升级；不改全局候选计数。
