---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
---

# Foundations & Architecture — Review Drill

## Quick-Fire Questions

1. **What does scaled dot-product attention compute?**
   softmax(QK^T / $\sqrt{d_k}$) × V — queries matched against keys, weighted sum of values.

2. **Why divide by $\sqrt{d_k}$?**
   Prevents dot products from growing large with dimension, keeping softmax gradients healthy.

3. **What's the difference between self-attention and cross-attention?**
   Self: Q, K, V from same sequence. Cross: Q from one sequence, K/V from another (e.g., decoder attending to encoder).

4. **Why do transformers need positional encoding?**
   Attention is permutation-invariant — without position info, "cat sat mat" and "mat sat cat" look identical.

5. **RoPE vs ALiBi — what's the key difference?**
   RoPE: rotates Q,K vectors by position-dependent angle. ALiBi: adds linear distance penalty to attention scores. Both encode relative position.

6. **What's the computational complexity of self-attention?**
   $O(n² × d)$ for sequence length n and head dimension d. Memory is $O(n²)$ for the attention matrix.

7. **How does Flash Attention achieve speedup without approximation?**
   IO-aware tiling: computes exact attention in SRAM tiles instead of materializing the full n² attention matrix in HBM. Same math, better memory access pattern.

8. **Encoder-only vs decoder-only — when to use which?**
   Encoder-only (BERT): classification, embeddings, NER. Decoder-only (GPT): generation, chat, reasoning. Decoder-only dominates general-purpose use.

9. **What is MoE and why does it help?**
   Mixture-of-Experts: replace FFN with multiple expert FFNs, router picks top-k per token. Scales total params without proportional compute increase.

10. **How does Mamba differ from a transformer?**
    Linear $O(n)$ complexity via selective state spaces instead of $O(n²)$ attention. Fixed-size state instead of growing KV cache. Weaker at precise retrieval from context.

## Conceptual Checks

11. **Pre-norm vs post-norm — which is used in modern LLMs and why?**
    Pre-norm (LN before sublayer). Improves training stability at scale. Used in LLaMA, GPT-3+.

12. **Why did decoder-only win over encoder-decoder for general LLMs?**
    Simpler architecture, natural fit for generation, better scaling properties, emergent capabilities with scale.

13. **BPE vs Unigram tokenization — what's the algorithmic difference?**
    BPE: bottom-up merging of frequent pairs. Unigram: top-down probabilistic pruning from large vocabulary.

14. **What is superposition in the context of neural network representations?**
    Models encode more features than dimensions by using sparse, nearly-orthogonal directions. Most features are only active for a small fraction of inputs.

15. **GQA (Grouped-Query Attention) — what problem does it solve?**
    Reduces KV cache memory by sharing K,V across groups of heads. Compromise between full MHA (each head has own KV) and MQA (all heads share one KV).

## Hands-On

- [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] — implement scaled dot-product attention, causal masking, multi-head reshaping, and shape tests.
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] — train a tiny causal LM and connect shifted targets, cross-entropy loss, validation loss, and generation.
