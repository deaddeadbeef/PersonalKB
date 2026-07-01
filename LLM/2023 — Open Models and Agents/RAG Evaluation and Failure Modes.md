---
tags: [llm, rag]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# RAG Evaluation and Failure Modes

> **One-line summary** RAG evaluation works only when you separately measure retrieval quality and answer quality, then diagnose which stage failed when the system gets something wrong.

## 🎯 Intuition

**The Core Idea:**  
Evaluating a RAG system means checking two linked systems at once: whether the right information was retrieved, and whether the model used that information correctly when generating the answer.

**Analogy:**  
Imagine a researcher and a writer working together. The researcher gathers source material, and the writer produces the final response. If the final answer is bad, you need to know whether the researcher brought the wrong documents or the writer misread the right ones.

**Why It Matters:**  
Without this separation, teams optimize blindly. They may improve prompts when retrieval is actually broken, or tune embeddings when the real problem is that the model ignored correct evidence already in context.

---

## ⚙️ Core Mechanics

### How It Works

Evaluating a RAG system requires measuring both retrieval quality and generation quality—and understanding the distinct failure modes at each stage. Without rigorous evaluation, teams cannot distinguish between a retrieval miss (the right passage was never found) and an extraction failure (the right passage was found but the LLM ignored or misread it), leading to misdirected optimization effort.

RAG evaluation spans two coupled subsystems. **Retrieval evaluation** asks: did the system find the right passages? Standard metrics include recall@k (fraction of relevant passages in the top-k), precision@k, and Mean Reciprocal Rank (MRR). **Generation evaluation** asks: given the retrieved context, did the LLM produce a correct, faithful, and relevant answer? This is harder to measure and requires metrics like faithfulness (is every claim in the answer supported by the retrieved context?), answer relevance (does the answer actually address the question?), and context relevance (are the retrieved passages pertinent to the question?).

The **RAGAS framework** (Retrieval-Augmented Generation Assessment) operationalizes these metrics using LLM-as-judge evaluation. It decomposes RAG quality into faithfulness, answer relevance, context precision, and context recall—each scored automatically by prompting an evaluator LLM. While not perfect, RAGAS provides a repeatable, scalable evaluation pipeline that catches regressions far better than manual spot-checking.

**Failure modes** are the practitioner's diagnostic framework. A **retrieval miss** means the relevant passage exists in the corpus but wasn't retrieved—caused by embedding blind spots, poor chunking, or query-document vocabulary mismatch. **Context poisoning** means irrelevant or contradictory passages were retrieved and confused the LLM. **Extraction failure** means the right passage was retrieved and present in the context, but the LLM failed to extract or synthesize the answer—often due to the "Lost in the Middle" effect (Liu et al. 2023), where models disproportionately attend to the beginning and end of the context window and neglect information in the middle. **Hallucination despite context** is the most insidious: the LLM generates a plausible-sounding answer that contradicts or is unsupported by the retrieved passages, drawing instead on parametric knowledge or fabrication.

### Key Specifications

- **Recall@k**: |relevant ∩ retrieved_top_k| / |relevant|. Measures retrieval coverage.
- **Precision@k**: |relevant ∩ retrieved_top_k| / k. Measures retrieval signal-to-noise.
- **MRR**: 1/rank of the first relevant result. Measures how quickly the system surfaces a relevant passage.
- **Faithfulness** (RAGAS): Fraction of claims in the generated answer that are entailed by the retrieved context.
- **Answer relevance** (RAGAS): Does the answer address the user's question? Scored via LLM-as-judge.
- **Context precision/recall** (RAGAS): Are the retrieved passages relevant (precision) and sufficient (recall)?
- **Failure mode — Retrieval miss**: Right passage exists but isn't retrieved. Fix: better embeddings, hybrid search, query transformation.
- **Failure mode — Context poisoning**: Irrelevant passages dilute or contradict. Fix: reranking, stricter top-k, metadata filtering.
- **Failure mode — Extraction failure**: Right passage retrieved but answer not extracted. Fix: passage ordering, smaller context, explicit instructions.
- **Failure mode — Hallucination despite context**: LLM ignores context and fabricates. Fix: stronger faithfulness instructions, citation requirements, post-generation verification.
- **"Lost in the Middle"** (Liu et al. 2023): LLMs perform best when key information is at the start or end of the context, worst when it's in the middle.
- **Ground truth creation**: Building evaluation datasets with known question-answer-passage triples is expensive but essential. Synthetic generation from passages + human validation is a common approach.
- **Multi-hop evaluation**: Requires verifying that each reasoning step is grounded, not just the final answer.

