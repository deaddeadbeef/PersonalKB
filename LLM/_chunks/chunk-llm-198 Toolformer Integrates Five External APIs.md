---
tags: [chunk, llm]
id: "chunk-llm-198"
source: "[[LLM/_raw/raw-llm-050 Toolformer Language Models Can Teach Themselves to Use Tools]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Toolformer API coverage"
claim: "Toolformer demonstrated learning to use five different APIs — calculator, Q&A system, search engine, translator, and calendar — each for contextually appropriate tasks."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What tools did Toolformer learn to use? A: A calculator (for arithmetic), a question-answering system (for factual lookup), a Wikipedia search engine (for knowledge retrieval), a machine translator, and a calendar/date API."
  - "Q: Did Toolformer use the right tool for each situation? A: Yes — it learned contextual appropriateness: using the calculator for math problems, search for factual questions, translator for foreign text, etc., with no explicit routing logic."
up: "[[LLM/LLM]]"
---

# Toolformer Integrates Five External APIs

Schick et al. demonstrated Toolformer on five diverse APIs: a calculator for arithmetic operations, a question-answering system for factual lookup, a Wikipedia search engine for knowledge retrieval, a machine translation system for multilingual content, and a calendar API for date-related queries. The model learned not just how to format API calls but when each tool was appropriate — it used the calculator for arithmetic embedded in text, search for factual claims it was uncertain about, and the translator when encountering foreign language text. No explicit tool-routing logic was needed; the self-supervised objective naturally taught contextual tool selection.
