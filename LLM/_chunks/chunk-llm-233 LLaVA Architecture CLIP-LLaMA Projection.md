---
tags: [chunk, llm]
id: "chunk-llm-233"
source: "[[LLM/_raw/raw-llm-059 Visual Instruction Tuning LLaVA]]"
source_loc: "What Is This, Chunk Candidates"
topic: "LLaVA architecture"
claim: "LLaVA connects a CLIP ViT-L vision encoder to a LLaMA language model via a simple linear projection layer, creating a multimodal model with minimal additional parameters."
confidence: "verified"
supports: ["[[LLM/2020–2021 — The Scaling Era/Vision-Language Models]]", "[[LLM/2023 — Open Models and Agents/Multimodal Tokenization and Fusion]]"]
qna_seeds:
  - q: "What is LLaVA's architecture?"
    a: "A frozen CLIP ViT-L/14 vision encoder extracts image features, a trainable linear projection maps them to the LLM's embedding dimension, and a LLaMA decoder processes the projected visual tokens interleaved with text tokens."
  - q: "How many additional parameters does LLaVA add beyond the base models?"
    a: "Only the linear projection layer — a single matrix mapping CLIP's 1024-dimensional features to LLaMA's embedding dimension — adding minimal parameters while connecting two pre-trained billion-parameter models."
up: "[[LLM/LLM]]"
---
# LLaVA Connects CLIP and LLaMA via Simple Linear Projection

LLaVA's architecture is remarkably simple: a frozen CLIP ViT-L/14 vision encoder processes an input image into a grid of feature vectors, a single trainable linear projection layer maps these visual features into the language model's embedding space, and a LLaMA decoder processes the projected visual tokens alongside text tokens using standard causal attention.

The key insight is that a simple linear projection is sufficient to bridge the representation spaces of a strong vision encoder and a strong language model. The projection layer adds only a few million parameters to billion-parameter base models, yet enables rich visual understanding when combined with appropriate training data. This minimalist design choice made LLaVA easy to replicate, modify, and scale, directly contributing to its outsized impact on the visual LLM research community.
