---
tags: [raw, llm]
id: "raw-llm-025"
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
author: "Yao et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2210.03629"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# ReAct: Synergizing Reasoning and Acting in Language Models

## What Is This?
A prompting framework that interleaves chain-of-thought reasoning traces ("Thought") with environment actions ("Act") and observations ("Obs"), allowing LLMs to reason about and interact with external tools.

## Why It Matters
ReAct established the foundational Thought → Act → Observe loop used by virtually all modern LLM agent frameworks (LangChain, AutoGPT, etc.) and showed that combining reasoning with grounded actions reduces hallucination.

## Key Takeaways
1. Interleaved Thought-Act-Obs traces let the model plan, execute, and update beliefs in a single generation loop
2. Outperforms chain-of-thought alone on knowledge-intensive tasks by grounding reasoning in retrieved facts
3. Outperforms act-only agents by maintaining explicit reasoning traces that improve planning
4. Demonstrated on HotpotQA (multi-hop QA) and ALFWorld (interactive decision making)

## Chunk Candidates
- [ ] ReAct prompting format: Thought → Action → Observation loop
- [ ] Comparison with chain-of-thought-only and action-only baselines
- [ ] Integration with external tools (search APIs, environments)
- [ ] Influence on modern agent architectures (LangChain, AutoGPT)
