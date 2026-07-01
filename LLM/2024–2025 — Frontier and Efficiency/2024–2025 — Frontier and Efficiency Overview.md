---
tags: [llm, era-hub]
up: "[[LLM]]"
confidence: established
freshness: current-sensitive
tier-coverage: [intuition, core, deep-dive]
---
# 2024–2025 — Frontier and Efficiency

Pushing the frontier on two axes — maximum capability (multimodal, agents, million-token context) and maximum efficiency (serving, inference, architecture alternatives). The field matures from research prototypes to production systems processing billions of requests daily, and the tension between capability and cost drives innovation at every layer of the stack.

## Beyond Attention

State space models challenge the transformer's dominance. Mamba (Gu & Dao, December 2023) introduced a selective state space mechanism with input-dependent gating, achieving transformer-competitive language modeling quality with linear-time sequence processing. Mamba-2 refined the approach, and hybrid architectures (Jamba, StripedHyena) combined SSM layers with attention layers to get the best of both worlds — linear-time long-sequence processing with the in-context learning strength of attention. Whether SSMs can fully replace attention at frontier scale remains an open question. See [[State Space Models and Mamba]] and [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]].

## The Long-Context Revolution

Context windows expanded from 4K tokens (GPT-3.5) to 128K (GPT-4 Turbo), 200K (Claude 3), and 1M+ tokens (Gemini 1.5 Pro). Techniques enabling this include RoPE scaling (NTK-aware interpolation, YaRN), ring attention for distributed long-context training, and architectural improvements that reduce the quadratic cost of full attention. Long context enables processing entire codebases, books, and document collections in a single call, partially substituting for traditional RAG retrieval. However, "lost in the middle" effects and degraded attention at extreme lengths remain active challenges. See [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]].

## Inference at Scale

The economics of serving LLMs drove a wave of inference optimization. KV cache management became critical — PagedAttention (vLLM, Kwon et al., 2023) applied virtual memory concepts to eliminate memory waste from fragmented KV caches. Speculative decoding (Leviathan et al., Chen et al.) used small draft models to propose token sequences verified in parallel by the large model, achieving 2–3× speedups without quality loss. Quantization (GPTQ, AWQ, GGUF) reduced memory footprint, enabling consumer-hardware deployment. See [[KV Cache and Context Reuse]] and [[Speculative Decoding]].

## Production Serving

Serving systems evolved to handle millions of concurrent users. Continuous batching (Orca, Yu et al., 2022) replaced static batching by dynamically inserting and retiring requests, dramatically improving GPU utilization. Disaggregated serving separated prefill (compute-bound) from decode (memory-bandwidth-bound) phases onto different hardware. Frameworks like vLLM, TensorRT-LLM, and SGLang provided production-ready serving with SLA-aware scheduling. The throughput-latency tradeoff — maximizing tokens/second while meeting time-to-first-token guarantees — became the central systems challenge. See [[Batching and Continuous Batching]] and [[Serving Architectures and Throughput-Latency Trade-offs]].

## Autonomous Agents

Agents evolved from single-tool-call patterns to persistent, autonomous systems. Multi-agent frameworks (AutoGen, CrewAI, LangGraph) orchestrated teams of specialized LLM agents that communicate, delegate, and collaborate. Code generation agents (Devin, SWE-Agent, Copilot Workspace) demonstrated end-to-end software engineering — reading codebases, writing code, running tests, and iterating on failures. Memory and state management — maintaining context across extended interactions via external memory stores, summarization, and retrieval — became essential for agent reliability. See [[Multi-Agent Systems]], [[Code Generation Agents]], and [[Memory and State Management]].

## Frontier Multimodal

Models became natively multimodal. GPT-4o (May 2024) processed text, images, and audio in a single model with near-real-time voice interaction. Gemini 1.5 Pro natively handled text, images, video, and audio with a 1M-token context. Speech-language models integrated ASR and TTS into the language model pipeline rather than using cascaded systems. Document understanding models (combining OCR with language reasoning) enabled processing of forms, invoices, and UI screenshots. See [[Speech-Language Models]], [[Video Understanding Models]], and [[OCR Documents and UI Understanding]].

## Multimodal Safety

Multimodal capabilities introduced new attack surfaces. Adversarial images could hijack model behavior, and cross-modal prompt injection (embedding instructions in images) proved difficult to defend against. Evaluating multimodal safety required new benchmarks covering visual question-answering hallucination, harmful image generation, and cross-modal consistency. The safety evaluation infrastructure that existed for text-only models needed significant extension. See [[Multimodal Evaluation and Safety]].

## Agentic Evaluation

Traditional benchmarks proved inadequate for evaluating agents and code generation systems. SWE-bench (Jimenez et al.) evaluated models on real GitHub issues, measuring their ability to produce correct patches. HumanEval and MBPP measured code generation accuracy. Agentic benchmarks needed to assess multi-step planning, tool selection, error recovery, and end-to-end task completion — capabilities poorly captured by single-turn QA metrics. See [[Code and Agentic Benchmarks]].

## What's Next

The frontier is expanding along multiple axes simultaneously: reasoning models (OpenAI o1, o3) that "think" before responding, synthetic data generation replacing human annotation, test-time compute scaling as a complement to training-time scaling, and increasingly autonomous agents operating in real-world environments. The tension between scaling capability and making it affordable and safe will continue to drive the field's evolution.

## Pages in This Era

- [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]]
- [[State Space Models and Mamba]]
- [[KV Cache and Context Reuse]]
- [[Speculative Decoding]]
- [[Batching and Continuous Batching]]
- [[Serving Architectures and Throughput-Latency Trade-offs]]
- [[Multi-Agent Systems]]
- [[Code Generation Agents]]
- [[Memory and State Management]]
- [[Speech-Language Models]]
- [[Video Understanding Models]]
- [[OCR Documents and UI Understanding]]
- [[Multimodal Evaluation and Safety]]
- [[Code and Agentic Benchmarks]]

## Related Eras

← Previous: [[2023 — Open Models and Agents Overview|2023 — Open Models and Agents]]
→ Next: [[2026 — Reasoning and Agents Overview|2026 — Reasoning and Agents]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Corpus Index]]
- [[LLM/LLM Book Reading Spine]]
