---
tags: [chunk, llm]
id: "chunk-llm-081"
source: "[[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness]]"
source_loc: "Key Takeaways 1-2, What Is This"
topic: "Constitutional AI self-critique methodology"
claim: "Constitutional AI uses AI self-critique against a set of principles to revise model outputs, replacing human annotation with RLAIF."
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Constitutional AI]]"]
up: "[[LLM/LLM]]"
---

# Constitutional AI Replaces Human Annotation with Self-Critique

## Context
Constitutional AI (CAI) introduced a two-phase approach to training harmless AI assistants. In the first phase, the model generates responses, then critiques its own outputs against a written set of principles — the "constitution" — and produces revised responses. This supervised critique-revision process generates training data without human annotators reviewing each output for safety.

In the second phase, RLAIF (Reinforcement Learning from AI Feedback) replaces the human preference labelers used in traditional RLHF. The model itself evaluates pairs of responses according to constitutional principles and generates preference labels, which then train a reward model for RL fine-tuning. This yields models that are both more harmless and more helpful than pure RLHF baselines.

## Why It Matters
CAI fundamentally changed the economics of safety training by showing that explicit principles plus AI self-evaluation can substitute for expensive, slow human red-teaming. This makes safety alignment more scalable and enables rapid iteration on safety criteria without bottlenecking on human annotator availability.

## QnA Seeds
- Q: What are the two phases of Constitutional AI training?
  A: Phase 1 is supervised critique-revision, where the model critiques and revises its own outputs against constitutional principles. Phase 2 is RLAIF, where the model generates preference labels for RL training instead of human labelers.
- Q: How does CAI reduce the need for human annotation?
  A: By using the model itself to critique outputs against written principles and to generate preference labels for reward model training, replacing human red-teamers and preference annotators.
