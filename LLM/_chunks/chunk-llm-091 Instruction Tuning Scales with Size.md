---
tags: [chunk, llm]
id: "chunk-llm-091"
source: "[[LLM/_raw/raw-llm-023 FLAN Instruction Tuning Zero-Shot]]"
source_loc: "Key Takeaways 4"
topic: "Instruction tuning scales with model size"
claim: "FLAN-PaLM scaling study showed instruction tuning benefits scale with model size — larger models benefit more."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Instruction Tuning]]"]
up: "[[LLM/LLM]]"
---

# Instruction Tuning Benefits Scale with Model Size

## Context
The original FLAN paper and the subsequent FLAN-PaLM study both examined the interaction between model scale and instruction tuning. The key finding was that instruction tuning provides increasing benefits at larger model sizes. For the largest models (137B+ parameters), instruction tuning produced dramatic improvements in zero-shot performance. For smaller models (under ~10B parameters), instruction tuning provided modest gains or, in some cases, could even degrade performance on certain tasks.

This scaling behavior suggests that larger models have more latent capability that instruction tuning can unlock. Smaller models may lack the underlying capacity to generalize from instruction-tuning examples, and the tuning process may interfere with their existing few-shot abilities on some tasks.

## Why It Matters
This finding has practical implications for resource allocation: instruction tuning is most cost-effective when applied to the largest models an organization can train. It also helps explain why the instruction-tuning paradigm became dominant only after models reached sufficient scale — the technique was always available, but it needed large enough models to produce its breakthrough results.

## QnA Seeds
- Q: How do instruction tuning benefits vary with model size?
  A: Larger models benefit more from instruction tuning, with 137B+ models showing dramatic zero-shot improvements, while models under ~10B show modest gains or even degradation on some tasks.
- Q: Why might small models degrade with instruction tuning?
  A: Smaller models may lack the underlying capacity to generalize from instruction examples, and the tuning process can interfere with their existing few-shot abilities.
