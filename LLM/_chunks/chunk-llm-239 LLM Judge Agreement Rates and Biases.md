---
tags: [chunk, llm]
id: "chunk-llm-239"
source: "[[LLM/_raw/raw-llm-060 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]]"
source_loc: "Chunk Candidates"
topic: "LLM judge agreement and biases"
claim: "Strong LLM judges (GPT-4) agree with human evaluators over 80% of the time but exhibit systematic position bias and verbosity bias."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/LLM-as-Judge]]"]
qna_seeds:
  - q: "How well do LLM judges agree with human evaluators?"
    a: "GPT-4 as judge achieves over 80% agreement with human expert preferences on pairwise comparisons, comparable to inter-annotator agreement among human evaluators themselves."
  - q: "What systematic biases do LLM judges exhibit?"
    a: "Position bias (preferring the response shown first), verbosity bias (preferring longer responses regardless of quality), and self-enhancement bias (GPT-4 slightly favoring GPT-4-generated responses) are the three main documented biases."
up: "[[LLM/LLM]]"
---
# LLM Judges Achieve 80%+ Human Agreement but Have Systematic Biases

The study found that GPT-4 as a judge agrees with human expert preferences over 80% of the time on pairwise response comparisons — comparable to the agreement rate between human annotators themselves (~81%). This high agreement rate validates LLM-as-judge as a practical and scalable alternative to expensive human evaluation for many use cases.

However, LLM judges exhibit systematic biases that must be mitigated. **Position bias**: judges prefer the response presented first, which can be addressed by evaluating in both orderings and averaging. **Verbosity bias**: judges favor longer responses even when the shorter response is more accurate or relevant. **Self-enhancement bias**: GPT-4 shows a small but measurable preference for GPT-4-generated text. Awareness of these biases and mitigation strategies (position swapping, calibrated scoring rubrics) are essential for reliable LLM-based evaluation.
