---
tags: [raw, llm]
id: "raw-llm-021"
title: "Constitutional AI: Harmlessness from AI Feedback"
author: "Bai et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2212.08073"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Constitutional AI: Harmlessness from AI Feedback

## What Is This?
A method for training harmless AI assistants using a set of written principles (a "constitution") to generate self-critiques and revisions, replacing most human red-team feedback with AI feedback.

## Why It Matters
CAI introduced a scalable alternative to human-labeled safety data, showing that models can self-improve on harmlessness via critique-revision loops guided by explicit principles, reducing reliance on costly human annotation.

## Key Takeaways
1. Two-phase approach: (1) supervised critique-revision using constitutional principles, (2) RLAIF with AI-generated preference labels
2. The constitution is a set of human-written principles (e.g., "choose the response that is less harmful")
3. RLAIF (RL from AI Feedback) uses the model itself to label preferences, substituting for human labelers
4. Produces models that are both more harmless and more helpful than pure RLHF baselines

## Chunk Candidates
- [ ] Constitution design: principles and critique-revision prompting
- [ ] RLAIF pipeline: AI-generated preference data for RL training
- [ ] Comparison of CAI vs RLHF on harmlessness and helpfulness axes
- [ ] Scalability advantages over human red-teaming
