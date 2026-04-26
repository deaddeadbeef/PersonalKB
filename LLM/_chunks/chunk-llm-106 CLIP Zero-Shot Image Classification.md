---
tags: [chunk, llm]
id: "chunk-llm-106"
source: "[[LLM/_raw/raw-llm-027 CLIP Visual Models Language Supervision]]"
source_loc: "Key Takeaways 2, 4"
topic: "CLIP zero-shot image classification"
claim: "CLIP enables zero-shot image classification by computing cosine similarity between image embeddings and text embeddings of class descriptions."
confidence: "verified"
supports: ["[[LLM/Multimodal/Vision-Language Models]]"]
up: "[[LLM/LLM]]"
---

# CLIP Enables Zero-Shot Image Classification

## Context
CLIP's aligned image-text embedding space enables a novel approach to image classification that requires no task-specific training. To classify an image, you encode the image with CLIP's image encoder and encode text descriptions of each candidate class (e.g., "a photo of a dog", "a photo of a cat") with CLIP's text encoder. The predicted class is whichever text description has the highest cosine similarity with the image embedding.

This zero-shot approach was competitive with fully supervised ResNets trained on ImageNet — a remarkable result given that CLIP never saw ImageNet labels during training. Moreover, CLIP showed significantly better robustness to distribution shift than supervised models: when tested on variants of ImageNet with different image styles or adversarial perturbations, CLIP's accuracy degraded much less than supervised baselines.

## Why It Matters
Zero-shot classification via natural language eliminates the need for labeled training data for new visual recognition tasks. Instead of collecting and annotating thousands of examples for each new category, practitioners can simply describe the categories in text. This dramatically accelerates deployment of visual AI to new domains and enables classification of categories that were never explicitly anticipated during model development.

## QnA Seeds
- Q: How does CLIP perform zero-shot image classification?
  A: By computing cosine similarity between the image embedding and text embeddings of natural language class descriptions (e.g., "a photo of a dog"), selecting the class with highest similarity.
- Q: How did CLIP's zero-shot performance compare to supervised models?
  A: Competitive with fully supervised ResNets on ImageNet, and significantly more robust to distribution shift (different image styles, adversarial perturbations).
