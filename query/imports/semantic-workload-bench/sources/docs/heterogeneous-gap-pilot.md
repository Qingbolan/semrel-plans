# Heterogeneous environment quality-gap pilot v1

Frozen design: 2026-09-05, before task model outputs or gold inspection.

## Question and decision

Can an adaptive Data Agent use public document tools and structured reference data to improve complete, repeated extraction tasks over a competitive static procedure with the same model and resources?

This is development screening, not confirmation or one-trace extraction. A positive pilot advances a candidate; it does not prove a population-level advantage. A static solution that already works is retained as a negative control. Do not change task, select error cases, or weaken the static arm to obtain a positive result.

## Candidate acquisition

BioDEX remains the preferred heterogeneous case (article text + terminology table + retrieval/normalization tools). Audit the complete text, terminology and gold provenance first. The dataset service is reachable but revision metadata currently returns HTTP 429; source/API failures are not model failures. Do not derive a terminology list from selected gold.

CUAD is the first executable alternative: complete contract text + official category-description table + deterministic search/read/exact-quote validation tools. This is heterogeneity of document/reference/tool roles, not evidence of multimodal or cross-source relational reasoning. Original PDFs and external knowledge are not assumed available.

## CUAD selection and task

- Source: TheAtticusProject/cuad commit 67faa0e6023b04fcaae6cc09497ab00e5d63a2a2; official `data.zip` and `category_descriptions.csv`.
- Universe: 102 contracts in official test.json. Order by SHA256("heterogeneous-gap-pilot-v1" + NUL + source title), select first 8, regardless of length or gold. No truncation or hidden exclusions.
- Shared task: extract all applicable 41 category spans from each full contract; return exact source quotations and exact category names. One contract is one independent scoring unit for this pilot. Template/near-duplicate isolation is not yet established, so no confirmation claim.
- Public: opaque record IDs, complete source text, official category definitions. Private: source mapping and original expert answers. Required definitions are supplied to every arm.

## Arms and controls

1. `lotus-map`: pinned lotus-ai 1.2.4, traditional sem_map, all categories in one call, no agentic optimizer. This is a contemporary common-model execution, not a historical DocETL replication.
2. `fixed-review`: same initial extraction, followed by a fixed coverage/quote review using public tools; the review model receives the same contract and definitions. It can correct the output once. This tests whether an ordinary fixed verification pass explains apparent Agent gains.
3. `data-agent`: same initial extraction, then a bounded adaptive review with public search/read/quote-check tools. Up to four model review turns, final turn forced to produce the answer. No shell, arbitrary Python, filesystem, network, gold access or generated code execution. Tool dispatch exposes only in-memory public assets.

All review arms reuse the same initial result per contract and include that call's usage and time in standalone cost. This paired design isolates correction ability. It is not evidence that the Agent independently selected its initial strategy. Compare both review arms with each other, not only with one-call LOTUS. Required input is always complete; no deliberate context truncation.

Provider: existing user-configured OpenAI-compatible service. Request gpt-5.4 with reasoning_effort=none for all arms; record returned model identity. A proxy alias is not a verified upstream snapshot. No claims about frontier status. An initial API-format probe is separate from scientific runs. If a parameter is unsupported, record and freeze the correction before task inference.

Initial envelope: 8 contracts, serial model requests, maximum 48 task requests (8 initial + 8 fixed + at most 32 adaptive), max 12,000 completion tokens per request. No automatic task retry or gold-driven repair. Unknown provider price remains null; record API token usage, reported cost if any, elapsed time, tool calls, failures and cache metadata. Do not silently replace the model or exceed this envelope. Historical gpt-4o-mini reproduction and another strong-model replication remain separate subsequent work.

## Scoring and interpretation

Primary: per-contract category-aware span extraction F1, macro-averaged over contracts, using one-to-one token-set Jaccard matching >0.15. Also report >0.5 sensitivity, exact-quotation support, coverage/ABSTAIN, selected contract-category relation precision/recall and per-category count absolute error. Incorrect nonempty spans incur both a false positive and a false negative. Unknown categories and unsupported quotations remain errors, not silently removed. Empty gold/prediction is explicitly distinguished from execution ABSTAIN.

This clean scorer is versioned separately from DocETL's artifact: its fuzzy category mapping and nonmatching-span recall accounting are not copied. Do not compare our numbers directly with its published table. Freeze predictions before scoring; score all selected records, including failures. Save paired per-contract deltas and bootstrap uncertainty as descriptive only (8 records, unresolved template clusters).

Advance only if adaptive review gains at least 0.05 absolute primary F1 over both the initial and fixed-review arms, without a gain explained by missing input or output-format repair alone, with improvements in at least 3 contracts and traceable public tool evidence. Otherwise report negative/inconclusive. This is a screening rule, not a statistical proof or deployment quality threshold. A positive result still requires resource ablation, budget-matched curves, DocETL/Coding Agent controls, another model and fresh entity-isolated confirmation.

No trajectory extraction is part of this pilot. Preserve every attempt and do not relabel this development set as a future confirmation set.
