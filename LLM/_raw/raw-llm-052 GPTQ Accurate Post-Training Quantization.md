---
tags: [raw, llm]
id: "raw-llm-052"
title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
author: "Frantar et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2210.17323"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# GPTQ: Accurate Post-Training Quantization

## What Is This?
A one-shot weight quantization method based on approximate second-order information (Hessian inverse) that compresses LLMs to 3-4 bits per weight with minimal accuracy loss, enabling 175 B parameter models to run on a single GPU.

## Why It Matters
Made large LLMs practical for consumer hardware deployment. GPTQ's speed (quantizes a 175 B model in ~4 GPU-hours) and accuracy (negligible perplexity increase at 4-bit) made it the standard post-training quantization method for open-source LLM deployment.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Optimal Brain Quantization (OBQ) framework and Hessian-based weight rounding
- [ ] Layer-wise quantization with lazy batch updates for speed
- [ ] 3-bit and 4-bit quantization accuracy vs. FP16 baselines on OPT and BLOOM
