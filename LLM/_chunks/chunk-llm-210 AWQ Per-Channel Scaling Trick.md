---
tags: [chunk, llm]
id: "chunk-llm-210"
source: "[[LLM/_raw/raw-llm-053 AWQ Activation-aware Weight Quantization]]"
source_loc: "Chunk Candidates"
topic: "AWQ per-channel scaling"
claim: "AWQ protects salient weight channels by applying per-channel scaling factors before uniform quantization, preserving quality without mixed-precision hardware."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]"]
qna_seeds:
  - q: "How does AWQ protect important weight channels during quantization?"
    a: "It multiplies salient channels by a scaling factor before quantization (enlarging them so they survive rounding) and divides the corresponding activations by the same factor to preserve mathematical equivalence — no mixed-precision support required."
  - q: "Why is the scaling trick preferable to keeping salient weights in higher precision?"
    a: "Mixed-precision (e.g., keeping 1% of weights in FP16) requires hardware support for mixed formats and complicates kernels, while per-channel scaling keeps all weights in uniform INT4 format, enabling simple and fast GPU kernels."
up: "[[LLM/LLM]]"
---
# AWQ Uses Per-Channel Scaling to Protect Salient Weights

Rather than keeping important weights in higher precision (which requires mixed-precision hardware support), AWQ applies a mathematically equivalent per-channel scaling trick. Salient channels are multiplied by a scaling factor s > 1 before quantization, which enlarges these weights relative to the quantization grid and reduces their rounding error. The corresponding input activations are divided by s to maintain mathematical equivalence.

This approach keeps all weights in uniform INT4 format, avoiding the complexity of mixed-precision kernels while achieving the quality benefits of protecting important channels. The scaling factors are computed analytically from the calibration data and require no backpropagation or iterative optimization, making AWQ faster and simpler than methods requiring gradient-based reconstruction.
