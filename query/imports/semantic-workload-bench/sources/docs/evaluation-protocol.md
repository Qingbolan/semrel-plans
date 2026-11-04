# Evaluation protocol

Arms: B0 direct semantic call; B1 same model with fixed knowledge/reference; B2 fixed retrieval/tool program with disclosed branches; B3 Coding Agent creates batch program once; B4 Data Agent may share cache and plans; B5 one-trace-derived operator; B6 same-trace summary/replay; B7 extraction with task/environment but no trace.

Implemented now: PCB sanity/fixed-geometry controls plus concrete CUAD/BioDEX development-pilot static, fixed-review and tool-Agent arms. These do not cover the full B0–B7 matrix. Observable model/tool receipts are recorded; automatic single-trace extraction is now implemented separately in the DataSpace development prototype, without a confirmed quality-gap or safe-materialization claim. See the frozen pilot designs and report.md for actual execution/scoring status.

Freeze data, predicate, source assets, gold mapping, budgets and model IDs before confirmation. Allow all compared systems the same evidence and tools; disclose cases where alignment is impossible. Each B5 instance uses one trace only. Repeated one-trace episodes are independent; selection/retries and unsuccessful demos count toward cost. No confirmation-gold-driven repairs.

Split by board group, document, original scene or patient as appropriate. Current24 PCB rows are exploratory only and all are scored for a baseline smoke; they are not a one-demo/23-test experiment in this new repository.

Metrics: critical-step macro-F1/recall and evidence sufficiency; coverage and abstentions; downstream selected-list precision/recall/count error. Confidence intervals clustered by source entity; report sample-size limits. Quality retention uses a predeclared noninferiority margin; do not infer it from point estimates alone.

Cost(N)=demonstration+extraction+validation+shared preprocessing+sum execution+fallback. Report token, actual money if known, tool compute, GPU/CPU, initialization, process startup and batch wall-clock separately. Runtime currently records fixed-loop time and package/code versions; it is not full economic costing or a controlled latency study.

For stochastic providers pin exact model/version/date/prompt, request parameters, retries, concurrency and caching; preserve raw returned outputs under redistribution rules. Provide at least one independently runnable configuration when practical. Replaying stored responses checks analysis, not independent inference reproduction.

## Accuracy-gap entry gate (2026-09-05)

Use [candidate evidence](accuracy-gap-candidates.md) to prioritize BioDEX then CUAD. First reproduce the published traditional-LOTUS setting, then a controlled common-model setting with all costs and ranking/parser differences disclosed. Agent improvement is a separate untested claim. Lock the exact LOTUS release/commit and operator configuration; current official documentation also describes agentic operators. DocETL is an essential strong comparator, not a surrogate for a single-task Agent trace. Keep original RP/F1 metrics; never relabel them ordinary accuracy.

## Historical experience as explicit supervision (2026-09-05)

Follow [the history protocol](historical-experience.md): freeze approved H inside E, its label/review provenance, source-entity split, duplicate audit and cutoff before independent evaluation. Current G_R stays private. Cases selected after examining evaluation errors become development history and need a fresh confirmation set. Historical labels are permitted explicit supervision; they are not evidence that current gold access is safe.

Run B0 without H as an information ablation; B1 fixed history examples; B2 fixed history retrieval/tool checks; B4 adaptive history/tool use; B3 once-generated program; B5 one-trace extraction with disclosed historical supervision. B1–B5 share approved history and tool access. Separate history benefit from dynamic selection benefit. Record actual historical cases/trajectories accessed, applicability failures, corrections and regressions, balanced metrics and downstream effects. Single trace does not mean single supervised example.

Add history labeling/curation/review/indexing to total cost; pre-existing history can additionally be evaluated as a disclosed sunk-cost deployment scenario. Local low-cost models form a deployment axis, with matching-model and strong static controls retained. No history-enriched run has been executed by this update, and existing frozen pilots are unchanged.

Actual Codex CLI batch arm now executed under the [frozen design](codex-cli-pilot.md), with [negative primary results and costs](codex-cli-results-2026-09-05.md). The earlier tool-Agent means a bounded Python review loop. Native Codex shares requested model/provider and public task resources, but uses Responses instead of Chat Completions and different system prompt/batch/code/budget conditions; not an equal-budget causal comparison or independent confirmation.

A five-arm CUAD annotation-history comparison now runs under the [frozen design](contract-history-pilot.md): direct LOTUS, fixed/no-H, fixed/H, native Codex/no-H, native Codex/H. See [results](contract-history-results-2026-09-05.md). Fixed request pairs are identical except H payload; native resource conditions share current inputs and model. No predeclared history/Agent screen passes, and B3/DocETL/extraction/independent confirmation remain missing.


## DataSpace amortization prototype (2026-09-06)

The new user-requested [protocol](dataspace-amortization-pilot.md) uses stable input/output semantics with an initially undiscovered internal execution plan. Exactly one observed native execution feeds synthesis; all300 later entities run the same frozen artifact. This engineering exercise does not relax the research quality-gap gate. Manager-disjoint development groups, explicit applicability/ABSTAIN, native LOTUS batching and the handwriting SQL control are retained. Missing currency/compute costs remain unknown. A projected token break-even is not measured monetary savings or independent noninferiority.
