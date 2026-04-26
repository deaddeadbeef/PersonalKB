---
tags: [chunk, llm]
id: "chunk-llm-019"
source: "[[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)]]"
source_loc: "Section 3"
topic: "compute-data trade-offs"
claim: "The Chinchilla scaling law revised Kaplan et al.: both data and parameters should scale equally with compute budget"
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# Chinchilla Revises Kaplan Scaling Recommendations

## Context

Kaplan et al. (2020) originally suggested that when scaling compute, most additional resources should go to increasing model size with relatively less allocated to training data. Specifically, Kaplan found that optimal model size scales as N_opt ∝ C^0.73, implying parameters should scale much faster than data with increasing compute. This led labs to build very large models trained on comparatively little data (e.g., Gopher 280B on 300B tokens).

Hoffmann et al. (Chinchilla) ran a more comprehensive set of experiments and found that the optimal scaling is closer to N_opt ∝ C^0.50 and D_opt ∝ C^0.50 — both data and parameters should scale equally. The discrepancy likely arose because Kaplan's experiments used a narrower range of configurations and didn't fully account for the learning rate schedule's interaction with training duration. Chinchilla's analysis used over 400 training runs spanning four orders of magnitude in compute.

## Why It Matters

The revision from "scale parameters fast" to "scale both equally" was one of the most consequential corrections in the history of LLM development. It redirected billions of dollars of training compute toward data collection and curation rather than pure parameter scaling. It also created urgency around data availability — at equal scaling, frontier models would soon exhaust available high-quality text data, a concern that materialized by 2024.

## QnA Seeds
- Q: Why did Kaplan and Chinchilla arrive at different optimal scaling ratios?
  A: The most likely explanations are: (1) Kaplan used a fixed learning rate schedule that wasn't adjusted for different training durations, biasing results toward shorter training on larger models; (2) Kaplan's experiments covered a narrower range of data sizes; and (3) Chinchilla used a much larger and more systematic experimental grid (400+ runs vs fewer). The learning rate schedule issue is considered the primary factor.
- Q: What does "scale both equally" mean in terms of resource allocation?
  A: If you double your compute budget, you should increase both model size and training data by approximately √2 (about 1.4×). Concretely, going from 10B parameters / 200B tokens to a 2× compute budget means approximately 14B parameters / 280B tokens, rather than Kaplan's recommendation of ~18B parameters / 200B tokens. The key shift is that data scaling matters as much as parameter scaling.
