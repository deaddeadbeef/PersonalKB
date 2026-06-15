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
| First local endpoint | Readiness and model-store snapshots exist; endpoint proof not yet captured | Use [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], then [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], then [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] after the loopback response |
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
| You need mixed recall | [[LLM/Study/LLM Active Recall Question Bank]] | 20-question score and miss route |
| You cannot explain a paper | [[LLM/Study/LLM Paper Reading Protocol]] | Claim, method, evidence, limitation, deployment implication |
| You can summarize a paper but cannot defend its evidence or local implication | [[LLM/Study/LLM Paper Claim Ledger]] | Claim, evidence type, limitation, mechanism, local implication, and follow-up proof |
| You have paper claim rows but need to know whether academic proof is complete | [[LLM/Study/LLM Paper Claim Audit Runner]] | Fast-path coverage, source proof, claim anatomy, local implication, and follow-up route audit |
| You have a paper claim but no local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] | Paper claim, mechanism, local implication, route, proof question, and next artifact |
| You have paper routes and local artifacts but cannot defend why they prove mastery | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] | Paper basis, mechanism, local prediction, artifact, metric, failure owner, decision, and oral defense answer |
| You cannot explain tokens, logits, loss, attention, or KV cache | [[LLM/Study/LLM Math and Tensor Shape Primer]] | Worked explanation or shape row |
| You can run local commands but cannot explain the whole serving path | [[LLM/Study/Local LLM End-to-End Mental Model]] | One request explained from artifact, tokenizer, runtime, prefill, decode, route, client, quality, and operations |
| Output continues the prompt, ignores roles, leaks role markers, or behaves unlike the chat model | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] | Model package, tokenizer, chat template, rendered prompt or non-exposure control, route behavior, stop boundary, and downstream evidence audit |
| You have local timing or memory numbers but cannot interpret them | [[LLM/Study/Local LLM Inference Metrics Field Guide]] | Metric owner, request phase, confounder, and next controlled action |
| You are ready for a scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] | Section scores, hard-fail checks, proof links, remediation rows |
| You need to know whether this machine is ready for a first local run | [[LLM/Study/Local LLM First Run Readiness Snapshot]] | Runtime/GPU/listener readiness card and first execution decision |
| You need to decide storage before the first model pull | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] | Disk/cache/PATH evidence and model-store decision card |
| You have workload and candidate facts but no shortlist | [[LLM/Study/Local LLM Model Selection Runner]] | Ranked candidates, memory fit, custody, compatibility, benchmark/quality status, and next route |
| You need to install Ollama without losing the evidence trail | [[LLM/Study/Local LLM Windows Runtime Install Gate]] | Installer source, new-shell PATH, model-store inheritance, listener, and log proof |
| You are ready to pull the first Ollama model | [[LLM/Study/Local LLM First Model Pull Gate]] | Model tag decision, store proof, pull output, list/tags/show metadata, and pass/hold/fail route |
| You need to know whether the local runtime is reachable before endpoint smoke | [[LLM/Study/Local LLM First Runtime Health Snapshot]] | Health JSON/Markdown, installed and loaded model ids, OpenAI-compatible ids, missing layer, and next action |
| You are ready to send the first controlled local inference request | [[LLM/Study/Local LLM First Smoke Request Runner]] | Native and OpenAI-compatible request/response/output files, status, missing layer, and next action |
| You are ready to execute the first local endpoint proof | [[LLM/Study/Local LLM First Endpoint Run Sheet]] | Filled run folder, native response, OpenAI-compatible response, benchmark row, decision row |
| You have a first endpoint run folder and need to know whether it counts | [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]] | Run card, preflight, model custody, runtime health, smoke response, debrief, boundary, and decision audit |
| You have the first response JSON and need to interpret it | [[LLM/Study/Local LLM First Response Debrief Card]] | Route claim, timing conversion, mechanism owner, benchmark add-on row, and next controlled action |
| You want the first saved response interpreted without hand-copying timing fields | [[LLM/Study/Local LLM First Response Debrief Runner]] | Debrief JSON, Markdown, JSONL, converted seconds, token rates, mechanism owner, quality boundary, and next action |
| You have saved request/response files and need phase evidence | [[LLM/Study/LLM Inference Request Lifecycle Runner]] | Client request, prompt assembly, tokenization, prefill, decode, stop, detokenization, application handling, findings, and next owner |
| You have route proof and need a first quality signal | [[LLM/Study/Local LLM First Quality Probe Suite]] | Private prompt-suite outputs, script-assisted checks, human scores, and pass/hold/fail owner |
| You want the first quality signal captured as runnable artifacts | [[LLM/Study/Local LLM First Quality Probe Runner]] | Five request/response/output files, results JSON/CSV/Markdown, JSONL, auto-checks, and next action |
| You have a local `/v1` endpoint and need a client-safe API contract | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] | `/v1/models`, non-streaming chat, streaming, wrong-model failure, contract decision, and JSONL handoff |
| You have an API contract and need sampler controls fixed | [[LLM/Study/Decoding and Sampling Controls Runner]] | Baseline, temperature, seed, stop-string, output-cap, CSV, Markdown, and JSONL evidence |
| You have an API contract and need a reusable client run | [[LLM/Study/Local LLM First Client Harness Runner]] | Python client script, request/response/output files, JSONL row, and next route |
| You have a reusable client run and need perceived-latency proof | [[LLM/Study/Local LLM First Streaming Timing Runner]] | Streaming script, event JSONL, TTFT, chunk counts, final output, and usage/error row |
| You have client or streaming JSONL and need a benchmark row | [[LLM/Study/Local LLM First Benchmark Row Builder]] | Benchmark JSON, Markdown copy row, missing-layer list, and next controlled action |
| You have a long, RAG, tool, or multi-turn prompt and need fit proof | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] | Context manifest, component tokens, reserve, margin, fit decision, drop plan, and JSONL row |
| You have scheduler, KV-cache, queue, or tuning evidence and need a decision audit | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] | Hypothesis, latency phase, scheduler state, long-prompt interference, tuning delta, capacity event, decision card, and next-route audit |
| You need concurrency, queue, saturation, or batch-throughput proof | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] | C1/C2/C4 ladder, per-request latency rows, p50/p95, throughput, errors, saturation, and JSONL row |
| You need repeated-prefix or prompt-cache proof | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] | Shared-prefix hits, changed-prefix controls, TTFT or prompt-eval timing, optional metrics, cache decision, CSV, Markdown, and JSONL row |
| You need speculative decoding proof | [[LLM/Study/Local LLM Speculative Decoding Runner]] | No-spec/spec profiles, TTFT, decode-rate speedup, accepted-token signal, quality checks, CSV, Markdown, and JSONL row |
| You need service-state, metrics, slots, logs, or resource-pressure proof | [[LLM/Study/Local LLM Observability and Operations Runner]] | `/v1/models`, loaded models, metrics, slots, local resource snapshot, redacted log tail, privacy posture, and next controlled action |
| You need restart, upgrade, backup, or rollback proof | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] | Lifecycle manifest, baseline artifacts, backup, rollback target, route state, before/after/rollback decision, CSV, Markdown, and JSONL evidence |
| You need endpoint exposure, log, RAG corpus, tool, UI storage, or export-boundary proof | [[LLM/Study/Local LLM Security and Privacy Runner]] | Manifest, host classification, read-only model-list routes, config/log secret scan, RAG/tool/UI/export boundary, and pass/hold/error decision |
| You need parseable JSON, tool-call, result-injection, or denial proof | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] | Structured JSON, tool call, validation, policy, execution, result injection, denial, CSV, Markdown, and JSONL row |
| You need first local inference proof | [[LLM/Study/Local LLM Windows First-Run Quickstart]] | Preflight, model id, response, listener proof |
| You need exact commands | [[LLM/Study/Local LLM Command Cookbook]] | Saved command output in one run folder |
| You have a response but no evidence packet | [[LLM/Study/Local LLM First Inference Evidence Pack]] | First-run evidence row |
| You have a local failure | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] | Failed layer, evidence, controlled next change |
| You have a saved local failure and need proof-quality diagnosis | [[LLM/Study/Local LLM Failure Triage Runner]] | Symptom, failed layer, proof, mechanism owner, ruled-out layers, and one controlled next action |
| You need to know whether the prompt suite is good enough before scoring quality | [[LLM/Study/Local LLM Evaluation Set Design Runner]] | Workload, held-out/private coverage, contamination controls, rubric, and next-route audit |
| You have quality doubts | [[LLM/Study/Local LLM Quality Evaluation Harness]] | Pass/hold/fail row |
| You used an LLM judge and need to know whether the score is trustworthy | [[LLM/Study/Local LLM Judge Calibration Runner]] | Human agreement, AB/BA order stability, position bias, verbosity bias, and next-route audit |
| You have many local-run artifacts but no keep/tune/reject decision | [[LLM/Study/Local LLM Result Synthesis Runner]] | Selected candidate, evidence contradictions, missing proof, rejected alternative, and next action |
| You need to decide local vs hosted vs hybrid | [[LLM/Study/LLM Deployment Decision Matrix]] | Deployment memo |
| You have a deployment memo and need to audit whether it is defensible | [[LLM/Study/LLM Deployment Readiness Audit Runner]] | Workload, path, model/runtime, endpoint, benchmark, quality, security, operations, cost, rejected alternative, and retest audit |

