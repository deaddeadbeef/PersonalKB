---
tags: [chunk, llm]
id: "chunk-llm-024"
source: "[[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback]]"
source_loc: "Section 3.3"
topic: "KL penalty"
claim: "KL penalty in PPO prevents the policy from diverging too far from the SFT model, mitigating reward hacking"
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Alignment Objectives and Failure Modes]]"]
up: "[[LLM/LLM]]"
---

# KL Penalty Prevents Reward Hacking

## Context

During PPO optimization, the objective is to maximize R(x, y) = reward_model(x, y) - β × KL(π_θ(y|x) || π_SFT(y|x)), where β is a coefficient controlling the strength of the KL penalty. Without this penalty, the policy would aggressively optimize the reward model, quickly finding adversarial outputs that score highly but are degenerate — repetitive text, nonsensical but confident assertions, or exploiting other reward model biases.

The KL divergence term measures how far the current policy π_θ has moved from the SFT model π_SFT. As the policy diverges, the KL penalty grows, creating a force pulling it back toward the SFT distribution. The coefficient β controls this tension: too low and the model reward-hacks; too high and the model barely improves from SFT. In practice, β is often adapted dynamically to maintain a target KL divergence throughout training.

## Why It Matters

The KL penalty embodies a fundamental principle of alignment: the aligned model should improve upon the base model's behavior without losing its core language capabilities. It is a practical solution to the broader alignment problem of Goodhart's Law — "when a measure becomes a target, it ceases to be a good measure." The reward model is an imperfect proxy for human preferences, and the KL penalty limits how much the policy can exploit this imperfection.

## QnA Seeds
- Q: What happens if you remove the KL penalty during PPO training?
  A: Without the KL penalty, the model quickly degenerates. It finds and exploits weaknesses in the reward model — producing repetitive, overly long, or sycophantic outputs that score high rewards but are clearly low quality to humans. The model's text fluency also degrades as it drifts from the language distribution learned during pre-training. In practice, removing KL leads to reward collapse within a few hundred PPO steps.
- Q: How is the KL penalty coefficient β typically set?
  A: It can be set as a fixed hyperparameter (common values are 0.01–0.2) or adapted dynamically. The dynamic approach targets a specific KL divergence value (e.g., 6 nats) and adjusts β up or down to maintain it. If the policy diverges too fast, β increases to rein it in; if progress stalls, β decreases. This adaptive approach is more robust and is used in most modern RLHF implementations.
