---
tags: [chunk, llm]
id: "chunk-llm-206"
source: "[[LLM/_raw/raw-llm-052 GPTQ Accurate Post-Training Quantization]]"
source_loc: "Chunk Candidates"
topic: "GPTQ lazy batch updates speed"
claim: "GPTQ processes weights in blocks with lazy batch Hessian updates, reducing quantization time for a 175B model to approximately 4 GPU-hours."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]"]
qna_seeds:
  - q: "How does GPTQ achieve fast quantization of very large models?"
    a: "Instead of updating the Hessian after every single weight, GPTQ processes weights in blocks of 128 columns with lazy batch updates, amortizing the cost and reducing quantization of OPT-175B from impractical to approximately 4 GPU-hours."
  - q: "Why is layer-wise processing important for GPTQ's scalability?"
    a: "By quantizing one layer at a time and only requiring a calibration dataset to compute per-layer Hessians, GPTQ avoids the memory overhead of whole-model optimization and scales linearly with model depth."
up: "[[LLM/LLM]]"
---
# GPTQ Uses Lazy Batch Updates for Speed

GPTQ achieves practical quantization speed by processing weights in blocks of 128 columns with lazy batch Hessian updates rather than recomputing after each individual weight. This batching strategy amortizes the cost of Hessian inverse updates and reduces the quantization time for OPT-175B to approximately 4 GPU-hours on a single A100 — making post-training quantization feasible as a routine deployment step.

Layer-wise processing is equally important: GPTQ quantizes each transformer layer independently using a small calibration dataset (typically 128 sequences) to estimate the per-layer Hessian. This avoids the prohibitive memory cost of whole-model optimization and allows the algorithm to scale linearly with model depth, making it applicable to models of arbitrary size.
