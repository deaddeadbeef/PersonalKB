---
tags: [study, llm, local-llm, ollama, structured-output, quality, remediation, evidence]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T06:51:34+08:00
---

# Local LLM Structured Format Remediation Proof - 2026-06-16

> **One-line summary** The held `C-01` strict-format probe is remediated only when the model emits validated structured IDs and the application renders the two five-word bullets; free-text and loose structured attempts still failed.

This follows [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]] and complements [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]]. It is a strict-format remediation proof, not a full quality pass.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Structured-format remediation runner | `pass/app_rendered_structured_format_ready` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner\20260616-065134-structured-format-remediation-structured-format-remediation-results.json` |
| Markdown result | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner\20260616-065134-structured-format-remediation-structured-format-remediation-results.md` |
| CSV result | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner\20260616-065134-structured-format-remediation-structured-format-remediation-results.csv` |
| JSONL log | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner\structured-format-remediation-runs.jsonl` |
| Runner script | `pass` compile | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner.py` |

## Result Summary

| Field | Value |
|---|---|
| Run id | `20260616-065134-structured-format-remediation` |
| Status | `pass` |
| Decision | `pass/app_rendered_structured_format_ready` |
| Runtime | Ollama |
| Model | `qwen3.5:2b-q4_K_M` |
| Route | `http://127.0.0.1:11434/api/chat` |
| Boundary | `loopback` |
| Source prompt | `C-01`: two bullets, exactly five words each, about why route proof is not quality proof |
| Pass / hold | `2` / `3` |
| Accepted remediation path | `schema_explicit_enum_claim_selection` |
| Rendered output | `- Route proof verifies endpoint reachability` and `- Quality proof verifies useful behavior` |

## Probe Outcomes

| Probe | Decision | What happened |
|---|---|---|
| `original_free_text_control` | `hold` | The model again produced three long bullets instead of two five-word bullets. |
| `schema_free_text_fields` | `hold` | The model returned parseable JSON, but the fields were off-topic and six words each: `The bullet is made of steel` and `This item has a strong finish`. |
| `schema_enum_claim_selection` | `hold` | The model returned parseable JSON but invented `RouteClaim_01` and `QualityClaim_02` instead of the allowed IDs. |
| `schema_explicit_enum_claim_selection` | `pass` | With explicit allowed IDs, the model returned `endpoint_reachability` and `useful_behavior`; the application rendered two valid five-word bullets. |
| `bad_shape_denial` | `pass` | A structured object with an extra `execute_shell` field was denied before rendering. |

## Interpretation

- Free-text generation is still not reliable for this strict-format contract.
- JSON mode alone is not enough: parseable JSON can still be semantically wrong, off-topic, or schema-invalid.
- The reliable remediation path is to reduce the model output to validated IDs, then let deterministic application code render the exact user-facing shape.
- The application, not the model, owns the final bullet count and word count.
- Schema validation is part of the safety boundary: extra fields are denied before rendering or downstream use.

## What This Proves

- `C-01` can be remediated for a local application by using explicit structured IDs and deterministic rendering.
- The current model can supply the required claim IDs when the allowed values are explicit in the prompt and schema.
- App-side validation catches invented labels and unexpected fields before they become user-facing output.

## What This Does Not Prove

- That the model can reliably count words or satisfy arbitrary formatting constraints in free text.
- That all structured-output schemas will be followed without explicit allowed values.
- That broad workload quality is ready; a rerun or full quality harness still needs to use the documented calculator and structured-rendering paths.
- That RAG, multi-tool loops, deployment, lifecycle, or academic mastery gates are complete.

## Next Actions

1. Treat `K-01` arithmetic as tool-owned via [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]].
2. Treat `C-01` strict formatting as renderer-owned via this note.
3. Run [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] to map raw prompt, schema, model JSON, validation, rendering, and final output phases.
4. Rerun quality or write the first evidence-pack audit only after the artifact states which rows are model-owned, tool-owned, or renderer-owned.

## References

Internal routes:

- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
