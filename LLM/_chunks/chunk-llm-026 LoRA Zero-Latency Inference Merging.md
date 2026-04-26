---
tags: [chunk, llm]
id: "chunk-llm-026"
source: "[[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation]]"
source_loc: "Section 4.2"
topic: "LoRA inference"
claim: "At inference, LoRA adapters merge into the base weights (W_0 + BA) with zero additional latency"
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# LoRA Zero-Latency Inference Merging

## Context

A critical advantage of LoRA over other parameter-efficient methods (like adapters that add serial layers, or prefix tuning that consumes context tokens) is that the trained matrices B and A can be multiplied together and added directly to the frozen weights: W_deployed = W_0 + BA. Once merged, the model architecture is identical to the original — same shape, same forward pass, same inference speed. There are no additional layers, no extra computations, and no consumed context tokens.

This merging is possible because the LoRA modification is a simple additive update to the weight matrix. During training, you keep W_0, B, and A separate (so gradients only flow through B and A). At deployment, you compute the product BA once, add it to W_0, and discard B and A. The deployed model is structurally indistinguishable from a fully fine-tuned model, making it compatible with all existing inference optimizations (quantization, KV caching, batching).

## Why It Matters

Zero-latency inference is what makes LoRA practical for production deployment. Alternative PEFT methods like serial adapters add ~1-10% latency per forward pass, which compounds across layers. Prefix tuning consumes context window tokens, reducing usable context. LoRA avoids both penalties. This property also enables efficient serving: a single base model in memory can serve different tasks by swapping the small BA matrices on a per-request basis without reloading the full model.

## QnA Seeds
- Q: Can you un-merge LoRA weights to train a different adapter?
  A: Yes. Since merging is just W_deployed = W_0 + BA, you can reverse it: W_0 = W_deployed - BA. In practice, you'd keep the original W_0 and separate BA matrices rather than merging and un-merging. This makes it trivial to maintain multiple adapters for the same base model — each is just a small file of BA matrices that can be swapped in.
- Q: How does LoRA merging compare to adapter layers in terms of inference overhead?
  A: LoRA adds exactly zero inference overhead after merging — the model is architecturally identical to the original. Serial adapter layers (Houlsby et al., 2019) add small bottleneck networks after each Transformer sub-layer, increasing inference time by the cost of these additional forward passes. For latency-sensitive applications, LoRA's merge-and-forget approach is strongly preferred.
