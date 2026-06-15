---
tags: [study, llm, recall, mastery, review, active-recall]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Active Recall Question Bank

> **One-line summary** This is the daily retrieval-practice bank for LLM mastery: answer mechanism, paper, evaluation, and local-inference questions from memory, then route misses to the exact note or lab that fixes the gap.

Use this with [[LLM/Study/LLM Mastery Study Cadence|LLM Mastery Study Cadence]], [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]], and [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. The category review drills are useful for warm-up. This bank is for mixed recall, where academic concepts and applied local-hosting decisions are interleaved.

## How To Use

Pick one row from each cluster:

| Step | Action | Output |
|---|---|---|
| 1 | Answer without notes in 2-4 sentences | Plain-language answer |
| 2 | Add one mechanism or equation when relevant | Concept anchor |
| 3 | Name one operational consequence | Local inference, RAG, tool, eval, or deployment consequence |
| 4 | Check the linked route | Corrected answer |
| 5 | If missed, add a capstone or cadence miss row | Next proof artifact |

Score:

| Score | Meaning |
|---:|---|
| 0 | Could not answer or guessed |
| 1 | Named the idea but missed mechanism or consequence |
| 2 | Correct mechanism, weak applied connection |
| 3 | Correct mechanism, applied consequence, and evidence route |

Repeat any 0 or 1 within two days. A score of 3 should survive a later mixed session, not only a same-note review.

## Field Map And Tokens

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| Why did neural language models beat n-grams? | Dense representations, generalization, context, learned features | [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]] |
| What does tokenization change about the problem? | Text becomes token IDs; tokens are not words; context and cost are token-based | [[LLM/Pre-2017 — Before Transformers/Tokenization]] |
| What is the path from user text to sampled output? | Template, tokens, embeddings, hidden states, logits, probabilities, sampling | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Why can two tokenizers change local quality and latency? | Different token counts, special tokens, template boundaries, stop behavior | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| What does perplexity measure, and what does it miss? | Average next-token surprise; misses instruction following and workload quality | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] |

## Math, Attention, And Transformer Blocks

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| Derive scaled dot-product attention in words. | Q/K matching, scale by sqrt(d), softmax weights, weighted V sum | [[LLM/Study/Attention Implementation Lab]] |
| Why does the causal mask exist? | Prevents attending to future tokens during next-token prediction | [[LLM/2017 — The Transformer/Attention Mechanism]] |
| What changes between training and autoregressive inference? | Parallel teacher-forced positions vs sequential generated-token loop | [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] |
| Why does KV cache lower compute but increase memory pressure? | Reuse prior K/V; memory grows with layers, KV heads, context, active requests | [[LLM/Study/LLM Math and Tensor Shape Primer]] |
| Why do MQA/GQA matter for local inference? | Fewer KV heads reduce cache memory and bandwidth pressure | [[LLM/Study/Attention Implementation Lab]] |

## Training, Scaling, And Adaptation

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What does pretraining optimize? | Next-token prediction over large corpora, not direct instruction obedience | [[LLM/Study/LLM Training Pipeline Map]] |
| Why can smaller overtrained models be good local choices? | Inference cost matters; data/parameter/compute trade-off; quality per hardware | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |
| What does SFT add that pretraining does not? | Demonstrated instruction-response behavior and task formatting | [[LLM/2022 — Alignment and Chat/Instruction Tuning]] |
| Contrast RLHF and DPO. | Reward-model/PPO style preference optimization vs direct preference objective | [[LLM/Study/LLM Training Pipeline Map]] |
| When is fine-tuning the wrong fix? | Retrieval miss, bad prompt, wrong template, weak evaluation, or deployment issue | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] |

## Papers And Research Literacy

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What changed after Attention Is All You Need? | Recurrence removal, parallel sequence modeling, attention as core mechanism | [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]] |
| What did GPT-3 prove operationally? | Scale enables in-context/few-shot behavior; prompting becomes an interface | [[LLM/2020–2021 — The Scaling Era/Few-Shot Prompting]] |
| What is the Chinchilla lesson for local model choice? | Compute/data/parameter balance; bigger is not automatically better | [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs]] |
| What did FlashAttention change without changing attention math? | IO-aware exact attention, less memory movement, faster training/inference kernels | [[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention]] |
| How do you read a new LLM paper skeptically? | Claim, baseline, method, evidence, limitation, transfer risk | [[LLM/Study/LLM Paper Reading Protocol]] |

## Evaluation And Quality

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| Why can one model win a benchmark and lose your deployment decision? | Workload mismatch, latency, memory, privacy, cost, safety, eval coverage | [[LLM/Study/LLM Deployment Decision Matrix]] |
| What does LLM-as-judge risk? | Position, verbosity, self-preference, rubric drift, contamination | [[LLM/2023 — Open Models and Agents/LLM-as-Judge]] |
| What is the difference between smoke, benchmark, and quality proof? | Route works; performance measured; answer fitness scored by rubric | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] |
| Why use private/local prompt suites? | Avoid contamination and match actual workload | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| What must a pass/hold/fail quality row record? | Prompt id, rubric, scores, failure owner, next action | [[LLM/Study/Local LLM Quality Evaluation Harness]] |

