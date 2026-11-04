# BioDEX heterogeneous pilot v1 — frozen before inference

Date: 2026-09-05. Development screening only. This accompanies the CUAD pilot; it does not replace a failed or inconvenient result.

Source: BioDEX/BioDEX-Reactions revision `01a5dacdabd144a120af04931a11a99febd48432`, verified through the x-revision header on every downloaded row response. Eight official test row indices are selected by SHA256("heterogeneous-biodex-pilot-v1" + NUL + decimal row index), ascending first eight among 4249. Indices: 2132, 670, 3961, 2561, 4190, 500, 1852, 990. No model results or gold labels were used to select these. Full original article text, title and abstract are public; expert reaction labels and identifying construction metadata remain private. Full text is not truncated. The official source provides processed text too, but it is not substituted silently for the full text.

The public terminology table has 24,369 distinct entries from lotus-data/lotus commit `136ae4f4a344a2f75d89f811e516dfcb0de30e46`. It is independent of selected gold. Its precise MedDRA release and redistribution rights are not established; this is a local research experiment, not a data release. Article licenses are retained per source. Duplicate patients/reports and training contamination have not been ruled out.

Task: identify and rank the standardized adverse drug reactions reported for patients in each article, up to 25 labels. Do not infer clinical causation, count every background condition as a patient reaction, or use expert reports as runtime evidence. Gold is the dataset's label list, which may omit article-supported reactions. Interpret metric errors as benchmark disagreements pending evidence audit, not medical facts.

Shared environment: complete article text, terminology table, exact cosine search over terminology embeddings, document word search/context reading, and exact label/quotation validation. All tools operate on public objects through allowlisted calls; no arbitrary execution or external article search.

Common model: user-configured proxy alias gpt-5.4, same request settings as CUAD. Embeddings: text-embedding-3-small, 256 dimensions, fixed for all arms. Save each request's usage and index receipt; proxy identity and exact prices remain unverified.

Arms:

1. `static-rank`: actual LOTUS sem_map generates a list of reaction search queries from the complete article. A fixed program searches the top 49 terms for the joined query and top 3 per individual query, takes their stable union (at most 124 terms for 25 queries), then the same model verifies applicability and ranks labels in one call. Both retrieval and LLM ranking are available to the static arm. This is a disclosed strengthened static control, not an exact reproduction of DocETL's 49-candidate/cosine-ranking baseline or LOTUS's current cascade join.
2. `fixed-review`: reuse the complete static result and candidates, provide deterministic exact label/quotation checks and a fixed instruction to audit missing and irrelevant reactions; one extra model pass. Include the initial two calls and embedding work in standalone cost.
3. `data-agent`: same initial result and candidates, up to four adaptive model review turns, including final answer; up to eight tool executions per turn. Can formulate new terminology queries or inspect article passages. All output terms must come from the full public terminology, not necessarily the original shortlist; the fixed arm may also name other catalog terms. Include the initial work in standalone cost.

Envelope: 8 articles; at most 56 chat requests (16 initial, 8 fixed, 32 adaptive), each at most 12000 completion tokens. The glossary index is shared preprocessing, built once in batches of 1000; query embedding calls are traced and counted separately. Serial within an arm; no automatic task retries. No inference begins until public/private construction and embedding index checks pass. Do not replace missing/failed requests with cached historical outputs.

Metrics: macro article RP@5, RP@10, RP@25 with denominator min(k, number of unique gold labels); duplicate outputs cannot earn repeat credit. Also report label-set precision/recall/F1, coverage, glossary membership, exact evidence quotation support, initial shortlist gold recall, and downstream article-label relation/count errors. A model outage is ABSTAIN, not a negative fact. Save all failures. Score only after all predictions are frozen.

Screening: require adaptive RP@10 improvement of at least 0.05 over both controls and improvement on at least three articles, then inspect whether newly used public resources support corrected answers. No automatic scientific VALIDATED state. Unequal review budgets, small n, annotation coverage, proxy routing, no second model and absent full DocETL/Coding Agent controls remain limitations. Resource ablation and fresh independent confirmation are required before a claim of heterogeneous-environment benefit. No trajectory extraction in this pilot.
