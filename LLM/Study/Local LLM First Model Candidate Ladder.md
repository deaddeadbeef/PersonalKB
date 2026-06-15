---
tags: [study, llm, local-llm, model-selection, ollama, hardware, first-run]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Model Candidate Ladder

> **One-line summary** For this Windows workstation, the first local LLM model should prove the runtime and loopback routes cheaply before testing stronger, larger, or more specialized candidates.

Use this after [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] and before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. The readiness snapshot says what is installed. This ladder says which first model class to pull, what that choice proves, and when to move to a larger tag.

Pair this with [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] when estimating memory and [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] when the workload is more specific than a route proof.

## Machine Scope

This ladder is scoped to the current first-run machine state:

| Field | Current value |
|---|---|
| Host boundary | Windows native first |
| GPU | NVIDIA GeForce RTX 3080 Ti |
| VRAM | 12288 MiB |
| Current runtime state | Ollama and LM Studio CLI not installed or not on PATH |
| Current endpoint state | no common local LLM listener on `11434`, `1234`, `8000`, `8001`, `8080`, or `30000` |
| First runtime target | Ollama on loopback |
| First proof target | native plus OpenAI-compatible route proof, not final model quality |

If any of these change, refresh the readiness snapshot before using this ladder.

## Ladder Rule

The first model is a control condition.

```text
small route-proof model
  -> stable loopback endpoint
  -> repeatable client call
  -> benchmark and quality row
  -> then scale, specialize, or switch runtime
```

Do not start with the largest model that might fit. If a large first pull fails, you will not know whether the owner is install/PATH, disk, model tag, memory, quantization, runtime compatibility, chat template, route, or quality.

## Candidate Ladder

| Slot | Current tag to try | Why this slot exists | What to prove before moving on |
|---|---|---|---|
| Route-proof baseline | `qwen3.5:4b` | Source-checked Ollama tag; about 4.66B parameters, Q4_K_M, 3.4GB. Small enough to test install, pull, native route, OpenAI-compatible route, and basic timing before quality work. | `ollama list`, native response JSON, `/api/tags`, `/v1/chat/completions`, listener boundary, and one smoke benchmark row. |
| Text-only instruct control | `qwen3:4b-instruct` | Smaller source-checked Qwen3 instruct tag; about 4.02B parameters, Q4_K_M, 2.5GB. Useful if multimodal/reasoning behavior in Qwen3.5 complicates the first text-only smoke proof. | Same route proof as the baseline, plus a note explaining why the control model replaced or supplemented `qwen3.5:4b`. |
| Practical stretch | `qwen3.5:9b` | Source-checked 9.65B Q4_K_M tag at 6.6GB. Plausible on 12GB VRAM for short, single-user tests, but it is a second run because KV-cache, runtime overhead, and other apps still need headroom. | Baseline route proof must already pass; then run the same prompt, sampler, context, benchmark, and quality rows for comparison. |
| Alternate text-only stretch | `qwen3:8b` or `qwen3:8b-q4_K_M` | Qwen3 text-only 8B-class control; the Q4_K_M tag is listed around 5.2GB with a 40K context window. Useful when the comparison should avoid Qwen3.5 multimodal features. | Same fixed prompt suite and benchmark fields as the baseline. Do not compare subjective chat feel. |
| Not first proof | 27B+, 30B+, 35B+, 122B+, 235B+ | The tags exist, but larger tags can exceed VRAM or leave too little KV-cache/runtime headroom. For example, a 27B int4 tag is listed around 16GB before local overhead. | Only test after sizing, artifact custody, quantization/offload, context budget, and failure rollback evidence exist. |

The advertised context windows are not permission to use huge contexts on the first run. A 256K or 40K context label does not prove local KV-cache headroom, prefill latency, quality, or truncation behavior on this workstation.

## First Pull Decision

Use this decision unless a current model page or local constraint changes it:

| Field | Decision |
|---|---|
| First pull | `qwen3.5:4b` |
| First fallback | `qwen3:4b-instruct` |
| First stretch | `qwen3.5:9b` |
| Avoid before baseline passes | `qwen3.5:27b-*`, `qwen3:30b`, `qwen3:235b`, any huge-context RAG run |
| First prompt class | smoke only, then known-answer and structured-output mini-suite |
| First failure owner to record | install/PATH, disk/cache, model tag, listener, route, memory, or quality |

If `qwen3.5:4b` is unavailable at pull time, do not improvise with a much larger tag. Choose the smallest source-checked instruct/chat tag and record the replacement in the run card.

## Upgrade Gates

Move from baseline to stretch only when these are true:

- [ ] the runtime version and model list are saved
- [ ] the model tag and pull output are saved
- [ ] the listener boundary is saved and loopback-only
- [ ] native route proof exists
- [ ] OpenAI-compatible route proof exists, or native-only is explicitly accepted
- [ ] one benchmark row exists for the baseline
- [ ] one quality mini-suite row exists or is explicitly pending
- [ ] the next run changes only model tag/size, not prompt, sampler, runtime, route, or context

## Recheck Trigger

Recheck model pages before pulling when:

- the current date is not 2026-06-15
- an Ollama pull fails with "not found" or resolves to an unexpected artifact
- the model page shows a different size, quantization, license, context, or input modality
- the workload changes from smoke chat to coding, RAG, tools, vision, long context, or batch
- the runtime changes from Ollama to LM Studio, llama.cpp, vLLM, SGLang, or Docker

The model ladder is operational guidance, not a timeless leaderboard.

## Completion Gate

This ladder has served its purpose for one run when:

- [ ] the run card names the selected slot and model tag
- [ ] the benchmark row records whether it was baseline, control, stretch, or rejected
- [ ] any larger model was tested only after baseline proof existed
- [ ] rejected candidates include the owner: memory, quality, route, runtime, license, or maintenance
- [ ] [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] links the final first-run decision

## References

Internal routes:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]

External/current sources checked 2026-06-15:

- [Ollama qwen3.5:4b model page](https://ollama.com/library/qwen3.5:4b)
- [Ollama qwen3.5:9b model page](https://ollama.com/library/qwen3.5:9b)
- [Ollama qwen3.5 tags](https://ollama.com/library/qwen3.5/tags)
- [Ollama qwen3:4b-instruct model page](https://ollama.com/library/qwen3:4b-instruct)
- [Ollama qwen3 tags](https://ollama.com/library/qwen3/tags)
