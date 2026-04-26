---
tags: [llm, alignment]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Mechanistic Interpretability

> **One-line summary** Mechanistic interpretability tries to reverse-engineer neural networks by identifying the features, circuits, and internal representations that produce model behavior.

## 🎯 Intuition

**The Core Idea:**  
Mechanistic interpretability aims to reverse-engineer the internal computations of neural networks — understanding not just what a model does, but how it does it at the level of individual features, circuits, and representations. The field studies features (meaningful directions in activation space), circuits (computational subgraphs that implement specific behaviors), and superposition (the phenomenon where models represent more features than they have dimensions). Key tools include sparse autoencoders, probing classifiers, and careful analysis of attention patterns.

The central challenge is that neural networks represent information in a way that is not human-readable. Activation vectors in a transformer are high-dimensional, and individual neurons rarely correspond to clean semantic concepts. Instead, models use **superposition**: they represent more features than they have dimensions by encoding features as nearly orthogonal directions in activation space. A model with $d$ dimensions can represent $\gg d$ features, as long as most features are sparse (rarely active). This means a single neuron participates in representing many different features — a phenomenon called **polysemanticity** — making it impossible to interpret the network one neuron at a time.

**Analogy:**  
Imagine trying to understand a factory by listening to the building vibrate instead of watching the machines directly. Mechanistic interpretability tries to separate that blended vibration into distinct machine parts and production lines.

**Why It Matters:**  
Mechanistic interpretability is the most ambitious approach to AI safety: rather than testing model behavior from the outside (red-teaming) or shaping it with training signal (RLHF, DPO), it aims to understand the internal mechanisms that produce behavior. If successful, it could enable verification of alignment — checking that a model doesn't contain deceptive circuits — rather than relying on behavioral testing alone.

The practical stakes are high. If we cannot understand what models compute internally, we are deploying increasingly powerful systems as black boxes. Mechanistic interpretability offers the possibility of auditing model internals before deployment, detecting features related to deception or harmful capabilities, and ultimately designing models that are interpretable by construction. The field is still early — current techniques work on toy models and small-to-medium transformers — but progress has been rapid, and the sparse autoencoder paradigm has opened new avenues for scaling.

---

## ⚙️ Core Mechanics

### How It Works

- **Features as directions**: A feature is a direction in activation space, not a single neuron. The activation of a feature is the dot product of the activation vector with the feature direction. Features can be linear (directions) or nonlinear (more complex manifolds), though the linear hypothesis is the working assumption.
- **Superposition**: Models represent $N \gg d$ features in $d$-dimensional space using nearly orthogonal directions. Sparsity enables this: if features rarely co-activate, interference is manageable. The degree of superposition increases with model capacity pressure.
- **Polysemanticity**: A single neuron responds to multiple unrelated features because multiple feature directions pass through it. This makes neuron-level interpretation unreliable.
- **Sparse autoencoders (SAEs)**: Encoder maps activations to a high-dimensional sparse latent space; decoder reconstructs. Training objective: reconstruction loss + L1 sparsity penalty on latents. Typical expansion factor: 4×–64× (latent dimension vs activation dimension). Each latent ideally corresponds to one interpretable feature.
- **Induction heads (Olsson et al., 2022)**: A circuit consisting of a "previous token head" (which attends to the token before a previous occurrence of the current token) and an "induction head" (which copies what followed the previous occurrence). Implements the pattern [A][B]...[A] → [B]. Responsible for a significant fraction of in-context learning. Emerges during a phase transition in training loss.
- **Probing classifiers**: Train a simple linear classifier on a model's internal activations to predict a property (e.g., part of speech, sentiment, factual correctness). If the probe succeeds, the information is linearly represented in the activations. Probes are cheap but can be misleading — a successful probe doesn't prove the model uses that information.
- **Activation patching / causal tracing**: Replace activations at specific positions and layers with activations from a different input to determine which components are causally responsible for a behavior. Used to localize factual recall (Meng et al., 2022) and other specific computations.
- **Challenges at scale**: Current interpretability techniques work best on small-to-medium models. Scaling to frontier models (100B+ parameters) requires automated interpretability — using models to interpret models. Polysemanticity and superposition make this harder, not easier, at scale.

### Key Specifications

**Sparse autoencoders** (SAEs), as developed by Bricken et al. (2023) and Cunningham et al. (2023), are the primary tool for decomposing superposed representations. An SAE is trained to reconstruct a model's activations through a bottleneck with a sparsity penalty, producing a dictionary of learned features that are more interpretable than raw neurons. Each learned feature (a direction in the SAE's latent space) ideally corresponds to a single human-interpretable concept. Anthropic's work on Claude found features corresponding to specific concepts like "Golden Gate Bridge," code syntax patterns, and safety-relevant behaviors. SAEs can be applied to any layer, revealing how representations evolve through the network.

