---
tags: [chunk, llm]
id: "chunk-llm-006"
source: "[[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]"
source_loc: "Section 1, Figures 1.2–1.3"
topic: "scaling laws"
claim: "Performance on downstream tasks scales smoothly as a power law with model size"
confidence: "verified"
supports: ["[[LLM/Pretraining/Scaling Laws]]"]
up: "[[LLM/LLM]]"
---

# Power-Law Scaling of Task Performance

## Context

The GPT-3 paper systematically evaluated models ranging from 125M to 175B parameters across a diverse set of NLP benchmarks. A consistent finding was that task performance improved smoothly and predictably as a function of model size, often following power-law relationships when plotted on log-log scales. There were no sharp discontinuities — larger models simply performed better across the board.

This smooth scaling held across dramatically different tasks: language modeling perplexity, reading comprehension, translation quality, arithmetic accuracy, and commonsense reasoning. The regularity of these improvements suggested that scaling was not just adding capacity for memorization but genuinely improving the model's ability to generalize.

## Why It Matters

The demonstration that performance scales predictably with size provided empirical justification for the massive investments in training ever-larger models. It transformed LLM development from a research experiment into an engineering problem: if you can predict what a 10× larger model will achieve, you can make informed investment decisions. This insight drove the scaling race from GPT-3 through PaLM, Chinchilla, and beyond.

## QnA Seeds
- Q: What does it mean that LLM performance follows a power law with model size?
  A: It means that when you plot task accuracy (or loss) against parameter count on a log-log scale, you get an approximately straight line. Performance improves by a predictable amount for each order-of-magnitude increase in model size. This relationship held across most tasks evaluated in GPT-3, though the slope (how much improvement per scale increase) varied by task.
- Q: Were there any tasks where GPT-3's scaling behavior broke down?
  A: Some tasks showed near-random performance across all model sizes, suggesting they required capabilities that even 175B parameters couldn't provide. Other tasks showed what appeared to be "emergent" behavior — near-random performance at smaller scales followed by sharp improvement at larger scales — though later analysis debated whether this was a genuine phase transition or an artifact of evaluation metrics.
