---
tags: [study, llm, inference, local-llm, architecture, systems]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [intuition, core, practice, deep-dive]
last-verified: 2026-06-15
---

# LLM Mechanism-to-Inference Bridge Map

> **One-line summary** Local LLM hosting is easier to reason about when every runtime decision is tied to a model mechanism: tokens, attention, positional encoding, KV cache, quantization, sampling, batching, RAG, tools, and evaluation.

Use this after [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]] and before the local inference labs. The paper map explains how the field got here. This bridge explains why the academic mechanisms show up as concrete local knobs, failures, and evidence rows. Use [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] when you need the whole local serving story from model bytes to operations decision.

## The Bridge Rule

Do not stop at "the model is slow" or "the answer is bad." Name the mechanism.

```text
symptom -> mechanism -> local control -> evidence artifact -> next decision
```

Examples:

- Slow first token -> long prefill and cache construction -> count prompt tokens and shorten context -> [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|context budget row]] plus benchmark -> keep, reduce context, or change runtime.
- OOM on startup -> weight memory and runtime overhead -> smaller model or stronger quantization -> [[LLM/Study/Local LLM Model and Hardware Sizing Guide|sizing estimate]] plus load log -> keep, quantize, or scale down.
- Wrong role markers -> chat template and stop-boundary mismatch -> render the prompt and inspect special tokens -> [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|tokenizer/template test]] -> fix template or switch artifact.
- Fast but wrong -> capability or post-training gap, not just serving speed -> run a workload rubric -> [[LLM/Study/Local LLM Quality Evaluation Harness|quality row]] -> prompt, RAG, model swap, or adaptation decision.

## Mechanism Translation Table

| Academic mechanism | What it means locally | First evidence to capture | Main vault route |
|---|---|---|---|
| Tokenization | Text becomes token IDs; token counts decide context use, cost, and prefill work. | Rendered prompt, token count, special-token check. | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Chat template | Messages become one model-specific string or token sequence. | System/user/assistant rendering and stop boundaries. | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Runtime stack ownership | Local inference failures belong to a layer: hardware, boundary, package environment, model bytes, artifact, tokenizer/template, runtime, scheduler/cache, route, client/UI, workload, or operations. | Stack Anatomy Card with the lowest unproven layer. | [[LLM/Study/Local LLM Runtime Stack Anatomy]] |
| Decoder-only autoregression | Generation is a next-token loop, not one whole answer computed at once. | Prompt tokens, output tokens, stop reason, streaming trace. | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Causal self-attention | A token reads prior tokens through Q/K/V attention while future tokens are masked. | Worked tensor shapes or implementation output. | [[LLM/Study/Attention Implementation Lab]] |
| Positional encoding | The model needs position information; RoPE/ALiBi/context-extension choices affect long-context behavior. | Context limit, rendered length, long-prompt quality test. | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| KV cache | Past keys and values are stored so decode can reuse prior context. Cache grows with layers, length, precision, and active sequences. | TTFT, context length, active sequences, memory notes. | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| MHA, MQA, and GQA | Sharing key/value heads can reduce cache memory and improve decode economics with a quality trade-off. | Model architecture note, cache risk, runtime compatibility card. | [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]] |
| Weight precision and quantization | Lower-bit weights reduce memory and bandwidth pressure but can damage hard reasoning, formatting, or rare-token behavior. | Quantization type, offload setting, KV-cache precision, quality row, benchmark row. | [[LLM/Study/Local LLM Quantization and GPU Offload Lab]] |
| Sampling and constraints | Logits become text through temperature, filters, penalties, stops, or grammar/schema constraints. | Frozen sampler settings and A/B sweep. | [[LLM/Study/Decoding and Sampling Controls Lab]] |
| Prefill versus decode | Long input mainly hurts time to first token; model size and memory bandwidth often dominate later tokens/sec. | Short-vs-long prompt timing. | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Inference metrics | TTFT, TPOT, output tokens/sec, total latency, memory, queue, and quality each prove different local claims. | Metric owner, phase, confounder, and next controlled action. | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| Batching and PagedAttention | Serving many requests is a cache-management and scheduling problem, not only a model-quality problem. | Concurrency, throughput, latency, queue, slot, preemption, and cache notes. | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Prompt caching | Repeated prefixes can reuse cache work when the runtime supports compatible prefix reuse. | Repeated-prefix benchmark and cache setting. | [[LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure]] |
| RAG context assembly | Retrieval controls what evidence the model can see; generation quality cannot rescue missing or wrong context. | Corpus manifest, top-k evidence, cited answer, refusal row. | [[LLM/Study/Local RAG Minimal Python Harness]] |
| Embedding and reranking inference | The retriever and reranker are separate model calls with their own dimensions, routes, batching, score semantics, and latency. | Embedding/reranker service card, vector-shape check, rerank gain row. | [[LLM/Study/Local Embedding and Reranker Hosting Lab]] |
| Tool calling | The model proposes structured actions; the application must validate, authorize, execute, and feed back results. | Tool schema, validated args, policy decision, execution log. | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]] |
| Post-training and alignment | Instruction following, refusal style, verbosity, and helpfulness are learned behaviors layered over the base model. | Prompt-suite score and failure-owner note. | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] |
| Metric interpretation | Loss, perplexity, benchmark, preference, calibration, latency, and memory numbers each prove different claims. | Metric card with claim, dataset, missed failure mode, and next proof route. | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]] |
| Evaluation | Quality is only meaningful relative to workload, rubric, and held-out examples. | Human rubric, LLM-as-judge note, pass/hold/fail decision. | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Deployment economics | A model can be academically strong but operationally wrong for latency, privacy, cost, or ownership. | Deployment memo with rejected alternatives. | [[LLM/Study/LLM Deployment Decision Matrix]] |

