---
tags: [chunk, llm]
id: "chunk-llm-207"
source: "[[LLM/_raw/raw-llm-052 GPTQ Accurate Post-Training Quantization]]"
source_loc: "Chunk Candidates, Why It Matters"
topic: "GPTQ 3-4 bit accuracy results"
claim: "GPTQ achieves 4-bit quantization of OPT-175B and BLOOM-176B with negligible perplexity increase, and viable 3-bit quantization with modest degradation."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]"]
qna_seeds:
  - q: "What accuracy does GPTQ achieve at 4-bit quantization?"
    a: "On OPT-175B and BLOOM-176B, 4-bit GPTQ quantization increases perplexity by less than 0.5 points compared to FP16, while reducing model size by roughly 4× and enabling single-GPU inference."
  - q: "Is 3-bit GPTQ quantization practical?"
    a: "3-bit quantization shows modest perplexity degradation (1-2 points) that may be acceptable for latency-sensitive applications, though 4-bit remains the standard quality-size sweet spot."
up: "[[LLM/LLM]]"
---
# GPTQ Achieves Near-Lossless 4-Bit and Viable 3-Bit Quantization

GPTQ's Hessian-based approach enables 4-bit weight quantization of 175B+ parameter models with negligible accuracy loss. On OPT-175B and BLOOM-176B, 4-bit GPTQ increases perplexity by less than 0.5 points compared to FP16 baselines while reducing model size by approximately 4×. This compression enables a 175B model to fit on a single 80GB A100 GPU, transforming deployment economics.

At 3-bit quantization, GPTQ shows modest degradation of 1–2 perplexity points — still functional for many applications but below the quality bar for tasks requiring peak accuracy. The 4-bit sweet spot became the standard for open-source LLM deployment, with GPTQ-quantized models dominating HuggingFace model repositories and enabling consumer-grade GPU inference.
