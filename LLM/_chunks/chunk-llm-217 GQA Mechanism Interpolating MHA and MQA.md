---
tags: [chunk, llm]
id: "chunk-llm-217"
source: "[[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]"
source_loc: "What Is This, Chunk Candidates"
topic: "GQA mechanism"
claim: "Grouped-Query Attention assigns G groups of key-value heads shared among H query heads, interpolating between MHA (G=H) and MQA (G=1)."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]", "[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]"]
qna_seeds:
  - q: "How does GQA generalize MHA and MQA?"
    a: "GQA uses G key-value head groups where each group is shared among H/G query heads. When G equals H it reduces to MHA; when G equals 1 it reduces to MQA. Intermediate values of G provide a tunable quality-speed tradeoff."
  - q: "What is a typical GQA configuration in practice?"
    a: "LLaMA 2 70B uses 8 KV heads with 64 query heads (G=8), reducing the KV cache by 8× compared to MHA while retaining near-MHA quality."
up: "[[LLM/LLM]]"
---
# GQA Interpolates Between Multi-Head and Multi-Query Attention

Grouped-Query Attention (GQA) introduces G key-value head groups, where each group's keys and values are shared among H/G query heads. This creates a continuous spectrum between standard Multi-Head Attention (G = H, every head has unique KV) and Multi-Query Attention (G = 1, all heads share one KV). Intermediate values of G allow architects to precisely tune the tradeoff between model quality and inference speed.

For example, LLaMA 2 70B uses 8 KV head groups with 64 query heads, reducing the KV cache by 8× compared to full MHA. This is less aggressive than MQA's 64× reduction but preserves more representational capacity in the key-value space. The GQA configuration has become the default for modern large language models because it occupies the Pareto-optimal point: near-MHA quality with near-MQA inference speed.
