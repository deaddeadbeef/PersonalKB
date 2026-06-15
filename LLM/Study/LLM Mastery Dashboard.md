---
tags: [study, llm, mastery, dashboard, review, capstone]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Dashboard

> **One-line summary** This is the daily home base for LLM mastery: choose today's recall, today's study route, today's proof artifact, and the next action when a concept or local inference run fails.

Use this before opening the broader map. The vault already has deep notes; this dashboard keeps the day small enough to execute.

## Today

| Slot | Choice | Link or evidence |
|---|---|---|
| Recall prompt |  | [[LLM/Study/LLM Active Recall Question Bank]] |
| Concept route |  | [[LLM/Study/LLM Concept Dependency Map]] |
| Applied proof |  | [[LLM/Study/Local LLM Hands-On Practicum Sequence]] |
| Evidence destination |  | [[LLM/Study/LLM Mastery Capstone Workbook]] |
| Session sheet |  | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] |
| Stop rule | Stop after one saved answer, row, command output, or decision |  |

If there is no saved answer or evidence row, the session was reading, not mastery progress.

## Current Snapshot

| Area | Status | Next proof |
|---|---|---|
| Field map and papers | Not yet proven today | Explain one paper cluster without notes |
| Math and mechanisms | Not yet proven today | Work one token/logit/attention/KV-cache explanation |
| Training and alignment | Not yet proven today | Trace one behavior through data, objective, post-training, and evaluation |
| First local endpoint | Readiness and model-store snapshots exist; endpoint proof not yet captured | Use [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], verify with [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]], then [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], then [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] and [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] before capstone promotion |
| Model and runtime choice | First model ladder exists; storage decision snapshot points to `D:\Models` | Write provenance, compatibility, or sizing row after runtime install evidence |
| Benchmark and quality | Not yet proven today | Run [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] after route proof, then save benchmark and quality row for one prompt class |
| RAG/tools | Not yet proven today | Save retrieval, citation, structured-output, tool-schema, tool-result, or denied-action row |
| Operations and deployment | Not yet proven today | Save security, lifecycle, observability, or deployment decision row |

Replace "Not yet proven today" only with a link to an artifact or a dated note.

## Next Action Router

