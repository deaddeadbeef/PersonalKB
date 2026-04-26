---
tags: [chunk, llm]
id: "chunk-llm-083"
source: "[[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness]]"
source_loc: "Key Takeaways 3, Chunk Candidates"
topic: "RLAIF scalable oversight"
claim: "RLAIF (RL from AI Feedback) uses the model's own judgments as reward signal, enabling scalable oversight."
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Constitutional AI]]"]
up: "[[LLM/LLM]]"
---

# RLAIF Uses Model Judgments as Reward Signal

## Context
Reinforcement Learning from AI Feedback (RLAIF) is the second phase of Constitutional AI training. Instead of collecting thousands of human preference comparisons to train a reward model, RLAIF has the model itself evaluate response pairs according to constitutional principles. The model's judgments — which response better satisfies the principles — become the preference labels used to train the reward model for RL fine-tuning.

This substitution is significant because human preference collection is the primary bottleneck in RLHF pipelines: it is slow, expensive, and inconsistent across annotators. By replacing human labels with AI-generated labels guided by explicit principles, RLAIF makes the feedback loop orders of magnitude faster and cheaper while maintaining — and in some cases improving — the quality of the resulting alignment.

## Why It Matters
RLAIF demonstrates that scalable oversight is achievable for current models: the AI can evaluate its own behavior against explicit criteria at a scale that would be infeasible for human reviewers. This is a key stepping stone toward alignment approaches that can keep pace with rapidly improving model capabilities.

## QnA Seeds
- Q: How does RLAIF differ from standard RLHF?
  A: In RLHF, human annotators provide preference labels for response pairs. In RLAIF, the model itself generates these preference labels by evaluating responses against constitutional principles.
- Q: What scalability advantage does RLAIF provide?
  A: It eliminates the human annotation bottleneck, allowing preference data generation at machine speed and cost, making it feasible to iterate quickly on alignment training.
