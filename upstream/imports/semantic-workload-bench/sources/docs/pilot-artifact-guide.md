# Quality-gap pilot artifact

This is a local development experiment. It does not establish Agent superiority, resource causality or single-trace reuse. Frozen designs: [CUAD](heterogeneous-gap-pilot.md), [BioDEX](biodex-gap-pilot.md). Operational observations: [notes](pilot-execution-notes.md). Results are appended to [report](../report.md).

## Environment and credentials

Use Python 3.12 in an isolated environment, install `pip install -e '.[pilot]'`, or recreate the observed package set from `experiments/pilot-requirements.lock.txt`. LOTUS is pinned at 1.2.4 and operator source hashes are in `experiments/lotus-pilot.lock.json`. Keep this environment separate from PCB's NumPy 2 vision environment.

The user-authorized `.env` contains `API_KEY` and `BASE_URL`; it is ignored by Git and must never enter snapshots, model prompts or published artifacts. Runtime sends only public task materials to that configured service. Model aliases, response model names, usage and failures are preserved. The proxy does not independently certify the actual upstream model snapshot. Actual charges are unknown, not zero.

## CUAD

Source URLs and byte hashes: `environments/contracts/sources.lock.json`. Current downloaded source directory: `data/source-audit-20260905-v1`. Its `sources.json` also records the BioDEX terminology CSV; the original CUAD pilot source identity includes that complete acquisition receipt, though the terminology table is not a CUAD runtime resource. That original receipt is preserved with the pilot. After inference, CUADBuilder construction_version=2 was corrected to consume only its two domain source entries. A rebuild at data/cuad-builder-check-v2 verified that all 11 public task asset files are byte-identical; provenance manifests/source identity intentionally differ. No model predictions were rerun or rewritten. The original construction/execution source is archived under each family's completed-experiment-source directory (and the initial CUAD launch-source directory).

```sh
export PYTHONPATH="$PWD/src"
python -m semantic_workload_bench.cli build-cuad --source data/source-audit-20260905-v1 --output data/cuad-new-v1
python -m semantic_workload_bench.contract_experiment --public data/cuad-new-v1/public --output runs/cuad-new-v1/lotus-map --arm lotus-map
python -m semantic_workload_bench.contract_experiment --public data/cuad-new-v1/public --output runs/cuad-new-v1/fixed-review --arm fixed-review --initial runs/cuad-new-v1/lotus-map
python -m semantic_workload_bench.contract_experiment --public data/cuad-new-v1/public --output runs/cuad-new-v1/data-agent --arm data-agent --initial runs/cuad-new-v1/lotus-map
```

After all three outputs are frozen, run `score-cuad --public ... --private ... --run ...` separately for each run, then `compare-cuad --runs runs/cuad-new-v1 --output runs/cuad-new-v1/comparison.json`. The complete sequence is in `artifact/reproduce-cuad-pilot.sh`; it requires `SWB_CUAD_SOURCE` and an unused `SWB_CUAD_OUTPUT`.

CUAD score is versioned `cuad-bipartite-jaccard-v1`, not DocETL's published evaluator. Exact categories, one-to-one matching and both FP/FN for unmatched nonempty predictions are intentional. Quote support and downstream contract-category relations/counts are reported separately. A score of 1 on category presence does not mean all gold spans were extracted.

## BioDEX

Source response URLs, revisions, sampling and hashes: `environments/biomedical/sources.lock.json`. Raw source rows: `data/biodex-source-pilot-v1`; resource: `data/biodex-terminology-v1`; snapshot: `data/biodex-gap-pilot-v1`. The terminology resource is frozen with aligned terms and normalized float32 vectors, model/dimension metadata and preprocessing usage. Query embeddings are logged separately in each run.

Builder interfaces, callable with `PYTHONPATH=src`:

```python
from pathlib import Path
from semantic_workload_bench.biodex import TerminologyIndex, BioDEXBuilder

TerminologyIndex.build(
    Path("data/source-audit-20260905-v1/biodex-terms.csv"),
    Path("data/biodex-terminology-new-v1"), Path(".env"))
BioDEXBuilder().build(
    Path("data/biodex-source-pilot-v1"),
    Path("data/biodex-terminology-new-v1"), Path("data/biodex-new-v1"))
```

```sh
python -m semantic_workload_bench.biodex_experiment --public data/biodex-new-v1/public --output runs/biodex-new-v1/static-rank --arm static-rank
python -m semantic_workload_bench.biodex_experiment --public data/biodex-new-v1/public --output runs/biodex-new-v1/fixed-review --arm fixed-review --initial runs/biodex-new-v1/static-rank
python -m semantic_workload_bench.biodex_experiment --public data/biodex-new-v1/public --output runs/biodex-new-v1/data-agent --arm data-agent --initial runs/biodex-new-v1/static-rank
```

After all outputs are frozen, use `BioDEXEvaluator().score(private, public, run)` with Path arguments for each run. RP is label agreement with released expert labels, which are not an exhaustive medical truth oracle. The strengthened static pipeline uses actual LOTUS sem_map, fixed embedding retrieval and LLM verification/ranking; it is neither the old cosine-ranking baseline nor a full LOTUS cascade-join or DocETL optimizer reproduction.

## Receipts and cost

`state.json` marks active/completed execution. A `RUNNING` directory or partial output is not a completed result. `run.json` plus prediction digest identifies a completed run; `metrics.json` is created by separate private scoring and refuses overwrite. Inspect `trace.json` for observable tools/arguments/results and `calls/call-*.json` for model requests, observable returned messages, finish reasons, usage and failures. Provider reasoning fields and credentials are excluded.

Initial outputs are shared between the two review arms to isolate correction behavior. Add the initial receipt's usage/time when comparing standalone costs; add glossary preprocessing for BioDEX. Sum actual calls only once when measuring total experiment expenditure. Usage of failed requests can be unknown. Local caching is disabled; provider caching is unknown except for any usage details returned. Per-family serialization and cross-family overlap do not constitute a controlled latency study.

Source identity and lexical duplicate audits are in each family run root. Neither substitutes for full source-entity isolation or model-training contamination checks. No sampled article or contract may be reused as a fresh confirmation record after this pilot.

TerminologyIndex construction now stages, verifies and publishes atomically; failed builds retain a separate failure/cost receipt and remove only their staging directory. This post-experiment construction fix does not alter the frozen index used by these runs.
