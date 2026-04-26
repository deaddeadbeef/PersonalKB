---
tags: [raw, llm]
id: "raw-llm-028"
title: "Robust Speech Recognition via Large-Scale Weak Supervision"
author: "Radford et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2212.04356"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Robust Speech Recognition via Large-Scale Weak Supervision

## What Is This?
Whisper is a speech recognition model trained on 680,000 hours of weakly supervised multilingual audio-text data from the internet, performing transcription, translation, and language identification in a single model.

## Why It Matters
Whisper demonstrated that scaling weakly labeled data can produce speech models that rival or exceed supervised systems in robustness, and its open release made production-quality ASR accessible to everyone.

## Key Takeaways
1. Trained on 680K hours of diverse, weakly labeled audio — orders of magnitude more than prior supervised datasets
2. Encoder-decoder transformer with multitask formatting: transcription, translation, timestamps, and language ID via special tokens
3. Zero-shot robustness across accents, noise, and domains without fine-tuning
4. Large-v2 model approaches human-level accuracy on standard benchmarks like LibriSpeech

## Chunk Candidates
- [ ] Weakly supervised training at scale (680K hours) and data pipeline
- [ ] Multitask token format: transcription, translation, timestamps, language ID
- [ ] Robustness results across diverse acoustic conditions
- [ ] Architecture details and comparison with supervised ASR systems
