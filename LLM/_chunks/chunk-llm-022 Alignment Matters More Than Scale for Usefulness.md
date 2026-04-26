---
tags: [chunk, llm]
id: "chunk-llm-022"
source: "[[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback]]"
source_loc: "Section 4, Table 1"
topic: "alignment vs scale"
claim: "A 1.3B InstructGPT model was preferred by human evaluators over the 175B GPT-3, showing alignment matters more than raw scale for usefulness"
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Reinforcement Learning from Human Feedback]]"]
up: "[[LLM/LLM]]"
---

# Alignment Matters More Than Scale for Usefulness

## Context

In human evaluation studies, InstructGPT 1.3B (a model 135× smaller than GPT-3 175B) was consistently preferred by human raters over the raw GPT-3 175B when assessed on helpfulness, truthfulness, and harmlessness. Raters were given prompts and two responses (one from each model) and asked which they preferred. The small aligned model won the majority of comparisons despite having vastly fewer parameters and lower perplexity.

This result was striking because it broke the assumption that bigger models are always better from the user's perspective. GPT-3 175B produced more fluent and knowledgeable text, but it often failed to follow instructions, generated irrelevant completions, or produced harmful content. InstructGPT 1.3B, while less capable in raw language modeling, was far better at understanding what the user actually wanted and providing relevant, helpful responses.

## Why It Matters

This finding established that capability (pre-training scale) and usefulness (alignment) are partially orthogonal dimensions. It provided the theoretical and empirical foundation for the alignment-focused approach that produced ChatGPT — rather than only scaling models, invest in aligning them to human preferences. It also democratized the field: smaller organizations could create useful models by focusing on alignment rather than competing on raw scale.

## QnA Seeds
- Q: How can a 1.3B model be preferred over a 175B model?
  A: Raw language modeling capability (predicting next tokens) doesn't directly translate to following user instructions. GPT-3 175B is a better text completer but a worse assistant — it may continue a prompt in unexpected directions rather than answering the question. InstructGPT 1.3B learned from human demonstrations what "helpful" means, so it provides focused, relevant answers despite having less general knowledge.
- Q: Does this mean we should stop scaling models and focus only on alignment?
  A: No — the ideal approach is both. Alignment and scale are complementary: a larger aligned model will outperform a smaller aligned model. The InstructGPT result shows that without alignment, additional scale yields diminishing returns in user satisfaction. The practical lesson is: first scale for capability, then align for usefulness. Modern best practice applies RLHF/DPO to the largest available base model.
