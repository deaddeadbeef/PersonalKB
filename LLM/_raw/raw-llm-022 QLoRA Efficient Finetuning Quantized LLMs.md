---
tags: [raw, llm]
id: "raw-llm-022"
title: "QLoRA: Efficient Finetuning of Quantized LLMs"
author: "Dettmers et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2305.14314"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# QLoRA: Efficient Finetuning of Quantized LLMs

## What Is This?
Combines 4-bit NormalFloat quantization of frozen base weights with LoRA adapters, enabling fine-tuning of a 65B parameter model on a single 48GB GPU with no quality loss.

## Why It Matters
QLoRA democratized LLM fine-tuning by making it possible on consumer hardware. A single GPU can fine-tune models that previously required multi-node setups, dramatically lowering the barrier to entry.

## Key Takeaways
1. 4-bit NormalFloat (NF4): information-theoretically optimal quantization type for normally distributed weights
2. Double quantization: quantize the quantization constants themselves to save additional memory
3. Paged optimizers: use unified memory to handle gradient checkpointing spikes without OOM
4. Matches 16-bit full fine-tuning quality while reducing memory by ~4× on 65B models

## Chunk Candidates
- [ ] NormalFloat 4-bit quantization and its optimality argument
- [ ] Double quantization technique for quantization constant compression
- [ ] Paged optimizers and unified memory management
- [ ] Guanaco results: QLoRA fine-tuned model vs ChatGPT on Vicuna benchmark