| If the problem is | Go to | Produce |
|---|---|---|
| You do not know what to study next | [[LLM/Study/LLM Concept Dependency Map]] | Lowest unproven dependency |
| You need to turn this study block into evidence | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] | Recall answer, mechanism bridge, applied artifact or blocker, capstone link |
| You are ready to turn the study path into one buildable project | [[LLM/Study/Local LLM Capstone Project Blueprint]] | Local assistant blueprint, evidence bundle, defense questions, and pass/hold/fail decision |
| You have proof links and need to know whether mastery evidence is defensible | [[LLM/Study/LLM Mastery Evidence Audit Runner]] | Academic, mechanism, local-inference, system, exam, pass/hold/fail, and next-route audit |
| You have many held gates and need one next action | [[LLM/Study/LLM Mastery Gap Triage Runner]] | Ranked gaps, top route, top action, owner, and domain summary |
| You need mixed recall | [[LLM/Study/LLM Active Recall Question Bank]] | 20-question score and miss route |
| You have scored recall/exam rows and need to know whether they count | [[LLM/Study/LLM Recall and Remediation Audit Runner]] | Coverage, scores, misses, remediation artifacts, next reviews, and applied proof |
| You cannot explain a paper | [[LLM/Study/LLM Paper Reading Protocol]] | Claim, method, evidence, limitation, deployment implication |
| You can summarize a paper but cannot defend its evidence or local implication | [[LLM/Study/LLM Paper Claim Ledger]] | Claim, evidence type, limitation, mechanism, local implication, and follow-up proof |
| You have paper claim rows but need to know whether academic proof is complete | [[LLM/Study/LLM Paper Claim Audit Runner]] | Fast-path coverage, source proof, claim anatomy, local implication, and follow-up route audit |
| You can read a paper but cannot answer defense questions without notes | [[LLM/Study/LLM Paper Oral Defense Runner]] | No-notes answers, source proof, mechanism, local implication, score, and remediation |
| You have a paper claim but no local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] | Paper claim, mechanism, local implication, route, proof question, and next artifact |
| You have paper routes and local artifacts but cannot defend why they prove mastery | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] | Paper basis, mechanism, local prediction, artifact, metric, failure owner, decision, and oral defense answer |
| You cannot explain tokens, logits, loss, attention, or KV cache | [[LLM/Study/LLM Math and Tensor Shape Primer]] | Worked explanation or shape row |
| You can run local commands but cannot explain the whole serving path | [[LLM/Study/Local LLM End-to-End Mental Model]] | One request explained from artifact, tokenizer, runtime, prefill, decode, route, client, quality, and operations |
| Output continues the prompt, ignores roles, leaks role markers, or behaves unlike the chat model | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] | Health-bound first-response debrief, model package, tokenizer, chat template, rendered prompt or non-exposure control, route behavior, stop boundary, and downstream evidence audit |
| You have local timing or memory numbers but cannot interpret them | [[LLM/Study/Local LLM Inference Metrics Field Guide]] | Metric owner, request phase, confounder, and next controlled action |
| You are ready for a scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] | Section scores, hard-fail checks, proof links, remediation rows |
| You need to know whether this machine is ready for a first local run | [[LLM/Study/Local LLM First Run Readiness Snapshot]] | Runtime/GPU/listener readiness card and first execution decision |
| You need to know whether the first model tags are still current | [[LLM/Study/Local LLM First Model Source Recheck Runner]] | Current source-page pass/hold/fail for selected tag, digest, size, context, modality, and quantization |
| You need to decide storage before the first model pull | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] | Disk/cache/PATH evidence and model-store decision card |
| You need one reviewed command plan before the first local run | [[LLM/Study/Local LLM First Run Command Plan Runner]] | Ordered PowerShell plan, run folder, evidence filenames, loopback checks, and next gate manifests |
| You have config, tokenizer, Ollama show, or file-list evidence but no normalized model facts | [[LLM/Study/Local LLM Model Metadata Card Runner]] | Architecture, tokenizer, template, context, quantization, inventory, and downstream handoff fields |
| You have model architecture, context, and concurrency facts but no KV-cache fit proof | [[LLM/Study/Local LLM KV Cache Sizing Runner]] | Head-aware MHA/MQA/GQA cache estimate, cache dtype, budget, margin, fit status, and next route |
| You have model size, context, and hardware facts but no fit decision | [[LLM/Study/Local LLM Hardware Sizing Runner]] | Weight memory, KV-cache, runtime overhead, active sequences, context target, headroom, fit status, and next route |
| You have workload and candidate facts but no shortlist | [[LLM/Study/Local LLM Model Selection Runner]] | Ranked candidates, memory fit, custody, compatibility, benchmark/quality status, and next route |
| You selected a candidate model but have not proven license, gated access, artifact pinning, and unsafe-file posture | [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]] | Candidate source, model card, requested use, license flags, gate status, pinned revision, file safety, pass/hold/fail decision, and next route |
| You have artifact, runtime, tokenizer, or route facts but no compatibility decision | [[LLM/Study/Local LLM Runtime Compatibility Runner]] | Architecture, artifact, quantization, tokenizer, template, runtime, route, custody, sizing, and next proof audit |
| You are serving a GGUF model with llama.cpp but have not proven the endpoint | [[LLM/Study/Local llama.cpp GGUF Server Runner]] | Launch command, GGUF path, alias, loopback listener, `/health`, `/v1/models`, chat response, metrics/offload, and upstream handoffs |
| You need to install Ollama without losing the evidence trail | [[LLM/Study/Local LLM Windows Runtime Install Gate]] | Installer source, new-shell PATH, model-store inheritance, listener, and log proof |
| You installed or opened Ollama and need a repeatable readiness verdict | [[LLM/Study/Local LLM Windows Runtime Install Runner]] | JSON, Markdown, CSV, and JSONL install-readiness verdict for command, version, model-store env, loopback listener, `/api/version`, and `/api/tags` |
| You are ready to pull the first Ollama model | [[LLM/Study/Local LLM First Model Pull Gate]] | Model tag decision, store proof, pull output, list/tags/show metadata, and pass/hold/fail route |
| You pulled the first model and need to know whether it counts | [[LLM/Study/Local LLM First Model Pull Runner]] | Selected tag, source check, store decision, pull output, CLI/API inventory, show metadata, and next route audit |
| You need to know whether the local runtime is reachable before endpoint smoke | [[LLM/Study/Local LLM First Runtime Health Snapshot]] | Health JSON/Markdown, installed and loaded model ids, OpenAI-compatible ids, missing layer, and next action |
| You need a repeatable no-generation runtime health verdict | [[LLM/Study/Local LLM First Runtime Health Runner]] | Listener, native API, `/api/tags`, `/api/ps`, `/v1/models`, expected-model visibility, boundary, and pass/hold/fail output |
| You are ready to send the first controlled local inference request | [[LLM/Study/Local LLM First Smoke Request Runner]] | Runtime-health JSON plus native and OpenAI-compatible request/response/output files, status, missing layer, and next action |
| You are ready to execute the first local endpoint proof | [[LLM/Study/Local LLM First Endpoint Run Sheet]] | Filled run folder, native response, OpenAI-compatible response, benchmark row, decision row |
| You have a first endpoint run folder and need to know whether it counts | [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]] | Run card, preflight, model custody, runtime health, smoke response, pass-state debrief, template/tokenizer compatibility, boundary, and decision audit |
| You have the first response JSON and need to interpret it | [[LLM/Study/Local LLM First Response Debrief Card]] | Route claim, timing conversion, mechanism owner, benchmark add-on row, and next controlled action |
| You want the first saved response interpreted without hand-copying timing fields | [[LLM/Study/Local LLM First Response Debrief Runner]] | Health-bound smoke proof, debrief JSON, Markdown, JSONL, converted seconds, token rates, mechanism owner, quality boundary, and next action |
| You have saved request/response files and need phase evidence | [[LLM/Study/LLM Inference Request Lifecycle Runner]] | Client request, prompt assembly, tokenization, prefill, decode, stop, detokenization, application handling, findings, and next owner |
| You have route proof and need a first quality signal | [[LLM/Study/Local LLM First Quality Probe Suite]] | Private prompt-suite outputs, script-assisted checks, human scores, and pass/hold/fail owner |
| You want the first quality signal captured as runnable artifacts | [[LLM/Study/Local LLM First Quality Probe Runner]] | Passing endpoint audit, five request/response/output files, results JSON/CSV/Markdown, JSONL, auto-checks, and next action |
| You have a local `/v1` endpoint and need a client-safe API contract | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] | `/v1/models`, non-streaming chat, streaming, wrong-model failure, contract decision, and JSONL handoff |
| You connected Open WebUI to a local provider and need to know whether the UI evidence counts | [[LLM/Study/Local Open WebUI Provider Integration Runner]] | Open WebUI identity, loopback boundary, provider route, expected model visibility, transcript, persistence, secret handling, and handoffs |
| You have an API contract and need sampler controls fixed | [[LLM/Study/Decoding and Sampling Controls Runner]] | Baseline, temperature, seed, stop-string, output-cap, CSV, Markdown, and JSONL evidence |
| You have thinking-mode or reasoning-effort evidence and need to know whether it is worth the cost | [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]] | Effort sweep, parser separation, trace policy, latency cost, quality delta, selected effort, and retest trigger |
| You have an API contract and need a reusable client run | [[LLM/Study/Local LLM First Client Harness Runner]] | Python client script, request/response/output files, JSONL row, and next route |
| You wired the client into an app, CLI, UI, job, RAG, or tool loop and need to know whether it counts | [[LLM/Study/Local LLM Application Integration Evidence Runner]] | App contract, endpoint, client flow, user flow, response handling, failure behavior, privacy/logging, evaluation, operations, and promotion audit |
| You have a reusable client run and need perceived-latency proof | [[LLM/Study/Local LLM First Streaming Timing Runner]] | Streaming script, event JSONL, TTFT, chunk counts, final output, and usage/error row |
| You have client or streaming JSONL and need a benchmark row | [[LLM/Study/Local LLM First Benchmark Row Builder]] | Benchmark JSON, Markdown copy row, missing-layer list, and next controlled action |
| You have benchmark rows and need to know whether the numbers are interpretable | [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]] | Workload, route/model identity, proof, token counts, timing, memory/context, fixed settings, quality boundary, and next-action audit |
| You compared local runtimes and need to know whether the winner is defensible | [[LLM/Study/Local LLM Runtime Comparison Runner]] | Fixed controls, endpoint proof, benchmark audit, quality boundary, security boundary, selected runtime, rejected alternative, and review trigger |
| You have a long, RAG, tool, or multi-turn prompt and need fit proof | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] | Context manifest, component tokens, reserve, margin, fit decision, drop plan, and JSONL row |
| You can quote tokens/sec but cannot explain p95 latency under load | [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]] | Arrival rate, service time, utilization, queue wait, tail latency, prefill/decode, admission policy, and proof worksheet |
| You have scheduler, KV-cache, queue, or tuning evidence and need a decision audit | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] | Hypothesis, latency phase, scheduler state, long-prompt interference, tuning delta, capacity event, decision card, and next-route audit |
| You have quantization, GPU-offload, KV-cache precision, benchmark, and quality rows and need a keep/reject audit | [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]] | Baseline, artifact/runtime support, memory estimate, load state, offload sweep, KV-cache/context, benchmark, quality, rejected alternative, decision card, and next-route audit |
| You need concurrency, queue, saturation, or batch-throughput proof | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] | C1/C2/C4 ladder, per-request latency rows, p50/p95, throughput, errors, saturation, and JSONL row |
| You have measured load evidence and need to know whether it satisfies the workload SLO | [[LLM/Study/Local LLM Capacity and SLO Planning Runner]] | Latency target, throughput target, concurrency limit, error budget, resource headroom, admission policy, security boundary, owner, and retest trigger audit |
| You need repeated-prefix or prompt-cache proof | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] | Shared-prefix hits, changed-prefix controls, TTFT or prompt-eval timing, optional metrics, cache decision, CSV, Markdown, and JSONL row |
| You need speculative decoding proof | [[LLM/Study/Local LLM Speculative Decoding Runner]] | No-spec/spec profiles, TTFT, decode-rate speedup, accepted-token signal, quality checks, CSV, Markdown, and JSONL row |
| You need service-state, metrics, slots, logs, or resource-pressure proof | [[LLM/Study/Local LLM Observability and Operations Runner]] | `/v1/models`, loaded models, metrics, slots, local resource snapshot, redacted log tail, privacy posture, and next controlled action |
| You need restart, upgrade, backup, or rollback proof | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] | Lifecycle manifest, baseline artifacts, backup, rollback target, route state, before/after/rollback decision, CSV, Markdown, and JSONL evidence |
| You need endpoint exposure, log, RAG corpus, tool, UI storage, or export-boundary proof | [[LLM/Study/Local LLM Security and Privacy Runner]] | Manifest, host classification, read-only model-list routes, config/log secret scan, RAG/tool/UI/export boundary, and pass/hold/error decision |
| You retrieved untrusted or poisoned RAG content and need to know whether the source boundary held | [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]] | Attack cases, selected context, delimiters, source tags, answer behavior, citations, tools, exports, guardrails, and pass/hold/fail decision |
| You need parseable JSON, tool-call, result-injection, or denial proof | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] | Structured JSON, tool call, validation, policy, execution, result injection, denial, CSV, Markdown, and JSONL row |
| You need first local inference proof | [[LLM/Study/Local LLM Windows First-Run Quickstart]] | Preflight, model id, response, listener proof |
| You need a generated first-run command sequence | [[LLM/Study/Local LLM First Run Command Plan Runner]] | Safe planning artifact before install, pull, health, smoke, audit, and capstone routing |
| You need exact commands | [[LLM/Study/Local LLM Command Cookbook]] | Saved command output in one run folder |
| You have a response but no evidence packet | [[LLM/Study/Local LLM First Inference Evidence Pack]] | First-run evidence row |
| You have a first-run folder and need to know whether it is capstone-ready | [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]] | Endpoint, API contract, client, benchmark, quality, security, and decision pass/hold/fail audit |
| You have a local failure | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] | Failed layer, evidence, controlled next change |
| You have a saved local failure and need proof-quality diagnosis | [[LLM/Study/Local LLM Failure Triage Runner]] | Symptom, failed layer, proof, mechanism owner, ruled-out layers, and one controlled next action |
| You need to know whether the prompt suite is good enough before scoring quality | [[LLM/Study/Local LLM Evaluation Set Design Runner]] | Workload, held-out/private coverage, contamination controls, rubric, and next-route audit |
| You have quality doubts | [[LLM/Study/Local LLM Quality Evaluation Harness]] | Pass/hold/fail row |
| You have scored prompt-suite rows and need machine-checkable quality proof | [[LLM/Study/Local LLM Quality Evaluation Runner]] | Prompt/response proof, rubric scores, boundary evidence, pass/hold/fail JSON, CSV, Markdown, and JSONL |
| You used an LLM judge and need to know whether the score is trustworthy | [[LLM/Study/Local LLM Judge Calibration Runner]] | Human agreement, AB/BA order stability, position bias, verbosity bias, and next-route audit |
| You have a quality gap and are tempted to fine-tune or train an adapter | [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]] | Baseline failure, selected method, rejected alternatives, dataset split, privacy, chat template, method config, held-out eval, deployment, and rollback audit |
| You have many local-run artifacts but no keep/tune/reject decision | [[LLM/Study/Local LLM Result Synthesis Runner]] | Selected candidate, evidence contradictions, missing proof, rejected alternative, and next action |
| You need to decide local vs hosted vs hybrid | [[LLM/Study/LLM Deployment Decision Matrix]] | Deployment memo |
| You have a deployment memo and need to audit whether it is defensible | [[LLM/Study/LLM Deployment Readiness Audit Runner]] | Workload, path, model/runtime, endpoint, benchmark, quality, security, operations, cost, rejected alternative, and retest audit |

