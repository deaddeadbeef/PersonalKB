---
tags: [llm, foundations]
up: "[[2017 — The Transformer Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Positional Encoding

> **One-line summary** Positional encoding injects sequence order into transformers so self-attention can tell not just which tokens exist, but where they occur.

## 🎯 Intuition
**The Core Idea:** Because self-attention is permutation-invariant, positional encoding gives the model a way to represent token order.
**Analogy:** Like seat numbers in a theater, positional encodings tell the model where each token is sitting so it does not confuse the same set of people arranged in a different order.
**Why It Matters:** Without positional information, a transformer cannot distinguish "the cat sat on the mat" from "mat the on sat cat the." Position encoding choice also strongly affects how well a model handles long contexts. The shift from absolute to relative position encoding was a key enabler of the jump from 4K to 128K to 1M context windows in modern models.

---

## ⚙️ Core Mechanics
### How It Works
- Self-attention is permutation-invariant, so transformers need extra information to represent order.
- The original transformer used fixed sinusoidal positional encodings: each position gets a unique vector composed of sine and cosine functions at different frequencies.
- This was designed to allow the model to attend to relative positions through linear transformations of the encoding.
- Learned absolute position embeddings, used in BERT and early GPT models, add a trained embedding for each position from 1 to max_length.
- Rotary Position Embedding (RoPE), used in LLaMA, Mistral, and most modern LLMs, applies a rotation matrix to query and key vectors based on position.
- The dot product between rotated Q and K naturally depends on relative position, providing a clean mathematical framework that supports length extrapolation.
- ALiBi takes a different approach: instead of modifying embeddings, it adds a linear penalty to attention scores based on distance between query and key positions.
- No positional embeddings are needed in ALiBi — just a bias term in the attention computation.
- **Sinusoidal**: PE(pos, 2i) = sin(pos / 10000^(2i/d)), PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
- **Learned absolute**: position embedding table of shape (max_len, d_model), added to token embeddings
- **RoPE**: apply rotation R_θ(pos) to Q and K; dot product Q·K encodes relative position
- **ALiBi**: Attention(Q, K, V) = softmax(QK^T/$\sqrt{d}$ - m × |i-j|) × V, where m is a head-specific slope
- **NTK-aware scaling**: modify RoPE base frequency for longer contexts without retraining
- **YaRN**: Yet another RoPE extension, combining NTK scaling with attention temperature adjustment
- **Length extrapolation**: ability to handle sequences longer than seen during training

### Key Specifications

| Method | Type | Length Extrapolation | Used By |
|--------|------|---------------------|---------|
| Sinusoidal | Fixed absolute | Limited | Original transformer |
| Learned | Trained absolute | None (fixed max) | BERT, GPT-2 |
| RoPE | Relative (rotation) | Good (with scaling) | LLaMA, Mistral, Qwen |
| ALiBi | Relative (bias) | Good | BLOOM, MPT |

### Key Facts
- Positional encoding exists because self-attention alone is permutation-invariant.
- Learned absolute embeddings are simple but cannot extrapolate beyond training length.
- RoPE is dominant in modern LLMs because it provides relative position information and supports scaling tricks.
- ALiBi encodes position through an attention-score bias rather than explicit positional embeddings.

---

## 🔬 Deep Dive
### Technical Details
The original transformer used fixed sinusoidal positional encodings, where each position receives a unique vector composed of sine and cosine functions at different frequencies:

PE(pos, 2i) = sin(pos / 10000^(2i/d)), PE(pos, 2i+1) = cos(pos / 10000^(2i/d))

This construction was intended to let the model recover relative positions through linear transformations. Learned absolute position embeddings instead use a trainable position embedding table of shape (max_len, d_model), added directly to token embeddings, as in BERT and early GPT models, but these methods cannot extrapolate beyond the trained maximum length. RoPE applies a rotation R_θ(pos) to queries and keys so that the dot product between rotated Q and K naturally depends on relative position. This clean formulation made RoPE the dominant method in models like LLaMA, Mistral, and Qwen. ALiBi instead adds a linear penalty directly to attention scores:

Attention(Q, K, V) = softmax(QK^T/$\sqrt{d}$ - m × |i-j|) × V

where m is a head-specific slope. Further long-context extensions include NTK-aware scaling, which modifies the RoPE base frequency without retraining, and YaRN, which combines NTK scaling with attention temperature adjustment.

### Limitations and Criticisms
- Learned absolute position embeddings cannot extrapolate beyond the maximum sequence length seen in training.
- Fixed sinusoidal encodings provide only limited length extrapolation compared with newer relative schemes.
- Long-context performance often depends not just on the base method, but on additional scaling or extension techniques such as NTK-aware scaling and YaRN.

### Impact and Legacy
Position encoding choice directly affects long-context capability. RoPE's dominance in modern LLMs comes from its clean relative-position formulation and compatibility with extension techniques. More broadly, the move from absolute to relative position handling was central to the rapid expansion of usable context windows in modern transformer systems.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can a transformer not recover word order from self-attention alone?
2. What is the main practical limitation of learned absolute position embeddings?
3. Why does RoPE tend to work better for long-context scaling than older absolute schemes?

### Core Problems
1. Compare sinusoidal encodings, learned absolute embeddings, RoPE, and ALiBi in terms of how each injects position and what that implies for extrapolation.
2. Explain how ALiBi changes the attention computation differently from RoPE, and analyze which parts of the model each method modifies.

### Challenge
1. Investigate one long-context extension technique for RoPE, such as NTK-aware scaling or YaRN, and explain why it helps models generalize beyond their original context window.

---

*See also:* [[Encoder-Only Models]] — learned positional embeddings in BERT and variants; [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]] — extending position representation to long contexts; [[State Space Models and Mamba]] — alternative architectures that handle position implicitly; [[KV Cache and Context Reuse]] — positional encoding interplay with cached keys and values

## References
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

- [[LLM/Sources/Sources Index]]
