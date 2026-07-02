---
tags: [llm, raw]
source_type: survey_pdf
source_title: "The Hitchhiker's Guide to Agentic AI: From Foundations to Systems"
authors: [Haggai Roitman]
year: 2026
version: "1.2.2"
arxiv: "2606.24937v1"
doi: "https://doi.org/10.48550/arXiv.2606.24937"
external_url: "https://arxiv.org/abs/2606.24937v1"
license: "CC BY-SA 4.0"
local_pdf: 'C:\Users\fpan1\OneDrive\2606.24937v1.pdf'
pdf_pages: 603
up: "[[Sources Index]]"
---

# The Hitchhiker's Guide to Agentic AI

## Summary

Haggai Roitman's 2026 survey frames agentic AI as a full-stack subject, not as a standalone prompt pattern. The guide moves from transformers and optimization, through systems foundations, post-training and reinforcement learning, reasoning models, evaluation, and finally agentic systems such as RAG, memory, harnesses, MCP, skills, multi-agent systems, and agent UIs.

The most useful contribution for this vault is its progressive teaching order: first make the model pipeline visible, then add training and systems constraints, then post-training and reasoning, then evaluation, and only then move into agent loops, harnesses, protocols, and production concerns. This is the right shape for an LLM wiki because it prevents the reader from treating agents, tools, and MCP as isolated product features.

## Key Claims

1. Building modern AI systems requires understanding the whole pipeline from transformer internals through deployment architecture, not just one layer.
2. A usable LLM curriculum should reveal the stack in order: architecture, efficient training, adaptation, compression, scaling, inference acceleration, post-training, reasoning, evaluation, and agentic systems.
3. RL for language models now has two major modes: preference alignment, such as RLHF and DPO, and capability improvement through verifiable rewards, especially for reasoning.
4. Evaluation is a central engineering discipline because LLM outputs are open-ended, quality is multidimensional, and the evaluator may itself be another language model.
5. Agentic AI changes the unit of engineering from a single model call to an observation-reason-action loop with memory, grounding, action interfaces, coordination, and safety constraints.
6. A robust agent harness separates reasoning, execution, memory, communication, and observability so the model can act without turning tool execution and state management into prompt sprawl.
7. MCP is presented as a protocol answer to the tool-integration explosion: without a standard, agent-framework-to-tool integrations scale as N*M; with a shared protocol, they scale closer to N+M.

## Useful Structure For This Vault

| Guide part | Vault use |
|---|---|
| Foundations | Make [[LLM/Study/LLM Progressive Systems Route]] start with tokens, embeddings, attention, logits, and the autoregressive loop. |
| Systems foundations | Keep training infrastructure, serving, batching, KV cache, and deployment notes before local operations. |
| RL methods | Tie SFT, RLHF, DPO, reward models, and reasoning RL into one post-training map. |
| Reasoning | Connect test-time compute, verifiable rewards, distillation, and local reasoning-budget experiments. |
| Evaluation | Require evaluation pages before accepting local model, RAG, tool, or agent claims. |
| Agentic AI | Reveal RAG, memory, harness, MCP, skills, multi-agent systems, and UI frameworks after the reader can explain the model and evaluation layers. |
| Assessment | End with oral defense, claim ledgers, and capstone proof instead of passive reading. |

## Page Evidence

- Page 1 identifies the title, author, arXiv id, date, and version.
- Page 24 states that the work is an independent educational survey, based on public sources, released under CC BY-SA 4.0, and that readers should verify claims before production use.
- Page 30 frames the guide as a first-principles-to-production-systems path and states that great AI systems require understanding the whole pipeline.
- Page 35 opens Chapter 1 by ordering architecture and optimization as a curriculum and presents the text -> tokens -> representations -> tokens -> text pipeline.
- Page 133 splits RL for language models into preference alignment and verifiable-reward capability enhancement.
- Page 251 frames reasoning RL around sparse rewards, long horizons, combinatorial search, and verifiability.
- Page 274 explains why LLM evaluation is hard: unbounded outputs, multidimensional quality, and evaluation as a language task.
- Page 292 defines agentic AI as an LLM loop over observations, reasoning, actions, and iteration, with persistence, grounding, action, coordination, and safety challenges.
- Page 343 defines the agent harness as runtime infrastructure that wraps a stateless model into a stateful, goal-directed agent.
- Page 392 presents MCP as a standard protocol that reduces custom agent-tool integrations from N*M to N+M.
- Page 513 starts the assessment section with questions that progress from foundations through algorithms, systems, and agentic AI.

## Chunks Extracted

- [[LLM/_chunks/chunk-llm-261 Agentic AI requires a full-stack first-principles-to-production curriculum|chunk-llm-261]]
- [[LLM/_chunks/chunk-llm-262 LLM foundations start with text to tokens to representations to logits|chunk-llm-262]]
- [[LLM/_chunks/chunk-llm-263 RL for LLMs splits into preference alignment and verifiable reward capability learning|chunk-llm-263]]
- [[LLM/_chunks/chunk-llm-264 Reasoning RL treats multi-step reasoning as verifiable search under sparse rewards|chunk-llm-264]]
- [[LLM/_chunks/chunk-llm-265 LLM evaluation must handle open-ended multidimensional language outputs|chunk-llm-265]]
- [[LLM/_chunks/chunk-llm-266 Agentic AI is an observation reason action loop with memory grounding action and safety|chunk-llm-266]]
- [[LLM/_chunks/chunk-llm-267 Agent harness design separates reasoning execution memory communication and observability|chunk-llm-267]]
- [[LLM/_chunks/chunk-llm-268 Agentic AI learning should end in self-assessment and proof artifacts|chunk-llm-268]]

## References

- Local PDF: `C:\Users\fpan1\OneDrive\2606.24937v1.pdf`
- [arXiv abstract](https://arxiv.org/abs/2606.24937v1)
- [DOI](https://doi.org/10.48550/arXiv.2606.24937)
- [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
