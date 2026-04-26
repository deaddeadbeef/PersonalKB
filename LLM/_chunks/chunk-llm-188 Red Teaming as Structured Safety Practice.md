---
tags: [chunk, llm]
id: "chunk-llm-188"
source: "[[LLM/_raw/raw-llm-047 Red Teaming Language Models to Reduce Harms]]"
source_loc: "Why It Matters"
topic: "Red teaming as safety discipline"
claim: "This paper established red teaming as a structured, repeatable safety evaluation practice for LLM deployment rather than ad hoc testing."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: How did this paper change LLM safety practices? A: It established red teaming as a structured discipline with taxonomies, scaling analysis, and reproducible methodologies, moving beyond ad hoc try-to-break-it testing."
  - "Q: What elements make red teaming structured? A: A harm taxonomy for coverage, consistent evaluation criteria, both automated and human testers, scaling analysis across model sizes, and documentation of attack success rates."
up: "[[LLM/LLM]]"
---

# Red Teaming as Structured Safety Practice

Before this work, LLM safety evaluation was largely ad hoc — developers would informally try to elicit harmful outputs without systematic methodology. Ganguli et al. established red teaming as a structured discipline with reproducible components: a harm taxonomy ensuring coverage, consistent evaluation criteria for scoring responses, both automated and human evaluation pipelines, and quantitative tracking of attack success rates across model sizes and alignment stages. This framework was adopted by major AI labs as a standard pre-deployment safety evaluation practice and influenced regulatory proposals for AI safety testing.
