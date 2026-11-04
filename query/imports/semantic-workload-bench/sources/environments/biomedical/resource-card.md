# Biomedical environment — BUILT / DEVELOPMENT PILOT

Primary workload: ../../workloads/biodex-reactions/workload-card.md . Source lock: sources.lock.json . Eight complete BioDEX-Reactions articles are frozen at revision 01a5dacdabd144a120af04931a11a99febd48432, verified from each dataset-service x-revision response header. Exact raw-row response bytes and hashes are retained outside Git. Selection did not inspect model outputs or gold labels.

Public inputs: title, abstract, full original text and per-article license. Public assisting resource: 24,369 distinct reaction names from the locked LOTUS benchmark table; 256-dimensional text-embedding-3-small vectors with exact cosine search. Shared tools search terminology, search/read article text and validate exact catalog labels/evidence quotations. Expert reaction lists, safety reports and answer-bearing metadata are private.

Resource role: terminology retrieval can normalize synonyms and surface candidate labels; article search can recover evidence missed in full-context extraction. The fixed program also uses the same embedding index and LLM verification/ranking. More resources or tool calls alone do not establish quality benefit. No clinical diagnosis or causal decision is evaluated.

Article licenses in this pilot include CC BY, CC BY-NC, CC BY-NC-SA and CC0. Precise MedDRA release and terminology redistribution rights remain unverified. No blanket code-license claim is applied to text or terminology. This is a local research artifact, not a public dataset release.

All eight PMIDs, DOIs and fulltext hashes are distinct, with no shared safety report ID among selected articles. Patient-level, full train/test and model-training overlaps are not resolved. Gold may omit supported conditions or reflect a different annotation scope; investigate benchmark disagreements after freezing predictions.

Snapshot: data/biodex-gap-pilot-v1. Frozen design: docs/biodex-gap-pilot.md from repository root. Outputs/failures/scoring: runs/biodex-gap-pilot-v1 and report.md. No independent confirmation or single-trace extraction has been performed.
