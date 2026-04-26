---
tags: [chunk, llm]
id: "chunk-llm-199"
source: "[[LLM/_raw/raw-llm-050 Toolformer Language Models Can Teach Themselves to Use Tools]]"
source_loc: "Chunk Candidates"
topic: "Toolformer decision boundary"
claim: "Toolformer learns an implicit decision boundary for when tool use is beneficial: it calls tools only when its internal knowledge is insufficient and the API result actually improves prediction."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: How does Toolformer decide when to use a tool? A: Through the loss-based filtering during training — it only learns to insert API calls in contexts where the tool result improved next-token prediction, so it implicitly learns to call tools when its own knowledge is insufficient."
  - "Q: Does Toolformer over-rely on tools? A: No — the perplexity-based filtering naturally prevents unnecessary tool calls, because calls that don't reduce perplexity are excluded from training data, teaching the model to be selective."
up: "[[LLM/LLM]]"
---

# Model Learns When to Call vs Not Call Tools

A subtle but important property of Toolformer is its learned decision boundary for tool invocation. Because the training data only includes API calls that actually reduced perplexity, the model learns to invoke tools selectively — calling them when its parametric knowledge is insufficient (e.g., recent facts, precise calculations) but relying on its own knowledge when it is adequate. This self-calibrating behavior emerges naturally from the loss-based filtering without any explicit confidence threshold or routing logic. The model effectively learns its own capability boundaries, a form of implicit uncertainty awareness that is valuable for practical agentic systems.
