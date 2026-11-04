# Artifact guide

## Reproduction

Run `bash artifact/reproduce.sh` from any location. It changes to repository root, sets PYTHONPATH, downloads pinned source bytes, builds a new snapshot, runs a standard-library sanity baseline and scores it. Optional first argument is a local source directory; this is an acceleration, not a required old-repository dependency. Set SWB_ARTIFACT_DIR to an unused directory for each run. Vision instructions are in README. Full source acquisition is approximately2.35MB for the selected72 assets; no multi-GB download.

`python -m unittest discover -s tests -v` checks integrity and scoring failure boundaries. Build rejects existing destinations; private gold never enters the public records. Current code trusts repository-owned tools; it does not sandbox malicious systems.

Python3.11+; standard-library core. Optional vision dependencies pinned in pyproject. Exact local observed versions/platform are recorded in run.json. A clean locked vision environment and an independent Linux/container reproduction remain to be validated. Do not claim a validated Docker image exists.

## VLDB alignment

PVLDB asks for system/build configuration, data or generation, experiment/measurement scripts and raw-result-to-figure scripts; central conclusions should be reproducible by an independent team. See https://vldb.org/pvldb/reproducibility/ . EA&B requirements depend on submission volume; see https://www.vldb.org/2027/submission-guidelines.html . These references were checked2026-09-05; preparation is not acceptance or certification.

Current artifact has no paper claims/figures. `artifact/claim-map.json` explicitly tracks missing evidence. Release still needs strong baselines, environment-validity results, one-trace evaluation, archived assets, complete license review, resource/cost estimates and independent reproduction. External API costs/restricted resources must be documented and reviewers given a feasible access path.

## Imported evidence and history metadata

[PCB evidence receipts](../artifact/evidence/pcb-native-lotus-20260905/provenance.json) preserve the previous repository's100-record comparison, paired statistics, protocols and fixed-program control. Every copied file is listed with its original relative path and SHA256. This is a result import, not inference reproduction, and introduces no runtime dependency on the former repository. It does not change the existing24-record source lock or reproduction command.

[Two history cases](../environments/pcb/history/history-cases.json) and the exposure exclusions are evaluator/development metadata. They are not a public runtime snapshot or a new executable workload. Do not recursively expose artifact receipts, source locks or historical evaluation IDs to a model. See [history construction and evaluation rules](historical-experience.md) before building an explicitly approved history snapshot. No raw images, credentials or private reasoning were imported.

DataSpace单轨迹原型的[最终开发结果](dataspace-amortization-results-2026-09-06.md)：工程链路已执行；300条完整成本比较未显示收益，保留为控制任务。


## 五湖批查询构造

[构造与复现](shared-environment-five-lakes-build.md)提供五个Partial的真实public/private快照、源锁、Q1–Q4和确定性下游执行；[统一目录](../workloads/shared-environment-five.json)。模型与评分尚未执行，UDRP保留为审查包。
