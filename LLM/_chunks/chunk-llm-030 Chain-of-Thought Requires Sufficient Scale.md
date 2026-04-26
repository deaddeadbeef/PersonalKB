---
tags: [chunk, llm]
id: "chunk-llm-030"
source: "[[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting]]"
source_loc: "Section 3.2, Figures 2-3"
topic: "scale dependence"
claim: "Chain-of-thought prompting only provides gains at sufficient model scale (originally observed at ~100B+ parameters)"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Chain-of-Thought Prompting]]"]
up: "[[LLM/LLM]]"
---

# Chain-of-Thought Requires Sufficient Scale

## Context

A critical finding from Wei et al. was that CoT prompting exhibits a strong scale dependence. When evaluated across models of different sizes (from 422M to 540B parameters), CoT provided no benefit — and sometimes hurt performance — on models below approximately 100B parameters. At and above this threshold, CoT dramatically improved accuracy on reasoning benchmarks. Below this threshold, the model-generated reasoning chains were often incoherent or logically flawed, leading to worse final answers than direct prediction.

The scale dependence appears related to the model's ability to generate faithful, logically coherent intermediate reasoning steps. Smaller models lack the capacity to maintain consistency across a multi-step reasoning chain — they may get individual steps right but fail to propagate information correctly between steps. This creates an apparent "emergence" of reasoning ability at scale, though subsequent analysis suggests this may be a gradual improvement that crosses a visibility threshold rather than a true phase transition.

## Why It Matters

The scale dependence of CoT has important practical implications: applying CoT prompting to small models (under ~10B parameters) is typically wasteful or counterproductive. It also contributed to the debate about "emergent capabilities" in LLMs — whether certain capabilities truly appear suddenly at scale or merely cross an accuracy threshold that makes them visible. Understanding this scale dependence is essential for choosing appropriate prompting strategies for different model sizes.

## QnA Seeds
- Q: Why does CoT hurt performance on small models?
  A: Small models generate unreliable intermediate reasoning steps — they may produce plausible-looking but logically incorrect chains. Since the final answer depends on the reasoning chain, bad intermediate steps lead to worse answers than if the model had simply guessed directly. The additional output also means more opportunities for the model to go off track. In effect, CoT amplifies the model's errors rather than structuring its reasoning.
- Q: Has the scale threshold for effective CoT changed since the original paper?
  A: Yes. Improved training techniques, better data, and instruction tuning have lowered the effective threshold. Models like LLaMA-2 70B and Mistral-7B (with instruction tuning) can benefit from CoT, whereas the original threshold was ~100B+ for base models. The threshold depends not just on parameter count but on training quality, alignment, and the specific reasoning task. For simpler reasoning, even 7B models can benefit from CoT.
