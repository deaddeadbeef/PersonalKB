---
tags: [study, llm, math, tensors, attention, inference]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
freshness: stable
tier-coverage: [core, deep-dive, practice]
---

# LLM Math and Tensor Shape Primer

> **One-line summary** The minimum math for LLM mastery is being able to trace token IDs into embeddings, hidden states, logits, probabilities, loss, attention matrices, KV cache, and local inference memory estimates.

Use this before [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]], [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]], and [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]]. The goal is not advanced math fluency. The goal is to stop treating formulas as decoration and start using them to debug model behavior, training loops, and local serving runs. Use [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]] after this primer when loss, perplexity, benchmark scores, calibration, or local quality rows become decision evidence.

## Symbols

| Symbol | Meaning |
|---|---|
| `B` | batch size |
| `T` | sequence length or context length |
| `V` | vocabulary size |
| `D` | model width, also called `d_model` |
| `H` | number of attention heads |
| `Dh` | per-head width, usually `D / H` |
| `L` | number of transformer layers |
| `P` | parameter count |
| `N` | number of training tokens |

Keep these symbols stable across notes. Most confusion in transformer math comes from changing the meaning of `T`, `D`, or `H` halfway through an explanation.

## The Five Objects To Track

| Object | Shape | What it means |
|---|---|---|
| Token IDs | `[B, T]` | Integer indexes into the vocabulary. |
| Embeddings | `[B, T, D]` | Dense vectors looked up from token IDs and position information. |
| Hidden states | `[B, T, D]` | Contextual token representations after transformer blocks. |
| Logits | `[B, T, V]` | Unnormalized scores for each vocabulary token at each position. |
| Probabilities | `[B, T, V]` | Softmax-normalized next-token distribution. |

The local inference loop only needs the final position's logits during decode:

```text
last_logits = logits[:, -1, :]  # [B, V]
next_token = sample(softmax(last_logits))
```

Training usually computes loss at every position, while inference samples one new token at a time.

## Logits, Softmax, And Sampling

Logits are scores, not probabilities. Softmax turns a vector of logits into a probability distribution:

```text
p_i = exp(z_i) / sum_j exp(z_j)
```

Temperature rescales logits before softmax:

```text
p = softmax(logits / temperature)
```

Practical consequence:

| Setting | Effect |
|---|---|
| lower temperature | Sharper distribution, more deterministic output. |
| higher temperature | Flatter distribution, more varied output. |
| top-k | Keep only the `k` highest-scoring tokens. |
| top-p | Keep the smallest likely set whose cumulative probability reaches `p`. |
| max tokens | Stop the autoregressive loop after a fixed output budget. |

This is why [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] belongs in the same mastery path as attention and cross-entropy. A bad sampler setting can make a good model look unreliable.

## Cross-Entropy And Perplexity

For next-token training, the target at each position is the following token. If the correct next token has probability `p_correct`, the per-token loss is:

```text
loss = -log(p_correct)
```

Cross-entropy averages that loss across positions and examples. Lower is better because the model assigned more probability to the true next tokens.

Perplexity is the exponentiated average negative log-likelihood:

```text
perplexity = exp(cross_entropy)
```

Interpretation:

| Observation | Meaning |
|---|---|
| training loss falls | The model is fitting the training distribution. |
| validation loss also falls | The fit transfers to held-out text. |
| training loss falls but validation rises | The model is overfitting. |
| perplexity falls | The model is less surprised by the evaluation text. |

Perplexity is useful for language-model pretraining, but it is not enough for assistant quality. A local model can have decent perplexity and still fail instruction following, citations, JSON, tools, or safety boundaries. Use [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]] to decide whether a number is training evidence, benchmark evidence, local quality evidence, or operations evidence.

## Shifted Targets

The causal LM objective is visible in one tiny row:

```text
tokens:  [t0, t1, t2, t3, t4]
input:   [t0, t1, t2, t3]
target:  [t1, t2, t3, t4]
```

The model predicts the next token at every position. That is why [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] requires a printed input/target shift example.

Teacher forcing lets training run in parallel across sequence positions because the true previous tokens are already present. Causal masking prevents the model from seeing future target tokens.

## Attention Shape Contract

Scaled dot-product attention:

```text
Attention(Q, K, V) = softmax((Q K^T) / sqrt(Dh)) V
```

Multi-head self-attention shapes:

| Tensor | Shape | Meaning |
|---|---|---|
| `X` | `[B, T, D]` | Input hidden states. |
| `Q, K, V` after projection | `[B, T, H, Dh]` | Per-head learned views. |
| `Q, K, V` after transpose | `[B, H, T, Dh]` | Head dimension moved before sequence. |
| `scores` | `[B, H, T, T]` | Every query position compared with every key position. |
| `weights` | `[B, H, T, T]` | Softmax over keys. |
| `head_output` | `[B, H, T, Dh]` | Weighted sum of values for each head. |
| merged output | `[B, T, D]` | Heads concatenated and projected. |

