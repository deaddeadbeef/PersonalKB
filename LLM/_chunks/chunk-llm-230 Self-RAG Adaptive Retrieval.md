---
tags: [chunk, llm]
id: "chunk-llm-230"
source: "[[LLM/_raw/raw-llm-058 Self-RAG Learning to Retrieve Generate and Critique]]"
source_loc: "Chunk Candidates"
topic: "self-RAG adaptive retrieval"
claim: "Self-RAG adaptively decides when to retrieve based on generation confidence, avoiding unnecessary retrieval when parametric knowledge suffices."
confidence: "verified"
supports: ["[[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]", "[[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]"]
qna_seeds:
  - q: "How does Self-RAG decide when to retrieve?"
    a: "The model generates a Retrieve token at segment boundaries — if it predicts 'Retrieve=Yes', it queries the retrieval system; if 'Retrieve=No', it continues generating from parametric memory, avoiding the latency and noise of unnecessary retrieval."
  - q: "Why is adaptive retrieval better than always-retrieve?"
    a: "Always-retrieve pipelines waste latency and risk injecting irrelevant context for queries the model can answer from training knowledge. Adaptive retrieval only invokes the retriever when the model is uncertain, improving both speed and accuracy."
up: "[[LLM/LLM]]"
---
# Self-RAG Adaptively Retrieves Only When Needed

Unlike standard RAG pipelines that always retrieve for every query, Self-RAG learns when retrieval is beneficial. At segment boundaries during generation, the model produces a Retrieve reflection token. If it predicts "Retrieve=Yes," the system queries the external retrieval corpus and conditions the next generation segment on the retrieved passages. If "Retrieve=No," the model continues generating from its parametric knowledge.

This adaptive behavior avoids two failure modes of fixed retrieval pipelines: unnecessary retrieval latency for questions the model can confidently answer from training knowledge, and context pollution where irrelevant retrieved passages degrade generation quality. Experiments show that Self-RAG retrieves for roughly 50–70% of segments depending on the task, skipping retrieval precisely for segments where parametric knowledge is sufficient and accurate.
