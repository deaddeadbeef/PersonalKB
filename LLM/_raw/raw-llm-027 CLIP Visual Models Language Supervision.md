---
tags: [raw, llm]
id: "raw-llm-027"
title: "Learning Transferable Visual Models From Natural Language Supervision"
author: "Radford et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2103.00020"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Learning Transferable Visual Models From Natural Language Supervision

## What Is This?
CLIP trains a vision encoder and a text encoder jointly on 400M image-text pairs using a contrastive objective, enabling zero-shot image classification by matching images to natural language descriptions.

## Why It Matters
CLIP proved that language supervision creates visual representations that transfer broadly without task-specific fine-tuning, and its dual-encoder architecture became the foundation for all modern vision-language models.

## Key Takeaways
1. Contrastive pre-training: align image and text embeddings in a shared space using an InfoNCE loss over (image, text) pairs
2. Zero-shot transfer: classify images by computing similarity between image embeddings and text embeddings of class descriptions
3. Trained on 400M image-text pairs (WebImageText) — far larger and more diverse than ImageNet
4. Competitive with fully supervised ResNets on ImageNet zero-shot, and more robust to distribution shift

## Chunk Candidates
- [ ] Contrastive learning objective and dual-encoder architecture
- [ ] Zero-shot classification via text prompt engineering
- [ ] Scale of training data (400M pairs) and its impact on generalization
- [ ] Downstream applications: DALL·E, Stable Diffusion, and multimodal LLMs
