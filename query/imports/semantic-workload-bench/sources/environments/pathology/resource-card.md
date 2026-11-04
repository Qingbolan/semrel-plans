# Pathology resource environment

| Resource | Concrete role | Evidence boundary |
|---|---|---|
| RGB patches | Complete per-record input to nine-class mapping | 28×28 benchmark patches, not whole slides |
| weights.pt | Reuse a domain classifier across the batch | Historical bootstrap CNN, not mature recovered weights |
| model_card.json + tool_code/pathology_model.py | Align architecture, channel order, scale, output IDs | Runtime checks code matches snapshot; load once on CPU |
| task class dictionary | Give output IDs stable tissue meanings | Does not supply per-test answers |
| 32 labeled train references | Illustrate tissue appearance for shared-resource comparisons | Explicit historical supervision, not current gold; benefit unmeasured |
| private gold/source indices | Independent evaluator and construction checks | Never runtime model resources |

Source lock: [sources.lock.json](sources.lock.json). Original Vision project code was inspected but its broken/unused application imports and training stack are not added to the runtime. New batch adapter preserves the inherited checkpoint architecture; source/weight redistribution authorization remains unresolved. Local artifacts are not a publication license grant.

Current entry point accepts a verified historical bundle and the pinned NPZ explicitly. It does not redownload or retrain missing weights. A fully independent source-to-checkpoint reproduction is not yet packaged. Public file separation is not an OS sandbox; this run uses trusted fixed local code, not arbitrary Agent-generated execution.
