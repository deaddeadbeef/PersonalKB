---
status: done
area: LLM
created: 2026-06-15
completed: 2026-06-15
---

# Local LLM Serving Internals and Scheduler Lab

## Outcome

Added [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] to bridge academic serving mechanisms with local hosting evidence.

## Coverage Added

- Scheduler mechanism map for cold load, prefill, decode, KV-cache allocation, PagedAttention, continuous batching, chunked prefill, prefix cache, and admission control.
- Runtime scheduler map for Ollama, LM Studio, llama.cpp, vLLM, SGLang, and Open WebUI.
- Lab rows for latency phase splitting, scheduler state, long-prompt interference, one-variable scheduler tuning, and preemption/OOM triage.
- Decision card for bottleneck owner, concurrency/slots, batched-token or queue policy, long-prompt policy, prefix-cache decision, and deployment outcome.

## Routing

Linked the lab from the main LLM map, study index, mechanism bridge, theory notes on KV cache/batching/serving, concurrency lab, observability runbook, benchmark/deployment routes, roadmap, capstone, and self-assessment.

## Sources Checked

- vLLM documentation and optimization/tuning docs.
- SGLang documentation.
- llama.cpp server README.
- LM Studio parallel requests.
- PagedAttention and SARATHI papers.
