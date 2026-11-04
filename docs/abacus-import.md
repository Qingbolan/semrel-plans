# Abacus workload collection

Added on 2026-10-14 from [Abacus v3](https://arxiv.org/abs/2505.14661v3) and its [official experiment artifact](https://github.com/mitdbg/palimpzest/tree/807ed301c4d2457ef304647e6095184556bd1e83/abacus-research), pinned to commit `807ed301c4d2457ef304647e6095184556bd1e83`. The artifact README identifies the three Table 2 workload scripts and their Table 3 variants. This is the available official source revision; it is not asserted to be the historical revision used to produce the paper's measurements.

| Collection / workflow | Direct input | Context resources | Output | Evaluation selection |
|---|---|---|---|---|
| Abacus / 1 — BioDEX | Article table: pmid, title, abstract, fulltext | Reaction terminology and supplied Chroma index | Ranked reaction labels | 250 articles per seed, seeds 0–9, from 4,249 test records |
| Abacus / 2 — CUAD | Contract table: contract_id, title, contract; semantic operator receives contract | 41 category definitions | Extracted spans for each category | 100 contracts per seed, seeds 0–9, from 102 test contracts |
| Abacus / 3 — MMQA | Question table: qid, question | Text, serialized table and image candidate tables | Answer list | 100 questions per seed, seeds 0, 1, 2, 3, 4, 6, 8, 9 |

The 451 distinct MMQA questions selected across those eight runs are also recorded individually in **Abacus MMQA**, numbered 1–451. Their English question text is copied verbatim from the supplied dev file, with source record selectors and SHA-256 checks. The three workflow-level query strings are exact instruction literals from the official code. BioDEX articles and CUAD contracts are rows processed by a parameterized workload, rather than newly invented natural-language questions.

## Local files

- `query/tasks/Abacus/`: three task JSON documents in the catalog's eight-key schema.
- `query/tasks/Abacus MMQA/`: 451 individual task JSON documents.
- `query/source-snapshots/abacus/<commit>/abacus-research/`: official workload definitions, all operator prompts, run scripts and scoring scripts.
- `data/abacus/biodex/`: official test, train and validation Parquet files; primary input table; separate test gold; per-seed evaluation and optimization selections.
- `data/abacus/cuad/`: official data.zip and extracted source JSON; contract input table; per-seed evaluation and optimization selections.
- `data/abacus/mmqa/`: question input table, separate gold, selections, 450 actual image files and their CRC-verified download manifest.
- `data/abacus/artifacts/`: the complete 2,371,162,388-byte author-supplied artifact and its extracted data/indexes.
- `environment/abacus/biodex/`: references to reaction terms and the local supplied index.
- `environment/abacus/cuad/categories.json`: all 41 category definitions copied from source.
- `environment/abacus/mmqa/`: 71 text records, 307 serialized table records and 450 image references; unique document pools and exact ordered candidate-row lists for every seed.
- `exports/abacus-import.json`, `exports/abacus-downloads.json`: counts and file checksums.

MMQA candidate datasets follow the official complex workload: contexts supporting the selected 100 questions form each run's candidate dataset. `pool-records.json` preserves repeated candidate rows and ordering. A single question is evaluated against that run's candidate dataset, not only its own supporting documents. The context tables store image file paths; the official loader encodes their bytes as base64. Text and table serialization was checked against the official dataset classes for all eight seeds.

Gold answers and supporting-context annotations remain separate from direct inputs. CUAD gold spans are in the original test JSON. Optimization selections are separate: BioDEX 20 training articles, CUAD 25 training contracts, MMQA 20 training questions per seed. These and evaluation record counts are not model batch sizes. No inference execution or reproduced paper metrics are claimed.

## Sources and rebuilding

- [BioDEX dataset](https://huggingface.co/datasets/BioDEX/BioDEX-Reactions)
- [CUAD data](https://github.com/TheAtticusProject/cuad)
- [MMQA data and image archive](https://github.com/allenai/multimodalqa)
- [Abacus data archive](https://palimpzest-workloads.s3.us-east-1.amazonaws.com/abacus-data.tar.gz)

With source artifacts present, run `python3 backend/scripts/download_abacus_images.py` to acquire/verify selected images, then `python3 backend/scripts/import_abacus.py` (requires numpy, pandas and pyarrow), followed by `python3 backend/scripts/build.py`. The importer replaces only Abacus-owned catalog rows. Run `python3 -m unittest discover -s tests -p 'test_abacus_import.py'` for source text, selection and paper-link validation.
