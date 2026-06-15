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
| RAG/tools | Not yet proven today | Save retrieval, citation, tool-schema, or denied-action row |
| Operations and deployment | Not yet proven today | Save security, lifecycle, observability, or deployment decision row |

Replace "Not yet proven today" only with a link to an artifact or a dated note.

## Next Action Router

| If the problem is | Go to | Produce |
|---|---|---|
| You do not know what to study next | [[LLM/Study/LLM Concept Dependency Map]] | Lowest unproven dependency |
| You need to turn this study block into evidence | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] | Recall answer, mechanism bridge, applied artifact or blocker, capstone link |
| You are ready to turn the study path into one buildable project | [[LLM/Study/Local LLM Capstone Project Blueprint]] | Local assistant blueprint, evidence bundle, defense questions, and pass/hold/fail decision |
| You need mixed recall | [[LLM/Study/LLM Active Recall Question Bank]] | 20-question score and miss route |
| You cannot explain a paper | [[LLM/Study/LLM Paper Reading Protocol]] | Claim, method, evidence, limitation, deployment implication |
| You can summarize a paper but cannot defend its evidence or local implication | [[LLM/Study/LLM Paper Claim Ledger]] | Claim, evidence type, limitation, mechanism, local implication, and follow-up proof |
| You cannot explain tokens, logits, loss, attention, or KV cache | [[LLM/Study/LLM Math and Tensor Shape Primer]] | Worked explanation or shape row |
| You can run local commands but cannot explain the whole serving path | [[LLM/Study/Local LLM End-to-End Mental Model]] | One request explained from artifact, tokenizer, runtime, prefill, decode, route, client, quality, and operations |
| You have local timing or memory numbers but cannot interpret them | [[LLM/Study/Local LLM Inference Metrics Field Guide]] | Metric owner, request phase, confounder, and next controlled action |
| You are ready for a scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] | Section scores, hard-fail checks, proof links, remediation rows |
| You need to know whether this machine is ready for a first local run | [[LLM/Study/Local LLM First Run Readiness Snapshot]] | Runtime/GPU/listener readiness card and first execution decision |
| You need to decide storage before the first model pull | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] | Disk/cache/PATH evidence and model-store decision card |
| You need to install Ollama without losing the evidence trail | [[LLM/Study/Local LLM Windows Runtime Install Gate]] | Installer source, new-shell PATH, model-store inheritance, listener, and log proof |
| You are ready to pull the first Ollama model | [[LLM/Study/Local LLM First Model Pull Gate]] | Model tag decision, store proof, pull output, list/tags/show metadata, and pass/hold/fail route |
| You are ready to execute the first local endpoint proof | [[LLM/Study/Local LLM First Endpoint Run Sheet]] | Filled run folder, native response, OpenAI-compatible response, benchmark row, decision row |
| You have the first response JSON and need to interpret it | [[LLM/Study/Local LLM First Response Debrief Card]] | Route claim, timing conversion, mechanism owner, benchmark add-on row, and next controlled action |
| You have route proof and need a first quality signal | [[LLM/Study/Local LLM First Quality Probe Suite]] | Private prompt-suite outputs, script-assisted checks, human scores, and pass/hold/fail owner |
| You have an API contract and need a reusable client run | [[LLM/Study/Local LLM First Client Harness Runner]] | Python client script, request/response/output files, JSONL row, and next route |
| You have a reusable client run and need perceived-latency proof | [[LLM/Study/Local LLM First Streaming Timing Runner]] | Streaming script, event JSONL, TTFT, chunk counts, final output, and usage/error row |
| You have client or streaming JSONL and need a benchmark row | [[LLM/Study/Local LLM First Benchmark Row Builder]] | Benchmark JSON, Markdown copy row, missing-layer list, and next controlled action |
| You need first local inference proof | [[LLM/Study/Local LLM Windows First-Run Quickstart]] | Preflight, model id, response, listener proof |
| You need exact commands | [[LLM/Study/Local LLM Command Cookbook]] | Saved command output in one run folder |
| You have a response but no evidence packet | [[LLM/Study/Local LLM First Inference Evidence Pack]] | First-run evidence row |
| You have a local failure | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] | Failed layer, evidence, controlled next change |
| You have quality doubts | [[LLM/Study/Local LLM Quality Evaluation Harness]] | Pass/hold/fail row |
| You need to decide local vs hosted vs hybrid | [[LLM/Study/LLM Deployment Decision Matrix]] | Deployment memo |

## Mastery Gates

| Gate | Prove with | Status |
|---|---|---|
| Concept dependency | [[LLM/Study/LLM Concept Dependency Map]] |  |
| Active recall | [[LLM/Study/LLM Active Recall Question Bank]] |  |
| Paper synthesis | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |  |
| Paper claim ledger | [[LLM/Study/LLM Paper Claim Ledger]] |  |
| Mechanism bridge | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] |  |
| End-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] |  |
| Local inference metric interpretation | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |  |
| Self-assessment exam | [[LLM/Study/LLM Mastery Exam Run Sheet]] |  |
| Attention implementation | [[LLM/Study/Attention Implementation Lab]] |  |
| Tiny decoder training | [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] |  |
| First local endpoint | [[LLM/Study/Local LLM First Inference Evidence Pack]] |  |
| Reproducible client call | [[LLM/Study/Local LLM Client Harness Lab]] |  |
| Runtime comparison | [[LLM/Study/Local LLM Runtime Comparison Lab]] |  |
| Quality evaluation | [[LLM/Study/Local LLM Quality Evaluation Harness]] |  |
| RAG assistant | [[LLM/Study/Local RAG Minimal Python Harness]] |  |
| Tool loop | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |  |
| Operations and safety | [[LLM/Study/Local LLM Security and Privacy Runbook]] |  |
| Deployment decision | [[LLM/Study/LLM Deployment Decision Matrix]] |  |
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
| One complete daily study session | [[LLM/Study/LLM Daily Mastery Session Run Sheet]] |
| One mechanism-to-local-control row | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] or capstone note |
| One end-to-end local inference explanation | [[LLM/Study/Local LLM End-to-End Mental Model]] or capstone note |
| One interpreted local inference benchmark row | [[LLM/Study/Local LLM Inference Metrics Field Guide]] or [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One machine-specific first-run readiness row | [[LLM/Study/Local LLM First Run Readiness Snapshot]] |
| One machine-specific model-store decision row | [[LLM/Study/Local LLM Model Store Readiness Snapshot]] |
| One runtime install gate row | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| One first model pull gate row | [[LLM/Study/Local LLM First Model Pull Gate]] |
| One first endpoint run folder | [[LLM/Study/Local LLM First Endpoint Run Sheet]] |
| One first response debrief row | [[LLM/Study/Local LLM First Response Debrief Card]] |
| One first quality probe suite | [[LLM/Study/Local LLM First Quality Probe Suite]] |
| One first client harness run | [[LLM/Study/Local LLM First Client Harness Runner]] |
| One first streaming timing row | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| One first benchmark-row builder output | [[LLM/Study/Local LLM First Benchmark Row Builder]] |
| One first endpoint command output | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| One benchmark row | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| One quality decision | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| One failure diagnosis | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| One scored oral/practical exam attempt | [[LLM/Study/LLM Mastery Exam Run Sheet]] |
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
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Command Cookbook]]