## Read A Local Failure Mechanistically

| Symptom | Likely mechanism | Do first | Do not do first |
|---|---|---|---|
| `curl` connection refused | Process, listener, host, or port, not model weights. | Check server process, binding, port, logs. | Redownload the model. |
| Model loads, then RAG prompt OOMs | KV cache and context length. | Count rendered prompt, reduce retrieved chunks, lower context or concurrency. | Assume quantization failed. |
| First token is slow | Prefill, cold load, queueing, or long prompt. | Compare short and long prompts. | Tune temperature. |
| Later tokens are slow | Decode loop, model size, memory bandwidth, offload, cache. | Log tokens/sec, hardware path, quantization, context. | Rewrite the prompt. |
| Output starts with stray role text | Chat template, special tokens, or stop sequence. | Render and inspect the exact prompt. | Fine-tune the model. |
| JSON is almost correct but fails parsing | Structured-output boundary. | Add schema validation or constrained decoding if supported. | Treat the answer as passed. |
| RAG answer cites unsupported facts | Retrieval/generation/citation boundary. | Inspect top-k chunks before the answer text. | Raise model size blindly. |
| Benchmark changed after one edit | Sampling or request drift. | Freeze prompt, seed support, sampler settings, max tokens, model, runtime. | Compare subjective impressions. |
| Quantized model is fast but misses details | Numerical compression and task sensitivity. | Run the same quality suite on less aggressive quantization or a smaller FP16 model. | Declare local hosting unsuitable. |
| Local endpoint works but client integration fails | API contract, route, streaming, error shape, or ignored fields. | Fill the OpenAI-compatible contract card. | Change model family. |

## Academic Concept To Local Prediction

Use this as an oral drill. For each concept, make a prediction before running the local lab.

