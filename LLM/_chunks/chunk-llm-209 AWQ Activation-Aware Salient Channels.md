---
tags: [chunk, llm]
id: "chunk-llm-209"
source: "[[LLM/_raw/raw-llm-053 AWQ Activation-aware Weight Quantization]]"
source_loc: "What Is This, Chunk Candidates"
topic: "AWQ activation-aware salient channels"
claim: "AWQ identifies the 1% of weight channels most critical for model quality by observing activation magnitudes rather than weight magnitudes."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Quantization]]"]
qna_seeds:
  - q: "How does AWQ identify salient weight channels?"
    a: "By observing the magnitude of activations flowing through each channel on a calibration set — channels with large activation magnitudes are disproportionately important for output quality, even if the weights themselves are small."
  - q: "Why use activation magnitudes instead of weight magnitudes?"
    a: "Weight magnitude alone is misleading because a small weight multiplied by a large activation has more impact on the output than a large weight multiplied by a near-zero activation. Activation-aware selection captures true importance."
up: "[[LLM/LLM]]"
---
# AWQ Identifies Salient Channels via Activation Magnitudes

AWQ's core insight is that approximately 1% of weight channels are disproportionately important for model quality, and these channels can be identified by observing activation magnitudes rather than weight magnitudes. On a small calibration dataset, AWQ measures which channels consistently carry large activation values — these are the channels where quantization error would cause the most output degradation.

This activation-aware approach is more accurate than weight-magnitude-based saliency because the impact of a quantization error depends on both the weight value and the activation it multiplies. A channel with moderate weights but consistently large activations contributes more to the output than a channel with large weights that rarely activates. This insight allows AWQ to protect exactly the channels that matter most.