**Circuits** are computational subgraphs that implement specific behaviors. The circuits agenda (Olah et al., 2020; Elhage et al., 2021) traces how information flows from input tokens through attention heads and MLP layers to produce specific outputs. A landmark finding is **induction heads** (Olsson et al., 2022): a two-head circuit where one attention head identifies a previous occurrence of the current token and a second head copies the token that followed it. Induction heads are responsible for much of in-context learning in transformers, and they emerge reliably across model scales during a phase transition in training. Circuit-level analysis has also revealed how models implement indirect object identification, greater-than comparison, and other specific tasks.

### Key Facts

| Concept | Definition | Example |
|---|---|---|
| Feature | Meaningful direction in activation space | "Golden Gate Bridge" direction in residual stream |
| Circuit | Computational subgraph implementing a behavior | Induction head circuit for in-context copying |
| Superposition | More features than dimensions | 1000 features in 256-dimensional space |
| Polysemanticity | Single neuron responds to multiple features | Neuron fires for both "cats" and "cars" |
| Monosemanticity | Single neuron responds to one feature | Rare in raw networks; goal of SAE decomposition |

| Tool | What It Does | Limitation |
|---|---|---|
| Sparse autoencoder | Decomposes superposed representations into features | Training cost; feature completeness unknown |
| Probing classifier | Tests if information is linearly represented | Correlation ≠ causation; probe may learn its own features |
| Activation patching | Identifies causal components | Combinatorial explosion at scale |
| Attention pattern analysis | Visualizes information routing | Attention ≠ contribution; misleading for MLPs |

---

## 🔬 Deep Dive

### Technical Details

One of the biggest conceptual shifts in mechanistic interpretability is moving away from neuron-centric explanations. If superposition is real and widespread, then semantic content lives in directions and subspaces rather than in single units. That is why SAEs are so important: they attempt to recover a more disentangled basis from raw activations.

Circuit analysis then asks how these features are transformed and routed. In transformers, this often means tracing attention heads, MLP updates, and residual-stream composition through a computation. Induction heads are a foundational example because they provide a concrete, mechanistic explanation for a major capability: copying patterns from context. Their emergence as a training phase transition also suggests that specific capabilities can appear suddenly when the network discovers reusable internal algorithms.

Activation patching provides one of the cleanest causal tools in the field. Rather than only observing correlations, it swaps internal states between prompts and asks whether behavior changes. This helps localize which layer-position activations matter for a given output.

### Limitations and Criticisms

- Current methods work best on small-to-medium models and do not yet scale cleanly to frontier systems
- SAE feature completeness is uncertain: interpretable recovered features may still be only part of the full representation
- Successful probes can overstate understanding because information being present does not prove the model actually uses it
- Attention visualizations can be misleading because attention alone does not equal causal contribution
- Polysemanticity and superposition make the whole enterprise harder at larger scales, not easier

### Impact and Legacy

Mechanistic interpretability has reframed alignment from a purely behavioral problem into an internal-understanding problem. It has produced a vocabulary — features, circuits, superposition, polysemanticity, induction heads — that now shapes how researchers discuss transformer internals.

The sparse autoencoder paradigm, in particular, has made the field feel more scalable than earlier neuron-by-neuron analysis. Even if full interpretability remains distant, the field has already changed safety research, capability analysis, and how people think about auditing advanced models before deployment.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. Why is interpreting one neuron at a time usually inadequate?
2. What problem are sparse autoencoders trying to solve?
3. What is an induction head in one sentence?

### Core Problems

1. Explain how superposition leads to polysemantic neurons.
2. Compare probes and activation patching as interpretability tools: what can each show, and what can each fail to show?
3. Why are induction heads considered a landmark result for transformer interpretability?
4. Suppose an SAE discovers a feature that strongly activates on code syntax. What would that mean, and what would it still not prove?

### Challenge

Sketch an interpretability workflow for investigating whether a model uses a deceptive strategy on a narrow task. Specify where you would use probes, SAEs, and activation patching, and explain what evidence would still be missing after each step.

## See Also

- [[LLM/Foundations/Embeddings and Representation Geometry|Representation Geometry]] — the geometric structure interpretability tries to decode
- [[LLM/Prompting and In-Context Learning/In-Context Learning Mechanisms|ICL Mechanisms]] — induction heads as a mechanistic explanation

## Supporting Chunks / References

### Supporting Chunks

*(To be populated as chunks are created)*

### References

- [[LLM/Sources/Sources Index]]
