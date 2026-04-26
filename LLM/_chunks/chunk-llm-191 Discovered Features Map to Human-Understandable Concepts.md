---
tags: [chunk, llm]
id: "chunk-llm-191"
source: "[[LLM/_raw/raw-llm-048 Towards Monosemanticity Sparse Autoencoders]]"
source_loc: "Chunk Candidates"
topic: "Qualitative feature analysis"
claim: "Sparse autoencoder features correspond to specific human-understandable concepts like DNA sequences, legal language, mathematical notation, and base64 strings."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What kinds of features did the sparse autoencoders discover? A: Highly specific concepts including DNA sequences, Python code patterns, legal terminology, mathematical notation, base64 encoded strings, and specific syntactic constructions."
  - "Q: How specific are the discovered features? A: Very specific — not just broad categories like science but narrow concepts like DNA base pair sequences or Python list comprehensions, demonstrating fine-grained concept representation in the model."
up: "[[LLM/LLM]]"
---

# Discovered Features Map to Human-Understandable Concepts

Qualitative analysis of the discovered sparse autoencoder features revealed remarkably specific correspondence to human-understandable concepts. Individual features activated selectively for narrow categories: DNA base pair sequences, Python code constructs, legal contract language, LaTeX mathematical notation, base64-encoded strings, and specific grammatical patterns. The specificity of these features was striking — they were not broad topic categories but fine-grained conceptual units. This demonstrates that Transformer MLPs develop rich, structured internal representations that can be meaningfully decomposed and understood at the individual feature level.
