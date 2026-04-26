---
tags: [raw, llm]
id: "raw-llm-058"
title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
author: "Asai et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2310.11511"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Self-RAG: Learning to Retrieve, Generate, and Critique

## What Is This?
A framework where an LLM learns to adaptively retrieve passages on demand, generate text, and self-critique its outputs using special reflection tokens — deciding when retrieval is needed and whether the generated text is supported by retrieved evidence.

## Why It Matters
Moved beyond fixed retrieve-then-generate pipelines to adaptive, self-reflective retrieval. The model learns its own retrieval policy and factuality checking, significantly reducing hallucination while maintaining generation fluency — a step toward self-correcting LLMs.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Reflection tokens: Retrieve, IsRel, IsSup, IsUse for self-critique during generation
- [ ] Adaptive retrieval: model decides when to retrieve vs. generate from parametric memory
- [ ] Hallucination reduction vs. standard RAG and no-retrieval baselines
