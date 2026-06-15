---
tags: [study, llm, mastery, exam, oral-exam, evidence, run-sheet]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Exam Run Sheet

> **One-line summary** This is the fill-in artifact for one LLM mastery exam attempt: answer without notes, score each section, link practical evidence, route misses, and decide pass, hold, or retake.

Use this while taking [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]]. The exam note contains the question bank and standards. This run sheet is the artifact you fill so the attempt becomes evidence in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. Use [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]] after scored rows are filled, then use [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] after proof links are filled to check whether the evidence bundle has any critical gaps.

This sheet is not proof unless the answer fields, scores, evidence links, and remediation rows are filled. A pass without linked local-inference and practical-gate evidence does not count.

## Run Contract

| Field | Value |
|---|---|
| Exam date |  |
| Attempt id |  |
| Mode | closed notes for answers, open notes only for grading |
| Time box | 90-150 minutes |
| Exam source | [[LLM/Study/LLM Mastery Self-Assessment Exam]] |
| Evidence destination | [[LLM/Study/LLM Mastery Capstone Workbook]] |
| Passing score | 80 percent or higher overall |
| Hard fail rules | any zero in local inference, RAG/evaluation, or safety/deployment; missing practical evidence links |
| Decision | pass / hold / retake |

## Step 0: Set Up The Attempt

Create one dated exam note or fill this run sheet directly.

```text
LLM/Study/Exam Attempts/
  YYYY-MM-DD LLM Mastery Exam Attempt.md
```

Before answering:

- [ ] Open [[LLM/Study/LLM Mastery Self-Assessment Exam]].
- [ ] Close or ignore all explanatory notes while answering.
- [ ] Keep [[LLM/Study/LLM Mastery Capstone Workbook]] available only for proof links.
- [ ] Choose whether this is a full exam, focused retake, or calibration attempt.
- [ ] Record the attempt id above.

Attempt type:

| Type | Use when | Pass rule |
|---|---|---|
| Full exam | You are testing complete LLM mastery. | All sections plus practical gates. |
| Focused retake | A prior full exam failed one or two sections. | Failed sections reach pass threshold and old misses have links. |
| Calibration | You want to find the next study gap. | No pass claim; only remediation rows. |

## Section Scoreboard

Score every answered prompt from `0` to `2`, using the exam note's standard.

| Section | Questions attempted | Raw score | Max score | Percent | Zero count | Status | Remediation link |
|---|---:|---:|---:|---:|---:|---|---|
| Field map |  |  |  |  |  | pass / hold / fail |  |
| Mechanisms and math |  |  |  |  |  | pass / hold / fail |  |
| Paper literacy |  |  |  |  |  | pass / hold / fail |  |
| Local inference practical oral |  |  |  |  |  | pass / hold / fail |  |
| Debugging scenarios |  |  |  |  |  | pass / hold / fail |  |
| RAG, tools, and evaluation |  |  |  |  |  | pass / hold / fail |  |
| Practical gates |  |  |  |  |  | pass / hold / fail |  |
| Total |  |  |  |  |  | pass / hold / fail |  |

Overall calculation:

| Field | Value |
|---|---|
| Total raw score |  |
| Total max score |  |
| Overall percent |  |
| Any hard-fail zero? | yes / no |
| All required practical links present? | yes / no |
| Final decision | pass / hold / retake |

## Answer Capture

Use short answers. A passing answer should name the mechanism, evidence, and operational consequence.

### Field Map

| Prompt chosen | Answer from memory | Score | Miss route |
|---|---|---:|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Mechanisms And Math

| Prompt chosen | Answer from memory | Score | Miss route |
|---|---|---:|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Paper Literacy

| Cluster or paper | Problem, method, evidence, limitation, deployment implication | Score | Miss route |
|---|---|---:|---|
| Transformer / attention |  |  |  |
| Scaling / Chinchilla |  |  |  |
| Alignment / preference methods |  |  |  |
| RAG / tools / evaluation |  |  |  |

### Local Inference Practical Oral

| Prompt chosen | Answer from memory | Score | Evidence link |
|---|---|---:|---|
| First thing to record before downloading a model |  |  | [[LLM/Study/Local LLM First Run Readiness Snapshot]] |
| First endpoint proof |  |  | [[LLM/Study/Local LLM First Endpoint Run Sheet]] |
| OpenAI-compatible contract |  |  | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Benchmark and quality decision |  |  | [[LLM/Study/Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Deployment decision |  |  | [[LLM/Study/LLM Deployment Decision Matrix]] |

### Debugging Scenarios

| Scenario | Failed layer | Evidence to collect | Next controlled change | Score |
|---|---|---|---|---:|
| Connection refused |  |  |  |  |
| `/v1/chat/completions` returns 404 |  |  |  |  |
| Model id not found |  |  |  |  |
| Startup OOM |  |  |  |  |
| Slow first token |  |  |  |  |
| Bad role markers or wrong speaker |  |  |  |  |
| Unsupported RAG citation |  |  |  |  |

### RAG, Tools, And Evaluation

| Prompt chosen | Answer from memory | Score | Evidence link |
|---|---|---:|---|
| RAG layers |  |  | [[LLM/Study/Local RAG Minimal Python Harness]] |
| Retrieval miss vs generation failure |  |  | [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]] |
| Tool safety boundary |  |  | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| Metric and judge risk |  |  | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] |
| Local vs hosted decision |  |  | [[LLM/Study/LLM Deployment Decision Matrix]] |

