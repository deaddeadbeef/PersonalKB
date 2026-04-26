---
tags: [chunk, llm]
id: "chunk-llm-021"
source: "[[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback]]"
source_loc: "Section 3"
topic: "RLHF pipeline"
claim: "RLHF pipeline: (1) SFT on human demonstrations, (2) train reward model on preference pairs, (3) optimize policy via PPO with KL penalty"
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Reinforcement Learning from Human Feedback]]"]
up: "[[LLM/LLM]]"
---

# RLHF Three-Stage Pipeline

## Context

InstructGPT introduced the canonical RLHF pipeline consisting of three sequential stages. Stage 1 (SFT): fine-tune the base language model on a dataset of human-written demonstrations of desired behavior — labelers are given prompts and write ideal responses, then the model is supervised-fine-tuned on these (prompt, response) pairs. Stage 2 (Reward Model): collect comparison data where labelers rank multiple model outputs for the same prompt, then train a reward model to predict these human preferences as a scalar score.

Stage 3 (PPO): use the reward model as an environment reward signal and optimize the SFT model's policy using Proximal Policy Optimization. A KL divergence penalty is added to prevent the policy from diverging too far from the SFT model, maintaining language quality while improving alignment. The model is trained to maximize reward_model(prompt, response) - β × KL(policy || SFT_model) across a distribution of prompts.

## Why It Matters

This three-stage pipeline became the de facto standard for aligning language models and directly led to ChatGPT. It demonstrated that alignment (making models follow instructions and behave safely) is a separable problem from capability (pre-training) — you can align a pre-trained model post-hoc. Every major LLM provider adopted some variant of this pipeline, and it remains the foundation even as alternatives like DPO simplify parts of it.

## QnA Seeds
- Q: Why does RLHF need three stages instead of directly training on human preferences?
  A: Each stage builds on the previous one. SFT gives the model a reasonable starting policy (without it, the model generates incoherent outputs that are hard to rank). The reward model converts expensive human judgments into a cheap, differentiable signal that can be used for large-scale optimization. PPO then optimizes against this signal with safeguards. Skipping stages degrades quality — training PPO from the base model (no SFT) produces worse results.
- Q: How much human annotation data was needed for InstructGPT?
  A: Relatively little by modern standards: about 13,000 demonstrations for SFT and 33,000 comparisons for the reward model. This small amount of human data aligned a 175B parameter model, demonstrating remarkable data efficiency. The key insight was that specifying what good behavior looks like (via demonstrations and rankings) is far cheaper than training the behavior from scratch.
