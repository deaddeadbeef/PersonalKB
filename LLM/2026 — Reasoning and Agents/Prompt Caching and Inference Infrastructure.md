---
tags: [llm, reasoning-agents]
up: "[[2026 — Reasoning and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Prompt Caching and Inference Infrastructure

> **One-line summary** Prompt caching stores processed prefixes to avoid recomputation on repeated prompts, reducing latency and cost for agentic and conversational workloads by 50–90%.

## 🎯 Intuition

### Core Idea

Many LLM requests repeat the same beginning: system prompts, conversation history, or large shared documents. Recomputing those tokens every time is wasteful, so prompt caching stores the processed prefix and reuses it.

### Analogy

Prompt caching is like keeping your bookmark in a textbook instead of re-reading from chapter 1 every time you want to continue.

### Why It Matters

This makes long-context conversations and agent loops much faster and cheaper, especially when the same context is reused over many requests.

---

## ⚙️ Core Mechanics

### How It Works

Every LLM inference request processes the prompt through the model to build a **key-value (KV) cache**, the internal state representing the processed context. When a later request shares a cached prefix, the model can skip recomputing that part and resume from where the new content diverges.

Anthropic introduced prompt caching for Claude in **August 2024**. OpenAI later added automatic caching for GPT models. In open-source serving:

- **vLLM** implemented automatic prefix caching
- **SGLang** developed **RadixAttention**, a radix-tree-based method for sharing prefixes across concurrent requests

### Key Specs

- Cost reduction on cached prefixes: **50–90%**
- Time-to-first-token reduction: **80%+**
- Biggest wins: repeated prefixes in **agentic** and **conversational** workloads

### Key Facts

- **Anthropic prompt caching**: launched August 2024 for Claude
- **OpenAI automatic caching**: launched for GPT-4 and later models
- **Cost reduction**: 50–90% on cached prefix tokens
- **Latency reduction**: 80%+ reduction in time-to-first-token for cached prefixes
- **vLLM**: automatic prefix caching in open-source serving
- **SGLang RadixAttention**: radix-tree KV cache sharing across requests
- **Key benefit for agents**: system prompt + project context cached across tool calls

| Aspect | No Caching | Prompt Caching | Prefix Sharing |
|--------|-----------|---------------|----------------|
| Scope | Single request | Repeated prefixes | Concurrent requests |
| Latency | Full processing | Skip cached prefix | Shared across batch |
| Cost | Full input tokens | Reduced (50–90%) | Further reduced |
| Implementation | Default | API-level feature | Serving framework |
| Example | vLLM default | Anthropic cache | SGLang RadixAttention |

---

## 🔬 Deep Dive

### Technical Details

The impact is especially large for agents. Coding agents like Claude Code repeatedly send the same system prompt and project context with each tool call. Without caching, an agent loop may reprocess **10K–100K tokens** of static context every turn. With caching, only the new user message and tool results need fresh processing.

### Limitations

- Benefits depend on repeated prefixes actually being reused
- Cache invalidation happens when the prompt diverges
- Infrastructure complexity moves into serving layers and APIs

### Impact

Prompt caching makes long-context and agentic workloads economically viable. A coding agent making 50 tool calls with a 100K-token context could otherwise process 5 million input tokens; caching reduces that dramatically and can improve costs by **10–50×** in practice.

### Related Notes

- [[KV Cache and Context Reuse]] — the underlying mechanism
- [[Serving Architectures and Throughput-Latency Trade-offs]] — broader serving infrastructure
- [[Agentic Coding Systems]] — primary beneficiaries of prompt caching
- [[Batching and Continuous Batching]] — complementary inference optimization
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]] — local proof for repeated-prefix KV reuse

---

## 🏋️ Practice

### Warm-Up

1. What is being cached in prompt caching?
2. Why do agentic workloads benefit so much from caching?

### Core Problems

1. Explain the relationship between prompt caching and the KV cache.
2. Compare no caching, prompt caching, and prefix sharing.
3. Describe why SGLang's RadixAttention matters for concurrent requests.

### Challenge

Estimate the difference between an uncached and cached agent loop for a workflow with repeated large context, and explain where the savings come from.

For a local applied workflow, use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] to separate warm-model residency from true repeated-prefix KV reuse, then measure TTFT, prefill, cache evidence, quality, and cache privacy.

---

## Supporting Chunks

- [[chunk-llm-260 Prompt caching stores KV attention states for common prefixes reducing agentic workflow costs by 60 to 90 percent]]

## References

→ [[Sources Index]]
