---
tags: [study, llm, inference, local-llm, speculative-decoding, draft-model, latency, benchmarking, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Speculative Decoding Lab

> **One-line summary** Speculative decoding is worth enabling only when the draft path increases accepted tokens per target-model step enough to beat its extra memory, load, and runtime complexity.

Use this after [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]], [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]], and [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] already separate prefill, decode, sampling, TTFT, TPOT, and quality. Those notes prove the request. This lab proves whether draft-verify decoding helps the local runtime. Use [[LLM/Study/Local LLM Speculative Decoding Runner|Local LLM Speculative Decoding Runner]] when the no-spec/spec comparison should be saved as JSON, CSV, Markdown, and JSONL artifacts.

Use [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] before this lab if the main model barely fits. Speculative decoding often needs a draft model, draft KV cache, verification buffers, or runtime-specific draft trees. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] when the speed claim depends on repeated prefixes rather than faster decode. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when the question is multi-user throughput rather than one interactive stream.

## What This Lab Decides

This lab answers four practical questions:

1. Does speculative decoding reduce inter-token latency or total response time on this workload?
2. Which draft path is being used: smaller draft model, EAGLE, MTP, n-gram, Medusa-style heads, or runtime-specific proposer?
3. Is the result still quality-equivalent for the workload after sampler, prompt, and output caps are frozen?
4. Is the extra memory and operational complexity worth keeping enabled?

Do not enable it because the runtime exposes a flag. Enable it only after a no-spec baseline and a spec-enabled run prove a better operating point.

## Academic Mental Model

Standard autoregressive decoding asks the target model for one new token per step. Speculative decoding changes the loop:

1. A cheap draft source proposes several candidate tokens.
2. The expensive target model verifies those candidates in one batched pass.
3. Accepted tokens are committed from left to right.
4. If a token is rejected, the target model corrects the continuation and the loop continues.

The speedup comes from turning multiple serial target-model decode steps into one target-model verification step. The quality guarantee comes from the rejection-sampling correction when the implementation preserves the target distribution.

The lab evidence must therefore separate:

| Concept | Meaning | Evidence |
| --- | --- | --- |
| Draft source | Where candidate tokens come from. | Draft model id, EAGLE/MTP setting, n-gram setting, or runtime flag. |
| Target model | The model whose output distribution is being preserved. | Main model id, artifact, quantization, runtime. |
| Draft width or depth | How many candidates are proposed before verification. | `num_speculative_tokens`, `draft_num_predict`, draft steps/top-k, or runtime equivalent. |
| Acceptance rate | Fraction of draft tokens the target accepts. | Accepted/predicted draft tokens, accepted tokens per step, or runtime metric. |
| Decode latency | Later-token speed after prefill. | TPOT, inter-token latency, output tokens/sec. |
| Quality equivalence | Output still satisfies the target workload. | Frozen quality harness, exact-output smoke test, parse/test result, or human rubric. |
| Memory overhead | Extra draft model/cache/buffers. | Peak RAM/VRAM and OOM evidence. |

Speculative decoding is mainly a decode-phase optimization. It does not fix long-prompt prefill by itself. If TTFT is high because the prompt is huge, use prompt/cache and context-budget labs first.

## When It Helps

| Workload pattern | Expected result | Why |
| --- | --- | --- |
| Deterministic factual answers | Often strong | Draft and target agree on obvious continuations. |
| Code completion in a narrow style | Often strong | Local syntax and boilerplate make next tokens predictable. |
| Rewriting repetitive text | Can be strong, especially with n-gram methods | Prior text supplies repeated sequences. |
| Long answers with low temperature | Often useful | More decode tokens means more opportunity to amortize target passes. |
| Creative writing at high temperature | Often weak | Many valid continuations reduce exact draft acceptance. |
| Hard reasoning with varied chains | Mixed | The draft may diverge from the target's reasoning path. |
| High-concurrency server already saturated | Mixed or negative | Draft work can compete with target work and reduce batch efficiency. |

