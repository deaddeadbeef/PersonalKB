---
tags: [chunk, llm]
id: "chunk-llm-205"
source: "[[LLM/_raw/raw-llm-052 GPTQ Accurate Post-Training Quantization]]"
source_loc: "What Is This, Chunk Candidates"
topic: "GPTQ OBQ hessian weight rounding"
claim: "GPTQ uses approximate Hessian inverse information to optimally round weights during quantization, minimizing the layer-wise reconstruction error."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]"]
qna_seeds:
  - q: "How does GPTQ decide how to round weights during quantization?"
    a: "It uses the inverse Hessian of the layer-wise reconstruction loss to determine the optimal rounding direction for each weight, compensating for quantization error by adjusting remaining unquantized weights in the same row."
  - q: "What is the connection between GPTQ and Optimal Brain Quantization?"
    a: "GPTQ extends the OBQ framework by making it computationally tractable for billion-parameter models through lazy batch updates and a fixed quantization order, reducing the cubic cost of the original algorithm."
up: "[[LLM/LLM]]"
---
# GPTQ Uses Hessian-Based Optimal Weight Rounding

GPTQ is a one-shot post-training quantization method rooted in the Optimal Brain Quantization (OBQ) framework. For each weight being quantized, it computes the quantization error and uses the inverse Hessian of the layer-wise reconstruction loss to optimally update the remaining unquantized weights, compensating for the rounding error. This second-order information allows GPTQ to make far better rounding decisions than naive round-to-nearest (RTN) approaches.

The key insight is that weights are not independent — quantizing one weight changes the optimal values of others. By using Hessian information to propagate error corrections, GPTQ achieves near-lossless 4-bit quantization even for 175B-parameter models, with perplexity increases typically under 0.5 points compared to FP16 baselines.