### Key Facts

Without evaluation, RAG development is guesswork. A system might produce good answers on easy questions while catastrophically failing on edge cases—and you'd never know which component to blame. Structured evaluation with failure-mode diagnosis turns RAG optimization from trial-and-error into systematic engineering: retrieval misses point to embedding or chunking improvements, context poisoning points to reranking, extraction failures point to prompt engineering or context assembly, and hallucinations point to faithfulness guardrails.

The "Lost in the Middle" finding is particularly actionable: simply reordering passages so the most relevant appear first and last can measurably improve answer quality without changing any model or retrieval component.

| Failure Mode | Symptom | Root Cause | Fix |
| --- | --- | --- | --- |
| Retrieval miss | Wrong or no answer; right passage exists in corpus | Embedding gap, chunking, vocab mismatch | Hybrid search, better embeddings, query transform |
| Context poisoning | Confident wrong answer | Irrelevant passages in context | Reranking, stricter filtering, metadata constraints |
| Extraction failure | Partial or vague answer despite good context | "Lost in the Middle", too much context | Passage reordering, smaller k, explicit extraction prompts |
| Hallucination | Plausible but unsupported answer | Parametric knowledge override | Citation requirements, faithfulness checks, verification |

---

## 🔬 Deep Dive

### Technical Details

RAG evaluation is harder than evaluating either retrieval or generation alone because the system's output depends on the interaction between both. Good retrieval can still yield bad answers if the model fails to synthesize evidence. Good generation behavior cannot rescue a system that never retrieves the relevant passage.

This is why diagnostic decomposition matters. Metrics such as recall@k, precision@k, and MRR tell you whether the corpus access layer is working. Metrics such as faithfulness and answer relevance tell you whether the generation layer stayed grounded and useful. Frameworks such as RAGAS make this decomposition scalable by automating judgment with an evaluator model, even if those judgments are themselves imperfect.

### Limitations and Criticisms

Ground-truth dataset creation is expensive. Reliable evaluation often requires question-answer-passage triples, and building those at scale usually needs synthetic generation plus human validation.

LLM-as-judge evaluation is useful but not infallible. It can be noisy, model-dependent, and sensitive to prompt phrasing. Multi-hop tasks are especially challenging because evaluation must verify not just the final answer, but whether each reasoning step was actually grounded in retrieved evidence.

### Impact and Legacy

The major contribution of this evaluation framing is that it turns RAG from vague prompt-tuning into an engineering discipline. Instead of saying "the system feels worse," teams can ask whether they have a retrieval miss, context poisoning, extraction failure, or hallucination problem.

The "Lost in the Middle" result also had durable impact because it highlighted that context assembly itself is an optimization lever. Passage order, top-k choice, and filtering rules can improve answer quality materially even when the retriever and generator stay fixed.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. What is the difference between retrieval evaluation and generation evaluation in RAG?
2. What does recall@k measure?
3. Why is hallucination despite context especially dangerous?

### Core Problems

1. Explain how you would distinguish a retrieval miss from an extraction failure in a failed RAG example.
2. Compare recall@k, precision@k, MRR, and faithfulness. What does each reveal about system quality?
3. Why can passage ordering improve RAG performance even if neither the retriever nor the model changes?
4. Describe how RAGAS helps make evaluation scalable, and what its limitations are.

### Challenge

A RAG system answers a question incorrectly even though the correct passage is somewhere in the corpus. Design a debugging workflow that would let you decide whether the problem is retrieval miss, context poisoning, extraction failure, or hallucination despite context, and recommend one concrete fix for each possible diagnosis.

For a local applied workflow, use [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] to separate top-k misses, low-rank evidence, context poisoning, reranking gains, and citation failures before tuning the generator.

## References
### Supporting Chunks

- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

### References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
