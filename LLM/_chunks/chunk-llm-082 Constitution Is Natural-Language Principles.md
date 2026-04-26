---
tags: [chunk, llm]
id: "chunk-llm-082"
source: "[[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness]]"
source_loc: "Key Takeaways 2, Chunk Candidates"
topic: "Constitution as natural-language principles"
claim: "The constitution is a set of natural-language principles that guide the model's self-evaluation without task-specific training."
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Constitutional AI]]"]
up: "[[LLM/LLM]]"
---

# Constitution Is Natural-Language Principles for Self-Evaluation

## Context
The "constitution" in Constitutional AI is a set of human-written, natural-language principles such as "choose the response that is less harmful" or "select the answer that is most honest." These principles are provided as prompts during the critique-revision phase and the preference-labeling phase. The model reads the principle and applies it to evaluate its own outputs — no task-specific training data or specialized classifiers are needed.

This design means the constitution is inherently modular and interpretable. Each principle can be read, understood, and debated by humans, and the set can be extended or modified by simply editing text. The principles operate at the level of general values rather than narrow behavioral rules, giving the system broad coverage across diverse scenarios.

## Why It Matters
Encoding alignment goals as readable natural-language principles makes the safety specification transparent and auditable. Unlike opaque reward models or implicitly learned preferences, a constitution can be reviewed, versioned, and debated by stakeholders — bringing alignment closer to a governance process than a purely technical optimization.

## QnA Seeds
- Q: What form does the "constitution" take in Constitutional AI?
  A: It is a set of human-written natural-language principles (e.g., "choose the response that is less harmful") used as prompts to guide the model's self-critique and preference labeling.
- Q: Why is a natural-language constitution advantageous over a trained reward model for safety?
  A: It is transparent, auditable, and modifiable by editing text — stakeholders can review and debate the principles without needing to retrain any model components.
