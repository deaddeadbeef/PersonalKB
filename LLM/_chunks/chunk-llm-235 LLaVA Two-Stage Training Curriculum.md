---
tags: [chunk, llm]
id: "chunk-llm-235"
source: "[[LLM/_raw/raw-llm-059 Visual Instruction Tuning LLaVA]]"
source_loc: "Chunk Candidates"
topic: "LLaVA two-stage training"
claim: "LLaVA uses two-stage training: feature alignment pre-training (frozen LLM, train projection) followed by visual instruction fine-tuning (end-to-end)."
confidence: "verified"
supports: ["[[LLM/2020–2021 — The Scaling Era/Vision-Language Models]]", "[[LLM/2023 — Open Models and Agents/Multimodal Tokenization and Fusion]]"]
qna_seeds:
  - q: "What are LLaVA's two training stages?"
    a: "Stage 1 (feature alignment): The LLM is frozen and only the linear projection is trained on image-caption pairs to align visual features with the language embedding space. Stage 2 (instruction tuning): Both the projection and LLM are fine-tuned end-to-end on the GPT-4-generated visual instruction data."
  - q: "Why is the two-stage approach necessary?"
    a: "Direct end-to-end training from scratch risks catastrophic forgetting of the LLM's language capabilities. Stage 1 creates a stable visual-language bridge before Stage 2 fine-tunes the full model with instruction-following data."
up: "[[LLM/LLM]]"
---
# LLaVA Uses Two-Stage Training for Visual Instruction Following

LLaVA's training follows a two-stage curriculum designed to preserve the LLM's language capabilities while acquiring visual understanding. In Stage 1 (feature alignment pre-training), the LLaMA language model is frozen and only the linear projection layer is trained on 595K image-caption pairs from CC3M. This stage learns to map CLIP visual features into the language model's embedding space without disturbing the LLM's weights.

In Stage 2 (visual instruction fine-tuning), both the projection layer and the LLaMA model are fine-tuned end-to-end on 158K GPT-4-generated visual instruction-following examples. This stage teaches the model to engage in multi-turn visual conversations, provide detailed descriptions, and perform complex visual reasoning. The two-stage design prevents catastrophic forgetting — the LLM retains its language abilities from pre-training while gaining visual instruction-following capabilities.
