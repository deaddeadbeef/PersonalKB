---
tags: [chunk, llm]
id: "chunk-llm-182"
source: "[[LLM/_raw/raw-llm-046 Training a Helpful and Harmless Assistant with RLHF]]"
source_loc: "Chunk Candidates"
topic: "RLHF alignment pipeline"
claim: "The Anthropic RLHF pipeline consists of three stages: collecting human preference comparisons, training a reward model on those preferences, and fine-tuning the language model with PPO against the reward model."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: What are the three stages of the RLHF pipeline? A: (1) Collect human preference data by having annotators rank model outputs, (2) train a reward model to predict human preferences, (3) fine-tune the LM with PPO to maximize the reward model's score."
  - "Q: Why is PPO used in RLHF rather than direct optimization? A: PPO is a stable reinforcement learning algorithm that optimizes the policy (LM) against the reward model while constraining updates with a KL penalty to prevent the model from diverging too far from the base policy."
up: "[[LLM/LLM]]"
---

# RLHF Pipeline for Alignment

The RLHF alignment pipeline described by Bai et al. follows three stages. First, human annotators compare pairs of model responses and indicate which is more helpful or less harmful, generating preference data. Second, a reward model is trained to predict these human preferences, learning to score arbitrary model outputs. Third, the language model is fine-tuned using Proximal Policy Optimization (PPO) to maximize the reward model's scores, with a KL divergence penalty to prevent the model from straying too far from its supervised fine-tuning baseline. This three-stage pipeline became the canonical RLHF approach used by OpenAI, Anthropic, and others.
