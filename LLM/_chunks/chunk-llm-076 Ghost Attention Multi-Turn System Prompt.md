---
tags: [chunk, llm]
id: "chunk-llm-076"
source: "[[LLM/_raw/raw-llm-019 LLaMA 2 Open Chat Models]]"
source_loc: "Key Takeaways 3"
topic: "Ghost Attention technique"
claim: "Ghost Attention (GAtt) in LLaMA 2 Chat maintained system prompt adherence across multi-turn conversations."
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/System Prompts and Role Conditioning]]"]
up: "[[LLM/LLM]]"
---

# Ghost Attention Multi-Turn System Prompt

## Context
A persistent challenge in chat models is maintaining adherence to the system prompt across long multi-turn conversations. Without special handling, models tend to "forget" their system instructions after several user turns, reverting to default behavior. LLaMA 2 introduced Ghost Attention (GAtt) to address this: during fine-tuning, the system message is synthetically inserted between all user messages in the training data, but attention is masked so the model doesn't "see" the repeated system messages in intermediate turns.

The result is that the model learns to maintain system prompt behavior throughout a conversation as if the system prompt were always present, without actually needing to include it in every turn's context. During inference, the system prompt appears only once at the beginning, but the model's trained behavior persists across turns. This technique significantly improved system prompt adherence in multi-turn dialogues, making the model more reliably controllable.

## Why It Matters
System prompt adherence is essential for deploying chat models in production — businesses need reliable persona control, safety instructions, and behavioral constraints that persist throughout conversations. GAtt was one of the first published techniques to explicitly address this problem, and the concept of training for multi-turn instruction persistence has influenced subsequent alignment approaches across the industry.

## QnA Seeds
- Q: What problem does Ghost Attention (GAtt) solve in chat models?
  A: Chat models tend to forget system prompt instructions after several conversation turns, reverting to default behavior. GAtt trains the model to maintain system prompt adherence across multi-turn dialogues by synthetically inserting (then attention-masking) the system message between all turns during fine-tuning.
- Q: How does GAtt work during training vs. inference?
  A: During training, the system message is inserted between all user turns but attention-masked so it's invisible to the model at intermediate positions. This teaches persistent behavior. During inference, the system prompt appears only once at the conversation start, but the model maintains adherence throughout as if it were always present.
