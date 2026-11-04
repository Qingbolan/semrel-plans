# Contract environment — BUILT / DEVELOPMENT PILOT

Primary workload: ../../workloads/cuad-clauses/workload-card.md . Source lock: sources.lock.json . CUAD official test 102 contracts; eight selected by the frozen hash rule, with complete text and all 41 category definitions. Snapshot: data/cuad-gap-pilot-v1, outside Git.

Public resources: full contract text, official category CSV transformed into explicit names/descriptions/answer formats/groups, deterministic search/read and exact-quote/category validation tools. Private: original expert spans, source titles and acquisition receipt. Source answer offsets were checked before publication. Category names map by exact case-insensitive source identity at construction; runtime/scoring uses exact canonical names.

The official CUAD page declares CC BY 4.0: https://www.atticusprojectai.org/cuad/ . Full labeling handbook availability was checked separately: https://www.atticusprojectai.org/labeling-handbook/ lists it as a purchasable download. It was not acquired, audited or provided to any arm. PDFs and richer external knowledge are not part of this pilot.

This tests complete document + structured category metadata + public tools. It is not a multimodal experiment and does not yet establish a resource's causal benefit. Fixed review also receives public search/validation outputs. Maximum review budgets differ. See docs/heterogeneous-gap-pilot.md and docs/pilot-execution-notes.md from repository root.

A lexical 5-word shingle check against all 102 test contracts found no near-duplicate above 0.8 Jaccard for the eight selected records; this does not establish entity/template/train-test independence. Actual outputs, failures and scoring are recorded under runs/cuad-gap-pilot-v1 and report.md. No single-trace extraction or independent confirmation is claimed.

Authorized CUAD history resource now exists at data/cuad-history-transfer-v1/history: 8 prior documents,328 category cases,312 official human-supervised spans, paired with prior model outputs. Current8-record gold remains separate in evaluation/private. This is retrospective annotation-backed supervision, not newly authored human correction rules. [Validity experiment and DAG](../../docs/contract-history-results-2026-09-05.md) did not establish a history-driven quality advantage.
