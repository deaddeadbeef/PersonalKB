---
tags: [chunk, llm]
id: "chunk-llm-229"
source: "[[LLM/_raw/raw-llm-058 Self-RAG Learning to Retrieve Generate and Critique]]"
source_loc: "What Is This, Chunk Candidates"
topic: "self-RAG reflection tokens"
claim: "Self-RAG trains special reflection tokens (Retrieve, IsRel, IsSup, IsUse) that enable the model to self-critique its generation and decide when to retrieve."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]", "[[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]"]
qna_seeds:
  - q: "What are Self-RAG's reflection tokens?"
    a: "Retrieve (should I retrieve?), IsRel (is retrieved passage relevant?), IsSup (is generation supported by passage?), and IsUse (is the generation useful overall?) — special tokens the model generates to critique its own process."
  - q: "How are the reflection tokens trained?"
    a: "A critic model (GPT-4) labels training examples with reflection token annotations, and the generator LLM is fine-tuned to produce these tokens inline during generation, learning to self-assess without external supervision at inference time."
up: "[[LLM/LLM]]"
---
# Self-RAG Uses Reflection Tokens for Self-Critique During Generation

Self-RAG introduces four special reflection tokens that enable the model to introspect and critique its own generation process. **Retrieve** signals whether external retrieval is needed for the current segment. **IsRel** assesses whether a retrieved passage is relevant to the query. **IsSup** evaluates whether the generated text is supported by the retrieved evidence. **IsUse** judges the overall utility of the generated response.

These tokens are trained by first having GPT-4 annotate a training corpus with reflection labels, then fine-tuning the generator LLM (LLaMA-based) to produce these tokens inline during generation. At inference time, the model generates reflection tokens without any external critic, using them to dynamically control its retrieval and generation behavior. This makes the retrieval decision learned and adaptive rather than fixed by a pipeline rule.