## Mastery Gates

| Gate | Prove with | Status |
|---|---|---|
| Concept dependency | [[LLM/Study/LLM Concept Dependency Map]] |  |
| Active recall | [[LLM/Study/LLM Active Recall Question Bank]] |  |
| Paper synthesis | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |  |
| Paper claim ledger | [[LLM/Study/LLM Paper Claim Ledger]] |  |
| Paper claim audit | [[LLM/Study/LLM Paper Claim Audit Runner]] |  |
| Paper-to-local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] |  |
| Academic-to-local defense matrix | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] |  |
| Mechanism bridge | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] |  |
| End-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] |  |
| Request lifecycle runner | [[LLM/Study/LLM Inference Request Lifecycle Runner]] |  |
| Template/tokenizer compatibility | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] |  |
| Failure triage | [[LLM/Study/Local LLM Failure Triage Runner]] |  |
| Local inference metric interpretation | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |  |
| Self-assessment exam | [[LLM/Study/LLM Mastery Exam Run Sheet]] |  |
| Mastery evidence audit | [[LLM/Study/LLM Mastery Evidence Audit Runner]] |  |
| Attention implementation | [[LLM/Study/Attention Implementation Lab]] |  |
| Tiny decoder training | [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] |  |
| First local endpoint | [[LLM/Study/Local LLM First Inference Evidence Pack]] and [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]] |  |
| Model selection runner | [[LLM/Study/Local LLM Model Selection Runner]] |  |
| OpenAI-compatible API contract | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |  |
| Decoding control runner | [[LLM/Study/Decoding and Sampling Controls Runner]] |  |
| Context/token budget runner | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |  |
| Scheduler evidence audit | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] |  |
| Concurrency/batch runner | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |  |
| Prompt cache runner | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |  |
| Speculative decoding runner | [[LLM/Study/Local LLM Speculative Decoding Runner]] |  |
| Observability runner | [[LLM/Study/Local LLM Observability and Operations Runner]] |  |
| Lifecycle runner | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |  |
| Security/privacy runner | [[LLM/Study/Local LLM Security and Privacy Runner]] |  |
| Reproducible client call | [[LLM/Study/Local LLM Client Harness Lab]] |  |
| Runtime comparison | [[LLM/Study/Local LLM Runtime Comparison Lab]] |  |
| Evaluation set design | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |  |
| Quality evaluation | [[LLM/Study/Local LLM Quality Evaluation Harness]] |  |
| Judge calibration | [[LLM/Study/Local LLM Judge Calibration Runner]] |  |
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
| One paper claim/evidence/limitation row | [[LLM/Study/LLM Paper Claim Ledger]] |
| One paper claim audit output | [[LLM/Study/LLM Paper Claim Audit Runner]] |
| One paper-to-local proof route | [[LLM/Study/LLM Paper-to-Local Proof Router]] |
| One academic-to-local defense matrix output | [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]] |
| One complete daily study session | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] |
| One mechanism-to-local-control row | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] or capstone note |
| One end-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] or capstone note |
| One interpreted local inference benchmark row | [[LLM/Study/Local LLM Inference Metrics Field Guide]] or [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One machine-specific first-run readiness row | [[LLM/Study/Local LLM First Run Readiness Snapshot]] |
| One machine-specific model-store decision row | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] |
| One runtime install gate row | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| One first model pull gate row | [[LLM/Study/Local LLM First Model Pull Gate]] |
| One first runtime health snapshot | [[LLM/Study/Local LLM First Runtime Health Snapshot]] |
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
| One model selection runner output | [[LLM/Study/Local LLM Model Selection Runner]] |
| One OpenAI-compatible contract runner output | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| One decoding control runner output | [[LLM/Study/Decoding and Sampling Controls Runner]] |
| One first client harness run | [[LLM/Study/Local LLM First Client Harness Runner]] |
| One first streaming timing row | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| One first benchmark-row builder output | [[LLM/Study/Local LLM First Benchmark Row Builder]] |
| One context/token budget runner output | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |
| One scheduler evidence audit output | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] |
| One concurrency/batch runner output | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]] |
| One prompt-cache runner output | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |
| One speculative decoding runner output | [[LLM/Study/Local LLM Speculative Decoding Runner]] |
| One observability runner output | [[LLM/Study/Local LLM Observability and Operations Runner]] |
| One lifecycle runner output | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |
| One security/privacy runner output | [[LLM/Study/Local LLM Security and Privacy Runner]] |
| One RAG evidence runner output | [[LLM/Study/Local RAG Evidence Runner]] |
| One tool/structured-output runner output | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |
| One deployment readiness audit output | [[LLM/Study/LLM Deployment Readiness Audit Runner]] |
| One first endpoint command output | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| One benchmark row | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One quality prompt-suite design audit | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |
| One quality decision | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| One judge calibration output when LLM-as-judge is used | [[LLM/Study/Local LLM Judge Calibration Runner]] |
| One local result synthesis output before writing the deployment memo | [[LLM/Study/Local LLM Result Synthesis Runner]] |
| One failure diagnosis | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| One machine-checkable failure triage output | [[LLM/Study/Local LLM Failure Triage Runner]] |
| One scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] |
| One mastery evidence audit output | [[LLM/Study/LLM Mastery Evidence Audit Runner]] |
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
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
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
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