The best first test is not a single prompt. Use at least one predictable prompt, one real workload prompt, and one prompt expected to have low acceptance.

## Runtime Support Map

| Runtime | Speculative path to inspect | First proof |
| --- | --- | --- |
| LM Studio | UI draft model, Python/TypeScript SDK `draftModel`, same-vocabulary draft pairing. | Accepted draft token stats, main/draft model keys, before/after generation speed. |
| llama.cpp / llama-server | `--spec-type`, `--model-draft` / `--spec-draft-model`, `--spec-draft-n-max`, n-gram spec types. | Startup command, draft model path or n-gram type, server metrics/logs, before/after TPOT. |
| vLLM | `--speculative-config` with draft model, EAGLE/MTP/PARD/MLP/n-gram/suffix methods where supported. | Server launch config, benchmark output, latency/throughput, known feature compatibility. |
| SGLang | `--speculative-algorithm` with `EAGLE`, `EAGLE3`, `STANDALONE`, `NGRAM`, `NEXTN`/MTP, plus draft model path when needed. | Server args, benchmark output, accepted draft tokens or throughput/latency deltas, OOM headroom. |
| Ollama | `draft_num_predict` controls speculative draft tokens when a draft model or embedded MTP path exists. | `ollama show --modelfile`, actual model support evidence, disabled-vs-enabled timing; do not infer support from the parameter alone. |
| TensorRT-LLM / Triton | EAGLE, Medusa, draft-model speculative serving in NVIDIA-oriented stacks. | Engine/server config, Triton or TensorRT-LLM benchmark, GPU memory and throughput evidence. |

If a runtime exposes no accepted-token metric, the comparison is still possible, but the decision is weaker. You need a clean A/B with identical prompt, sampler, output cap, and model state.

## Lab 0: Freeze Eligibility

Before enabling anything, fill this card.

| Field | Value |
| --- | --- |
| Main model id and artifact |  |
| Main model quantization |  |
| Draft source | none / smaller model / EAGLE / MTP / n-gram / Medusa / unknown |
| Draft model id or config |  |
| Same tokenizer/vocabulary evidence |  |
| Runtime and version |  |
| Speculative feature flag or UI path |  |
| Current baseline prompt suite |  |
| Sampler preset |  |
| Output cap |  |
| Hardware headroom before draft |  |
| Expected risk | memory / low acceptance / unsupported route / quality drift |

Pass signal: you know what will generate drafts and how you will turn it off again.

## Lab 1: No-Spec Baseline

Run the target model with speculative decoding disabled. Keep this run boring and reproducible.

| Run | Spec path | Prompt id | Output cap | TTFT | TPOT / ITL | Output tok/s | Total latency | Peak RAM/VRAM | Quality |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| BASE-SMOKE | off | SMOKE-01 |  |  |  |  |  |  |  |
| BASE-WORK | off | WORK-01 |  |  |  |  |  |  |  |
| BASE-LOW-ACCEPT | off | CREATIVE-01 or HARD-01 |  |  |  |  |  |  |  |

Use `temperature=0` or the workload's frozen sampler. Do not change the prompt after seeing the spec-enabled run.

## Lab 2: Enable One Speculative Path

Enable exactly one speculative method.

### LM Studio

Use the UI draft-model selector or SDK `draftModel` setting. Save the main model key, draft model key, and accepted draft token stats when the SDK exposes them.

```python
import lmstudio as lms

model = lms.llm("<main-model-key>")
result = model.respond(
    "Reply with exactly: speculative check",
    config={"draftModel": "<draft-model-key>"},
)
print(result.stats)
```

### llama.cpp / llama-server

Use a draft model when you have a compatible small model, or an n-gram method when the workload has repetition.

