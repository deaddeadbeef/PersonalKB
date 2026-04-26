---
tags: [chunk, llm]
id: "chunk-llm-085"
source: "[[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs]]"
source_loc: "What Is This, Key Takeaways 1"
topic: "QLoRA 4-bit NormalFloat with LoRA adapters"
claim: "QLoRA combines 4-bit NormalFloat quantization of the base model with LoRA adapters, enabling fine-tuning of 65B models on a single 48GB GPU."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# QLoRA Combines 4-bit Quantization with LoRA Adapters

## Context
QLoRA introduced a method to fine-tune very large language models on a single consumer-grade GPU by combining two techniques. First, the base model weights are quantized to 4-bit NormalFloat (NF4), an information-theoretically optimal data type for normally distributed neural network weights. The frozen quantized base model occupies roughly 4× less memory than 16-bit weights. Second, small LoRA (Low-Rank Adaptation) adapter matrices are added at each layer and trained in 16-bit precision.

During forward passes, NF4 weights are dequantized to 16-bit for computation, combined with the LoRA adapter outputs, and gradients flow only through the small adapter parameters. This approach enabled fine-tuning a 65B parameter model on a single 48GB GPU (e.g., A6000 or A100-48GB) — a task that previously required multiple high-end GPUs or entire compute nodes.

## Why It Matters
QLoRA democratized LLM fine-tuning by reducing hardware requirements by an order of magnitude. Researchers and small companies could now customize 65B-class models on hardware they already had, breaking the monopoly of large compute clusters on model adaptation and enabling a wave of open-source fine-tuned models like Guanaco.

## QnA Seeds
- Q: What two techniques does QLoRA combine to reduce memory for fine-tuning?
  A: 4-bit NormalFloat (NF4) quantization of the frozen base model weights, combined with trainable LoRA adapters in 16-bit precision.
- Q: What hardware does QLoRA enable for fine-tuning a 65B parameter model?
  A: A single 48GB GPU (such as an A6000 or A100-48GB), compared to the multi-GPU setups previously required.
