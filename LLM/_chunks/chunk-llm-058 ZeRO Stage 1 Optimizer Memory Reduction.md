---
tags: [chunk, llm]
id: "chunk-llm-058"
source: "[[LLM/_raw/raw-llm-015 ZeRO Memory Optimizations]]"
source_loc: "Key Takeaways 1, 4"
topic: "ZeRO Stage 1 efficiency"
claim: "ZeRO Stage 1 alone reduces optimizer memory by N× (where N = number of GPUs) with minimal communication overhead."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# ZeRO Stage 1 Optimizer Memory Reduction

## Context
ZeRO Stage 1 is the simplest and most widely used stage because it provides substantial memory savings with virtually no performance overhead. In Adam optimization, the optimizer states (fp32 master weights, first moment, second moment) consume 12 bytes per parameter — often more than the model weights and gradients combined. Stage 1 partitions these optimizer states across N GPUs, so each GPU stores only 12Ψ/N bytes of optimizer state instead of 12Ψ.

The communication pattern for Stage 1 is identical to standard data parallelism: an all-reduce of gradients after backward. The only difference is that each GPU updates only its 1/N partition of the optimizer states and then performs an all-gather to broadcast the updated parameters. The all-gather adds modest overhead, but on modern interconnects it is negligible — typically less than 5% wall-clock slowdown for a ~4× memory reduction with 4 GPUs.

## Why It Matters
ZeRO Stage 1 is the "no-brainer" optimization: it reduces the largest memory consumer (optimizer states) with almost zero downside. Most practitioners use Stage 1 by default when training with multiple GPUs, and it's the default setting in many DeepSpeed configurations. The minimal overhead makes it applicable to all scales of training, from research experiments to frontier model pre-training.

## QnA Seeds
- Q: Why is ZeRO Stage 1 considered a "no-brainer" optimization?
  A: It targets optimizer states, which are the largest memory consumer (12 bytes/param for Adam vs. 2 bytes/param for fp16 weights). It provides N× reduction in optimizer memory with minimal communication overhead (~5% wall-clock for 4× memory saving on 4 GPUs), and no accuracy impact.
- Q: What is the communication difference between ZeRO Stage 1 and standard data parallelism?
  A: Both perform an all-reduce of gradients. Stage 1 adds an all-gather after the optimizer step to broadcast the updated parameters, since each GPU only updates its partition. This additional communication is small relative to the gradient all-reduce.
