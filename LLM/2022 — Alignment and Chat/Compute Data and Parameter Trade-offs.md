---
tags: [llm, pretraining]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Compute Data and Parameter Trade-offs

> **One-line summary** Pretraining is an allocation problem: with fixed compute, you must decide how much to spend on model size versus training tokens.

## 🎯 Intuition
**The Core Idea:** Compute, data, and parameter trade-offs represent the fundamental allocation question in pretraining: given a fixed budget, how do you distribute resources between model size and training tokens to maximize performance?

The relationship C ≈ 6ND provides a rough approximation: compute (in FLOPs) scales linearly with parameters N and dataset size D, with a constant factor ~6 representing forward pass (2ND) + backward pass (4ND). Given a compute budget C, you must choose how to split between N and D. This is not a technical detail—it's a multi-billion-dollar allocation decision.

**Kaplan et al. (2020)** argued you should favor bigger models: when doubling compute, increase N by ~2× but data D by only ~1.2×. Under this paradigm, GPT-3 (175B parameters, 300B tokens) made sense—build the biggest model you can, train it on moderate data. The logic: parameter count determines capacity, and you can always add more data later (though they didn't anticipate how expensive "later" would be).

**Analogy:** It is like outfitting a factory with a fixed budget: you can buy a huge building with few raw materials, or a right-sized building with enough materials to keep it busy. A giant factory that sits half-idle looks impressive but wastes money; a well-matched factory produces more output per dollar.

**Why It Matters:** The Kaplan vs Chinchilla debate isn't academic—it's the difference between wasting hundreds of millions on undertrained models and training efficiently. Post-Chinchilla, the field converged on ~20:1 token-to-parameter ratios for compute-optimal training. Models like PaLM, LLaMA 2, Mistral, and Gemini all follow this guidance. The realization that Gopher, MT-NLG, and even GPT-3 were undertrained reshaped training runs.

But compute-optimal isn't always optimal. If you're Meta or Google serving billions of users, inference cost dwarfs training cost. LLaMA's decision to over-train smaller models was economically rational: spend an extra $1M on training to save $10M/year on inference. This creates a multi-objective optimization: maximize performance subject to training budget and inference cost constraints. There's no universal answer—the right trade-off depends on your deployment scenario.

The broader insight is that scaling laws provide principled guidance, but real-world decisions involve costs beyond loss: inference latency, memory footprint, API pricing, hardware availability. The trend toward smaller, over-trained models (Mistral 7B, Phi, Gemma) reflects this: competitive performance with radically lower inference cost. The trade-off space is rich, and we're still exploring it.

---

## ⚙️ Core Mechanics
### How It Works
- **Compute relationship**: C ≈ 6ND (forward + backward passes); measured in FLOPs (e.g., 3.14×10²³ for GPT-3)
- **Kaplan allocation**: Favor parameters; N ∝ $C^{0}$.73, D ∝ $C^{0}$.27; leads to big, undertrained models
- **Chinchilla allocation**: Equal scaling; N ∝ $C^{0}$.5, D ∝ $C^{0}$.5; tokens ≈ 20× parameters for compute-optimal
- **Over-training (inference-aware)**: Train smaller models on more data than compute-optimal; minimize inference cost
- **LLaMA ratios**: 7B model trained on 1T tokens (~140:1), 65B on 1.4T (~21:1); over-trained small models
- **Cost breakdown**: Training is one-time (weeks, millions); inference is continuous (years, billions of requests)
- **Emergent trade-off**: Training cost vs inference cost vs model quality; pick two

### Key Specifications
- **Approximate compute law**: C ≈ 6ND
- **Kaplan scaling**: N ∝ $C^{0}$.73, D ∝ $C^{0}$.27
- **Chinchilla scaling**: N_optimal ∝ $C^{0}$.5 and D_optimal ∝ $C^{0}$.5
- **Compute-optimal token ratio**: tokens ≈ 20× parameters
- **Example comparison**: Chinchilla (70B, 1.4T tokens) vs Gopher (280B, 300B tokens)
- **Example inference-aware ratios**: 7B on 1T tokens (~140:1), 65B on 1.4T (~21:1)

### Key Facts
- A fixed compute budget does not determine a single best model size by itself.
- Kaplan-style scaling favored larger models with relatively less data.
- Chinchilla showed that many prominent large models were undertrained.
- Inference-aware training can rationally choose smaller models than compute-optimal scaling suggests.

### Common Distinctions

| Approach | Parameter Scaling | Token Scaling | Use Case |
|----------|------------------|---------------|----------|
| Kaplan (2020) | Favor large N | Tokens ≈ 5-10× params | Compute-limited, one-shot training |
| Chinchilla (2022) | Balanced | Tokens ≈ 20× params | Compute-optimal, research |
| Inference-aware (LLaMA) | Smaller models | Over-train (tokens >> 20× params) | Production serving at scale |
| Mixture-of-Experts | Massive params, sparse | Standard data scaling | High capacity, controlled inference cost |

---

## 🔬 Deep Dive
### Technical Details
**Chinchilla (Hoffmann et al., 2022)** flipped the script by reanalyzing the trade-off. They found that most large models were **undertrained**—you should scale parameters and tokens roughly equally. For compute-optimal training, N_optimal ∝ $C^{0}$.5 and D_optimal ∝ $C^{0}$.5. A 70B model needs ~1.4T tokens (20:1 ratio). Chinchilla (70B, 1.4T tokens) outperformed Gopher (280B, 300B tokens) despite being 4× smaller, purely because it saw 4× more data. This finding reshaped the field.

However, **inference-aware scaling** (e.g., LLaMA) adds another dimension: if inference cost dominates, you want the smallest model that achieves target performance. LLaMA over-trained relative to Chinchilla (smaller models, more tokens) because serving a 7B model is far cheaper than serving a 70B model. The trade-off becomes: spend extra on training (over-train on data) to save massively on inference. This is rational when training is a one-time cost but inference serves billions of requests.

### Limitations and Criticisms
- Compute-optimal scaling is not necessarily deployment-optimal scaling.
- Loss-minimizing recommendations do not directly account for latency, memory footprint, pricing, or hardware bottlenecks.
- There is no universal optimal ratio because the answer depends on whether training cost or inference cost dominates.

### Impact and Legacy
The field's post-Chinchilla shift toward ~20:1 token-to-parameter ratios influenced both frontier and open-weight training runs. At the same time, the rise of smaller over-trained models such as Mistral 7B, Phi, and Gemma shows that the most influential legacy of these scaling laws may be strategic flexibility: researchers now treat scaling as an economic design problem, not just a curve-fitting exercise.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What does the approximation C ≈ 6ND mean in words?
2. Why did Chinchilla call many earlier large models undertrained?
3. How does inference-aware scaling differ from compute-optimal scaling?

### Core Problems
1. Explain why a 70B model trained on more tokens can outperform a much larger model trained on fewer tokens under the same broad compute regime.
2. Compare Kaplan-style scaling and Chinchilla-style scaling in terms of their assumptions about where capability comes from.

### Challenge
1. Suppose you are training a model for a product that will serve billions of daily requests. How would you choose between a Chinchilla-optimal model and a smaller over-trained model, and what costs would dominate your decision?

## Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

## See Also

- [[Language Model Fundamentals]] — foundational understanding of model capacity and data
- [[Scaling Laws]] — the power laws that govern compute-data-parameter trade-offs
- [[Data Curation and Deduplication]] — data quality as a compute multiplier
- [[Training Infrastructure and Parallelism]] — hardware constraints shaping trade-off decisions
- [[Open-Weight Model Ecosystem]] — applying Chinchilla-optimal training to open models

## References
- [[LLM/Sources/Sources Index]]
