# Codex CLI common-model development pilot

Frozen before task inference on 2026-09-05 (Asia/Singapore). User explicitly requested Codex CLI with the same model. This adds an actual unmodified Codex CLI 0.151.0 arm; the earlier `data-agent` arms are bounded Python tool-review loops, not Codex.

## Question and unchanged evidence

Can Codex CLI improve the same CUAD/BioDEX development batch using the existing public environment and shared static predictions? Reuse all eight records per family from the frozen [CUAD](heterogeneous-gap-pilot.md) and [BioDEX](biodex-gap-pilot.md) designs, source manifests, task instructions, terminology and scoring. No new gold-derived prompt, resources or examples. These records have already been evaluated: this remains development, never independent confirmation. BioDEX's previously identified patient-ADR prompt/gold scope mismatch remains an explicit limitation; do not fix the prompt only for Codex.

CUAD receives the original LOTUS initial predictions. Its one initial timeout propagates as ABSTAIN, just as in both previous review arms; evaluate all eight and report coverage. BioDEX receives all eight initial predictions and their initial candidate lists. Neither CLI sees metrics, gold, reports, source locks, prior adaptive predictions or this research conversation.

## Execution and model

Actual `codex exec`, npm package `@openai/codex@0.151.0`, installed in `swb-codex-pilot:0.151.0`; record the actual immutable image ID. Stock Codex system instructions, native planning/shell/code execution and file editing; no injected imitation of a Codex loop. Fresh context/configuration per family, one session for the whole batch so plans and computations may be shared. No nested Agents, web search, plugins or user/project instructions.

The exact previous `.env` BASE_URL/API_KEY provider is used, requesting `gpt-5.4`. Codex uses native Responses API, while the earlier static calls used Chat Completions. The transport enforces requested reasoning effort `none`, temperature 0, store=false and maximum 12,000 output tokens/request. No model substitution. Returned model and token usage are recorded; proxy upstream snapshot identity and equivalence across API endpoints cannot be independently established. `none` did not mean zero provider-reported reasoning tokens in the API probe.

Per-family batch caps: 48 model requests, 96,000 cumulative output tokens, no next request after 2,000,000 reported input tokens (the last accepted request may exceed this input threshold), 192 public tool requests, 30-minute wall deadline. All failures/retries count; CLI HTTP/stream retry settings are zero, broker has no automatic retry. These budgets and native system prompts differ from the old bounded loops; same-model means a common requested provider/model, not budget-matched causal isolation. No superiority claim from more compute alone. Tool errors are observations, not FALSE labels. Missing/invalid final output is ABSTAIN; preserve original output and failure receipt.

## Public tools and actual isolation

Offline Docker container with `--network none`, read-only root filesystem, read-only `/inputs`, writable `/work` and request/response mailbox only, dropped Linux capabilities and no-new-privileges. No repository, private labels, host home, credentials or Docker socket is mounted. Preflight verifies missing host paths/socket, denied external network, read-only input and executable Python. Native Codex internal sandbox is bypassed only inside this externally isolated container; shell remains inside the Docker namespace.

A localhost HTTP shim in the container passes requests through a file mailbox to a host broker. The host routes only `/v1/responses` to the fixed model and `/tool` to the existing public-only tool implementations. It cannot fetch arbitrary URLs, read model-specified host files, or evaluate generated host code. The model credential stays in the host process. Actual native SSE events are relayed after completion; no model output or tool decisions are synthesized. Private reasoning payloads are excluded from stored/relayed events; observable calls, outputs, usage, errors and timing are retained. The transport buffering makes latency unsuitable for production claims.

CUAD tools are the same `PublicContractTools`; BioDEX uses the same `BioDEXTools` and frozen `TerminologyIndex`, including identical query embeddings. The CLI can additionally implement local algorithms over the public files. Catalog JSON is available for exact membership and local search; host vector search avoids installing NumPy in the isolated container. Static comparators are permitted the same public resources; these runs alone do not compare an equally optimized generated static program or DocETL.

## Evaluation and decision

Score after the CLI exits, with the existing independent evaluator outside the container. Preserve predictions, scripts, event logs, requests, token usage, errors, tool operations and image/code/input hashes. Report primary CUAD span F1 at Jaccard >0.15 (sensitivity >0.5), BioDEX RP@10 (also RP@5/@25), all-record coverage, quote support, downstream relations/count and paired deltas to both static and fixed-review arms. Keep the old exploratory screen: +0.05 primary over both controls and at least three improved documents, with descriptive paired bootstrap. Eight records are insufficient to prove population superiority.

Costs include the shared initial once in standalone comparison, existing terminology preprocessing, new query embeddings, CLI model calls, container startup and failures. Dollar cost remains unknown unless actual billing is available. Image setup and connectivity probes are separately reported. Actual shell actions may not use the provided tool wrapper; audit scripts/events as well as tool-call counts. No single-trace extraction follows unless evidence supports proceeding.

## Reproduction

```sh
docker build -f artifact/Dockerfile.codex-pilot -t swb-codex-pilot:0.151.0 .
PYTHONPATH=src .venv/bin/python -m semantic_workload_bench.codex_pilot --probe --output runs/codex-cli-probe-NEW
PYTHONPATH=src .venv/bin/python -m semantic_workload_bench.codex_pilot --family cuad --output runs/cuad-codex-cli-v1
PYTHONPATH=src .venv/bin/python -m semantic_workload_bench.codex_pilot --family biodex --output runs/biodex-codex-cli-v1
```

Requires existing validated snapshots/static runs and the configured `.env`; never overwrite existing run directories. Official configuration references checked: [custom providers](https://learn.chatgpt.com/docs/config-file/config-advanced), [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference). Actual CLI behavior and captured requests take precedence over documentation assumptions.
