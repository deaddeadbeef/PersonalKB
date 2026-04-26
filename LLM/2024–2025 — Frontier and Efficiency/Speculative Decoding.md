---
tags: [llm, inference]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Speculative Decoding

> **One-line summary**: Speculative decoding speeds up autoregressive generation by letting a small model draft several tokens ahead and a larger model verify them in parallel without changing the final output distribution.

---

## 🎯 Intuition

### Core Idea
Autoregressive decoding is slow because large models repeatedly load massive weights to generate one token at a time. Speculative decoding reduces that waste by having a smaller draft model guess the next few tokens, then asking the larger target model to verify them together in one pass.

### Analogy
Speculative decoding is like **a secretary drafting sentences for the boss to approve — faster than writing from scratch**.

### Why It Matters
This is one of the few inference tricks that can reduce latency without degrading output quality. When the draft model is accurate, the system accepts many proposed tokens and achieves major speedups for interactive generation.

---

## ⚙️ Core Mechanics

### How It Works
The draft model generates `K` candidate tokens, often around **4–8**. The larger target model then verifies those candidates in a single forward pass. Tokens are accepted from left to right until one fails the acceptance test. The first rejected token is resampled from an adjusted target distribution, and generation continues. The method is mathematically lossless: the output distribution matches standard target-model decoding.

### Key Specs
- **Draft model**: typically a smaller **500M–1B** model.
- **Target model**: the larger model whose output distribution is preserved.
- **Acceptance criterion**: simplified as accepting a token when `p_target(t) ≥ p_draft(t)`.
- **Rejection sampling**: first rejected token is sampled from `max(0, p_target - p_draft)`.
- **Parallelization benefit**: verifying `K` tokens together is much faster than generating `K` tokens serially.
- **Speedup**: often about **2–3×** when draft and target models are well matched.

### Key Facts
- The main bottleneck in autoregressive decoding is usually **memory bandwidth**, not raw compute.
- On an **A100**, loading a **7B** model’s weights from HBM may take roughly **14ms**, while single-token attention compute is often **<1ms**.
- Speculative decoding works best when the draft model is both fast and accurate.
- It requires both models in memory, which can be expensive at large scale.
- Variants include **Medusa** (extra decoding heads on the target model) and tree-based speculation.


| Concept | What It Is | What It's Not |
| --- | --- | --- |
| **Speculative Decoding vs Parallel Decoding** | Serial verification with early stopping | Beam search or non-autoregressive methods |
| **Draft Model vs Teacher Model** | Draft is smaller, generates candidates | Teacher in distillation provides training signal |
| **Mathematically Lossless vs Approximate** | Output distribution identical to target-only | Not a heuristic or sampling shortcut |
| **Medusa vs Two-Model Speculation** | Single model with extra heads | Separate draft and target models |
| **Acceptance Rate vs Speedup** | Acceptance rate = % tokens kept | Speedup depends on rate, K, and latency ratio |
| **Memory-Bound vs Compute-Bound** | Works best when memory-bound (typical for LLMs) | Less effective if compute is the bottleneck |

---

## 🔬 Deep Dive

### Technical Details
The key systems insight is that verifying several guessed tokens together amortizes the cost of loading target-model weights. Because large LLM inference is often memory-bandwidth-bound, a single pass over several candidate tokens barely costs more than one-token verification. That is why acceptance rate matters so much: the more of the draft survives, the more useful each target pass becomes.

**Medusa** removes the separate draft model by attaching multiple decoding heads to the target model so it can predict several next tokens at once, but that requires extra training. Tree-based speculative decoding broadens the idea further by verifying multiple candidate continuations instead of a single straight-line draft.

### Limitations
- Low draft-model accuracy means low acceptance rates and weak speedups.
- Mismatched model families or training data can reduce benefit sharply.
- Loading both models raises memory requirements.
- If the workload is compute-bound rather than memory-bound, speculative decoding helps less.

### Impact
For chat and other interactive workloads, reducing response latency from something like **300ms to 100ms** can materially improve perceived quality. Speculative decoding is therefore valuable not just as a systems trick, but as a user-experience optimization that preserves exact sampling behavior.

---

## 🏋️ Practice

### Warm-Up
- Why does speculative decoding need both a draft model and a target model?
- What does “mathematically lossless” mean here?

### Core Problems
- Why is memory bandwidth more important than raw compute in this setting?
- How does acceptance rate affect realized speedup?
- Compare Medusa with the standard two-model setup.

### Challenge
- Explain why speculative decoding can speed up generation without changing the final distribution.
- Give one reason why a fast draft model might still produce poor end-to-end speedup.

## Supporting Chunks
_Placeholder for links to specific techniques, implementation details, and case studies._

## See Also
- [[Decoder-Only Models]] — both draft and target models are autoregressive decoders
- [[Transformer Architecture]] — speculative decoding exploits transformer structure
- [[Quantization]] — quantized models often serve as efficient draft models
- [[Distillation and Model Compression]] — distilled models as lightweight draft models
- [[Scaling Laws]] — speed-quality trade-offs connect to scaling relationships

## References
_Placeholder for references to papers, documentation, and source materials._
