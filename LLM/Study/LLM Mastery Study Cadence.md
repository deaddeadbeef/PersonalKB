---
tags: [study, llm, mastery, cadence, review, capstone]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Study Cadence

> **One-line summary** This is the operating rhythm for mastering LLMs: every week pairs academic understanding with one applied proof artifact, so reading turns into usable local inference skill.

Use this with [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]], [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]], and [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]]. The roadmap says what mastery means. The capstone workbook stores proof. This cadence says what to do this week.

This is not a calendar deadline. If a week fails, repeat the week with a smaller artifact. The goal is durable recall and evidence, not page-count completion.

## Daily Loop

Use the same loop for academic and applied work.

| Block | Timebox | Output |
|---|---:|---|
| Recall | 10 minutes | Answer yesterday's questions without notes |
| Study | 30-60 minutes | One paper section, concept note, or lab section read closely |
| Explain | 10 minutes | One paragraph in your own words |
| Build or prove | 30-90 minutes | One command output, card, row, sketch, or code artifact |
| Route | 5 minutes | Link the artifact from the capstone workbook or active lab |

If the day only produces highlights, it does not count as progress toward mastery. There must be a recall answer, an explanation, or an evidence artifact.

## Weekly Gate

Each week ends with four checks:

| Gate | Pass signal |
|---|---|
| Concept recall | You can answer the week's main questions without opening notes |
| Mechanism bridge | You can connect at least one academic mechanism to a local inference control or failure |
| Applied artifact | A proof row, command output, benchmark, code file, card, or rubric exists |
| Capstone link | The artifact is linked from [[LLM/Study/LLM Mastery Capstone Workbook]] or a dated capstone note |

Do not move forward if the mechanism bridge is missing. The user's goal is academic and applied mastery together, not two separate tracks.

## Twelve-Week Spine

Treat the weeks as modules. A strong week can finish quickly; a weak week should be repeated.

| Week | Focus | Academic proof | Applied proof |
|---|---|---|---|
| 0 | Setup and baseline | Explain the full roadmap and capstone gates | Create a capstone note and choose the first local workload |
| 1 | Field map and tokens | Trace n-grams to decoder-only assistants | Token-to-logit sketch and request lifecycle row |
| 2 | Attention and tensor shapes | Derive Q/K/V, attention scores, causal mask, KV cache | Attention implementation or worked tensor-shape proof |
| 3 | Training pipeline | Trace data, objective, pretraining, SFT, preference optimization, eval, deployment | Tiny decoder training run or training-pipeline capability trace |
| 4 | Papers and evaluation | Fill paper protocol rows for core clusters; explain HELM-style multi-metric evaluation | Metric card and quality rubric draft |
| 5 | First local endpoint | Explain weights, quantization, tokenizer, chat template, runtime, route | Windows/Ollama/LM Studio/llama.cpp loopback smoke response |
| 6 | Model selection and custody | Defend why the candidate is smallest plausible for the workload | Candidate card, provenance card, artifact/cache card |
| 7 | Compatibility and request controls | Explain template mismatch, sampler drift, context budget, TTFT vs decode | Compatibility card, API contract, sampler/context rows |
| 8 | Benchmark and serving internals | Explain prefill, decode, KV cache, batching, prompt cache, speculation | Benchmark row plus one scheduler/cache/latency diagnosis |
| 9 | Operations and safety | Explain endpoint exposure, logs, data boundary, lifecycle, rollback | Observability row, security row, lifecycle/rollback row |
| 10 | RAG | Explain retrieval, chunking, embeddings, reranking, context assembly, citation failures | RAG harness or retrieval-evaluation artifact set |
| 11 | Tools, adaptation, deployment | Explain tool policy, structured output, adaptation choices, deployment trade-offs | Tool proof, adaptation decision, deployment memo |
| 12 | Oral exam and capstone | Pass self-assessment or write remediation | Capstone evidence ledger with gaps closed or explicitly scheduled |

## Week 0: Setup And Baseline

Goal: make the work measurable.

Read:

- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]

Produce:

| Artifact | Minimum content |
|---|---|
| Capstone note | Date, target workload, hardware assumptions, initial gaps |
| Baseline self-score | Which exam sections feel strong, weak, or unknown |
| First workload contract | From [[LLM/Study/Local LLM Workload to Model Selection Playbook]] |

Pass signal: you know what evidence will prove progress.

## Week 1: Field Map And Tokens

Goal: understand the interface from text to next-token prediction.

Read:

- [[LLM/LLM — Learning Path]]
- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]

Recall questions:

- Why did neural language models beat n-grams?
- What does tokenization change about the problem?
- What is the path from token IDs to sampled text?
- Why is an LLM API still a next-token engine under the hood?

Applied proof: one request lifecycle row with prompt, output cap, stop condition, and raw response shape. If no local endpoint exists yet, use a hypothetical request body and mark endpoint proof pending.

## Week 2: Attention And Shapes

Goal: make the Transformer mechanism concrete.

Read:

- [[LLM/2017 — The Transformer/Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/Attention Implementation Lab]]

Recall questions:

- What are Q, K, and V?
- Why divide by the square root of the key dimension?
- What does the causal mask prevent?
- Why does KV cache exist during inference but not as a saved training artifact?

Applied proof: attention implementation output or a written tensor-shape proof linked from the capstone workbook.

## Week 3: Training Pipeline

Goal: stop treating "the model" as one training stage.

Read:

- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws]]
- [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs]]

