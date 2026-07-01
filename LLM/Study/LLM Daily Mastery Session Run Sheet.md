---
tags: [study, llm, mastery, daily, session, recall, evidence, run-sheet]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Daily Mastery Session Run Sheet

> **One-line summary** This is the fill-in artifact for one LLM study session: answer one recall prompt, explain one mechanism, produce or route one applied proof, and link the result into the capstone.

Use this with [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]] and [[LLM/Study/LLM Mastery Study Cadence|LLM Mastery Study Cadence]]. The dashboard chooses the route. The cadence sets the rhythm. This run sheet is the saved evidence that the session combined academic knowledge with local inference practice. Use [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]] after scored rows when the session supports mastery or exam evidence.

This sheet is intentionally small. A session passes when it leaves one durable answer, one mechanism-to-local consequence, and one evidence link or blocker. Reading without an answer or artifact does not count.

## Session Contract

| Field | Value |
|---|---|
| Date |  |
| Session id |  |
| Week focus |  |
| Recall source | [[LLM/Study/LLM Active Recall Question Bank]] |
| Concept route | [[LLM/Study/LLM Concept Dependency Map]] |
| Applied route | [[LLM/Study/Local LLM Hands-On Practicum Sequence]] |
| Evidence destination | [[LLM/Study/LLM Mastery Capstone Workbook]] |
| Stop rule | stop after one saved answer, artifact, row, command output, or blocker |
| Final decision | pass / repeat / blocked |

## Step 1: Pick One Prompt

Pick exactly one recall prompt or oral-exam prompt. Do not start with more.

| Field | Value |
|---|---|
| Prompt |  |
| Source note |  |
| Answer without notes |  |
| Score | 0 / 1 / 2 / 3 |
| Corrected answer after checking |  |
| Miss route |  |

Scoring:

| Score | Meaning |
|---:|---|
| 0 | Could not answer or guessed. |
| 1 | Named the idea but missed mechanism or consequence. |
| 2 | Mechanism is correct but applied consequence is weak. |
| 3 | Mechanism, consequence, and evidence route are all correct. |

## Step 2: Name The Mechanism

Turn the recall answer into one mechanism bridge.

| Field | Value |
|---|---|
| Mechanism | tokenization / loss / attention / KV cache / quantization / sampler / RAG / tool / evaluation / deployment |
| Academic claim |  |
| Local control or symptom |  |
| Evidence that would prove it |  |
| Wrong shortcut rejected |  |
| Route if weak | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] |

Examples:

| Academic mechanism | Local consequence |
|---|---|
| KV cache grows with context and active sequences. | Long RAG prompts can OOM even when the model weights fit. |
| Chat templates define role boundaries and stop behavior. | Bad role markers can be a template/tokenizer problem, not a weak model. |
| Perplexity is next-token fit on a distribution. | It cannot decide whether a local assistant is good for a private workload. |
| Quantization changes memory transfer and numeric error. | A faster local model still needs a quality row before it becomes the default. |

## Step 3: Produce Or Route One Applied Proof

Choose one applied path. If the endpoint is not installed yet, the applied proof can be a readiness, sizing, provenance, or blocker row.

| Applied state | Route | Minimum artifact |
|---|---|---|
| No runtime installed | [[LLM/Study/Local LLM First Run Readiness Snapshot]] | readiness row or first execution decision |
| Can run a command but cannot explain the whole path | [[LLM/Study/Local LLM End-to-End Mental Model]] | one request explained from artifact, tokenizer, runtime, prefill, decode, route, client, quality, and operations |
| Ready for first Ollama run | [[LLM/Study/Local LLM First Endpoint Run Sheet]] | run folder plan or saved endpoint evidence |
| Endpoint works but evidence is thin | [[LLM/Study/Local LLM First Inference Evidence Pack]] | first-run evidence row |
| Need exact commands | [[LLM/Study/Local LLM Command Cookbook]] | saved command output |
| Model choice is unclear | [[LLM/Study/Local LLM Workload to Model Selection Playbook]] | candidate card |
| Failure happened | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] | failed layer and next controlled change |
| Quality is unclear | [[LLM/Study/Local LLM Quality Evaluation Harness]] | pass/hold/fail row |
| Need API compatibility | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] | contract card |
| Need RAG proof | [[LLM/Study/Local RAG Minimal Python Harness]] | retrieval/citation artifact |
| Need deployment choice | [[LLM/Study/LLM Deployment Decision Matrix]] | decision memo |

Applied proof row:

| Field | Value |
|---|---|
| Applied route chosen |  |
| Artifact produced or updated |  |
| Command output, file, or note link |  |
| Pass/hold/fail signal |  |
| If blocked, failed layer | hardware / runtime / model artifact / tokenizer-template / route / client / quality / RAG / security / unknown |
| Next controlled action |  |

## Step 4: Link The Session

Link the session output so it is findable later.

| Destination | Link or action |
|---|---|
| Dashboard status | [[LLM/Study/LLM Mastery Dashboard]] |
| Capstone workbook row | [[LLM/Study/LLM Mastery Capstone Workbook]] |
| Active recall miss row | [[LLM/Study/LLM Active Recall Question Bank]] or dated note |
| Recall remediation audit | [[LLM/Study/LLM Recall and Remediation Audit Runner]] |
| Mechanism bridge row | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] or this note |
| Applied lab or run sheet |  |

Session summary:

```text
Today I proved:
Today I failed or held:
Next session:
```

## Anti-Drift Check

Before ending, answer these:

- [ ] Did I answer one prompt without notes?
- [ ] Did I write the corrected answer?
- [ ] Did I name one mechanism and one local consequence?
- [ ] Did I produce or route one applied proof?
- [ ] Did I link the result to the capstone workbook or a dated note?
- [ ] Did I avoid adding another reading target before saving evidence?

## Completion Gate

This session is complete only when:

- [ ] the recall prompt has a score
- [ ] the corrected answer exists
- [ ] the mechanism bridge names a local control or symptom
- [ ] one applied route has an artifact, command output, row, or explicit blocker
- [ ] the capstone destination is linked or the missing link is named as the next action
- [ ] recall/remediation audit output is linked when the session has misses or supports exam evidence
- [ ] the next session is written in one sentence

## References

- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Study Cadence]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