Why this matters locally:

- The `T x T` score matrix explains why long context is expensive.
- During decode, new tokens reuse cached K/V tensors instead of recomputing the whole prefix.
- MQA and GQA reduce KV-cache memory by sharing K/V heads.

## Transformer Block Shape Contract

A decoder block usually preserves `[B, T, D]` from input to output:

```text
X
-> layer norm
-> causal self-attention
-> residual add
-> layer norm
-> MLP
-> residual add
```

The MLP expands and contracts the channel dimension:

```text
[B, T, D] -> [B, T, 4D] -> [B, T, D]
```

This is why transformer blocks are easy to stack: each block accepts and returns the same shape. It is also why hidden width `D`, layer count `L`, and MLP expansion heavily affect parameter count and inference cost.

## Parameter And FLOP Planning

Rough pretraining compute estimate:

```text
training FLOPs ~= 6 x P x N
```

Rough weight memory estimate:

```text
weight memory ~= P x bytes_per_parameter
```

Planning bytes:

| Format | Bytes per parameter |
|---|---:|
| FP32 | 4 |
| FP16 / BF16 | 2 |
| INT8 | 1 |
| INT4 | 0.5 |

This estimate explains why [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] starts with model size and quantization before runtime tuning. A 7B FP16 model needs roughly 14 GB just for weights before KV cache and runtime overhead.

## KV-Cache Arithmetic

Simplified KV-cache estimate:

```text
KV cache ~= 2 x L x T x D x bytes_per_element x active_sequences
```

The `2` is for keys and values. The real implementation may use head dimensions, grouped KV heads, paging, or cache quantization, but the planning lesson is stable:

- longer context increases cache memory
- more concurrent active sequences increase cache memory
- weight quantization does not automatically shrink the KV cache
- MQA/GQA can reduce KV-cache footprint by using fewer K/V heads
- prompt caching helps only when repeated prefixes can actually be reused

This is the bridge from math to local serving: prompt length, RAG chunk count, tool schemas, chat history, and output reserve all become memory and latency pressure.

When the estimate needs to become a saved local-hosting decision, use [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]]. That runner uses the head-aware formula for MHA, MQA, and GQA models instead of assuming every attention head has its own key/value cache.

## Prefill Versus Decode

| Phase | What happens | Metric |
|---|---|---|
| Prefill | Process the whole prompt and build initial KV cache. | Time to first token. |
| Decode | Generate one token at a time, extending the cache. | Tokens/sec. |

If a long prompt makes the first token slow but later tokens are normal, suspect prefill or context assembly. If every later token is slow, suspect model size, memory bandwidth, quantization/backend, CPU/GPU offload, or cache pressure.

## Common Math-To-Implementation Bugs

| Symptom | Likely mistake |
|---|---|
| Loss never decreases | Targets not shifted, logits/targets reshaped incorrectly, optimizer not stepping. |
| Softmax rows do not sum to one | Softmax over the wrong dimension. |
| Model learns future tokens too well | Causal mask missing or inverted. |
| Output tensor has unexpected head dimension | Transpose or reshape mistake in multi-head attention. |
| JSON output is unstable across runs | Sampling settings not frozen or temperature too high. |
| Long prompt OOMs even with quantized weights | KV-cache memory, not weight memory. |
| Smoke test is fast but quality is weak | Endpoint proof is not a quality proof. |

## Oral Drill

Answer these without notes:

1. What is the shape difference between token IDs, embeddings, hidden states, and logits?
2. Why does softmax run over vocabulary for sampling but over keys for attention?
3. Why are causal LM targets shifted by one token?
4. What does cross-entropy measure at one position?
5. Why does the attention score matrix have shape `[B, H, T, T]`?
6. Why does KV cache grow with context length?
7. Why can quantizing weights still leave long-context OOMs?
8. Why are TTFT and tokens/sec different measurements?
9. Why is a fast smoke response not enough to choose a model?
10. Which math object would you inspect first for a chat-template failure: token IDs, logits, KV cache, or loss?

## Completion Gate

This primer is complete when you can:

- [ ] explain token IDs, embeddings, hidden states, logits, probabilities, and sampled tokens
- [ ] derive the shifted next-token target example
- [ ] explain cross-entropy and perplexity in plain language
- [ ] trace every attention shape from `X` to `scores` to merged output
- [ ] connect `T x T` attention to long-context cost
- [ ] estimate weight memory from parameter count and precision
- [ ] estimate why KV cache grows with context and active sequences
- [ ] explain TTFT versus decode tokens/sec
- [ ] diagnose one local inference symptom using a math object from this note

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives]]
- [[LLM/Pre-2017 — Before Transformers/Perplexity and Intrinsic Metrics]]
- [[LLM/2017 — The Transformer/Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/_chunks/chunk-llm-001 Scaled Dot-Product Attention Formula]]
- [[LLM/_chunks/chunk-llm-017 Compute-Optimal Scaling Ratio]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