## Mastery Gates

| Gate | Prove with | Status |
|---|---|---|
| Concept dependency | [[LLM/Study/LLM Concept Dependency Map]] |  |
| Active recall | [[LLM/Study/LLM Active Recall Question Bank]] |  |
| Recall remediation audit | [[LLM/Study/LLM Recall and Remediation Audit Runner]] |  |
| Paper synthesis | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |  |
| Paper claim ledger | [[LLM/Study/LLM Paper Claim Ledger]] |  |
| Paper claim audit | [[LLM/Study/LLM Paper Claim Audit Runner]] |  |
| Paper oral defense | [[LLM/Study/LLM Paper Oral Defense Runner]] |  |
| Paper-to-local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] |  |
| Academic-to-local defense matrix | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] |  |
| Mechanism bridge | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] |  |
| End-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] |  |
| Request lifecycle runner | [[LLM/Study/LLM Inference Request Lifecycle Runner]] |  |
| Template/tokenizer compatibility | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] |  |
| Failure triage | [[LLM/Study/Local LLM Failure Triage Runner]] |  |
| Local inference metric interpretation | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |  |
| Benchmark evidence audit | [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]] |  |
| Self-assessment exam | [[LLM/Study/LLM Mastery Exam Run Sheet]] |  |
| Mastery evidence audit | [[LLM/Study/LLM Mastery Evidence Audit Runner]] |  |
| Mastery gap triage | [[LLM/Study/LLM Mastery Gap Triage Runner]] |  |
| Attention implementation | [[LLM/Study/Attention Implementation Lab]] |  |
| Tiny decoder training | [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] |  |
| First local endpoint | [[LLM/Study/Local LLM First Inference Evidence Pack]], [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]], and [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]] |  |
| First model pull runner | [[LLM/Study/Local LLM First Model Pull Runner]] |  |
| First runtime health runner | [[LLM/Study/Local LLM First Runtime Health Runner]] |  |
| First smoke request runner | [[LLM/Study/Local LLM First Smoke Request Runner]] |  |
| First response debrief runner | [[LLM/Study/Local LLM First Response Debrief Runner]] |  |
| Model metadata card runner | [[LLM/Study/Local LLM Model Metadata Card Runner]] |  |
| KV-cache sizing runner | [[LLM/Study/Local LLM KV Cache Sizing Runner]] |  |
| Hardware sizing runner | [[LLM/Study/Local LLM Hardware Sizing Runner]] |  |
| Model selection runner | [[LLM/Study/Local LLM Model Selection Runner]] |  |
| Model acquisition license gate | [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]] |  |
| Artifact custody audit | [[LLM/Study/Local LLM Artifact Custody Audit Runner]] |  |
| Runtime compatibility runner | [[LLM/Study/Local LLM Runtime Compatibility Runner]] |  |
| llama.cpp GGUF server runner | [[LLM/Study/Local llama.cpp GGUF Server Runner]] |  |
| Quantization/offload evidence | [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]] |  |
| OpenAI-compatible API contract | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |  |
| Open WebUI provider integration | [[LLM/Study/Local Open WebUI Provider Integration Runner]] |  |
| Decoding control runner | [[LLM/Study/Decoding and Sampling Controls Runner]] |  |
| Reasoning budget runner | [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]] |  |
| Context/token budget runner | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |  |
| Queueing/tail latency | [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]] |  |
| Scheduler evidence audit | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] |  |
| Concurrency/batch runner | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |  |
| Prompt cache runner | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |  |
| Speculative decoding runner | [[LLM/Study/Local LLM Speculative Decoding Runner]] |  |
| Observability runner | [[LLM/Study/Local LLM Observability and Operations Runner]] |  |
| Lifecycle runner | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |  |
| Security/privacy runner | [[LLM/Study/Local LLM Security and Privacy Runner]] |  |
| RAG injection/source boundary | [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]] |  |
| Reproducible client call | [[LLM/Study/Local LLM Client Harness Lab]] |  |
| Application integration audit | [[LLM/Study/Local LLM Application Integration Evidence Runner]] |  |
| Runtime comparison | [[LLM/Study/Local LLM Runtime Comparison Lab]] |  |
| Runtime comparison runner | [[LLM/Study/Local LLM Runtime Comparison Runner]] |  |
| Capacity/SLO planning | [[LLM/Study/Local LLM Capacity and SLO Planning Runner]] |  |
| Evaluation set design | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |  |
| Quality evaluation | [[LLM/Study/Local LLM Quality Evaluation Harness]] |  |
| Quality evaluation runner | [[LLM/Study/Local LLM Quality Evaluation Runner]] |  |
| Judge calibration | [[LLM/Study/Local LLM Judge Calibration Runner]] |  |
| Adaptation readiness | [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]] |  |
| Result synthesis | [[LLM/Study/Local LLM Result Synthesis Runner]] |  |
| RAG assistant | [[LLM/Study/Local RAG Minimal Python Harness]] |  |
| RAG evidence runner | [[LLM/Study/Local RAG Evidence Runner]] |  |
| Tool loop | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |  |
| Tool/schema runner | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |  |
| Operations and safety | [[LLM/Study/Local LLM Security and Privacy Runbook]] |  |
| Deployment decision | [[LLM/Study/LLM Deployment Decision Matrix]] |  |
| Deployment readiness audit | [[LLM/Study/LLM Deployment Readiness Audit Runner]] |  |
| Capstone project | [[LLM/Study/Local LLM Capstone Project Blueprint]] |  |

