---
tags: [chunk, llm]
id: "chunk-llm-031"
source: "[[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting]]"
source_loc: "Section 5"
topic: "self-consistency"
claim: "Self-consistency (sample multiple reasoning chains, majority-vote on the final answer) further improves CoT accuracy"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Chain-of-Thought Prompting]]"]
up: "[[LLM/LLM]]"
---

# Self-Consistency Improves Chain-of-Thought

## Context

Self-consistency (Wang et al., 2022) is a decoding strategy that enhances CoT prompting. Instead of greedily generating a single reasoning chain, you sample multiple chains (typically 5–40) from the model using temperature sampling, extract the final answer from each chain, and return the most common answer (majority vote). Different reasoning paths may make errors at different steps, but if the correct reasoning is more likely than any single incorrect path, the majority vote converges on the right answer.

For example, on a math problem, the model might generate 20 different reasoning chains. 15 of them arrive at "42" through various correct (and some partially incorrect) reasoning paths, while the remaining 5 arrive at different wrong answers. The majority vote correctly selects "42." This works because the model's distribution over reasoning paths is calibrated enough that correct chains are collectively more probable than any individual incorrect chain.

## Why It Matters

Self-consistency consistently improves CoT accuracy by 5–20% across reasoning benchmarks with no changes to the model or prompt template — only the decoding strategy changes. It demonstrates that LLMs already "know" the right answer with high probability but may not surface it on any single sample. This insight influenced the development of best-of-N sampling, reward model-guided search, and more sophisticated reasoning strategies like tree-of-thought.

## QnA Seeds
- Q: Why does majority voting work when individual reasoning chains may be wrong?
  A: Errors in reasoning chains tend to be diverse — different chains fail in different ways, producing different wrong answers. But correct reasoning paths, while they may differ in wording or intermediate steps, converge on the same final answer. With enough samples, the correct answer accumulates more votes than any single incorrect answer. This is essentially a wisdom-of-crowds effect applied to the model's own reasoning distribution.
- Q: What are the computational trade-offs of self-consistency?
  A: Self-consistency requires generating N complete reasoning chains, multiplying inference cost by N. With N=20, you use 20× the compute of a single greedy chain. For latency-sensitive applications, this can be prohibitive. The benefit also shows diminishing returns — going from 5 to 10 samples helps more than going from 20 to 40. In practice, N=5–10 provides most of the benefit at acceptable cost for batch evaluation.
