---
tags: [llm, chunk]
source: "[[raw-llm-037]]"
confidence: high
supports:
  - "[[LLM/2023 — Open Models and Agents/Multimodal Tokenization and Fusion]]"
qna_seeds:
  - "Q: How does Gemini's multimodal approach differ from prior models? A: Gemini is natively multimodal — trained from the ground up on interleaved sequences of text, image, audio, and video — rather than bolting a vision encoder onto a pre-trained language model like LLaVA or GPT-4V."
---

# Gemini Is Natively Multimodal From the Ground Up

Gemini (Google DeepMind, 2023) was designed as a natively multimodal model, trained jointly on interleaved sequences of text, image, audio, and video from the start of pre-training. This contrasts with approaches like LLaVA or GPT-4V that bolt a vision encoder onto an already-trained language model. Native multimodal training allows the model to learn cross-modal representations during pre-training rather than adapting them post-hoc, enabling more natural reasoning across modalities such as understanding diagrams within text or answering questions about video content.