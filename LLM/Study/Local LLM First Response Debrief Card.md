---
tags: [study, llm, inference, local-llm, ollama, metrics, benchmark, debrief, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local LLM First Response Debrief Card

> **One-line summary** After the first local response is saved, use this card to translate the raw JSON into route proof, timing interpretation, academic mechanism, benchmark row, quality boundary, and next controlled action.

Use this after [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] or [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] creates `ollama-native-response.json`, a native smoke response, or an equivalent first-response file. The endpoint run sheet proves that a local route answered. The smoke runner preserves request/response/output files in a repeatable shape. Use [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]] when you want the same debrief as JSON, Markdown, and JSONL without hand-copying the timing fields. This card explains what that response proves, what it does not prove, and which next lab owns the next action. Use [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] next when the route works and you need a small private quality signal before the full harness.

This card is intentionally small. It is the bridge between one saved response and the larger [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]], and [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]].

## Source Response

For Ollama native `/api/generate` or `/api/chat`, the response can include:

| Field | Meaning | Local interpretation |
|---|---|---|
| `model` | Model used for the response. | Must match the model tag from [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]]. |
| `response` or `message.content` | Generated text. | Endpoint proof, not quality proof. |
| `done` and `done_reason` | Whether generation finished and why. | Separates normal stop from truncation, unload, or error-shaped output. |
| `total_duration` | End-to-end generation time in nanoseconds. | User-visible request time from Ollama's perspective. |
| `load_duration` | Model load time in nanoseconds. | Cold-load or model-residency cost. |
| `prompt_eval_count` | Number of input tokens processed. | Prompt/context size and prefill denominator. |
| `prompt_eval_duration` | Prompt-evaluation time in nanoseconds. | Prefill cost. |
| `eval_count` | Number of output tokens generated. | Decode denominator and answer-length confounder. |
| `eval_duration` | Output-token generation time in nanoseconds. | Decode cost and tokens/sec source. |
| `thinking` | Separate thinking output when supported and enabled. | Reasoning trace policy, not automatically quality evidence. |

Ollama's usage metrics are nanosecond values. Convert them before copying into a human-facing row.

## Step 1: Extract A Debrief Row

Run this from the evidence folder after the native response exists:

```powershell
$RunRoot = "<paste-run-folder-path>"
$ResponsePath = "$RunRoot\ollama-native-response.json"
$Response = Get-Content -Raw $ResponsePath | ConvertFrom-Json

function Convert-NsToSeconds($Value) {
  if ($null -eq $Value) { return $null }
  return $Value / 1e9
}

function Round-Optional($Value, $Digits = 3) {
  if ($null -eq $Value) { return $null }
  return [math]::Round($Value, $Digits)
}

$PromptEvalSeconds = Convert-NsToSeconds $Response.prompt_eval_duration
$EvalSeconds = Convert-NsToSeconds $Response.eval_duration
$TotalSeconds = Convert-NsToSeconds $Response.total_duration
$LoadSeconds = Convert-NsToSeconds $Response.load_duration
$PromptTokensPerSecond = if ($Response.prompt_eval_count -and $PromptEvalSeconds -and $PromptEvalSeconds -gt 0) {
  [math]::Round($Response.prompt_eval_count / $PromptEvalSeconds, 2)
} else { $null }
$DecodeTokensPerSecond = if ($Response.eval_count -and $EvalSeconds -and $EvalSeconds -gt 0) {
  [math]::Round($Response.eval_count / $EvalSeconds, 2)
} else { $null }
$GeneratedText = if ($Response.response) {
  $Response.response
} elseif ($Response.message -and $Response.message.content) {
  $Response.message.content
} else {
  ""
}
$ResponseExcerpt = ($GeneratedText -replace "\s+", " ")

[pscustomobject]@{
  model = $Response.model
  done = $Response.done
  done_reason = $Response.done_reason
  total_seconds = Round-Optional $TotalSeconds
  load_seconds = Round-Optional $LoadSeconds
  prompt_tokens = $Response.prompt_eval_count
  prompt_eval_seconds = Round-Optional $PromptEvalSeconds
  prompt_tokens_per_second = $PromptTokensPerSecond
  output_tokens = $Response.eval_count
  decode_seconds = Round-Optional $EvalSeconds
  decode_tokens_per_second = $DecodeTokensPerSecond
  response_excerpt = $ResponseExcerpt.Substring(0, [Math]::Min(160, $ResponseExcerpt.Length))
} | ConvertTo-Json -Depth 5 |
  Tee-Object -FilePath "$RunRoot\first-response-debrief.json"
```

Pass signal: `first-response-debrief.json` exists and includes model, stop state, token counts, converted durations, and decode tokens/sec.

If a field is missing, keep the missing value. Do not invent timing numbers from wall-clock memory.