| Concept | Prediction to make before testing | Evidence that proves or falsifies it |
|---|---|---|
| Attention complexity | Longer prompts should increase prefill cost and memory pressure. | Prompt-token sweep with TTFT and memory notes. |
| KV cache | More context or active sequences should increase cache memory. | Context/concurrency row in the sizing guide. |
| GQA/MQA | A model with fewer KV heads should be easier to serve at long context than comparable MHA, all else equal. | Architecture note plus benchmark under matched prompt length. |
| Quantization | Lower-bit weights should reduce memory, but the quality hit may appear on exact formatting, code, math, or rare facts. | Quality harness comparison. |
| Chat template | An instruct model should degrade if messages are rendered in the wrong format. | Template A/B with same user prompt. |
| Sampling | Higher randomness should change wording and may damage factual/structured tasks. | Decoding controls sweep. |
| RAG | Missing retrieved evidence should cause refusal or a correctly diagnosed retrieval miss, not confident invention. | Retrieval evidence plus unsupported-question row. |
| Tool loop | The model should not be trusted to grant permission to its own tool call. | Policy decision outside model output. |
| Post-training | If the model knows the fact but will not follow instructions, the failure may be SFT/preference/template related. | Base-vs-chat behavior test and quality rubric. |
| Deployment | The best benchmark model may still lose if privacy, latency, cost, or operations fail. | Deployment decision matrix. |

## Mechanism Explanation Template

Copy this into a paper note, lab result, benchmark note, or capstone row.

| Field | Answer |
|---|---|
| Observed behavior |  |
| Mechanism named | tokenization / template / attention / position / KV cache / quantization / sampling / batching / RAG / tool / alignment / eval |
| Why that mechanism is plausible |  |
| Evidence collected |  |
| Confounders controlled | model / runtime / prompt / sampler / context / hardware / route |
| Next controlled change |  |
| Decision | keep / retry / reduce context / quantize / change runtime / change model / add RAG / adapt / deploy / reject |

Pass signal: another person can read the row and see why the next action follows from the mechanism, not from trial-and-error.

## Capstone Use

For the mastery capstone, use this bridge in three places:

1. After the paper map: explain how at least five paper mechanisms become local inference controls.
2. Before the first local endpoint run: predict the likely bottleneck from model size, context, quantization, runtime, and hardware.
3. After quality evaluation: name whether the observed failure belongs to the model, data, prompt, RAG, tokenizer/template, runtime, tool boundary, or evaluation design.

Minimum bridge proof:

- [ ] one architecture mechanism explained with a tensor, formula, or paper claim
- [ ] one systems mechanism explained with a benchmark or memory row
- [ ] one compatibility mechanism explained with a tokenizer/template/runtime card
- [ ] one quality mechanism explained with an evaluation row
- [ ] one metric interpreted as claim, distribution, limitation, and next proof route
- [ ] one deployment decision that rejects at least one plausible alternative

## Completion Gate

This bridge is complete when you can answer these without notes:

- [ ] How does attention become a local context and memory problem?
- [ ] Why are prefill latency and decode throughput different measurements?
- [ ] Why can a quantized model be operationally useful and academically lossy at the same time?
- [ ] Why is a chat template a learned interface rather than formatting decoration?
- [ ] Why does RAG move some failures outside the model weights?
- [ ] Why is OpenAI-compatible API support not the same as full feature compatibility?
- [ ] Why does quality evaluation need workload-specific prompts, not only a fast benchmark?
- [ ] How would you choose the next controlled change after one failed local run?

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[chunk-llm-049 FlashAttention Exact Attention with Tiling]]
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[chunk-llm-217 GQA Mechanism Interpolating MHA and MQA]]
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]]

External/current sources checked 2026-06-15:

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [GQA: Training Generalized Multi-Query Transformer Models](https://arxiv.org/abs/2305.13245)
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [GPTQ](https://arxiv.org/abs/2210.17323)
- [AWQ](https://arxiv.org/abs/2306.00978)
- [Hugging Face chat templates](https://huggingface.co/docs/transformers/en/chat_templating)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [llama.cpp server](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [LM Studio OpenAI compatibility](https://lmstudio.ai/docs/developer/openai-compat)
