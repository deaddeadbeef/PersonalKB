---
tags: [chunk, llm]
id: "chunk-llm-017"
source: "[[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)]]"
source_loc: "Section 3, Section 4"
topic: "compute-optimal training"
claim: "Compute-optimal training scales data and parameters roughly equally — tokens ≈ 20× parameters"
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# Compute-Optimal Scaling Ratio

## Context

The Chinchilla paper (Hoffmann et al., 2022) established that for a given compute budget, the optimal allocation between model size and training data follows a roughly 1:1 scaling ratio — both parameters and training tokens should increase proportionally with compute. Empirically, this works out to approximately 20 tokens per parameter. A compute-optimal 10B parameter model should be trained on ~200B tokens, and a 70B model on ~1.4T tokens.

This ratio was derived from three complementary approaches: (1) fixing model size and varying token count, (2) fitting a parametric loss function across all experiments, and (3) directly fitting an optimal model size function. All three converged on the same conclusion. The key insight was that both data and model size contribute equally to performance improvement — dedicating compute disproportionately to either one wastes resources.

## Why It Matters

The 20:1 token-to-parameter ratio became one of the most influential heuristics in LLM development. It immediately revealed that nearly every existing large model (GPT-3, Gopher, PaLM) was significantly undertrained — trained on far fewer tokens than compute-optimal. This finding redirected the industry toward training smaller models on more data, producing better models at lower inference cost, and directly influenced the design of LLaMA, Mistral, and other efficient models.

## QnA Seeds
- Q: What does "20 tokens per parameter" mean practically for training a model?
  A: It means a compute-optimal 7B parameter model should see approximately 140B training tokens, a 13B model about 260B tokens, and a 70B model about 1.4T tokens. If you train a 70B model on only 300B tokens (as Gopher did), you're significantly undertraining it — spending compute on extra parameters that aren't being fully utilized due to insufficient data.
- Q: Is the 20:1 ratio a hard rule or a guideline?
  A: It's a guideline for compute-optimal training — minimizing loss for a fixed compute budget. In practice, many teams deliberately deviate from it. Training a smaller model on more tokens than compute-optimal ("over-training") reduces inference cost because the deployed model is smaller, even though each training FLOP is slightly less efficient. LLaMA-2 (7B trained on 2T tokens) is an example of this deliberate over-training strategy.
