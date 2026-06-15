---
tags: [study, llm, local-llm, ollama, tools, calculator, quality, remediation, evidence]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:38:01+08:00
---

# Local LLM Calculator Tool Remediation Proof - 2026-06-16

> **One-line summary** The held `K-01` arithmetic probe is remediated when `qwen3.5:2b-q4_K_M` routes through a native Ollama calculator tool loop, but direct ad hoc result injection still produced a placeholder-shaped answer and strict-format quality needed a separate structured-renderer proof.

This follows [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]]. It is an arithmetic/tool remediation proof, not a full quality pass.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Calculator tool remediation runner | `pass/native_tool_loop_remediation_ready` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner\20260616-063801-calculator-tool-remediation-calculator-tool-remediation-results.json` |
| Markdown result | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner\20260616-063801-calculator-tool-remediation-calculator-tool-remediation-results.md` |
| CSV result | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner\20260616-063801-calculator-tool-remediation-calculator-tool-remediation-results.csv` |
| JSONL log | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner\calculator-tool-remediation-runs.jsonl` |
| Runner script | `pass` compile | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner.py` |

## Result Summary

| Field | Value |
|---|---|
| Run id | `20260616-063801-calculator-tool-remediation` |
| Status | `pass` |
| Decision | `pass/native_tool_loop_remediation_ready` |
| Runtime | Ollama |
| Model | `qwen3.5:2b-q4_K_M` |
| Route | `http://127.0.0.1:11434/api/chat` |
| Boundary | `loopback` |
| Source prompt | `K-01`: `Compute 17 * 23 + 19. Return exactly: answer=<number>; reason=<one short sentence>.` |
| Expected value | `410` |
| Pass / hold | `4` / `1` |
| Accepted remediation path | `native_tool_loop` |
| Direct tool-result injection | `hold` diagnostic |
| Native tool-call emission | `pass` |
| Native tool-result follow-up | `pass` |

## Probe Outcomes

| Probe | Decision | What happened |
|---|---|---|
| `deterministic_calculator_result` | `pass` | The local Python AST calculator accepted only allowlisted integer arithmetic and produced `410` for `17 * 23 + 19`. |
| `bad_argument_denial` | `pass` | A bad expression using `__import__('os').system('whoami')` was denied before execution because it contained disallowed characters. |
| `native_model_tool_call_probe` | `pass` | The model emitted one `calculate_integer_expression` tool call with `{"expression": "17 * 23 + 19"}`. |
| `native_tool_result_followup` | `pass` | After the validated tool result was injected through the native tool-role path, the model returned `answer=410; reason=The calculation of 17 multiplied by 23 plus 19 results in 410.` |
| `tool_result_injection_final_answer` | `hold` | The ad hoc direct finalizer included placeholder brackets: `answer=410; reason=<one short sentence>...`; use the native loop or a stricter finalizer. |

## Interpretation

- The original arithmetic failure was not fixed by asking the model to think harder or by changing output caps.
- The failure is remediated when the client treats arithmetic as a tool decision: validate arguments outside the model, execute a deterministic calculator, inject the result, then require the model to format the final answer.
- Native Ollama tool-call emission and native tool-result follow-up both passed for this small calculator tool.
- Directly pasting a tool result into a finalizer prompt was weaker than the native tool loop because the model copied placeholder text.
- This did not clear the held `C-01` strict-format probe by itself; see [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]] for the separate renderer-owned route.
- This does not prove general workload quality and does not replace model selection for tasks that require reasoning instead of deterministic tools.

## What This Proves

- For arithmetic-like local tasks, the first accepted remediation path is a native calculator tool loop, not more prompting.
- Tool safety must live outside the model: the bad expression denial was performed by schema/policy code before execution.
- The current model can participate in the narrow loop of selecting a calculator tool, receiving a result, and producing the required one-line answer.

## What This Does Not Prove

- That arbitrary tools, file access, shell access, network calls, or RAG tools are safe.
- That a multi-step agent loop is reliable under ambiguous instructions or multiple tools.
- That the current model is quality-ready for non-tool reasoning.
- That the first inference evidence pack can pass without reconciling tool-owned arithmetic, renderer-owned formatting, request lifecycle, benchmark, and capstone audit gaps.

## Next Actions

1. Add this native calculator pattern to [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] or a small client harness before real tool use.
2. Use [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]] for the separate `C-01` renderer-owned strict-format route.
3. Use [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] to map the native tool-call request, tool-role response, and final answer into lifecycle phases.
4. Keep security scope loopback-only; tool expansion needs a separate policy, logging, and denial proof.

## References

Internal routes:

- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]]
