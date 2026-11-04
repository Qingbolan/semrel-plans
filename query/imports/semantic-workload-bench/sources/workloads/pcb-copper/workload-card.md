# PCB copper control pilot

Dataset: DeepPCB, original paper arXiv1902.06197 (2019 preprint). Source: https://github.com/tangsanli5201/DeepPCB ; frozen commit08e98c4db5922613fb97176eb3d6497d48260cb1.

Population1500 image pairs; officialtrainval1000/test500. Current inherited24test records are selected by sorted SHA256 of manufacturing-pilot-v1 NUL test-list line, no label-based selection. This recipe is inherited provenance; builder reproduces the pinned selection, not a fresh population resampling.

Unit: tested640x640 board image and aligned clean template. Target: class5 copper presence from any corresponding official bbox label. Other labels do not imply target presence. Structured masks/boxes remain private. Intermediate Boolean filter → selected IDs → count. No repair or severity claim.

Source CCD board images include manually added defects; do not claim all natural defects. Template cleaning is part of source preparation. This small test-derived set has already been examined in earlier research; group-disjoint new confirmation data required. Current full24 scoring is an engineering control only, not learned operator validation.

Fixed geometry assumption: dark copper, aligned scale, isolated complete connected component absent from template. Three-pixel tolerance/eight-pixel area/10percent overlap are inherited engineering choices; not tuned in this repository, not official standards. Compare legitimate stronger baselines before conclusions.

## Historical experience development extension

An additional experiment was executed in the previous repository on100 record-disjoint test pairs (not new board groups): native LOTUS image-only89/100, paired91/100, same-model tool Agent92/100, fixed program100/100. Agent corrected9 and regressed8; exact paired p=1.0. [Imported receipts](../../artifact/evidence/pcb-native-lotus-20260905/provenance.json) are not a run of this repository's24-record workload and do not validate Agent superiority.

[History catalog](../../environments/pcb/history/history-cases.json) registers12000085 (Agent correction) and50600063 (Agent regression). Both official class5 labels are FALSE. Official human annotations are distinguished from model evidence summaries and researcher-derived connectivity lessons. Source assets have pinned URLs/hashes; image bytes have not been copied, and no history is mounted by the current builder.

These cases are post-hoc development material. [Exposure exclusions](../../environments/pcb/history/exposure-exclusions.json) conservatively register all179 previously used source IDs. Any history-enhanced confirmation needs a new entity-disjoint split and duplicate audit; no performance improvement from history has yet been measured. Apply [the common history protocol](../../docs/historical-experience.md), preserving fixed-example/retrieval/tool and Coding Agent baselines.
