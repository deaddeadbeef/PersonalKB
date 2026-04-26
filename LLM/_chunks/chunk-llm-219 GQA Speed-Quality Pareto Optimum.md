---
tags: [chunk, llm]
id: "chunk-llm-219"
source: "[[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]"
source_loc: "Chunk Candidates"
topic: "GQA speed-quality Pareto curve"
claim: "GQA achieves near-MHA accuracy with near-MQA inference throughput, occupying the Pareto-optimal point on the speed-quality tradeoff curve."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]", "[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]"]
qna_seeds:
  - q: "Where does GQA sit on the speed-quality Pareto curve?"
    a: "GQA with 8 KV groups achieves quality within 0.5% of MHA while reaching inference throughput within 10-15% of MQA, making it Pareto-optimal for most production use cases."
  - q: "Why is GQA preferred over MQA in modern models?"
    a: "MQA's extreme KV sharing (G=1) causes noticeable quality degradation at large scale, while GQA with moderate G recovers nearly all MHA quality with most of MQA's speed benefit."
up: "[[LLM/LLM]]"
---
# GQA Occupies the Speed-Quality Pareto Optimum

Empirical evaluation shows that GQA with a moderate number of KV groups (e.g., 8) achieves quality within 0.5% of full Multi-Head Attention while reaching inference throughput within 10–15% of Multi-Query Attention. This Pareto-optimal positioning makes GQA strictly preferable to both extremes for most production deployments where both quality and speed matter.

MQA's extreme sharing (G=1) causes measurable quality degradation that becomes increasingly problematic at larger model scales and on harder tasks. GQA avoids this by preserving enough key-value diversity for the model to maintain rich attention patterns. The result is that GQA has become the default attention configuration for virtually all modern large language models — including LLaMA 2 70B, Mistral 7B, Mixtral, and LLaMA 3 — displacing both MHA and MQA.
