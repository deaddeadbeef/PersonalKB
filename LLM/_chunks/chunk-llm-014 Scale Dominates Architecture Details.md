---
tags: [chunk, llm]
id: "chunk-llm-014"
source: "[[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models]]"
source_loc: "Section 4"
topic: "scaling laws"
claim: "Model performance is largely determined by scale (compute, data, parameters) rather than architectural details like depth vs width ratio"
confidence: "verified"
supports: ["[[LLM/Pretraining/Scaling Laws]]"]
up: "[[LLM/LLM]]"
---

# Scale Dominates Architecture Details

## Context

A surprising finding from Kaplan et al. was that model performance is overwhelmingly determined by the total parameter count, dataset size, and compute budget — not by architectural choices like the ratio of depth (number of layers) to width (hidden dimension), number of attention heads, or feed-forward network size. Models with the same parameter count but very different depth/width ratios achieved nearly identical loss values.

This held across a wide range of configurations tested: varying depth from 2 to 80+ layers, changing head counts, and adjusting the FFN hidden dimension ratio. As long as the total parameter count remained constant and the model was not pathologically narrow or shallow, the specific architectural choices had minimal impact on final loss. This finding was somewhat counterintuitive — researchers had spent years optimizing architecture details that turned out to matter far less than simply making the model bigger.

## Why It Matters

This insight dramatically simplified the design space for large language models. Rather than extensive architecture search, teams could focus on scaling up standard designs. It justified the "just make it bigger" approach and implied that the Transformer architecture has significant absorptive capacity — its performance ceiling is determined by scale, not by fine-grained structural decisions. However, later work showed architecture does matter for efficiency (inference speed, memory) even if not for raw loss.

## QnA Seeds
- Q: Does "architecture doesn't matter" mean all Transformer configurations are equal?
  A: Not quite. The finding is that for a fixed parameter budget, most reasonable depth/width configurations achieve similar loss. Extremely shallow or narrow models are exceptions. Also, architecture still matters enormously for practical considerations like inference speed, memory footprint, and parallelizability — a wide shallow model trains differently on GPU clusters than a deep narrow one, even if both converge to similar loss.
- Q: Has the "scale over architecture" finding held up in subsequent research?
  A: Partially. The core insight that scale is the dominant factor for training loss has been confirmed repeatedly. However, research into efficient architectures (MoE, state-space models, linear attention) shows that architecture can improve the compute-efficiency of reaching a given loss. So while a standard Transformer scales predictably, better architectures can shift the scaling curve to achieve the same loss with less compute.
