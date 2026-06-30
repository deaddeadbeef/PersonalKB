---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
---
# Agents & Evaluation — Review Drill

## Quick-Fire Questions

1. **What is the ReAct pattern?**
   Interleave Thought (reasoning) → Action (tool call) → Observation (result) in a loop. Combines reasoning and acting for more robust agent behavior.

2. **Function calling: how does it work at the API level?**
   Define tools with JSON Schema in the request. Model outputs a structured JSON object with function name + arguments instead of text. Runtime executes, feeds result back.

   For local practice, use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] to prove schema validation, policy checks, tool execution, tool-result injection, and loop stopping.

3. **What is pass@k in code evaluation?**
   Generate k code solutions, pass@k = probability that at least one passes all test cases. Measures breadth of generation quality.

4. **Chatbot Arena / ELO ratings — how does it work?**
   Users submit prompts, see two anonymous model responses, pick the better one. Pairwise preferences converted to ELO ratings via Bradley-Terry model.

5. **What is benchmark contamination?**
   Test questions appearing in training data, inflating reported performance. Detection: n-gram overlap, canary strings. Mitigation: dynamic benchmarks (LiveBench), private test sets.

6. **LLM-as-Judge: what are the known biases?**
   Position bias (prefer first response), verbosity bias (longer = better), self-preference (models rate own outputs higher), authority bias.

7. **Multi-agent vs single-agent: when is multi-agent better?**
   When tasks benefit from specialization, parallel execution, or checks/balances (debate). Single-agent with better prompting often beats naive multi-agent on simple tasks.

8. **What is SWE-Bench evaluating?**
   Ability to resolve real GitHub issues: given an issue description + repo, produce a patch that fixes the bug and passes tests. Tests real software engineering, not just function writing.

9. **What is the memory bottleneck in agent systems?**
   Context window is finite. Every token for memory is unavailable for reasoning. Trade-off between remembering past context and processing current task.

10. **MMLU vs Chatbot Arena — what does each measure?**
    MMLU: broad knowledge across 57 subjects (multiple choice, static). Arena: overall chat quality as judged by humans (dynamic, preference-based). They can rank models differently.

## Hands-On

- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] — build a small local tool loop with validated arguments, policy checks, error rows, and bounded stopping.
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] — score tool and agent behavior with workload-specific prompts instead of trusting fluent prose.

## References
- [[LLM/Sources/Sources Index|LLM Sources Index]]
