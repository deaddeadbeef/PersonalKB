---
tags: [chunk, llm]
id: "chunk-llm-211"
source: "[[LLM/_raw/raw-llm-053 AWQ Activation-aware Weight Quantization]]"
source_loc: "Chunk Candidates"
topic: "AWQ INT4 edge deployment"
claim: "AWQ achieves INT4 quantization with speedups on edge devices while outperforming GPTQ and round-to-nearest on quality benchmarks."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]", "[[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]"]
qna_seeds:
  - q: "How does AWQ compare to GPTQ at INT4 quantization?"
    a: "AWQ achieves lower perplexity than GPTQ at the same 4-bit precision on LLaMA and OPT models, while being simpler and faster to run since it requires no iterative weight reconstruction."
  - q: "Is AWQ practical for on-device inference?"
    a: "Yes — AWQ's uniform INT4 format maps directly to efficient INT4 GPU kernels and has been demonstrated on edge devices with real-time inference speedups over FP16."
up: "[[LLM/LLM]]"
---
# AWQ Outperforms GPTQ at INT4 with Edge Device Speedups

In benchmark evaluations on LLaMA and OPT model families, AWQ achieves lower perplexity than both GPTQ and naive round-to-nearest (RTN) quantization at 4-bit precision. The improvement is especially pronounced on smaller models (7B–13B) where each weight matters more, and on challenging benchmarks where the 1% salient channels carry critical knowledge.

AWQ's uniform INT4 format is particularly advantageous for on-device and edge deployment because it maps directly to efficient INT4 GEMM kernels without requiring mixed-precision hardware support. Combined with its simplicity — no backpropagation, no iterative reconstruction, just a calibration pass and analytical scaling — AWQ has become a preferred quantization method for mobile and embedded LLM deployment.