```powershell
.\llama-server.exe `
  --model C:\models\main.gguf `
  --model-draft C:\models\draft.gguf `
  --spec-type draft-simple `
  --spec-draft-n-max 5 `
  --host 127.0.0.1 `
  --port 8080
```

For no-extra-model repetition tests, try a documented n-gram spec type and record that it is not a separate draft model.

### vLLM

Use a server-side speculative config, then call the same OpenAI-compatible endpoint as the baseline.

```powershell
vllm serve Qwen/Qwen3-4B-Thinking-2507 `
  --host 127.0.0.1 `
  --port 8000 `
  --max-model-len 2048 `
  --speculative-config '{"model":"Qwen/Qwen3-0.6B","num_speculative_tokens":5,"method":"draft_model"}'
```

### SGLang

Choose one algorithm and record the exact args. Example shape:

```powershell
python -m sglang.launch_server `
  --model-path <main-model> `
  --host 127.0.0.1 `
  --port 30000 `
  --speculative-algorithm STANDALONE `
  --speculative-draft-model-path <draft-model> `
  --speculative-num-draft-tokens 5
```

For EAGLE/EAGLE3/MTP, use the runtime's method-specific parameters and record whether the draft path is a separate model, built-in heads, or n-gram.

### Ollama

Record `draft_num_predict` only when the model package or embedded MTP path actually supports speculative drafting.

```text
PARAMETER draft_num_predict 4
```

If you cannot prove the draft source, mark the row as "speculative support unproven" instead of counting it as an enabled run.

## Lab 3: A/B Measurement

Run the exact same prompt suite with speculative decoding enabled.

| Run | Spec method | Prompt id | Draft tokens setting | Accepted/predicted draft tokens | Acceptance rate | TTFT | TPOT / ITL | Output tok/s | Total latency | Peak RAM/VRAM | Quality |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| SPEC-SMOKE |  | SMOKE-01 |  |  |  |  |  |  |  |  |  |
| SPEC-WORK |  | WORK-01 |  |  |  |  |  |  |  |  |  |
| SPEC-LOW-ACCEPT |  | CREATIVE-01 or HARD-01 |  |  |  |  |  |  |  |  |  |

Interpretation:

- If output tokens/sec improves and quality is unchanged, speculative decoding is useful for this prompt class.
- If TTFT changes but TPOT does not, you may be measuring load, prefill, warmup, or queue effects rather than speculation.
- If accepted draft tokens are low, try a closer draft model, lower draft depth, lower temperature, or a different prompt class.
- If memory rises near the limit, keep it off unless the latency win is large and stable.

## Lab 4: Prompt Sensitivity

Speculative decoding is prompt dependent. Use one high-acceptance and one low-acceptance prompt on purpose.

| Prompt id | Prompt style | Expected acceptance | Actual acceptance | Speed delta | Decision |
| --- | --- | --- | --- | --- | --- |
| FACT-01 | short factual / formula / definition | high |  |  |  |
| CODE-01 | boilerplate code or refactor | medium-high |  |  |  |
| CREATIVE-01 | open-ended story or style | low |  |  |  |
| REASON-01 | hard multi-step reasoning | mixed |  |  |  |

Do not generalize from the easy prompt to all workloads. A local coding assistant, RAG summarizer, and creative writer can have different acceptance profiles.

## Lab 5: Memory And Concurrency Check

Repeat the winning spec setting under the selected operating mode.

| Test | Baseline | Spec enabled | Decision |
| --- | --- | --- | --- |
| Peak RAM/VRAM |  |  |  |
| Single-user TPOT |  |  |  |
| p95 TTFT at chosen concurrency |  |  |  |
| Error/OOM count |  |  |  |
| Quality under load |  |  |  |

If the draft model consumes the headroom needed for context or concurrency, disable speculation for that deployment and use a smaller model, better quantization, prompt caching, or batching instead.

## Decision Card

Copy this into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], or the capstone workbook.

