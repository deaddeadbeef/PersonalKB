---
tags: [llm, foundations]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Embeddings and Representation Geometry

> **One-line summary** Dense token vectors and their high-dimensional geometry reveal how language models encode meaning, similarity, and knowledge.

## 🎯 Intuition
**The Core Idea:** Tokens begin as learned dense vectors and are transformed layer by layer into contextual representations whose geometry organizes concepts in high-dimensional space.

**Analogy:** Embeddings are like GPS coordinates for words in a semantic landscape: nearby points mean similar meanings, important directions encode concepts like sentiment or truthfulness, and transformer layers keep updating the route based on the surrounding terrain.

**Why It Matters:** Understanding representation geometry — how concepts are organized in high-dimensional space — is key to both interpretability and practical applications because it reveals how language models encode and process knowledge. Embedding models (E5, BGE, OpenAI embeddings) power all of RAG by encoding semantic similarity as vector distance. Representation engineering offers a way to control model behavior without fine-tuning, and superposition research is central to the mechanistic interpretability agenda because decomposing representations into interpretable features can help us better understand and control what models are doing.

---

## ⚙️ Core Mechanics
### How It Works
- A token embedding is simply a row in a learned lookup table: each token ID maps to a dense vector of dimension `d_model` (typically 768-8192).
- These initial embeddings are combined with positional encodings and then transformed through successive transformer layers into contextual representations — vectors whose meaning depends on the surrounding tokens.
- **Token embedding**: learned matrix of shape `(vocab_size, d_model)`, one row per token.
- **Contextual representation**: output of a transformer layer; the same token produces different vectors in different contexts.
- **Layer progression**: early layers capture syntactic features, later layers encode semantic/task-relevant information.
- **Probing**: train a simple classifier on internal representations to test what information is encoded.
- **Linear probes**: test whether a concept is linearly decodable from a representation.
- **Superposition**: more features than dimensions; features are sparse and nearly orthogonal.
- **Sparse autoencoders**: decompose superposed representations into interpretable, monosemantic features.
- **Representation engineering**: steer model behavior by adding/subtracting directions in activation space.

### Key Specifications
- Typical embedding dimensionality: `d_model = 768-8192`.
- Token embeddings are stored as a matrix of shape `(vocab_size, d_model)`.
- Contextual representations are produced after positional information and transformer-layer processing are applied.

### Key Facts
- Embeddings are the dense vector representations that transformers operate on.
- The same token can map to different contextual representations depending on surrounding tokens.
- Many concepts appear to be encoded as approximately linear directions in activation space.
- Models can represent more features than dimensions through superposition.
- Sparse autoencoders are a major tool for extracting interpretable features from superposed representations.

---

## 🔬 Deep Dive
### Technical Details
The linear representation hypothesis suggests that many concepts are represented as directions in activation space. `"King - man + woman ≈ queen"` (from Word2Vec) is the classic example: gender and royalty are encoded as roughly linear directions. Modern interpretability work finds similar structure in transformer representations, including truth directions, sentiment directions, and factual recall directions.

Superposition is the phenomenon where models encode more features than they have dimensions, using sparse, nearly-orthogonal directions. A 4096-dimensional layer might represent tens of thousands of interpretable features because most features are active for only a small fraction of inputs. This is both a feature, because it uses capacity efficiently, and a challenge, because features interfere with each other.

### Limitations and Criticisms
- Superposition makes features interfere with each other, which complicates clean interpretation.
- Linear directions can be useful approximations without fully capturing every nonlinear aspect of a representation.
- Probing can show that information is decodable from a representation, but that does not always prove the model actively uses that information in the way the probe suggests.

### Impact and Legacy
Embedding geometry underlies retrieval systems because semantic similarity can be operationalized as vector distance. Representation engineering builds on the idea that directions in activation space can be manipulated to steer behavior without full fine-tuning. Superposition and sparse autoencoder research have become central to mechanistic interpretability because they offer a path toward decomposing model internals into more interpretable features.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can the same token have different contextual representations in different sentences?
2. What does it mean for a concept to be encoded as a direction in activation space?
3. Why is superposition both useful and problematic for interpretability?

### Core Problems
1. Explain how a learned embedding matrix of shape `(vocab_size, d_model)` is used before and after positional encodings are added in a transformer pipeline.
2. Suppose a 4096-dimensional layer appears to represent many more than 4096 interpretable features. Use superposition and sparsity to explain how that can happen, and describe how a sparse autoencoder could help analyze it.

### Challenge
1. Design an experiment using linear probes or representation engineering to test whether a model contains a robust “truthfulness” direction rather than a probe artifact.

*See also:*
- Retrieval-Augmented Generation
- [[Mechanistic Interpretability]]
- Sparse Autoencoders
- Representation Engineering

## Supporting Chunks
### Supporting Chunks
- No supporting chunk notes are attached yet.

## References
- [[LLM/Sources/Sources Index]]