## First Local Endpoint

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What proves the runtime boundary on Windows? | OS/hardware/GPU/disk/preflight, process, listener, host/port | [[LLM/Study/Local LLM Environment Preflight Lab]] |
| What does a local smoke response prove? | Endpoint can generate for one request; not quality, safety, or workload fit | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| What commands prove Ollama native and OpenAI-compatible routes? | `/api/generate`, `/api/tags`, `/v1/chat/completions`, saved JSON | [[LLM/Study/Local LLM Command Cookbook]] |
| What proves the served model id? | Runtime model list, UI/server registry, `/v1/models`, exact request model | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Why keep the first endpoint on loopback? | Prompts, outputs, logs, RAG data, and tools can leak | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Local Serving And Performance

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| Explain TTFT vs TPOT. | Prefill/queue to first token vs decode time per output token | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| What causes OOM only on long prompts? | KV cache/context budget, retrieved chunks, output reserve, concurrency | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| What variables must stay fixed in runtime comparison? | Model/artifact, prompts, sampler, context target, output cap, quality rubric | [[LLM/Study/Local LLM Runtime Comparison Lab]] |
| When should vLLM/SGLang be tested under WSL first? | Before interpreting GPU serving, scheduler, or throughput behavior from Windows | [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]] |
| What does a benchmark row need? | Model, runtime, quantization, hardware, context, TTFT, tokens/sec, memory, quality | [[LLM/Study/Local LLM Inference Benchmark Log]] |

## Model Selection And Compatibility

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| Why is there no universal best local model? | Workload, hardware, license, latency, memory, API support, quality differ | [[LLM/Study/Local LLM Workload to Model Selection Playbook]] |
| What must be recorded before downloading a model? | Card, license, gated access, revision/file, artifact safety, local path | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]] |
| What proves local bytes are the served artifact? | Cache path, file list, hash/revision, import/conversion command, runtime id | [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]] |
| Why can GGUF, AWQ, GPTQ, FP8, and BF16 imply different runtime paths? | Artifact format, quantization support, hardware/backend compatibility | [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]] |
| What is the smaller-plausible-candidate rule? | Start with the smallest model likely to pass; scale only when quality fails | [[LLM/Study/Local LLM Workload to Model Selection Playbook]] |

## RAG And Context Assembly

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What are the RAG layers? | Corpus, chunking, embedding/reranker, index, retrieve, pack, generate, cite, evaluate | [[LLM/Study/Local RAG Assistant Lab]] |
| What proves an embedding endpoint is compatible? | Model, route, vector shape, normalization, batching, latency, privacy | [[LLM/Study/Local Embedding and Reranker Hosting Lab]] |
| What does reranking fix, and what can it not fix? | Low-rank relevant candidates; cannot recover absent evidence | [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]] |
| How do you distinguish retrieval miss from hallucination? | Top-k/citation evidence vs generated unsupported claim after evidence exists | [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]] |
| Why can long context be worse than RAG? | Cost, lost-in-middle, noise, privacy/logging, weak citation control | [[LLM/Study/Local RAG Minimal Python Harness]] |

## Tools, Structure, And Agents

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What makes local tool calling safe enough to test? | Schema, validation, policy, allowlist, bounded loop, denied unsafe action | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| What does structured output prove and not prove? | Syntax/schema compliance; not factuality or tool safety by itself | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| Why can agent memory harm performance? | Context budget trade-off, stale state, retrieval/summary errors | [[LLM/Study/LLM Concept Dependency Map]] |
| What should a tool failure row include? | Prompt, tool schema, model args, validation result, policy decision, retry/stop | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| When is a single well-scoped tool loop better than multi-agent setup? | Simple tasks, easier evaluation, lower context and orchestration overhead | [[LLM/Study/Agents and Evaluation - Review Drill]] |

## Operations, Security, And Deployment

| Prompt | A good answer must include | Route if missed |
|---|---|---|
| What changes when loopback becomes LAN access? | Auth, firewall, logging, data boundary, abuse risk, client trust | [[LLM/Study/Local LLM Security and Privacy Runbook]] |
| What logs can contain private data? | Prompts, retrieved docs, tool args/results, outputs, errors, eval rows | [[LLM/Study/Local LLM Security and Privacy Runbook]] |
| What proves a local endpoint is maintainable? | Startup mode, pinned runtime/model, cache path, backup, rollback, validation | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]] |
| What should observability capture before tuning? | Model state, route, timings, logs/metrics, resource pressure, next action | [[LLM/Study/Local LLM Observability and Operations Runbook]] |
| How do you decide local vs hosted vs hybrid? | Workload, quality, latency, memory/cost, privacy, ops burden, failure plan | [[LLM/Study/LLM Deployment Decision Matrix]] |

## Miss Routing

| Miss pattern | Route backward to |
|---|---|
| You cannot define the mechanism | [[LLM/Study/LLM Concept Dependency Map]] |
| You can explain the concept but not the equation or shape | [[LLM/Study/LLM Math and Tensor Shape Primer]] |
| You can explain the mechanism but not the local control | [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]] |
| You can run a command but cannot explain the evidence | [[LLM/Study/Local LLM First Inference Evidence Pack]] |
| You can get an answer but cannot judge it | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] and [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| You can judge quality but cannot choose a fix | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] |
| You can make a prototype but cannot maintain it | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]] |

## Completion Gate

This bank is doing its job when:

- [ ] a mixed 20-question session scores at least 80 percent
- [ ] no local-inference, RAG/evaluation, or safety cluster has a zero
- [ ] every missed question has a route and a next proof artifact
- [ ] capstone rows use evidence, not confidence, as the pass signal

## References

- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Study Cadence]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
