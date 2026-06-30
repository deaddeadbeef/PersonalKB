---
tags: [llm, agents]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Planning and Task Decomposition

> **One-line summary** Planning lets an agent turn a complex goal into a sequence of manageable actions, with different strategies trading off adaptability, coherence, and cost.

## 🎯 Intuition

**The Core Idea:**  
Planning is the mechanism that lets an agent do more than react once. It breaks a larger objective into steps, decides what to do next, and sometimes revises the plan after seeing what happened.

**Analogy:**  
It is like navigating a trip: ReAct is checking the map after every turn, plan-and-execute is plotting the whole route before leaving, and hierarchical planning is organizing the trip by country, city, then street.

**Why It Matters:**  
Without planning, an LLM behaves like a responsive assistant. With planning, it behaves more like an agent that can pursue multi-step goals, coordinate tools, and recover when reality does not match its assumptions.

---

## ⚙️ Core Mechanics

### How It Works

Planning is how an agent breaks a complex goal into a sequence of achievable steps. The dominant paradigm is the ReAct framework (Yao et al., 2022), which interleaves reasoning traces with actions in a Thought → Action → Observation loop. Alternatives include plan-and-execute approaches that generate a full plan upfront, and hierarchical planning that decomposes at multiple levels of abstraction.

ReAct (Reasoning + Acting) merges chain-of-thought reasoning with tool use into a single loop. At each step, the model generates a *Thought* (internal reasoning about what to do next), an *Action* (a tool call or operation), and then receives an *Observation* (the result). This interleaving is powerful because the model can adapt its plan based on intermediate results—if a search returns unexpected information, the next thought can adjust course. The original paper showed that ReAct outperforms both pure reasoning (chain-of-thought without actions) and pure acting (tool use without explicit reasoning) on tasks requiring knowledge retrieval and multi-step decision-making.

Plan-and-execute takes a different approach: generate a complete plan first, then execute each step sequentially. This mirrors how humans tackle well-understood problems—outline the steps, then work through them. The advantage is coherence: the full plan can be reviewed (by the model or a human) before any action is taken. The disadvantage is brittleness: if step 3 fails or returns unexpected results, the remaining plan may be invalid. Sophisticated implementations re-plan after each step or at failure points, creating a hybrid between pure planning and ReAct-style adaptation.

Hierarchical planning adds levels of abstraction. A high-level planner breaks "Build a web app" into major phases (design, implement, test), and sub-planners decompose each phase into concrete steps. This mirrors software project management and helps with complex, long-horizon tasks. The tradeoff is overhead: more planning layers mean more LLM calls before any real work begins, and coordination between levels introduces its own failure modes.

### Key Specifications

- **ReAct loop**: Thought → Action → Observation, repeated until the task is complete or a stopping condition is met
- **Plan-and-execute**: Generate full step list → execute sequentially → optionally re-plan on failure
- **Hierarchical decomposition**: High-level goals → sub-goals → concrete actions, each level potentially handled by a different prompt or model
- **When planning helps**: Complex multi-step tasks, tasks requiring coordination of multiple tools, tasks where order matters
- **When planning hurts**: Simple single-tool queries, highly dynamic environments where plans become stale immediately, tasks where the cost of planning exceeds the cost of trial-and-error
- **Plan drift**: The plan becomes increasingly irrelevant as real-world observations diverge from assumptions—a major failure mode in plan-and-execute
- **Over-planning**: Spending excessive tokens on detailed plans for simple tasks, or planning at a granularity finer than the model can reliably execute
- **Error recovery**: Re-planning from current state, backtracking to last known good state, or escalating to human-in-the-loop
- **Human-in-the-loop**: Presenting the plan for approval before execution, or pausing at critical decision points for human review

### Key Facts

Planning is what separates a chatbot from an agent. Without planning, a model can only react to the immediate prompt. With planning, it can pursue multi-step goals, recover from setbacks, and coordinate complex workflows. The choice of planning strategy—reactive (ReAct), deliberative (plan-and-execute), or hierarchical—fundamentally shapes the agent's behavior, reliability, and cost profile.

The frontier challenge is *when* to plan and *how much*. Over-planning wastes tokens and introduces fragility. Under-planning leads to incoherent action sequences. The best systems adapt their planning depth to task complexity—simple queries get direct action, complex projects get structured decomposition.

| Strategy | Plan Timing | Adaptability | Best For |
| --- | --- | --- | --- |
| ReAct | Per-step | High (adapts each turn) | Exploratory tasks, uncertain environments |
| Plan-and-Execute | Upfront | Low (unless re-planning) | Well-defined multi-step procedures |
| Hierarchical | Multi-level upfront | Medium | Complex, long-horizon projects |
| Human-in-the-Loop | Upfront + checkpoints | High (human corrects) | High-stakes or ambiguous tasks |

---

## 🔬 Deep Dive

### Technical Details

The central design question in planning systems is whether reasoning should be tightly coupled to action or separated from it. ReAct couples them at every step, making the system responsive to new evidence. Plan-and-execute separates deliberation from execution, making the system easier to audit upfront but more vulnerable when conditions change. Hierarchical planning adds another layer by distributing reasoning across abstraction levels.

These strategies are not mutually exclusive. In practice, many strong agent systems are hybrids. They may create an initial high-level plan, execute with ReAct at the step level, and trigger re-planning after failures or unexpected observations. This is often necessary because fully static plans break in dynamic environments, while fully reactive loops can lose global coherence.

### Limitations and Criticisms

Planning introduces its own costs. Each extra reasoning layer consumes tokens, latency, and implementation complexity. If the task is simple, planning can be worse than acting immediately.

Failure modes also differ by strategy. ReAct can meander or over-explore. Plan-and-execute can suffer from plan drift when later steps no longer fit reality. Hierarchical systems can fail through poor coordination between levels or by creating so much planning overhead that execution becomes inefficient.

### Impact and Legacy

Planning frameworks shaped how modern agents are built. ReAct became the dominant reference pattern because it offered a clear loop for mixing reasoning and tool use. Plan-and-execute remained influential for tasks where auditability and procedural clarity matter. Hierarchical planning helped frame long-horizon agents more like project managers than single-turn assistants.

The lasting insight is that good agents do not merely have more tools; they need the right amount of structure for the task. The frontier is less about choosing one planning strategy forever and more about selecting planning depth adaptively.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. What are the three parts of the ReAct loop?
2. Why can plan-and-execute become brittle?
3. When is hierarchical planning especially useful?

### Core Problems

1. Compare ReAct and plan-and-execute on the dimensions of adaptability, coherence, and cost.
2. Explain plan drift in your own words and give a concrete example.
3. Describe a task where human-in-the-loop planning would be preferable to fully autonomous planning.
4. Suppose an agent is solving a dynamic research problem with uncertain intermediate results. Which strategy or hybrid would you choose, and why?

### Challenge

Design a planning approach for an agent that must research a topic, write a draft, verify sources, and revise errors. Decide which parts should use upfront planning, which should use ReAct-style adaptation, and where a human checkpoint would be most valuable.

## Supporting Chunks

### Supporting Chunks

- No supporting chunk notes are attached yet.

## References

- [[LLM/Sources/Sources Index]]
