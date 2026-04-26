---
tags: [chunk, llm]
id: "chunk-llm-079"
source: "[[LLM/_raw/raw-llm-020 Llama 3 Herd of Models]]"
source_loc: "Architecture details"
topic: "LLaMA 3 grouped-query attention"
claim: "LLaMA 3 used GQA (grouped-query attention) instead of MHA, reducing KV cache memory for efficient serving."
confidence: "verified"
supports: ["[[LLM/Inference and Serving/KV Cache and Context Reuse]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 3 GQA for Efficient Serving

## Context
Standard multi-head attention (MHA) uses separate key and value projections for each attention head. For a model with H attention heads, this means H sets of key-value pairs must be stored in the KV cache during inference. Grouped-query attention (GQA) reduces this by sharing key-value projections across groups of query heads. If 8 query heads share 1 KV head, the KV cache is 8× smaller than with MHA.

LLaMA 3 adopted GQA across all model sizes, using 8 KV heads for the 8B model and 8 KV heads for the 70B and 405B models (which have 32 and 128 query heads respectively). This dramatically reduced KV cache memory: the 405B model's KV cache is 16× smaller than it would be with standard MHA (8 KV heads instead of 128). The quality impact of GQA is minimal — the model achieves near-identical performance to MHA while enabling much larger batch sizes and longer context lengths during serving.

## Why It Matters
KV cache memory is the primary constraint on inference throughput and context length. By adopting GQA, LLaMA 3 made serving the 405B model practical on available hardware — without GQA, the KV cache alone for 128K context would exceed most GPU memory budgets. GQA has since become standard in all new LLM architectures, representing the consensus that the MHA-to-GQA trade-off is overwhelmingly worthwhile for serving efficiency.

## QnA Seeds
- Q: How does grouped-query attention (GQA) reduce KV cache memory compared to standard MHA?
  A: GQA shares key-value projections across groups of query heads. If G query heads share 1 KV head, the KV cache is G× smaller. LLaMA 3 405B uses 8 KV heads with 128 query heads, giving a 16× reduction in KV cache size compared to standard MHA.
- Q: Why is GQA's KV cache reduction critical for serving large models like LLaMA 3 405B?
  A: Without GQA, a 405B model with 128K context would require enormous KV cache memory (potentially exceeding available GPU RAM). The 16× reduction makes serving practical on available hardware, enables larger batch sizes for higher throughput, and allows longer context windows within memory budgets.