Recall questions:

- What does pretraining optimize?
- What does SFT add that pretraining does not?
- What do preference methods optimize?
- When is fine-tuning the wrong fix?

Applied proof: tiny decoder training output or a capability trace that names the likely failure owner.

## Week 4: Papers And Evaluation

Goal: read papers as claims with evidence, not as lore.

Read:

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]

Recall questions:

- What problem did each paper solve relative to its baseline?
- What evidence supports the paper's claim?
- What does the metric miss?
- Why can one model win one metric and lose the deployment decision?

Applied proof: one paper protocol row and one metric card tied to a local model or deployment decision.

## Week 5: First Local Endpoint

Goal: prove that a model can answer locally through a route you understand.

Read:

- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]

Recall questions:

- What proves the runtime boundary?
- What proves the served model id?
- What proves loopback-only exposure?
- What does the smoke response prove, and what does it not prove?

Applied proof: first inference evidence pack with raw response, route, model id, timing, and next decision.

## Week 6: Model Selection And Custody

Goal: choose and acquire a candidate model defensibly.

Read:

- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]

Recall questions:

- Why is there no universal best local model?
- What does the model card prove?
- What does the local artifact card prove?
- Why can the smallest plausible candidate be better than the largest loadable candidate?

Applied proof: candidate card, provenance card, artifact/cache card, and sizing estimate.

## Week 7: Compatibility And Request Controls

Goal: make requests comparable.

Read:

- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]

Recall questions:

- Why can a chat template failure look like a weak model?
- Which sampler settings must be fixed for a fair comparison?
- What proves OpenAI-compatible enough for a client?
- How do context and output reserve affect TTFT and OOM risk?

Applied proof: compatibility card, API contract card, sampler row, and context budget row.

## Week 8: Benchmark And Serving Internals

Goal: explain latency and memory symptoms.

Read:

- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]

Recall questions:

- What is TTFT mostly measuring?
- What is TPOT mostly measuring?
- How does KV cache scale with context and active requests?
- When can prompt caching or speculation hurt instead of help?

Applied proof: one benchmark row and one diagnosis row that names prefill, decode, KV cache, scheduler, prompt cache, or speculation.

## Week 9: Operations And Safety

Goal: turn a working endpoint into a responsible local service candidate.

Read:

- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Recall questions:

- What changes when loopback becomes LAN or shared access?
- Which logs can contain private data?
- What must be pinned before an upgrade?
- What proves rollback?

Applied proof: observability row, security row, lifecycle card, and deployment decision draft.

## Week 10: RAG

Goal: separate retrieval failures from generation failures.

Read:

- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]

Recall questions:

- What does an embedding service card prove?
- What does top-k recall prove?
- Why can citations still be wrong when retrieval succeeds?
- What should the model do when the source does not support an answer?

Applied proof: corpus manifest, retrieval evaluation row, generated cited answer, unsupported-question refusal, and one RAG failure diagnosis.

## Week 11: Tools, Adaptation, Deployment

Goal: decide whether to add tools, train, or deploy differently.

Read:

- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Recall questions:

- Why must model-proposed tool calls be validated externally?
- When is RAG better than fine-tuning?
- What evidence is needed before LoRA or QLoRA?
- How do quality, latency, privacy, cost, and operations decide deployment?

Applied proof: tool schema and policy row, quality harness row, adaptation decision, and deployment memo.

## Week 12: Oral Exam And Capstone

Goal: prove that the knowledge is available without hand-holding.

Read:

- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

Produce:

| Artifact | Minimum content |
|---|---|
| Exam score | Section scores, missed prompts, remediation links |
| Capstone ledger | Every gate linked or explicitly marked blocked |
| Final explanation | One-page answer to "how do I host a local LLM and know whether it is good?" |

Pass signal: no zero in the practical sections, 80 percent or higher overall, and every capstone gap has a next artifact.

## Retake Rules

If a week fails:

| Failure | Retake action |
|---|---|
| Cannot recall concepts | Write five Q/A cards and repeat the recall block next day |
| Cannot explain mechanism to local consequence | Add one row to [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] or a dated capstone note |
| Local command fails | Add one diagnostic row from [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Output works but quality is weak | Run [[LLM/Study/Local LLM Quality Evaluation Harness]] before changing the model |
| RAG answer is unsupported | Run retrieval evaluation before changing generation |
| Tool output is unsafe or invalid | Add schema, policy, and bounded-loop evidence before retrying |

The retake is complete only when the failed gate has a new artifact.

## Weekly Log Template

Copy this into the capstone note.

| Field | Value |
|---|---|
| Week |  |
| Focus |  |
| Academic concept learned |  |
| Paper or note read |  |
| Recall questions answered |  |
| Mechanism-to-inference bridge |  |
| Applied artifact |  |
| Commands or files |  |
| Capstone link updated |  |
| Failed gate |  |
| Next controlled action |  |

## Completion Gate

This cadence has done its job when:

- [ ] every week has either a pass row or an explicit repeat row
- [ ] the capstone workbook links academic, implementation, local inference, RAG, tools, evaluation, adaptation, and deployment evidence
- [ ] the self-assessment is passed or has remediation scheduled
- [ ] at least one local model endpoint has been hosted, called, benchmarked, quality-scored, and explained through mechanisms
- [ ] every remaining gap is a named artifact, not a vague feeling

## References

- [[LLM/LLM]]
- [[LLM/LLM — Learning Path]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
