---
tags: [llm, foundations]
up: "[[2017 — The Transformer Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Attention Mechanism

> **One-line summary** Attention lets each token directly compare itself with all other tokens and build a relevance-weighted representation of the whole sequence.

## 🎯 Intuition
**The Core Idea:** Attention computes a weighted sum of value vectors, where the weights come from how well queries and keys match.
**Analogy:** Like a spotlight on a stage, each token can shine its focus across the full cast and decide which other performers matter most for understanding its role.
**Why It Matters:** Attention is the core operation that gives transformers their power. It allows every token in a sequence to directly interact with every other token, capturing complex dependencies regardless of distance. It also replaced recurrence as the primary sequence modeling mechanism because it enables direct long-range interaction, full training-time parallelization, and partially interpretable patterns of what the model focuses on.

---

## ⚙️ Core Mechanics
### How It Works
- The attention mechanism computes a weighted sum of "value" vectors, where the weights are determined by the compatibility between "query" and "key" vectors.
- Given matrices Q (queries), K (keys), and V (values), scaled dot-product attention computes:
- Attention(Q, K, V) = softmax(QK^T / $\sqrt{d_k}$) × V
- The scaling factor $\sqrt{d_k}$ prevents the dot products from growing too large in magnitude, which would push the softmax into regions with extremely small gradients.
- Multi-head attention runs h parallel attention operations with different learned projections, then concatenates the results.
- This allows the model to attend to information from different representation subspaces at different positions simultaneously — one head might track syntactic relationships while another tracks semantic similarity.
- Self-attention, where Q, K, V all come from the same sequence, is what makes transformers powerful for language: each token can "look at" every other token to build its contextual representation.
- **Scaled dot-product attention**: softmax(QK^T / $\sqrt{d_k}$) × V
- **Multi-head attention**: h parallel heads with independent W_Q, W_K, W_V projections
- **Self-attention**: Q, K, V derived from the same input sequence
- **Cross-attention**: Q from one sequence (decoder), K,V from another (encoder output)
- **Causal masking**: mask future positions to -∞ before softmax for autoregressive models
- **Computational cost**: $O(n² × d)$ for sequence length n and head dimension d
- **Memory cost**: $O(n²)$ for attention weights, key bottleneck for long sequences
- **Multi-query attention (MQA)**: share K,V across heads to reduce KV cache size
- **Grouped-query attention (GQA)**: share K,V among groups of heads (compromise between MHA and MQA)

### Key Specifications

| Aspect | Self-Attention | Cross-Attention |
|--------|---------------|----------------|
| Q, K, V source | Same sequence | Q from one, K/V from another |
| Used in | All transformer blocks | Encoder-decoder models |
| Purpose | Build contextual representations | Integrate information across sequences |

### Key Facts
- Attention is the core operation that gives transformers their power.
- It lets every token directly interact with every other token regardless of distance.
- The main limitation is quadratic cost in sequence length.
- Efficient attention research is largely motivated by the $O(n²)$ compute and memory bottleneck.

---

## 🔬 Deep Dive
### Technical Details
Given matrices Q (queries), K (keys), and V (values), scaled dot-product attention computes:

Attention(Q, K, V) = softmax(QK^T / $\sqrt{d_k}$) × V

The scaling factor $\sqrt{d_k}$ prevents the dot products from growing too large in magnitude, which would otherwise push the softmax into regions with extremely small gradients. Multi-head attention runs h parallel attention operations with different learned projections and then concatenates the results, allowing the model to attend to different representation subspaces at different positions simultaneously. In practice, one head might track syntactic relationships while another tracks semantic similarity. Self-attention uses Q, K, and V from the same sequence, while cross-attention uses Q from one sequence and K,V from another, such as a decoder attending to encoder outputs. Causal masking sets future positions to -∞ before softmax in autoregressive models. Standard attention has computational cost $O(n² × d)$ for sequence length n and head dimension d, and memory cost $O(n²)$ for storing attention weights. Multi-query attention (MQA) shares K,V across heads to reduce KV cache size, while grouped-query attention (GQA) shares K,V among groups of heads as a compromise between full multi-head attention and MQA.

### Limitations and Criticisms
- Standard attention has $O(n² × d)$ compute cost, which becomes expensive at long sequence lengths.
- Attention weights require $O(n²)$ memory, creating a major bottleneck for long-context models.
- The quadratic cost in sequence length is the main limitation and has driven extensive work on efficient attention variants.

### Impact and Legacy
Attention replaced recurrence as the primary sequence modeling mechanism. It enabled direct interaction between any two positions regardless of distance, full parallelization during training, and interpretable attention patterns that reveal what the model focuses on. Its limitations also inspired later work on efficient attention, KV cache optimization, MQA, GQA, and broader long-context transformer design.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does scaled dot-product attention divide by $\sqrt{d_k}$ before applying softmax?
2. What is the difference between self-attention and cross-attention?
3. Why does attention make long-range dependencies easier to model than recurrence?

### Core Problems
1. Given Q, K, and V matrices for a short sequence, compute Attention(Q, K, V) and explain how the attention weights affect the output.
2. Compare the trade-offs between standard multi-head attention, MQA, and GQA for inference-time memory and representational flexibility.

### Challenge
1. Investigate one efficient-attention variant that reduces the $O(n²)$ bottleneck and explain what approximation or architectural trade-off it introduces relative to standard attention.

### Implementation Lab
Use [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] to implement the formula, apply causal masking, and verify tensor shapes.

---

*See also:* [[LLM/Architecture Variants/Efficient Attention and Long-Context Variants|Efficient Attention]] — reducing attention's $O(n²)$ cost; [[LLM/Inference and Serving/KV Cache and Context Reuse|KV Cache]] — caching attention computations for fast generation

## Supporting Chunks
### Supporting Chunks
- [[LLM/_chunks/chunk-llm-001 Scaled Dot-Product Attention Formula|Scaled dot-product attention formula]]
- [[LLM/_chunks/chunk-llm-002 Multi-Head Attention Parallel Projections|Multi-head attention parallel projections]]
- [[LLM/_chunks/chunk-llm-004 Residual Connections and Layer Normalization|Residual connections and layer normalization]]
- [[LLM/_chunks/chunk-llm-213 Multi-Query Attention Shared KV Heads|Multi-query attention shared KV heads]]
- [[LLM/_chunks/chunk-llm-220 GQA Default Attention Modern LLMs|Grouped-query attention as a modern default]]

## References
- [[LLM/_raw/raw-llm-001 Attention Is All You Need|raw-llm-001 Attention Is All You Need]]
- [[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA|raw-llm-054 Fast Transformer Decoding One Write-Head MQA]]
- [[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models|raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]
- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Attention Implementation Lab]]