Status values should be links, not feelings: `not started`, `in progress: <artifact>`, `passed: <artifact>`, or `blocked: <diagnostic row>`.

## Weekly Board

| Week focus | Recall proof | Applied proof | Capstone link |
|---|---|---|---|
| 0 Setup and baseline |  |  |  |
| 1 Field map and tokens |  |  |  |
| 2 Attention and shapes |  |  |  |
| 3 Training pipeline |  |  |  |
| 4 Papers and evaluation |  |  |  |
| 5 First local endpoint |  |  |  |
| 6 Model selection and custody |  |  |  |
| 7 Compatibility and request controls |  |  |  |
| 8 Benchmark and serving internals |  |  |  |
| 9 Operations and safety |  |  |  |
| 10 RAG |  |  |  |
| 11 Tools, adaptation, deployment |  |  |  |
| 12 Oral exam and capstone |  |  |  |

Use [[LLM/Study/LLM Mastery Study Cadence]] for the full weekly rhythm. This table is only the working status board.

## Evidence Queue

| Evidence to add | Destination |
|---|---|
| One unanswered recall prompt and corrected answer | [[LLM/Study/LLM Active Recall Question Bank]] or dated study note |
| One recall/remediation audit output | [[LLM/Study/LLM Recall and Remediation Audit Runner]] |
| One paper claim/evidence/limitation row | [[LLM/Study/LLM Paper Claim Ledger]] |
| One paper claim audit output | [[LLM/Study/LLM Paper Claim Audit Runner]] |
| One paper oral defense runner output | [[LLM/Study/LLM Paper Oral Defense Runner]] |
| One paper-to-local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] |
| One academic-to-local defense matrix output | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] |
| One complete daily study session | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] |
| One mechanism-to-local-control row | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] or capstone note |
| One end-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] or capstone note |
| One interpreted local inference benchmark row | [[LLM/Study/Local LLM Inference Metrics Field Guide]] or [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One machine-specific first-run readiness row | [[LLM/Study/Local LLM First Run Readiness Snapshot]] |
| One first model source recheck row | [[LLM/Study/Local LLM First Model Source Recheck Runner]] |
| One machine-specific model-store decision row | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] |
| One reviewed first-run command plan | [[LLM/Study/Local LLM First Run Command Plan Runner]] |
| One runtime install gate row | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| One runtime install runner output before first model pull | [[LLM/Study/Local LLM Windows Runtime Install Runner]] |
| One first model pull gate row | [[LLM/Study/Local LLM First Model Pull Gate]] |
| One first model pull runner output before runtime health or endpoint smoke | [[LLM/Study/Local LLM First Model Pull Runner]] |
| One first runtime health snapshot | [[LLM/Study/Local LLM First Runtime Health Snapshot]] |
| One first runtime health runner output before smoke request | [[LLM/Study/Local LLM First Runtime Health Runner]] |
| One first smoke request summary | [[LLM/Study/Local LLM First Smoke Request Runner]] |
| One first endpoint run folder | [[LLM/Study/Local LLM First Endpoint Run Sheet]] |
| One first endpoint evidence audit output | [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]] |
| One first response debrief row | [[LLM/Study/Local LLM First Response Debrief Card]] |
| One first response debrief runner output | [[LLM/Study/Local LLM First Response Debrief Runner]] |
| One request lifecycle runner output | [[LLM/Study/LLM Inference Request Lifecycle Runner]] |
| One template/tokenizer compatibility runner output before quality or deployment decisions that depend on chat behavior | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] |
| One first quality probe suite | [[LLM/Study/Local LLM First Quality Probe Suite]] |
| One first quality probe runner output | [[LLM/Study/Local LLM First Quality Probe Runner]] |
| One evaluation set design runner output before repeated quality, model/runtime, or deployment decisions | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |
| One head-aware KV-cache sizing output before long-context, concurrency, or model-selection evidence depends on cache fit | [[LLM/Study/Local LLM KV Cache Sizing Runner]] |
| One hardware sizing runner output before model selection, model pull, or serving | [[LLM/Study/Local LLM Hardware Sizing Runner]] |
| One model selection runner output | [[LLM/Study/Local LLM Model Selection Runner]] |
| One model acquisition/license gate output before download, serving, benchmark, or deployment evidence depends on a candidate | [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]] |
| One artifact custody audit output before compatibility, serving, benchmark, or deployment evidence depends on local bytes | [[LLM/Study/Local LLM Artifact Custody Audit Runner]] |
| One runtime compatibility runner output before model pull, runtime health, smoke testing, or benchmarking | [[LLM/Study/Local LLM Runtime Compatibility Runner]] |
| One OpenAI-compatible contract runner output | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| One Open WebUI provider integration runner output before UI transcripts support app, security, lifecycle, or capstone claims | [[LLM/Study/Local Open WebUI Provider Integration Runner]] |
| One decoding control runner output | [[LLM/Study/Decoding and Sampling Controls Runner]] |
| One reasoning-budget runner output before quality, runtime, result-synthesis, or deployment decisions depend on thinking mode | [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]] |
| One first client harness run | [[LLM/Study/Local LLM First Client Harness Runner]] |
| One application integration evidence audit output | [[LLM/Study/Local LLM Application Integration Evidence Runner]] |
| One first streaming timing row | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| One first benchmark-row builder output | [[LLM/Study/Local LLM First Benchmark Row Builder]] |
| One benchmark evidence audit output before result synthesis or deployment depends on timing, throughput, or memory numbers | [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]] |
| One runtime comparison runner output before deployment depends on an Ollama, LM Studio, llama.cpp, vLLM, SGLang, Docker, WSL, or UI-over-provider choice | [[LLM/Study/Local LLM Runtime Comparison Runner]] |
| One context/token budget runner output | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |
| One queueing/tail-latency worksheet output | [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]] |
| One scheduler evidence audit output | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] |
| One quantization/offload evidence runner output before result synthesis depends on a lower-bit artifact, GPU-offload setting, CPU fallback, or KV-cache precision | [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]] |
| One concurrency/batch runner output | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |
| One capacity/SLO audit output | [[LLM/Study/Local LLM Capacity and SLO Planning Runner]] |
| One prompt-cache runner output | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |
| One speculative decoding runner output | [[LLM/Study/Local LLM Speculative Decoding Runner]] |
| One observability runner output | [[LLM/Study/Local LLM Observability and Operations Runner]] |
| One lifecycle runner output | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |
| One security/privacy runner output | [[LLM/Study/Local LLM Security and Privacy Runner]] |
| One RAG evidence runner output | [[LLM/Study/Local RAG Evidence Runner]] |
| One RAG prompt-injection/source-boundary runner output before untrusted retrieved content supports tools, exports, app workflows, or capstone claims | [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]] |
| One tool/structured-output runner output | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |
| One deployment readiness audit output | [[LLM/Study/LLM Deployment Readiness Audit Runner]] |
| One first endpoint command output | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| One first inference evidence pack audit output | [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]] |
| One benchmark row | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One quality prompt-suite design audit | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |
| One quality decision | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| One quality evaluation runner output before result synthesis or deployment readiness depends on quality | [[LLM/Study/Local LLM Quality Evaluation Runner]] |
| One judge calibration output when LLM-as-judge is used | [[LLM/Study/Local LLM Judge Calibration Runner]] |
| One adaptation/fine-tuning readiness output before training, adapter serving, or no-train decision supports result synthesis | [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]] |
| One local result synthesis output before writing the deployment memo | [[LLM/Study/Local LLM Result Synthesis Runner]] |
| One failure diagnosis | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| One machine-checkable failure triage output | [[LLM/Study/Local LLM Failure Triage Runner]] |
| One scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] |
| One mastery evidence audit output | [[LLM/Study/LLM Mastery Evidence Audit Runner]] |
| One mastery gap triage output after a hold/fail audit | [[LLM/Study/LLM Mastery Gap Triage Runner]] |
| One end-to-end capstone project spec | [[LLM/Study/Local LLM Capstone Project Blueprint]] |
| One final pass signal | [[LLM/Study/LLM Mastery Capstone Workbook]] |

## Anti-Drift Rules

- Do not add another reading target until today's recall answer exists.
- Do not benchmark until model id, route, sampler, and context target are fixed.
- Do not change two runtime variables in the same comparison.
- Do not judge RAG generation until retrieval evidence exists.
- Do not expose a local endpoint beyond loopback until the security row exists.
- Do not call a gate complete unless the capstone workbook links the artifact.

## Completion Gate

This dashboard is useful when:

- [ ] today's section has one filled recall row
- [ ] today's section has one filled evidence destination
- [ ] the current snapshot uses artifact links instead of vague status
- [ ] the next action router points every miss to a concrete note
- [ ] the capstone workbook has the final pass or remediation link

## References

- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Study Cadence]]
- [[LLM/Study/LLM Daily Mastery Session Run Sheet]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM Capstone Project Blueprint]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Mastery Gap Triage Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper Oral Defense Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM First Run Command Plan Runner]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM Windows Runtime Install Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM Application Integration Evidence Runner]]
- [[LLM/Study/Local Open WebUI Provider Integration Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Runner]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
