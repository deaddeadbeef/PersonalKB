---
tags: [chunk, llm]
id: "chunk-llm-190"
source: "[[LLM/_raw/raw-llm-048 Towards Monosemanticity Sparse Autoencoders]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "Superposition in neural networks"
claim: "Neural networks use superposition to encode more concepts than they have neurons, overlapping multiple features in the same dimensions; sparse autoencoders provide evidence this superposition can be disentangled."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What is the superposition hypothesis? A: The idea that neural networks encode more features than they have dimensions by representing multiple concepts as overlapping, approximately orthogonal directions in activation space."
  - "Q: Can superposition be reversed? A: Yes — Bricken et al. showed that sparse autoencoders can disentangle superposed features into individual interpretable directions, with the dictionary size exceeding the original activation dimensionality."
up: "[[LLM/LLM]]"
---

# Superposition Hypothesis and Feature Disentanglement

The superposition hypothesis proposes that neural networks represent far more features than they have neurons by encoding multiple concepts as nearly orthogonal directions in the same activation space. This makes individual neurons polysemantic — they fire for multiple unrelated inputs. Bricken et al. provided the most compelling evidence that this superposition can be reversed at scale. Their sparse autoencoders learned dictionaries with far more features than the original MLP dimensionality, successfully disentangling overlapping representations into individually interpretable features. This validated the theoretical prediction that superposition is a recoverable compression strategy, not an irreversible loss of structure.
