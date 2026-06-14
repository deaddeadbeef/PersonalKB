---
tags: [study, llm, mastery, exam, self-assessment]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Self-Assessment Exam

> **One-line summary** You know LLMs when you can explain the field, derive the core mechanisms, read papers skeptically, operate a local model, diagnose failures, and defend adaptation and deployment decisions without guessing.

Use this after [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] and before filling the final proof rows in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. The roadmap says what to learn. The capstone workbook stores evidence. This exam tests whether the knowledge is available without hand-holding.

This is not a trivia quiz. Prefer short, precise answers that connect mechanism, evidence, and operational consequence.

## Passing Standard

Score each answer:

| Score | Meaning |
| --- | --- |
| 0 | Cannot answer, or answer is mostly wrong. |
| 1 | Partly correct but misses mechanism, evidence, or consequence. |
| 2 | Correct, concise, and tied to at least one concrete mechanism or artifact. |

Minimum pass:

- 80 percent or higher overall
- no zero in the local inference, RAG/evaluation, or safety sections
- every practical gate has linked evidence in the capstone workbook
- every missed question has a remediation link

If a section fails, do not reread randomly. Use the remediation map at the end of this note.

## Section 1: Field Map

Answer without opening the timeline.

| Prompt | A passing answer must include |
| --- | --- |
| What changed from n-gram language models to neural language models? | Distributed representations, learned probability model, generalization beyond exact counts. |
| Why did attention matter before the Transformer? | Seq2seq bottleneck, alignment over source tokens, better long-range conditioning. |
| Why did the Transformer replace recurrence for large-scale training? | Parallel sequence processing, self-attention, scaling efficiency, hardware fit. |
| Why did decoder-only models become dominant for general assistants? | Autoregressive pretraining, next-token interface, prompting, scalable generation. |
| What is the BERT vs GPT split? | Bidirectional masked encoder for understanding tasks vs autoregressive decoder for generation. |
| Why did scaling laws change model planning? | Predictable loss trends, compute/data/model trade-offs, Chinchilla correction. |
| What are the major stages in the LLM training pipeline? | Data curation, tokenization, pretraining, base evaluation, SFT, preference optimization, adaptation/RAG, deployment, and monitoring. |
| Why did alignment become a separate stage after pretraining? | Raw next-token models do not reliably follow user intent; SFT/RLHF/preference methods shape behavior. |
| Why did open-weight models matter? | Local control, inspection, adaptation, deployment, and runtime ecosystem. |
| Why are RAG and tools not just prompting tricks? | They add external state/action channels and shift failure modes outside model weights. |
| Why is inference now a systems problem? | KV cache, batching, memory bandwidth, quantization, routing, serving latency, and cost. |

Core remediation: [[LLM/LLM — Learning Path]], [[LLM/Study/LLM Architecture Cheatsheet]], and the review drills in [[LLM/Study/LLM Study Index]].

## Section 2: Mechanisms And Math

You should be able to explain these with a small sketch or equation.

| Prompt | A passing answer must include |
| --- | --- |
| Derive scaled dot-product attention in words. | Q/K similarity, scale by key dimension, softmax weights, weighted V sum. |
| Why does causal masking matter for decoder-only training and inference? | Prevents attending to future tokens; preserves autoregressive objective. |
| What are Q, K, and V projections doing? | Different learned views for matching positions and carrying content. |
| Why do multi-head attention, MQA, and GQA trade quality for memory/speed differently? | KV head sharing changes cache size and representational capacity. |
| What does the KV cache store and why does it grow? | Past keys/values by layer/head; grows with sequence length and active sequences. |
| Why does prompt length affect TTFT more than later decode speed? | Prefill processes the prefix before first generated token. |
| Why is decode often memory-bandwidth-bound? | Each generated token repeatedly reads model weights and cache. |
| What does quantization change? | Numeric representation and memory transfer, with possible quality loss. |
| What is LoRA's core parameterization? | Low-rank update added to frozen base weights. |
| How do you assign a failure to the right training stage? | Identify whether the symptom points to data, objective, SFT, preference optimization, RAG, adaptation, runtime, or policy before changing the model. |
| What must a tiny decoder-only training loop prove? | Shifted next-token targets, causal masking, logits-to-cross-entropy loss, gradients, train/validation loss, and autoregressive generation. |
| When should you avoid fine-tuning? | When the failure is missing external knowledge, current facts, retrieval, tool policy, prompt formatting, or model capacity rather than learnable task behavior. |
| Why can a smaller overtrained model be better for inference economics? | More training data/compute can improve quality while reducing serving cost. |

