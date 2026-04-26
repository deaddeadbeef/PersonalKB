---
tags: [chunk, llm]
id: "chunk-llm-027"
source: "[[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation]]"
source_loc: "Section 5"
topic: "parameter-efficient fine-tuning"
claim: "LoRA trains <1% of parameters while achieving comparable quality to full fine-tuning on most tasks"
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Parameter-Efficient Fine-Tuning]]"]
up: "[[LLM/LLM]]"
---

# LoRA Achieves Full Fine-Tuning Quality with Under 1% Parameters

## Context

Across experiments on GPT-3 175B and various smaller models, LoRA achieved performance comparable to full fine-tuning on benchmark tasks including GLUE, E2E NLG, WikiSQL, and SAMSum, while training fewer than 1% of the total parameters. For GPT-3 175B, a typical LoRA configuration with r=4 applied to attention layers results in approximately 4.7M trainable parameters out of 175B total — about 0.003% of the model.

The quality comparison is nuanced: LoRA matches full fine-tuning closely on focused tasks (classification, summarization, structured generation) but may slightly underperform on tasks requiring broad capability changes. The gap is typically within 1-2% on standard benchmarks. Importantly, LoRA consistently outperforms other parameter-efficient methods like prefix tuning and adapter layers, achieving the best trade-off between parameter count and task performance.

## Why It Matters

The practical implications are transformative. Full fine-tuning of a 70B model requires 140+ GB of optimizer state memory (with Adam) plus gradient memory, necessitating multiple high-end GPUs. LoRA reduces this to a few hundred MB of adapter parameters, enabling fine-tuning on a single consumer GPU. This reduction in hardware requirements democratized model adaptation and enabled the explosion of specialized fine-tuned models on platforms like Hugging Face.

## QnA Seeds
- Q: In what scenarios might LoRA significantly underperform full fine-tuning?
  A: LoRA may struggle when the task requires large, high-rank changes to the model's behavior — for example, adapting an English-only model to a completely new language, or fundamentally changing the model's output format. These scenarios require changes that can't be well-approximated by a low-rank update. For domain-specific knowledge injection or moderate task adaptation, LoRA performs well.
- Q: How does LoRA compare to other PEFT methods like prefix tuning and adapters?
  A: LoRA consistently outperforms prefix tuning (which prepends learnable tokens to the input) and serial adapter layers (which add bottleneck networks) at the same parameter budget. Its advantages are: (1) no inference overhead after merging, (2) no reduction in usable context length, (3) better optimization properties (direct weight-space updates vs. indirect input manipulation). The main alternatives that compete with LoRA are its own variants (DoRA, LoRA+, PiSSA).
