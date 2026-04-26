---
tags: [chunk, llm]
id: "chunk-llm-013"
source: "[[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models]]"
source_loc: "Section 1, Section 6"
topic: "scaling laws"
claim: "Language model loss follows power laws: L(N) ≈ (N_c/N)^α_N for parameter count N, with similar laws for data and compute"
confidence: "verified"
supports: ["[[LLM/Pretraining/Scaling Laws]]"]
up: "[[LLM/LLM]]"
---

# Power-Law Loss Scaling

## Context

Kaplan et al. (2020) discovered that language model cross-entropy loss follows remarkably clean power-law relationships with three independent variables: parameter count N, dataset size D (in tokens), and compute budget C (in FLOPs). Specifically, L(N) ≈ (N_c/N)^α_N where N_c is a constant and α_N ≈ 0.076. Similar power laws govern L(D) and L(C), each with their own constants and exponents.

These relationships hold over many orders of magnitude and across different model architectures, training procedures, and data distributions. When plotted on log-log scales, the empirical data falls on remarkably straight lines. The power-law form implies diminishing returns — each 10× increase in resources yields a fixed absolute improvement in log-loss — but the returns diminish slowly enough that continued scaling remains worthwhile.

## Why It Matters

The scaling laws transformed LLM development from an empirical art into a predictive science. Training runs costing millions of dollars could be planned with quantitative confidence by extrapolating from cheaper experiments. The power-law relationships also provided deep insight into the nature of language modeling: the smooth, continuous improvement suggests that language understanding is not a discrete capability but a continuum that models traverse as they scale.

## QnA Seeds
- Q: What does the power-law exponent α_N ≈ 0.076 tell us about scaling models?
  A: It means that loss decreases as a power of parameter count with exponent ~0.076. Concretely, doubling the number of parameters reduces loss by approximately 2^0.076 ≈ 5.4%. This is a slow power law, meaning you need large increases in scale for substantial improvements, but the relationship is extremely reliable and shows no sign of saturating within the ranges studied.
- Q: Do the scaling laws apply to individual downstream tasks or only to pre-training loss?
  A: The original Kaplan scaling laws characterize pre-training cross-entropy loss. The relationship between pre-training loss and specific downstream task accuracy is more complex and task-dependent. Some tasks improve smoothly with lower loss, while others appear to show "emergent" jumps. However, lower pre-training loss generally correlates with better downstream performance across the board.
