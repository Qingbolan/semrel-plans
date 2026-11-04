# DataSpace source and resource roles

Authenticity: full release ZIP2,878,651,222bytes verified against upstream SHA25668f221fafcf0b50396eca55f8298af1ad73d586a6cac6995916afca535a560af. Exact revision, repository commit, task asset inventory and metadata hash are in [source lock](sources.lock.json). Task184 has19files totaling40,624,940bytes and six original modalities. Official public-reference table and evaluator config stay in private snapshots; source archive and task metadata with reference paths are never mounted into model containers.

The derived [fund workload](../../workloads/dataspace-fund/workload-card.md) uses three file types:

| Resource | Concrete role | Boundary |
| --- | --- | --- |
| SQLite benchmark-return table | Distinguish current-day benchmark rate from other periods | Necessary task evidence |
| SQLite archive table | Link fund identity to verbatim investment scope | Necessary task evidence; several name fields require a precise output convention |
| Other fund-keyed SQLite tables | Natural irrelevant returns/fees/assets with overlapping terminology | Distractors, not claimed assistance |
| Original industry CSV | Authentic irrelevant industry-investment data, retaining original fields | No measured positive resource contribution |
| Original risk JSON | Authentic irrelevant risk classification | Risk class does not determine daily benchmark positivity |
| Offline Python/SQLite | Inspect schemas, perform exact joins/comparisons and copy long fields | Real computed tool output; same tools available to fixed programs |
| Official gold CSV | Independent source output used only by builder/evaluator | Never model input |

Entity slicing retains all columns of the selected source tables, using public IDs only. It simplifies discovery compared with the full original workspace and is explicitly counted as shared preprocessing. It does not manufacture missing necessary inputs. CSV/JSON presence alone does not establish heterogeneous-resource value or Agent advantage; no causal ablation has been run.

Upstream declares MIT for code/data. Underlying financial-source provenance and redistribution rights have not been independently cleared; local acquisition is not a release approval. No raw dataset is committed. Near-duplicate text, manager aliases, source contamination and training overlap remain unverified. No source or snapshot hash proves scientific validity.