| Field | Value |
| --- | --- |
| Workload |  |
| Main model |  |
| Draft method/model |  |
| Runtime and version |  |
| Frozen sampler/output cap |  |
| Baseline TPOT / output tok/s |  |
| Spec TPOT / output tok/s |  |
| Accepted/predicted draft tokens |  |
| Prompt classes that benefit |  |
| Prompt classes that do not benefit |  |
| Extra RAM/VRAM |  |
| Quality result | pass / hold / fail |
| Keep enabled? | yes / no / only for specific workload |
| Retest trigger | new model, draft model, runtime, prompt class, context, concurrency, or hardware |

## Failure Triage

| Symptom | Likely cause | First check |
| --- | --- | --- |
| No speedup | Draft model too slow, low acceptance, high temperature, or runtime overhead. | Accepted-token stats and draft/main latency ratio. |
| Slower than baseline | Draft path consumes memory/compute or acceptance is too low. | Disable speculation and compare peak RAM/VRAM plus TPOT. |
| Load fails | Draft model incompatible with tokenizer, architecture, quantization, or runtime. | Compatibility card and same-vocabulary evidence. |
| Output differs unexpectedly | Sampler nondeterminism, floating-point/batch variation, or non-lossless implementation path. | Greedy exact-output smoke test and runtime known-issues docs. |
| OOM after enabling | Draft model, draft KV cache, tree buffers, CUDA graphs, or verification buffers exceed headroom. | Lower draft tokens, memory fraction, context, or concurrency. |
| Helps factual prompt but not real workload | Real workload has low draft-target agreement. | Prompt sensitivity table. |
| Helps single request but hurts concurrency | Draft work reduces scheduler/batch efficiency. | Concurrency ladder with spec on/off. |
| TTFT still high | Problem is prefill, cold load, queue, or long prompt, not decode. | Request lifecycle and prompt-cache labs. |

## Completion Gate

This lab is complete when you have:

- [ ] one no-spec baseline for at least three prompt classes
- [ ] one spec-enabled run with the same prompts, sampler, output cap, model, and route
- [ ] draft method/model/version recorded
- [ ] accepted-token evidence or an explicit "runtime does not expose acceptance" note
- [ ] runner output is saved when the proof needs repeatable JSON, CSV, Markdown, or JSONL evidence
- [ ] TPOT, output tokens/sec, total latency, and peak memory compared
- [ ] quality checked with the same harness or exact-output smoke test
- [ ] prompt classes separated into helps / neutral / hurts
- [ ] concurrency or memory impact checked if the service is not strictly single-user
- [ ] a keep/disable/conditional decision written into the benchmark log or deployment matrix

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]

Supporting chunks:

- [[LLM/_chunks/chunk-llm-221 Speculative Decoding Draft-Verify Algorithm|chunk-llm-221]]
- [[LLM/_chunks/chunk-llm-222 Speculative Sampling Distribution Guarantee|chunk-llm-222]]
- [[LLM/_chunks/chunk-llm-223 Speculative Decoding Speedup Analysis|chunk-llm-223]]
- [[LLM/_chunks/chunk-llm-224 Speculative Decoding Production Adoption|chunk-llm-224]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck|chunk-llm-214]]

Current external docs checked 2026-06-15:

- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318)
- [vLLM speculative decoding](https://docs.vllm.ai/en/stable/features/speculative_decoding/)
- [vLLM draft models](https://docs.vllm.ai/en/latest/features/speculative_decoding/draft_model/)
- [llama.cpp speculative decoding](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md)
- [SGLang speculative decoding](https://sgl-project.github.io/advanced_features/speculative_decoding.html)
- [LM Studio speculative decoding](https://lmstudio.ai/docs/app/advanced/speculative-decoding)
- [LM Studio Python SDK speculative decoding](https://lmstudio.ai/docs/python/llm-prediction/speculative-decoding)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [TensorRT-LLM speculative decoding with Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html)