Practical proof: complete [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain every tensor shape.

## Section 3: Paper Literacy

Use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] for one paper from each cluster.

| Cluster | Exam task |
| --- | --- |
| Training pipeline | Trace one capability from corpus choice and objective through pretraining, post-training, evaluation, adaptation, and deployment. |
| Tiny decoder training | Explain the code path from token IDs to logits, loss, optimizer step, validation loss, and generated text. |
| Transformer | State the pre-paper baseline, the new mechanism, and the evidence that it worked. |
| BERT/GPT | Explain how objective and architecture changed downstream behavior. |
| GPT-3/scaling | Separate scale, data, compute, and in-context learning claims. |
| Chinchilla | Explain what Kaplan-style scaling missed and why inference cost matters. |
| InstructGPT/RLHF | Trace SFT, reward model, PPO, and the behavior being optimized. |
| DPO/Constitutional AI | Compare preference optimization and principle-guided self-critique. |
| LoRA/QLoRA | Explain what is frozen, what is trained, and what memory is saved. |
| RAG/ReAct/Toolformer | Distinguish retrieval, reasoning traces, and tool-use supervision. |
| vLLM/FlashAttention | Identify the systems bottleneck and the implementation-level fix. |
| HELM/LLM-as-Judge | Explain what the evaluation measures and what bias remains. |

Pass signal: for every paper, you can fill problem, method, evidence, limitation, and deployment implication without copying the abstract.

## Section 4: Local Inference Practical Oral

Use your actual machine or a hypothetical machine with clear assumptions.

| Prompt | A passing answer must include |
| --- | --- |
| What is the first thing to record before downloading a model? | [[LLM/Study/Local LLM Environment Preflight Lab|Environment preflight]]: OS, shell, CPU/RAM, GPU/VRAM, disk, runtime boundary, port plan. |
| What proves a local model artifact is safe enough to acquire? | Model card, intended use, license, gated access, exact revision/tag/file, safe-format decision, local path, and hash/digest or revision proof. |
| How do you choose the first model? | Workload, quality gate, context target, memory estimate, runtime support, smallest plausible candidate. |
| How do you prove the exact model artifact is compatible with the runtime? | Artifact container, quantization, tokenizer, chat template, runtime support, model id, route, hardware path, and workload contract are recorded. |
| How do you estimate weight memory? | Parameters multiplied by bytes per parameter plus runtime overhead and headroom. |
| How do you estimate KV-cache risk? | Context length, layers, hidden size, precision, active sequences, and retrieved context. |
| What is the safe default network binding? | Loopback only until auth, firewall, logs, and data boundary are explicit. |
| What must a smoke test prove? | Runtime/model id, startup command, endpoint route, non-streaming response, and safe binding. |
| What proves a local endpoint is OpenAI-compatible enough for a client? | Base URL, route, served model id, non-streaming response, streaming decision, harmless failure behavior, required feature support, and unsupported or ignored fields. |
| What must a client harness log? | Config, request settings, latency, TTFT if streaming, usage tokens, status, error class, excerpt or output path. |
| What sampling controls must be fixed for a fair benchmark? | Temperature, top-p, top-k, min-p when supported, penalties, seed behavior, stop strings, structured-output mode, and output cap. |
| How do you prove a long, RAG, tool, or multi-turn request fits? | Count the rendered prompt with the serving tokenizer, reserve output tokens, include history/RAG/tool/template overhead, leave a safety margin, and test truncation behavior. |
| How do you prove a local tool call is safe enough to execute? | Validate model arguments against schema, check an external policy boundary, enforce least privilege, log the decision, and bound retries/timeouts before execution. |
| What makes a benchmark reproducible? | Same prompt, model, runtime, quantization, hardware, sampling, context, and output cap. |
| What distinguishes fast-but-wrong from good? | Quality harness scoring tied to workload, not subjective feel. |
| What makes an adaptation decision defensible? | Baseline failure, method matched to failure mode, clean data boundary, held-out eval, regression checks, deployment impact, and rollback, as in [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]]. |
| What makes the deployment decision defensible? | Workload, quality, latency, memory/cost, privacy, security, operational owner, and rejected alternatives, as in [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]. |

