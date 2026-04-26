---
tags: [raw, llm]
id: "raw-llm-005"
title: "Training Compute-Optimal Large Language Models"
author: "Hoffmann et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2203.15556"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Training Compute-Optimal Large Language Models (Chinchilla)

## What Is This?
Showed that most large language models are significantly undertrained — compute-optimal training requires scaling data and parameters roughly equally.

## Why It Matters
Changed the industry's scaling strategy. Chinchilla (70B, 1.4T tokens) outperformed Gopher (280B, 300B tokens) with 4x fewer parameters.

## Key Takeaways
1. Compute-optimal: scale data and parameters equally with compute budget
2. Most existing models were undertrained on data
3. Chinchilla 70B beat Gopher 280B on most benchmarks
4. The relationship: tokens ≈ 20× parameters for optimal training

## Chunk Candidates
- [ ] Compute-optimal scaling ratio
- [ ] Chinchilla vs Gopher comparison
- [ ] Implications for model sizing decisions
- [ ] Over-training rationale (inference cost)
