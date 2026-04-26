---
tags: [chunk, llm]
id: "chunk-llm-189"
source: "[[LLM/_raw/raw-llm-048 Towards Monosemanticity Sparse Autoencoders]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Sparse autoencoder methodology"
claim: "Sparse autoencoders can decompose Transformer MLP activations into interpretable, monosemantic features — individual directions in activation space that each correspond to a single human-understandable concept."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What are monosemantic features? A: Individual directions in neural network activation space that activate for a single, interpretable concept (e.g., DNA sequences, Python code, the concept of deception) rather than a mixture of unrelated concepts."
  - "Q: How does a sparse autoencoder extract monosemantic features? A: It trains an autoencoder with a sparsity penalty on the hidden layer, forcing it to reconstruct MLP activations using a small number of active features at any time, each corresponding to a distinct concept."
up: "[[LLM/LLM]]"
---

# Sparse Autoencoders Decompose Activations Into Monosemantic Features

Bricken et al. applied sparse autoencoders (SAEs) with learned dictionaries to decompose MLP layer activations in a one-layer Transformer into interpretable features. The autoencoder is trained to reconstruct activations using a hidden layer with a sparsity penalty, forcing only a few features to be active at any given time. The resulting features are monosemantic — each activates for a single, human-interpretable concept rather than a mixture of unrelated patterns. This dictionary learning approach overcomes the polysemanticity problem where individual neurons respond to multiple unrelated stimuli, enabling feature-level analysis of model behavior.
