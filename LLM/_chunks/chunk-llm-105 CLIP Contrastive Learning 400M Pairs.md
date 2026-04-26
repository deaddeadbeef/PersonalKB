---
tags: [chunk, llm]
id: "chunk-llm-105"
source: "[[LLM/_raw/raw-llm-027 CLIP Visual Models Language Supervision]]"
source_loc: "What Is This, Key Takeaways 1, 3"
topic: "CLIP contrastive learning on 400M pairs"
claim: "CLIP learns aligned image-text representations through contrastive learning on 400M image-text pairs from the internet."
confidence: "verified"
supports: ["[[LLM/Multimodal/Vision-Language Models]]"]
up: "[[LLM/LLM]]"
---

# CLIP Learns Aligned Image-Text Representations via Contrastive Learning

## Context
CLIP (Contrastive Language-Image Pre-training) trains two encoders — one for images (a Vision Transformer or ResNet) and one for text (a Transformer) — jointly on 400 million image-text pairs collected from the internet (the WebImageText dataset). The training objective is contrastive: given a batch of image-text pairs, the model learns to maximize the cosine similarity between matching pairs while minimizing similarity between non-matching pairs, using an InfoNCE loss.

This approach learns a shared embedding space where images and text descriptions that refer to the same concept are close together. The 400M pair dataset is far larger and more diverse than curated datasets like ImageNet, giving CLIP exposure to an enormous range of visual concepts described in natural language rather than a fixed set of predefined categories.

## Why It Matters
CLIP demonstrated that natural language supervision at internet scale can produce visual representations that are both highly capable and remarkably flexible. By learning from free-form text descriptions rather than fixed category labels, CLIP's representations transfer to tasks and domains never seen during training — fundamentally changing how the field approaches visual representation learning.

## QnA Seeds
- Q: What training objective does CLIP use to align images and text?
  A: Contrastive learning with InfoNCE loss — maximizing cosine similarity between matching image-text pairs while minimizing similarity between non-matching pairs in each batch.
- Q: How large was CLIP's training dataset and why does scale matter?
  A: 400 million image-text pairs from the internet (WebImageText), far larger than curated datasets like ImageNet, providing exposure to an enormous diversity of visual concepts described in natural language.
