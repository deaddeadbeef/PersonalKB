---
tags: [chunk, llm]
id: "chunk-llm-086"
source: "[[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs]]"
source_loc: "Key Takeaways 2"
topic: "Double quantization technique"
claim: "Double quantization in QLoRA quantizes the quantization constants themselves, saving additional memory."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# Double Quantization Compresses Quantization Constants

## Context
When quantizing model weights to 4-bit, each block of weights requires quantization constants (scale factors and zero points) stored in higher precision (typically 32-bit float). For very large models, these constants consume non-trivial memory — roughly 0.5 GB for a 65B model. Double quantization applies a second round of quantization to these constants themselves, compressing them from 32-bit to 8-bit.

This nested quantization reduces the per-parameter memory overhead of the quantization constants from 32 bits to approximately 8 bits, saving an additional ~0.37 bits per parameter. While this sounds small, at 65 billion parameters it translates to meaningful memory savings that can make the difference between fitting a model on a given GPU or not.

## Why It Matters
Double quantization exemplifies the principle that every source of memory overhead matters at scale. By systematically eliminating even secondary memory costs, QLoRA pushes the boundaries of what fits on a single GPU, making the difference between feasible and infeasible fine-tuning for researchers with limited hardware.

## QnA Seeds
- Q: What is double quantization in QLoRA?
  A: It quantizes the quantization constants (scale factors and zero points) themselves from 32-bit to 8-bit, reducing the memory overhead of storing these constants.
- Q: How much memory does double quantization save?
  A: Approximately 0.37 bits per parameter, which translates to meaningful savings (~0.5 GB reduction) for 65B-scale models.
