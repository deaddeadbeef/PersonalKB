---
tags: [chunk, llm]
id: "chunk-llm-113"
source: "[[LLM/_raw/raw-llm-029 Survey of Large Language Models]]"
source_loc: "Key Takeaways 3, What Is This"
topic: "LLM development pipeline stages"
claim: "The dominant LLM development pipeline is: pretraining → SFT → RLHF/DPO, with each stage serving distinct purposes."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Supervised Fine-Tuning]]"]
up: "[[LLM/LLM]]"
---

# LLM Pipeline Is Pretraining → SFT → RLHF/DPO

## Context
The survey by Zhao et al. synthesized the dominant LLM development pipeline into three distinct stages. First, pretraining on large text corpora teaches the model language understanding, world knowledge, and reasoning capabilities through next-token prediction. Second, supervised fine-tuning (SFT) on instruction-response pairs teaches the model to follow instructions and produce helpful outputs in the desired format. Third, alignment via RLHF (Reinforcement Learning from Human Feedback) or DPO (Direct Preference Optimization) refines the model's outputs to match human preferences for helpfulness, honesty, and safety.

Each stage serves a distinct purpose that cannot easily be collapsed: pretraining provides capability breadth, SFT provides format and task understanding, and alignment provides quality refinement and safety guardrails. Skipping or under-investing in any stage produces characteristic failure modes — capable but uncontrollable (no SFT), controllable but shallow (no pretraining), or helpful but unsafe (no alignment).

## Why It Matters
Understanding this three-stage pipeline is essential for anyone building or deploying LLMs. It explains why base models behave differently from chat models, why fine-tuned models still need alignment, and provides a framework for diagnosing model behavior issues by identifying which stage might be responsible for the observed shortcomings.

## QnA Seeds
- Q: What are the three stages of the dominant LLM development pipeline?
  A: Pretraining (next-token prediction on large corpora for capability), supervised fine-tuning (instruction-response pairs for format and task understanding), and RLHF/DPO (preference optimization for quality, helpfulness, and safety).
- Q: What happens if you skip one of the three pipeline stages?
  A: Skipping SFT produces capable but uncontrollable models, skipping pretraining produces controllable but shallow models, and skipping alignment produces helpful but potentially unsafe models.
