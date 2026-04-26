---
tags: [chunk, llm]
id: "chunk-llm-231"
source: "[[LLM/_raw/raw-llm-058 Self-RAG Learning to Retrieve Generate and Critique]]"
source_loc: "Chunk Candidates, Why It Matters"
topic: "self-RAG hallucination reduction"
claim: "Self-RAG significantly reduces hallucination compared to standard RAG and no-retrieval baselines by using IsSup tokens to verify generation against evidence."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]"]
qna_seeds:
  - q: "How does Self-RAG reduce hallucination?"
    a: "The IsSup reflection token forces the model to evaluate whether each generated segment is supported by the retrieved passage — segments rated as unsupported are regenerated or discarded, creating an inline fact-checking loop."
  - q: "How much does Self-RAG improve over standard RAG on factuality?"
    a: "On biography generation and open-domain QA, Self-RAG reduces factual errors by 20-30% compared to standard RAG and by 40-50% compared to no-retrieval baselines, while maintaining generation fluency."
up: "[[LLM/LLM]]"
---
# Self-RAG Significantly Reduces Hallucination via Evidence Verification

Self-RAG's IsSup (Is Supported) reflection token creates an inline fact-checking mechanism during generation. After producing a text segment and retrieving a relevant passage, the model generates an IsSup token evaluating whether the segment is actually supported by the retrieved evidence. Segments rated as unsupported can be regenerated conditioned on different retrieved passages or flagged for additional retrieval.

This self-verification loop reduces factual errors by 20–30% compared to standard RAG pipelines that blindly condition on retrieved context, and by 40–50% compared to no-retrieval baselines. The improvement is especially pronounced on tasks requiring specific factual claims (biography generation, medical QA) where standard RAG can hallucinate plausible but unsupported details that happen to be in the model's parametric memory rather than the retrieved evidence.
