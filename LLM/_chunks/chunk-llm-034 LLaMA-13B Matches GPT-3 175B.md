---
tags: [chunk, llm]
id: "chunk-llm-034"
source: "[[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models]]"
source_loc: "Section 3, Table 3"
topic: "compute-optimal training"
claim: "LLaMA-13B matched GPT-3 (175B) on most benchmarks by applying Chinchilla-optimal training to a smaller model"
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# LLaMA-13B Matches GPT-3 175B

## Context

LLaMA-13B, with approximately 13× fewer parameters than GPT-3 175B, matched or exceeded GPT-3's performance on the majority of standard benchmarks including MMLU, HellaSwag, ARC, WinoGrande, and various reading comprehension tasks. This was achieved by applying Chinchilla-optimal training principles: LLaMA-13B was trained on 1T tokens, giving it a token-to-parameter ratio of ~77:1 — far above the compute-optimal ~20:1 ratio, representing deliberate over-training.

By comparison, GPT-3 175B was trained on only 300B tokens, giving it a token-to-parameter ratio of ~1.7:1 — severely undertrained by Chinchilla standards. The massive parameter advantage of GPT-3 was nullified by insufficient training data. LLaMA-13B's smaller architecture was fully utilized because it saw enough data to develop rich representations, while GPT-3's vast parameter space was largely underutilized.

## Why It Matters

This head-to-head comparison provided the most visceral demonstration of the Chinchilla scaling law's practical implications. A model that could run on a single GPU (LLaMA-13B in fp16 ≈ 26GB VRAM) matching the performance of a model requiring multiple A100s drove home the message that training recipe matters as much as model size. It motivated the industry shift toward smaller, well-trained models for deployment and established LLaMA as the benchmark for efficient open models.

## QnA Seeds
- Q: How can 13B parameters match 175B parameters in performance?
  A: GPT-3 175B was trained on only ~1.7 tokens per parameter, meaning its parameters were severely undertrained — the model had more capacity than the data could fill. LLaMA-13B saw ~77 tokens per parameter, fully utilizing its smaller capacity. A well-trained small model outperforms a poorly trained large model because parameter count only sets the ceiling; the amount of training data determines how close to that ceiling the model gets.
- Q: Does this mean there's no reason to train models larger than 13B?
  A: No. A well-trained larger model will always outperform a well-trained smaller model — LLaMA-65B outperformed LLaMA-13B across the board. The lesson is that you shouldn't increase model size without proportionally increasing training data. The practical question is about deployment: if 13B meets your accuracy requirements and fits on your hardware, the additional quality from 65B may not justify the 5× higher inference cost.