Required evidence: [[LLM/Study/Local LLM Hosting and Inference Lab]], [[LLM/Study/Local LLM Serving Runbook]], [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]], [[LLM/Study/Local LLM Client Harness Lab]], [[LLM/Study/Decoding and Sampling Controls Lab]], [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]], [[LLM/Study/Local RAG Minimal Python Harness]], [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]], [[LLM/Study/Local LLM Inference Benchmark Log]], [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]], and [[LLM/Study/LLM Deployment Decision Matrix]].
Add [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the exam answer depends on artifact format, tokenizer, chat template, quantization, runtime support, or API route.

## Section 5: Debugging Scenarios

For each scenario, name the failed layer, the evidence to collect, and the next controlled change.

| Scenario | Expected diagnosis path |
| --- | --- |
| `curl` gets connection refused. | Server/process: listener, host, port, server logs. |
| `/v1/chat/completions` returns 404. | Route mismatch: native vs OpenAI-compatible route, missing `/v1`, wrong method. |
| Model id is not found. | Runtime registry: list served models and copy exact id. |
| The server OOMs on startup. | Weight memory, quantization, runtime overhead, GPU offload, free RAM/VRAM. |
| It loads but OOMs on RAG prompts. | KV cache/context/retrieved chunks/concurrency. |
| First token is slow but later tokens are acceptable. | Prefill, long prompt, cold load, queueing, prefix cache. |
| Later tokens are slow. | Decode bottleneck, model size, memory bandwidth, offload, quantization, backend. |
| Non-streaming works but streaming crashes the app. | Client stream parser, raw event sample, first delta, final chunk. |
| Output includes role markers or wrong speaker. | Chat template, tokenizer, role boundary, stop strings. |
| RAG answer cites a source that does not support the claim. | Retrieval vs generation vs citation boundary; inspect top-k and claim support. |

Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] as the answer key for the diagnostic order.

## Section 6: RAG, Tools, And Evaluation

| Prompt | A passing answer must include |
| --- | --- |
| What are the layers of a local RAG assistant? | Corpus boundary, chunking, embedding, indexing, retrieval, reranking, context assembly, generation, citation, evaluation. |
| How do you distinguish retrieval failure from generation failure? | Expected source and retrieved top-k before judging answer text. |
| Why can chunking be the problem even with a strong model? | Evidence can be split, buried, duplicated, or missing from retrieved context. |
| What does a citation prove? | Only that a claim is supported by a retrieved passage when checked claim by claim. |
| What is LLM-as-judge useful for and where can it fail? | Fast comparative signal; vulnerable to bias, verbosity, position, and calibration issues. |
| Why must a local quality suite use private/workload prompts? | Public prompts can be contaminated or irrelevant to the real workload. |
| How should tools be controlled? | Schema validation, external policy gate, least privilege, audit log, no model-generated permission. |
| What is prompt injection in RAG? | Untrusted retrieved text tries to override system, developer, tool, or output rules. |
| What should a safety/refusal test measure? | Boundary compliance without blocking allowed benign work. |
| When is local hosting preferable to hosted APIs? | Privacy, offline control, cost, latency, customization, or policy requirements outweigh operations burden. |

