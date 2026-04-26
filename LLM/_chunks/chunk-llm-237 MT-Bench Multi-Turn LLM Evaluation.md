---
tags: [chunk, llm]
id: "chunk-llm-237"
source: "[[LLM/_raw/raw-llm-060 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]]"
source_loc: "What Is This, Chunk Candidates"
topic: "MT-Bench multi-turn evaluation"
claim: "MT-Bench consists of 80 multi-turn questions across 8 categories, scored by GPT-4 as judge on a 1-10 scale to evaluate LLM conversational ability."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/LLM-as-Judge]]", "[[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]"]
qna_seeds:
  - q: "What is MT-Bench?"
    a: "A benchmark of 80 multi-turn questions spanning 8 categories (writing, roleplay, reasoning, math, coding, extraction, STEM, humanities) where GPT-4 rates model responses on a 1-10 scale, testing both initial response quality and follow-up consistency."
  - q: "Why is the multi-turn aspect important?"
    a: "Single-turn benchmarks miss critical capabilities like instruction retention, context tracking, and the ability to refine or correct responses — multi-turn evaluation captures the conversational competence users actually experience."
up: "[[LLM/LLM]]"
---
# MT-Bench Evaluates Multi-Turn Conversational LLM Quality

MT-Bench is a benchmark consisting of 80 multi-turn questions distributed across 8 categories: writing, roleplay, reasoning, mathematics, coding, information extraction, STEM knowledge, and humanities. Each question involves two turns — an initial question and a challenging follow-up — and GPT-4 rates each model's responses on a 1–10 scale with detailed justifications.

The multi-turn design is critical because it tests capabilities that single-turn benchmarks miss entirely: maintaining context across turns, following up on prior instructions, correcting or refining earlier responses, and handling increasingly complex requests that build on initial answers. MT-Bench scores have become one of the most widely cited metrics for comparing chat-oriented LLMs, complementing traditional NLP benchmarks that focus on isolated task performance.
