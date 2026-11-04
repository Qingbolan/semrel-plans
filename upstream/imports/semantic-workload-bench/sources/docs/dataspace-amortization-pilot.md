# DataSpace amortizable exploration development pilot v1

Frozen before the first workload model call (provider arithmetic preflight is separate).

## Task and evidence

DataSpace task_184 asks for funds with positive current-day benchmark growth and their investment scope. Upstream dataset revision `96be19257d7aa251dbce4771d46a26fc36f6dc52`, repository commit `6491caa4c70cc06cacb6103ba73cefb00746abfe`. Archive and exact asset lock: [sources](../environments/dataspace/sources.lock.json). Source audit observed 1,048 distinct fund records, 77 manager groups, and 374 public-reference positive rows. A separate SQL audit exactly reproduces the upstream reference multiset. This is an easy-SQL counterexample candidate, not a presumed quality-gap workload.

Recurring task: for each fund, select on current-day benchmark rate > 0, then return abbreviation and verbatim archive investment scope. One fixed filter/map semantics, no changed thresholds. Output is {selected, fund, investment_scope}; nonselected fields are null. Default static path receives complete entity-local SQLite rows, industry CSV and risk JSON, without answer-column selection or truncation. Static and Agent input information is equal; representations and tool access differ and are disclosed.

## Construction and splits

Keep all columns and matching rows in every source SQLite table keyed by fund identity, plus matching original industry CSV and risk JSON rows. No PDFs/video are used by the transformed task. Do not call this a multimodal perception experiment or the full original workspace. SQLite contains all necessary task evidence; CSV/JSON are authentic distractors. Their existence does not establish heterogeneous resource value.

Partition managers by SHA256("fund-split-v1" + NUL + manager). One entity from the first manager is demonstration x0. Take 16 entities from the next manager groups for validation V; take 300 hash-ordered entities from remaining manager groups for R. Unused entities are excluded, not duplicated to enlarge the sample. Source lookup/indexing is shared preprocessing. All splits are development: manager separation does not establish absence of shared templates, source contamination or training overlap. Public-reference availability is disclosed. Gold is a private one-to-one projection of the official answer table, not labels from the proposed operator.

## Frozen execution

Requested model gpt-5.4, existing configured .env provider; official snapshot identity and actual currency charges unknown. Temperature 0, no automatic task retries, serial calls within each arm; independent arms may overlap. Native Codex uses Responses and its own system prompt; LOTUS uses Chat Completions. Docker swb-codex-pilot:0.151.0, offline/read-only public mount, no host private paths. Record tools, outputs, budgets, failed attempts and startup costs; never private reasoning or keys.

LOTUS code pinned at `136ae4f4a344a2f75d89f811e516dfcb0de30e46` (upstream metadata still says 1.2.4, so package version alone is insufficient). Retain native agentic worker and Corpus map behavior. Agentic batched/shared-context strategies must not be described as unsupported. Use map with explicit JSON outputs to avoid upstream filter's default-KEEP parser becoming a fabricated successful label.

Development screen on V: traditional LOTUS sem_map, native LOTUS agentic map (batched strategy allowed), native Codex one batch. Record static quality, Agent quality and costs. A mean joint-record improvement above 0.05 is only a candidate screening signal, not confirmation. If no gain, reject this as a killer-task candidate and retain negative results. Do not choose another metric to make it pass.

Engineering extraction: one actual x0 native execution, one automatic synthesis request, frozen Python plus applicability. No V/R gold or additional traces enter extraction. Validate V, then execute frozen artifact on all 300 R without repairs. Failure or unsafe applicability means ABSTAIN; no silent model fallback. This engineering exercise may run even if the research screen fails, but cannot be reported as validating the quality-gap hypothesis. No-trace coding and same-trace replay remain required before any causal claim about trajectory information.

Budgets: native x0 at most16 calls/900sec, native V at most24 calls/1800sec; synthesis one call/12000 output tokens; LOTUS each request at most12000 output tokens, agentic at most6 tool steps plus its native finalization call. Any budget mismatch is reported. Screening is not an equal-compute causal experiment. Tool Python at most30sec per call, frozen operator at most120sec for a batch. Synthesis and generated execution cannot access current private labels.

## Metrics and acceptance

Report selection accuracy, exact joint-record success, selected output precision/recall/F1, selected count error, execution coverage, operator coverage, Agent calls, tokens and wall-clock separately. Whitespace at the outer edges of text is ignored as in the source audit; do not use an LLM judge. Failures remain in full denominator.

Predeclared epsilon0.05, one-sided confidence0.95, paired manager-cluster bootstrap10000 samples, seed0. Development status cannot authorize materialization regardless of point scores. Cost analysis reports each dimension separately; unknown money/compute remains unknown. C(N)=demo+extraction+validation+shared preprocessing+execution+fallback. Strict cheaper-than integer break-even is a linear projection and only reported where all needed phase costs are known; no extrapolated latency is a measured batch latency. Acquisition and provider preflight are reported separately; demo/synthesis failures and retries remain in the ledger.

## Current implementation boundary

This file is a protocol, not a completion receipt. See report.md for actual execution. Neither a static quality shortfall, Agent superiority, nor safe independent materialization has been established.


## Explicit transport supplement 2026-09-06T03:38:04.750214+08:00

The initial Chat Completions native agentic run failed in its adapter because provider usage included nested dictionaries; scalar-counter normalization fixed this implementation defect, and all failed receipts were retained. The corrected run completed8/16correct and had8ABSTAIN from HTTP403 affecting two shards. Traditional LOTUS also receivedHTTP403. These are infrastructure failures, not a quality-gap finding. Add explicit Responses-transport repeats of both LOTUS arms on the same16V, unchanged data/model/task/LOTUS prompts/tool budgets/batching. Native broker remains the same as the successful Codex arm. This is a separately labeled post-protocol engineering transport comparison, never a silent fallback or replacement of original scores. No new model requests for synthesis, no operator modification, no R gold tuning.


Additional strong batch control: execute the unchanged native Codex prompt on all300R with24calls/1800sec, shared planning/code/caching permitted. This prevents extrapolating sixteen-record per-item token usage as if an Agent could not amortize its own batch program. It is a development comparison added after observing the learned run; no prompt, data, model or operator repair is allowed, and no independent-confirmation claim follows.


Post-output validity audit: the Chat static arm completed14/16 (twoHTTP403), with correct selection and verbatim scopes in all completed records. Three selected fund names use another public abbreviated-name field, giving11/16 under the frozen exact-name score. The Responses static arm completed16/16, with the same three alternate-name-only mismatches (13/16 exact joint score). This exposes an under-specified abbreviation convention, not evidence of a semantic reasoning/resource gain. Do not alter v1 outputs/gold/prompt after this observation. A future semantic clarification requires a new task version and fresh protocol; the present workload is rejected as a killer-task candidate.

The native LOTUS finalization adapter was also corrected: the advertised six tool steps plus one final tool-free call permit a completed answer on that final call. Its original returned answers are reparsed through the pinned native map parser; no new inference or gold-dependent answer editing is performed. Original projection receipts remain archived. The corrected adapter has a native-library regression test with six tool turns plus finalization and nested provider token-detail dictionaries.