Remediation: [[LLM/Study/Local RAG Assistant Lab]], [[LLM/Study/Local RAG Minimal Python Harness]], [[LLM/Study/Local LLM Quality Evaluation Harness]], [[LLM/Study/Local LLM Security and Privacy Runbook]], [[LLM/Study/LLM Deployment Decision Matrix]], and [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]].

## Practical Gates

These gates are stricter than the oral questions.

| Gate | Required proof |
| --- | --- |
| Architecture | Attention implementation or worked tensor-shape proof. |
| Tiny decoder training | Toy causal LM proof using [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]]. |
| Paper literacy | One paper protocol row for each major cluster. |
| Training pipeline | Capability trace using [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]]. |
| Local endpoint | CLI and HTTP endpoint response from one local model. |
| Environment | Preflight snapshot tied to the machine/runtime that served the model. |
| Model acquisition | Provenance card proving model card, license, gated access, exact artifact, revision/tag/digest, local path, and unsafe-file risk. |
| Runtime compatibility | Evidence card proving artifact format, quantization, tokenizer, chat template, runtime, model id, route, and workload contract. |
| API contract | Evidence card proving OpenAI-compatible base URL, route, model id, non-streaming response, streaming behavior, harmless failure behavior, and required feature gaps. |
| Decoding controls | Evidence proving sampler settings are frozen or intentionally varied with temperature/filter/penalty/stop behavior recorded. |
| Context budget | Evidence proving rendered prompt tokens, output reserve, RAG/tool/history overhead, safety margin, and truncation behavior are known. |
| Tool loop | Evidence proving tool schema, argument validation, policy check, execution, result injection, bounded retry/stop rules, and failure rows. |
| Benchmark | Reproducible row with model, runtime, quantization, context, TTFT, tokens/sec, memory, and prompt class. |
| Quality | Prompt-suite result with pass/hold/fail decision. |
| Adaptation | Decision memo choosing prompt, RAG, SFT, LoRA, QLoRA, DPO, distillation, continued pretraining, or no training from measured evidence. |
| Failure diagnosis | One failure or explicit no-failure row with failed layer and controlled next action. |
| RAG | Retrieval/citation proof with at least one diagnosed failure mode. |
| Deployment | Decision memo using [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to choose local CPU, local GPU, self-hosted server, hosted API, hybrid, or batch inference. |

Do not mark the capstone complete until every proof link exists in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]].

## Remediation Map

| Failed area | Study next |
| --- | --- |
| Timeline or field map | [[LLM/LLM — Learning Path]] |
| Architecture and tensor shapes | [[LLM/Study/LLM Architecture Cheatsheet]] and [[LLM/Study/Attention Implementation Lab]] |
| Training loop mechanics | [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]], [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]], and [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives]] |
| Paper skepticism | [[LLM/Study/LLM Paper Reading Protocol]] |
| Training and scaling | [[LLM/Study/LLM Training Pipeline Map]], [[LLM/2020–2021 — The Scaling Era/Scaling Laws]], and [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism]] |
| Adaptation and fine-tuning | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]], [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]], and [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA]] |
| Alignment and preference methods | [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback]] and [[LLM/2022 — Alignment and Chat/Direct Preference Optimization]] |
| Inference memory and latency | [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]] and [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]] |
| Local setup | [[LLM/Study/Local LLM Environment Preflight Lab]] and [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| Endpoint and client | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]], [[LLM/Study/Local LLM Serving Runbook]], [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]], and [[LLM/Study/Local LLM Client Harness Lab]] |
| Request behavior | [[LLM/Study/LLM Inference Request Lifecycle Lab]], [[LLM/Study/Decoding and Sampling Controls Lab]], [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]], [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]], and [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| Debugging | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| RAG and citations | [[LLM/Study/Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness]] |
| Evaluation | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Security and deployment | [[LLM/Study/Local LLM Security and Privacy Runbook]], [[LLM/Study/LLM Deployment Decision Matrix]], and [[LLM/Study/LLM Mastery Capstone Workbook]] |

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM — Learning Path]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
