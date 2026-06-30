---
tags: [llm, evaluation]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Code and Agentic Benchmarks

> **One-line summary**: Code and agentic benchmarks test whether models can generate correct code and complete multi-step tasks in interactive environments, with execution-based evaluation providing unusually objective ground truth.

---

## 🎯 Intuition

### Core Idea
Code and agentic benchmarks evaluate LLMs on their ability to generate working code and operate autonomously in complex environments. **HumanEval** and **MBPP** test isolated function synthesis, while **SWE-Bench** tests real-world bug fixing in full repositories. **WebArena**, **GAIA**, and **AgentBench** push further into agentic behavior: web navigation, tool use, and multi-step reasoning in interactive settings.

### Analogy
These benchmarks are like **standardized exams — HumanEval is a quiz, SWE-Bench is a final project**. One checks whether the model can solve a neat, self-contained exercise; the other asks whether it can work through messy real software and still deliver a correct result.

### Why It Matters
Execution-based evaluation is the defining feature: correctness is checked by **running code or tasks**, not by pattern-matching text. That makes this area one of the clearest ways to measure real capability rather than fluent-looking output.

---

## ⚙️ Core Mechanics

### How It Works
**HumanEval** contains **164** hand-written Python problems, each with a function signature, docstring, and tests. The central metric is **pass@k**, the probability that at least one of k generated samples passes all tests. **MBPP** adds about **1,000** easier crowd-sourced Python problems and is commonly evaluated with 3-shot prompting.

**SWE-Bench** raises difficulty dramatically: the model must resolve real GitHub issues in repositories such as Django, Flask, and scikit-learn by generating a patch that passes the repository test suite. **SWE-Bench Lite** is a curated **300-issue** subset, and **SWE-Bench Verified** is a human-validated subset of roughly **500** issues.

**WebArena**, **GAIA**, and **AgentBench** move from code synthesis to interactive agency. They test whether a model can execute plans, recover from errors, use tools, and navigate environments rather than merely emit plausible text.

### Key Specs
- **HumanEval**: 164 Python problems; execution-based; pass@k metric
- **MBPP**: ~1,000 crowd-sourced Python problems; generally easier; 3-shot prompting common
- **pass@k**: `P(at least 1 of k samples correct) = 1 − C(n−c, k) / C(n, k)`
- **SWE-Bench**: ~2,294 real GitHub issues; evaluated by repository test suites
- **SWE-Bench Lite**: curated 300-issue subset
- **SWE-Bench Verified**: human-validated subset (~500 issues)
- **WebArena**: 812 tasks across 5 cloned real-world websites
- **GAIA**: 466 questions across 3 difficulty levels with objectively verifiable answers
- **AgentBench**: 8 distinct environments including OS, DB, web, knowledge graph, games, and shopping tasks

### Key Facts
- HumanEval and MBPP mostly test function-level synthesis.
- SWE-Bench tests full-repository understanding and edit integration.
- Agentic benchmarks expose failures in planning, recovery, and environment grounding.
- Benchmarks are not just model tests; scaffolding quality can heavily affect outcomes.


| Benchmark | Scope | Environment | Evaluation | Top Performance |
| --- | --- | --- | --- | --- |
| HumanEval | Function synthesis | Isolated Python | pass@k (unit tests) | ~95%+ pass@1 |
| MBPP | Function synthesis | Isolated Python | pass@k (unit tests) | ~90%+ pass@1 |
| SWE-Bench Full | Real bug-fixing | Full repositories | Patch + test suite | ~30-50% (with scaffolding) |
| SWE-Bench Verified | Validated bug-fixing | Full repositories | Patch + test suite | ~50-65% (with scaffolding) |
| WebArena | Web navigation | Cloned websites | Functional correctness | ~35-45% |
| GAIA | General assistant tasks | Tools + web | Exact-match answers | ~50-70% (Level 1) |
| AgentBench | Multi-environment agent | 8 diverse environments | Environment-specific | Varies widely |

---

## 🔬 Deep Dive

### Technical Details
The progression from HumanEval to SWE-Bench tracks a real capability ladder:
1. **Can the model write a correct function?**
2. **Can it solve many such functions robustly?**
3. **Can it understand and modify a real codebase?**
4. **Can it act autonomously inside an environment with tools, state, and failure modes?**

This is why a model can look excellent on HumanEval but still fail badly on WebArena or SWE-Bench. Function synthesis is narrow and clean; agentic environments require planning, tool grounding, exploration, and recovery.

### Limitations
- Benchmark scores can be inflated or depressed by prompting, retrieval, and orchestration choices.
- Top-line numbers across papers are often not directly comparable.
- Agentic benchmarks are more realistic, but also noisier and harder to standardize.

### Impact
These benchmarks shape how labs and products track progress toward real software engineering and autonomous assistant behavior. They also reveal one of the most important current gaps: strong isolated coding does not automatically translate into strong autonomous performance.

---

## 🏋️ Practice

### Warm-Up
1. What does pass@k measure?
2. Why is SWE-Bench considered much harder than HumanEval?
3. What makes execution-based evaluation more objective than text-only grading?

### Core Problems
1. Compare HumanEval, MBPP, and SWE-Bench in terms of scope, realism, and failure modes.
2. Explain why agentic benchmarks like WebArena and AgentBench test different abilities than pure coding benchmarks.
3. Describe how scaffolding can materially change a benchmark result.

### Challenge
Propose a benchmark ladder for evaluating an AI coding assistant from simple function synthesis through full repository bug fixing and then into tool-using autonomous workflows.

---

## Supporting Chunks
- No supporting chunk notes are attached yet.

---

## References
- [[LLM/Sources/Sources Index]]
