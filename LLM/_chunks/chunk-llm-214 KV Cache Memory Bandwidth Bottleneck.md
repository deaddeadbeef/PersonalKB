---
tags: [chunk, llm]
id: "chunk-llm-214"
source: "[[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA]]"
source_loc: "Chunk Candidates, Why It Matters"
topic: "KV cache memory bandwidth bottleneck"
claim: "Autoregressive Transformer decoding is bottlenecked by memory bandwidth for loading the KV cache, not by arithmetic computation."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]", "[[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]"]
qna_seeds:
  - q: "Why is autoregressive decoding memory-bandwidth-bound?"
    a: "Each token generation requires loading the entire KV cache from GPU memory to compute attention, but the arithmetic per loaded byte is very low (only one query vector), making memory read speed the bottleneck rather than FLOPS."
  - q: "How does Shazeer quantify the bandwidth bottleneck?"
    a: "During incremental decoding of a single sequence, the ratio of memory operations to arithmetic operations is extremely unfavorable — the GPU spends most of its time waiting for KV cache data to arrive from HBM rather than computing."
up: "[[LLM/LLM]]"
---
# KV Cache Memory Bandwidth Is the Decoding Bottleneck

Shazeer's key observation is that autoregressive Transformer decoding is fundamentally bottlenecked by memory bandwidth, not arithmetic compute. During token-by-token generation, each step requires loading the full KV cache from GPU high-bandwidth memory (HBM) to compute attention scores for a single new query vector. The arithmetic intensity — FLOPs per byte loaded — is extremely low, meaning the GPU's compute units sit idle waiting for data to arrive from memory.

This memory-bandwidth bottleneck explains why larger batch sizes improve GPU utilization during inference (more queries amortize the cost of loading the same KV cache) and why reducing KV cache size translates directly to faster decoding. MQA addresses this by shrinking the KV cache by a factor of H, proportionally reducing the memory bandwidth required per decoding step and enabling the GPU to approach its arithmetic throughput ceiling.
