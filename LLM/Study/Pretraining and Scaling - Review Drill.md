---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
---

# Pretraining & Scaling — Review Drill

## Quick-Fire Questions

1. **What is the autoregressive language modeling objective?**
   Maximize P(x_t | x_1, ..., x_{t-1}) for each token — predict the next token given all previous tokens.

2. **Kaplan scaling laws: what are the three key variables?**
   Parameters (N), dataset size (D), and compute budget (C). Loss follows power laws in each.

3. **What did Chinchilla change about scaling strategy?**
   Showed models were undertrained on data. Compute-optimal training scales data and parameters equally. Tokens ≈ 20× parameters.

4. **Why is bf16 preferred over fp16 for LLM training?**
   bf16 has the same exponent range as fp32 (8 bits), preventing overflow/underflow. fp16 has only 5 exponent bits, causing training instabilities.

5. **What is ZeRO and what are its 3 stages?**
   Zero Redundancy Optimizer. Stage 1: shard optimizer states. Stage 2: + shard gradients. Stage 3: + shard parameters. Progressively reduces memory per GPU.

6. **Data parallelism vs tensor parallelism vs pipeline parallelism?**
   Data: replicate model, split batches. Tensor: split individual layers across GPUs. Pipeline: split layer stack across GPUs with micro-batch scheduling.

7. **C ≈ 6ND — what does this formula mean?**
   Training compute (FLOPs) ≈ 6 × parameters × tokens. Useful for estimating training cost.

8. **What is the "over-training" strategy and who uses it?**
   Train smaller models on more data than compute-optimal. LLaMA approach — trades training efficiency for cheaper inference.

9. **What's the difference between The Pile, RedPajama, and FineWeb?**
   All are open pretraining datasets. The Pile (2021): diverse 800GB. RedPajama: LLaMA reproduction. FineWeb (2024): curated web-scale from HuggingFace.

10. **Why does data quality matter more than quantity?**
    Carefully filtered/curated data produces better models at the same token count. FineWeb and DCLM showed quality filtering >> raw scale.

11. **What are the main gates in the LLM training pipeline?**
    Data curation, tokenization, pretraining objective, distributed optimization, base evaluation, SFT, preference optimization, adaptation, deployment, and monitoring. See [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]].

12. **What does a tiny decoder-only training lab prove?**
    It proves the causal LM objective end to end: shifted next-token targets, masked self-attention, logits, cross-entropy loss, gradients, train/validation loss, and autoregressive generation. See [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]].
