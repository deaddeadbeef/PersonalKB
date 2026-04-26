---
tags: [chunk, llm]
id: "chunk-llm-163"
source: "[[LLM/_raw/raw-llm-041 Layer Normalization]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "Pre-LN vs Post-LN Transformer placement"
claim: "Placing LayerNorm before the attention/FFN sub-layer (Pre-LN) produces more stable gradients and removes the need for learning rate warmup, compared to the original Post-LN placement."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
  - "[[LLM/2017 — The Transformer/2017 — The Transformer]]"
qna_seeds:
  - "Q: What is the difference between Pre-LN and Post-LN Transformers? A: Pre-LN applies LayerNorm before each sub-layer (attention, FFN), while Post-LN applies it after the residual addition. Pre-LN produces more stable gradients at initialization."
  - "Q: Why do most modern LLMs use Pre-LN? A: Pre-LN avoids gradient explosion at early training, removes the need for careful warmup schedules, and enables stable training of very deep models."
up: "[[LLM/LLM]]"
---

# Pre-LN vs Post-LN Placement Affects Training Stability

The original Transformer placed LayerNorm after the residual connection (Post-LN), which can cause gradient instability in deep networks and requires careful learning rate warmup. Later work showed that moving LayerNorm before the attention and feed-forward sub-layers (Pre-LN) produces well-behaved gradients at initialization and enables stable training without warmup. Most modern LLMs (GPT-2 onward, LLaMA, etc.) use Pre-LN or its variant RMSNorm. The choice between Pre-LN and Post-LN has measurable effects on final model quality, with some evidence that Post-LN achieves marginally better converged performance when training is stabilized by other means.
