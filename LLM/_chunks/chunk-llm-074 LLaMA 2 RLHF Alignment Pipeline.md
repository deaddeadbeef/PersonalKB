---
tags: [chunk, llm]
id: "chunk-llm-074"
source: "[[LLM/_raw/raw-llm-019 LLaMA 2 Open Chat Models]]"
source_loc: "Key Takeaways 2"
topic: "LLaMA 2 RLHF alignment"
claim: "LLaMA 2 Chat was aligned using RLHF with over 1 million human preference annotations."
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Reinforcement Learning from Human Feedback]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 2 RLHF Alignment Pipeline

## Context
LLaMA 2 Chat's alignment followed a multi-stage pipeline: supervised fine-tuning (SFT) on high-quality dialogue data, then reward model training on over 1 million human preference comparisons, followed by iterative RLHF using both rejection sampling and PPO. The scale of human annotation — over 1 million preference pairs — was the largest publicly documented alignment dataset at the time.

The RLHF pipeline was applied iteratively: the model was improved through multiple rounds of reward model training and policy optimization, with each round's reward model trained on fresh preference data that included comparisons against the latest model version. This iterative approach prevented the reward model from becoming stale and ensured continued improvement. Meta also trained separate reward models for helpfulness and safety, allowing them to balance these sometimes-competing objectives during optimization.

## Why It Matters
LLaMA 2 Chat was the first open-weight model to publish detailed RLHF methodology at this scale, providing a public blueprint for alignment. The 1M+ preference annotations set a scale benchmark, and the iterative RLHF approach (multiple rounds with refreshed reward models) became a best practice adopted by subsequent alignment efforts. It demonstrated that open models could match closed models on safety through rigorous alignment.

## QnA Seeds
- Q: What were the stages of LLaMA 2 Chat's alignment pipeline?
  A: (1) Supervised fine-tuning (SFT) on dialogue data, (2) reward model training on 1M+ human preference comparisons, (3) iterative RLHF using rejection sampling and PPO. Multiple rounds were performed, with each round's reward model retrained on fresh comparisons against the latest model version.
- Q: Why did LLaMA 2 use separate reward models for helpfulness and safety?
  A: Helpfulness and safety can conflict — the most helpful response to a dangerous query might be unsafe. Separate reward models allowed Meta to explicitly balance these objectives during RLHF optimization, tuning the trade-off rather than collapsing both into a single score.