## Practical Evidence Gate

Do not pass the exam on oral answers alone. Link proof or mark the gap.

| Gate | Required evidence | Link or gap | Status |
|---|---|---|---|
| Dashboard route chosen | Today's route, proof artifact, and evidence destination | [[LLM/Study/LLM Mastery Dashboard]] | pass / gap |
| Active recall | 20 mixed questions or focused retake score | [[LLM/Study/LLM Active Recall Question Bank]] | pass / gap |
| Recall remediation audit | Recall rows cover required domains; low-score rows have routes, remediation artifacts, next reviews, and applied proof | [[LLM/Study/LLM Recall and Remediation Audit Runner]] | pass / gap |
| Paper literacy | One cluster summary or protocol row | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Paper Reading Protocol]] | pass / gap |
| Mechanism bridge | Mechanism, control, evidence, and next decision row | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] | pass / gap |
| Math and tensor shapes | Token/logit/loss/attention/KV-cache explanation | [[LLM/Study/LLM Math and Tensor Shape Primer]] | pass / gap |
| Local endpoint | Runtime/model/route response proof | [[LLM/Study/Local LLM First Endpoint Run Sheet]] | pass / gap |
| API contract | OpenAI-compatible base URL, route, model id, behavior | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] | pass / gap |
| Benchmark | Model/runtime/timing/memory row | [[LLM/Study/Local LLM Inference Benchmark Log]] | pass / gap |
| Quality | Prompt-suite score and pass/hold/fail decision | [[LLM/Study/Local LLM Quality Evaluation Harness]] | pass / gap |
| RAG or tools | Retrieval/citation proof or safe tool loop proof | [[LLM/Study/Local RAG Minimal Python Harness]], [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] | pass / gap |
| Security and deployment | Loopback/privacy/logging/tool boundary and deployment memo | [[LLM/Study/Local LLM Security and Privacy Runbook]], [[LLM/Study/LLM Deployment Decision Matrix]] | pass / gap |
| Capstone ledger | Proof links copied into the workbook | [[LLM/Study/LLM Mastery Capstone Workbook]] | pass / gap |
| Evidence audit | Mastery audit JSON/Markdown has no critical gaps | [[LLM/Study/LLM Mastery Evidence Audit Runner]] | pass / gap |

## Miss Routing

Every `0`, every `1`, and every unlinked practical gate gets exactly one next route.

| Miss | Why it failed | Lowest unproven dependency | Route | Next proof artifact | Retake date |
|---|---|---|---|---|---|
|  | mechanism missing / evidence missing / consequence missing / practical link missing |  |  |  |  |
|  | mechanism missing / evidence missing / consequence missing / practical link missing |  |  |  |  |
|  | mechanism missing / evidence missing / consequence missing / practical link missing |  |  |  |  |

Common routes:

| Miss pattern | Route |
|---|---|
| Timeline or field map is fuzzy | [[LLM/LLM — Learning Path]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |
| Mechanism is named but not derived | [[LLM/Study/LLM Math and Tensor Shape Primer]], [[LLM/Study/Attention Implementation Lab]] |
| Paper claim is remembered but not evaluated | [[LLM/Study/LLM Paper Reading Protocol]] |
| Training behavior cannot be assigned to a stage | [[LLM/Study/LLM Training Pipeline Map]] |
| Local command works but evidence is weak | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| Local failure owner is unclear | [[LLM/Study/Local LLM Runtime Stack Anatomy]], [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Quality decision is subjective | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]], [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| RAG citation trust is unclear | [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]] |
| Tool loop safety is unclear | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| Deployment choice is hand-wavy | [[LLM/Study/LLM Deployment Decision Matrix]] |

## Pass Or Retake Decision

| Decision field | Answer |
|---|---|
| Overall percent >= 80? | yes / no |
| Any hard-fail zero? | yes / no |
| Local inference evidence linked? | yes / no |
| RAG/evaluation evidence linked? | yes / no |
| Security/deployment evidence linked? | yes / no |
| Miss remediation rows complete? | yes / no |
| Recall remediation audit linked? | yes / no |
| Capstone workbook updated? | yes / no |
| Final decision | pass / hold / retake |

If the final decision is `hold` or `retake`, write the next session in one sentence:

```text
Next session:
```

## Completion Gate

This run sheet is complete only when:

- [ ] every attempted answer has a score
- [ ] every section has a percent and status
- [ ] every zero or one has a remediation route
- [ ] local inference, RAG/evaluation, and security/deployment have no zero scores
- [ ] practical evidence links are present or explicitly marked as gaps
- [ ] recall/remediation audit output is linked
- [ ] the capstone workbook links this attempt
- [ ] the mastery evidence audit has no critical gaps or links remediation rows
- [ ] the final decision is pass, hold, or retake

## References

Internal routes:

- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
