---
tags: [chunk, llm]
id: "chunk-llm-174"
source: "[[LLM/_raw/raw-llm-044 The Pile An 800GB Dataset]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "Pre-training data diversity"
claim: "Training on the diverse Pile dataset improved downstream task performance compared to training on an equivalent volume of web-only text, demonstrating that data diversity matters as much as sheer scale."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
qna_seeds:
  - "Q: Does data diversity improve LLM performance beyond just scale? A: Yes — models trained on The Pile (22 diverse sources) outperformed models trained on equivalent-size web-only corpora on a broad set of downstream benchmarks."
  - "Q: Why does domain diversity help pre-training? A: Different domains expose the model to different vocabulary, reasoning patterns, and knowledge, reducing the narrow distribution bias of web-only crawls."
up: "[[LLM/LLM]]"
---

# Data Diversity Matters as Much as Volume

Gao et al. demonstrated that domain diversity in pre-training data has an impact comparable to simply increasing data volume. Models trained on The Pile outperformed models trained on equivalent-size web-only corpora (e.g., pure Common Crawl) across a range of downstream tasks. The inclusion of academic papers improved reasoning benchmarks, code improved structured generation, and books improved long-range coherence. This finding shaped subsequent dataset curation efforts (RedPajama, Dolma, FineWeb), all of which emphasize multi-domain composition over single-source scale.
