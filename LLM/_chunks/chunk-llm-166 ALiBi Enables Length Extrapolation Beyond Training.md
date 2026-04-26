---
tags: [chunk, llm]
id: "chunk-llm-166"
source: "[[LLM/_raw/raw-llm-042 ALiBi Train Short Test Long]]"
source_loc: "What Is This, Why It Matters"
topic: "ALiBi length extrapolation"
claim: "ALiBi enables models trained on short sequences (e.g., 1024 tokens) to generalize to much longer sequences at inference (e.g., 2048+) without performance degradation."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: What is length extrapolation in the context of position encoding? A: The ability of a model to handle sequence lengths at inference that are longer than those seen during training, without retraining or fine-tuning."
  - "Q: How well does ALiBi extrapolate? A: Models trained on 1024 tokens with ALiBi maintained perplexity when tested on 2048+ tokens, while sinusoidal and learned position embeddings degraded sharply beyond training length."
up: "[[LLM/LLM]]"
---

# ALiBi Enables Length Extrapolation Beyond Training

A key limitation of absolute position embeddings (sinusoidal or learned) is that models perform poorly on sequences longer than those seen during training. ALiBi solves this because its linear bias is defined for any distance — there is no maximum position index. Press et al. demonstrated that models trained with ALiBi on 1024-token sequences maintained perplexity when evaluated on sequences of 2048 tokens and beyond. This "train short, test long" capability significantly reduces training costs, since training on shorter sequences is far cheaper while inference can handle longer contexts.
