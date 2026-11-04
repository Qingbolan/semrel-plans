# Semantic Workload Bench

Evaluating semantic data processing and single-trace operator reuse in heterogeneous data environments.

研究目标：默认语义步骤能够完成任务；环境中的工具、文档和知识可能改善关键步骤及下游结果。评测从一次 Agent 示范中提取算子后，在独立批次上的质量与完整摊销成本。

**当前状态：DeepPCB控制底座 + CUAD/BioDEX各8条真实开发pilot + 已实现的静态、固定复核和工具Agent比较。结果以[研究账本](report.md)和pilot收据为准；新增DataSpace单轨迹自动提取原型已在300条后续基金记录上执行；尚无独立确认或Agent质量优势。**

Start here: [spec](BENCHMARK_SPEC.md), [research context](docs/research-context.md), [environment validity](docs/environment-validity.md), [evaluation](docs/evaluation-protocol.md), [artifact guide](docs/artifact-guide.md), [results/limitations](report.md).

新增研究资源：[历史纠错经验协议](docs/historical-experience.md)与[两个真实PCB历史案例](environments/pcb/history/history-cases.json)。历史人工标注允许作为显式资源，当前测试答案仍私有；案例目前只登记在开发侧，尚未接入运行器或验证收益。

另已导入旧仓库100条PCB[实验收据](artifact/evidence/pcb-native-lotus-20260905/provenance.json)：原生LOTUS带模板91%，同模型工具Agent92%，未形成可靠改善，固定程序100%。这是既有结果同步，不是本仓库复跑，也不使PCB成为Agent优势正例。

## Current research priority

先复现传统LOTUS静态语义步骤的质量差距，再验证同环境Agent改善，最后研究单次轨迹提取。优先[BioDEX](workloads/biodex-reactions/workload-card.md)、[CUAD](workloads/cuad-clauses/workload-card.md)；[证据、局限和进入实验门槛](docs/accuracy-gap-candidates.md)。两者已完成共同模型的各8条开发比较，均未通过Agent主指标优势筛选；BioDEX还需核对提示口径与gold范围。[本轮结果](docs/pilot-results-2026-09-05.md)保留完整阴性观察。[pilot复现入口](docs/pilot-artifact-guide.md)、[CUAD设计](docs/heterogeneous-gap-pilot.md)、[BioDEX设计](docs/biodex-gap-pilot.md)说明实际对照与局限。PCB继续作为工程控制，以下命令只适用于PCB。

## Quick start

Python 3.11+; run from repository root. Core construction/scoring uses only the standard library.

```sh
export PYTHONPATH="$PWD/src"
python -m semantic_workload_bench.cli build --lock environments/pcb/sources.lock.json --output data/pcb-v1
python -m semantic_workload_bench.cli verify --snapshot data/pcb-v1/public
python -m semantic_workload_bench.cli run --public data/pcb-v1/public --system always-false --output runs/sanity-v1
python -m semantic_workload_bench.cli score --private data/pcb-v1/private --run runs/sanity-v1
python -m unittest discover -s tests -v
```

Build downloads pinned, hash-checked files. An optional `--source /path/to/existing/deeppcb` reuses matching local files. No dependency on the previous research repository is required. Existing outputs are never overwritten by build/run.

For the migrated fixed geometric baseline install `pip install -e '.[vision]'`, then use `--system fixed-geometry` with a new output path. This program is not our learned operator. The constant negative baseline is a sanity control, not a competitive static semantic operator.

Data/weights and run outputs are ignored by Git. Source lock is evaluator-side: never expose its label URLs to a model. Runtime receives only public/. Filesystem separation is not a security sandbox.

## Scope

The PCB task filters class-5 spurious copper and counts selected boards. Source labels contain six defect types. No repair, severity or factory compliance labels are invented. Template images are legitimate resources; bbox annotations are private gold. Existing 24 rows are exploratory and cannot serve as fresh confirmation data.

Historical documents under docs/history are snapshots from the previous repository; relative output paths there refer to that repository. They are context, not current runtime configuration. New repository guidance takes precedence for new experiments.

No new software license is asserted in this bootstrap. Upstream image/annotation and copied-code rights need review before external release; see environments/pcb/resource-card.md. This is a local artifact, not a published or VLDB-certified benchmark.

## Local bootstrap validation

Remote pinned reconstruction matched local import byte-for-byte. Six contract tests passed. The fixed geometry control scored24/24 on the exploratory sample (17positive/7negative); this is not independent generalization or evidence of Agent necessity. See [validation receipt](artifact/local-validation.json) and [research log](report.md).

新增用户指定医疗切片原型：[PathMNIST batch指南](docs/pathology-batch-pilot.md)。历史1,000图与补建权重已核验导入并本地复跑，accuracy45.7%，仅开发控制；不是恢复原Vision模型或Agent优势。

新增实际Codex CLI同模型批实验：CUAD F1 **0.5023**、BioDEX RP@10 **0.3393**，均未优于旧静态/固定复核。原`data-agent`为受限Python工具循环；本轮才使用Codex CLI原生执行。[结果、完整成本和复现](docs/codex-cli-results-2026-09-05.md)。

人工标注历史经验实测已完成：[五组结果与固定DAG](docs/contract-history-results-2026-09-05.md)。8份历史合同/328类别案例用于8份新合同；固定DAG F1无H0.6750/有H0.6810，Codex无H0.7009/有H0.6936，未支持明显历史驱动Agent优势。


## DataSpace 可摊销探索原型

[冻结协议](docs/dataspace-amortization-pilot.md)定义一个按实体重复执行的基金筛选/属性抽取任务。[构造与复现](docs/dataspace-artifact-guide.md)提供原始来源校验、实体隔离、静态/agentic LOTUS、native Codex、单轨迹提取、冻结算子、私有评分和成本曲线入口。`python -m semantic_workload_bench.cli amortization --help`。当前300条算子执行299正确/1 ABSTAIN；手写SQL300/300，因此这是工程控制，不能据此宣称发现需要Agent的killer task。

DataSpace单轨迹原型的[最终开发结果](docs/dataspace-amortization-results-2026-09-06.md)：工程链路已执行；300条完整成本比较未显示收益，保留为控制任务。


## 五个 Partial 的数据湖与 Query

新增 [STARD / AnnoCTR / CodiEsp / HSCodeComp / UDRP 五湖构造](docs/shared-environment-five-lakes-build.md)：沿用公私快照契约，提供5个固定语义任务、20个query定义、可执行下游筛选/聚合/未完成清单。[统一目录](workloads/shared-environment-five.json)。已实际构造全量开发输入并保留原gold与证据缺口；没有新模型推理、质量评分或Strong升级。UDRP仅供审查。