## Step 2: Decide What The Response Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Native response file exists | Runtime route can generate text. | OpenAI-compatible clients work. |
| OpenAI-compatible response exists | Generic `/v1/chat/completions` route can answer. | Full OpenAI feature compatibility. |
| `model` matches selected tag | The intended model id was used. | Exact local bytes without pull/show evidence. |
| `prompt_eval_count` exists | Runtime processed a prompt and exposed token count. | Tokenizer/template correctness by itself. |
| `eval_count` exists | Runtime generated output tokens. | Answer quality. |
| `done_reason` is normal | Generation reached a stop condition. | Response is useful or safe. |
| Loopback listener proof exists | Endpoint stayed local. | Log/privacy policy is acceptable. |

Write the first sentence like this:

```text
This run proves <route> answered on <boundary> with <model>; it does not yet prove <quality/client/RAG/tool/deployment claim>.
```

## Step 3: Name The Mechanism

Choose the primary mechanism before choosing a next action:

| Observation | Mechanism | Next route |
|---|---|---|
| `load_duration` dominates total time | Cold load or model residency | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]] or [[LLM/Study/Local LLM Observability and Operations Runbook]] |
| `prompt_eval_duration` is high relative to output | Prefill, prompt length, context assembly, tokenizer/template | [[LLM/Study/LLM Inference Request Lifecycle Lab]] and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| `eval_duration` is high per output token | Decode loop, model size, memory bandwidth, quantization, offload | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| `eval_count` is much larger than expected | Output cap, stop condition, prompt looseness | [[LLM/Study/Decoding and Sampling Controls Lab]] |
| Output is fast but wrong | Quality/evaluation, not serving | [[LLM/Study/Local LLM First Quality Probe Suite]] first, then [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Output ignores role or format | Chat template, tokenizer, stop policy, route shape | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Native works but OpenAI-compatible route fails | API compatibility layer | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Route works but client script fails | Client harness, timeout, auth placeholder, JSON parsing | [[LLM/Study/Local LLM Client Harness Lab]] |

The most useful first debrief usually names one of four mechanisms: cold load, prefill, decode, or quality.

## Step 4: Copy The Benchmark Add-On

Copy this into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] or a dated capstone note:

| Field | Value |
|---|---|
| Run id |  |
| Response file |  |
| Runtime and route | Ollama native `/api/generate` / Ollama native `/api/chat` / OpenAI-compatible `/v1/chat/completions` |
| Model |  |
| Prompt class | smoke / known-answer / structured / workload |
| Done reason |  |
| Total seconds |  |
| Load seconds |  |
| Prompt tokens |  |
| Prompt eval seconds |  |
| Prompt tokens/sec |  |
| Output tokens |  |
| Decode seconds |  |
| Decode tokens/sec |  |
| Listener boundary | loopback / exposed / unclear |
| Quality status | route-only / pass / hold / fail |
| Main mechanism | cold load / prefill / decode / quality / route / template / client |
| Next controlled action |  |

Use `route-only` until a quality prompt suite has been scored.

## Step 5: Capstone Decision Row

Copy this row into [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] or the dated capstone note:

| Field | Answer |
|---|---|
| First response debrief status | pass / hold / fail |
| Evidence folder |  |
| Native response file |  |
| OpenAI-compatible response file |  |
| Debrief JSON |  |
| What this proves |  |
| What this does not prove |  |
| Mechanism named | cold load / prefill / decode / KV cache / quantization / sampling / template / quality |
| Metric interpreted | total duration / load duration / prompt eval / eval duration / tokens/sec / missing metrics |
| Next route |  |

Pass means the first response has been interpreted and routed. It does not mean the model is good.

## Failure Handling

| Failure | First action |
|---|---|
| Response JSON cannot parse | Save the raw body and route to [[LLM/Study/Local LLM Troubleshooting Decision Tree]]. |
| No usage fields | Record route limitation and use client wall-clock timing in [[LLM/Study/Local LLM Client Harness Lab]]. |
| `done` is false or stop reason is unclear | Treat as endpoint hold; inspect stream/final chunk behavior. |
| Model id differs from pull gate | Stop and rerun [[LLM/Study/Local LLM First Model Pull Gate]]. |
| Response text is empty | Keep route evidence and diagnose prompt, stop, template, and model. |
| Response is unsafe or exposed beyond loopback | Route to [[LLM/Study/Local LLM Security and Privacy Runbook]] before further testing. |

## Completion Gate

This debrief is complete only when:

- [ ] raw response path is recorded
- [ ] model id is checked against model-pull evidence
- [ ] `done` and `done_reason` are interpreted
- [ ] timing fields are converted from nanoseconds or marked missing
- [ ] prompt and output token counts are copied or marked missing
- [ ] one benchmark add-on row is filled
- [ ] one mechanism is named
- [ ] one next route is chosen
- [ ] route-only evidence is not mistaken for quality proof

## References

Internal routes:

- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama list models API](https://docs.ollama.com/api/tags)
- [Ollama list running models API](https://docs.ollama.com/api/ps)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
