---
tags: [chunk, llm]
id: "chunk-llm-197"
source: "[[LLM/_raw/raw-llm-050 Toolformer Language Models Can Teach Themselves to Use Tools]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Toolformer self-supervised annotation"
claim: "Toolformer learns tool use self-supervisedly: the model generates candidate API call insertions, executes them, and keeps only those that reduce perplexity on subsequent tokens — no human annotation of tool use needed."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: How does Toolformer learn to use tools without human annotation? A: It generates candidate API calls at various positions in text, executes them, computes whether including the result reduces the loss on following tokens, and fine-tunes on the successful examples."
  - "Q: What is the loss-based filtering criterion? A: A candidate tool call is kept if the model's perplexity on tokens after the call is lower when the API result is included versus when it is not — meaning the tool genuinely helped the model predict better."
up: "[[LLM/LLM]]"
---

# Self-Supervised Tool-Use Learning via Loss-Based Filtering

Toolformer's key innovation is a self-supervised method for annotating training data with tool use. Given a text corpus, the model first generates candidate API call insertions at various positions using few-shot prompting. Each candidate is executed against the actual API, and the result is inserted. The filtering criterion is simple: keep the API call only if including the tool's response reduces the model's perplexity on the subsequent tokens compared to leaving it out. The model is then fine-tuned on this filtered dataset. This approach requires no human annotation of when or how to use tools — the model learns entirely from whether tool use improves its language modeling objective.
