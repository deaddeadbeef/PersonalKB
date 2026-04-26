---
tags: [llm, agents]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Memory and State Management

> **One-line summary**: Memory systems let stateless LLMs act as if they remember past turns by deciding what to keep in context, what to summarize, and what to store and retrieve externally.

---

## 🎯 Intuition

### Core Idea
Memory and state management is how LLM agents maintain context beyond a single conversational turn. The core constraint is the **context window**: everything the model can directly reason about must fit into that token budget. Memory systems work around this by storing, summarizing, retrieving, and reinserting information so the agent behaves as if it has long-term memory even though the model itself is stateless from call to call.

### Analogy
This is like **OS virtual memory — context window is RAM, vector store is disk**. Keeping everything in-context is fast but limited; pushing information out to external storage scales farther but requires intelligent retrieval.

### Why It Matters
Without memory management, long-running agents forget instructions, lose earlier decisions, repeat work, and eventually overflow context limits. Good memory design is what separates a short-chat assistant from an agent that can sustain long tasks or persistent user relationships.

---

## ⚙️ Core Mechanics

### How It Works
The simplest approach is just appending the full conversation history into the prompt every turn. That works until the token budget fills up. After that, systems need policies:
- keep only a **sliding window** of recent turns,
- periodically create **summaries**,
- maintain explicit **working memory** or scratchpads,
- or store facts externally in a **vector store** or other long-term memory system.

### Key Specs
- **Conversation history**: full message log in context; accurate but context-limited
- **Sliding window**: keep the last N turns; simple but loses early context
- **Summarization memory**: compress history into shorter summaries; saves tokens but loses detail
- **Hierarchical summarization**: recent turns verbatim, mid-range summarized, distant past highly compressed
- **Working memory**: structured task state or key-value scratchpad kept across turns
- **Long-term memory (vector store)**: write facts, preferences, and decisions to external storage and retrieve by similarity
- **Episodic memory**: records of specific events or interactions
- **Semantic memory**: general facts extracted from interactions
- **MemGPT / virtual context**: explicit `store/search/update/delete` style memory operations managed by the agent itself
- **Context-window management**: recency, priority, and relevance determine what gets injected

### Key Facts
- A **128K** context window can still fill quickly during long coding or tool-heavy sessions.
- Naive truncation often drops the most important early instruction: the original task.
- Summaries free tokens but are inherently lossy.
- Vector-store memory scales well but depends on retrieval quality.
- **MemGPT (Packer et al., 2023)** explicitly framed this as **virtual context management**.


| Memory Type | Capacity | Accuracy | Latency | Cost |
| --- | --- | --- | --- | --- |
| Full conversation history | Context-window-limited | Perfect (until truncated) | None (already in context) | High (long prompts) |
| Summarization | 2–10× compression | Lossy (detail loss) | Low (summary injection) | Medium |
| Vector store (RAG) | Unlimited | Depends on retrieval quality | Medium (embedding + search) | Low per-query |
| MemGPT (virtual context) | Unlimited | Agent-controlled (explicit read/write) | Medium (tool calls for memory ops) | Medium |
| Working memory (scratchpad) | Small (structured) | High (explicit key-value) | None (in-context) | Low |

---

## 🔬 Deep Dive

### Technical Details
Long-term memory via vector stores works by writing important facts, decisions, or past interactions into an external database, then retrieving relevant items each turn using semantic similarity. This decouples memory capacity from the context window: the store can hold millions of items while only a few are injected into the prompt.

Summarization memory takes the opposite approach. Instead of storing externally, it compresses the conversation itself. Hierarchical summarization creates a telescoping memory structure: recent turns in full, medium-past in detailed summaries, distant past in coarse summaries.

Working memory is different again: it is not a passive history but an explicit state representation, such as current objectives, known constraints, unresolved subtasks, and intermediate results.

### Limitations
- Retrieval can miss the right memory at the right moment.
- Summaries can discard the exact detail later needed.
- Larger context windows help, but they raise cost and latency too.
- Explicit memory tools increase control but also orchestration complexity.

### Impact
Memory engineering is one of the main ways agent systems scale beyond one-off chats. It directly determines coherence over long tasks, cross-session continuity, and whether an assistant feels persistent rather than amnesiac.

---

## 🏋️ Practice

### Warm-Up
1. Why is an LLM described as stateless even if a chat app seems to remember past turns?
2. What problem does summarization memory solve?
3. How is vector-store memory different from just keeping the whole conversation in context?

### Core Problems
1. Compare sliding-window memory, summarization, and vector-store retrieval in terms of cost and failure modes.
2. Explain the difference between episodic memory and semantic memory for an agent.
3. Why is the virtual-memory analogy useful for understanding MemGPT-style systems?

### Challenge
Design a memory system for a coding agent that must preserve task goals, repository facts, user preferences, and recent tool outputs across very long sessions without exceeding context limits.

---

## Supporting Chunks
*(To be populated as chunks are created)*

---

## References
- [[LLM/Sources/Sources Index]]
