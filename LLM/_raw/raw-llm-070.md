---
tags: [llm, raw]
source_type: technical_analysis
source_title: "Reasoning Distillation: From Frontier to Compact Models"
authors: [Various]
year: 2025
up: "[[Sources Index]]"
---

# Reasoning Distillation Techniques

## Summary

Reasoning distillation trains smaller models on the chain-of-thought reasoning traces of larger models, transferring reasoning capabilities to compact architectures. DeepSeek's R1 distillation is the most prominent example: starting from the R1 reasoning model, they produced variants from 70B down to 1.5B parameters. The distilled 14B model outperformed o1-mini on several benchmarks, and the 7B model outperformed Llama 3.1 70B on math reasoning. The technique works by fine-tuning on (problem, reasoning trace, answer) triples, suggesting reasoning is a learnable generation style that transfers across scales.

## Key Claims

1. Small models trained on reasoning traces can outperform much larger base models on reasoning tasks
2. Reasoning transfers as a generation style rather than as factual knowledge
3. DeepSeek's 7B distilled model outperforms Llama 3.1 70B on mathematical reasoning
4. The technique dramatically reduces inference cost while preserving reasoning quality
5. Synthetic reasoning trace generation from frontier models creates scalable training data

## Atomic Facts

1. DeepSeek distilled R1 into 1.5B, 7B, 8B, 14B, 32B, and 70B variants
2. 14B distilled model outperformed o1-mini on multiple benchmarks
3. 7B distilled model outperformed Llama 3.1 70B on math reasoning
4. Training data: (problem, reasoning trace, answer) triples from teacher model
5. o1-mini is likely an internal distillation of o1
6. Cost reduction: 10-100× cheaper inference than the teacher model

## Significance

Reasoning distillation makes advanced reasoning accessible on consumer hardware and at low cost, potentially the most impactful technique for democratising AI reasoning capabilities.

## Chunks Extracted

*Pending*