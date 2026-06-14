---
tags: [study, llm, inference, local-llm, api, openai-compatible, contract, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-14
---

# Local LLM OpenAI-Compatible API Contract Lab

> **One-line summary** A local server is "OpenAI-compatible" only after you prove the base URL, model id, route, request fields, response shape, streaming behavior, errors, and unsupported features that your client actually depends on.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves that a model endpoint answers at all. Use it before [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] so the harness is testing a known API contract instead of guessing at a runtime's compatibility surface. Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] to decide which sampler fields must be accepted, ignored, translated, or rejected for the workload. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] after the contract says whether `tools`, `tool_choice`, JSON/schema output, and tool-call response fields are dependable.

Pair this with [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the failure may come from artifact format, tokenizer, chat template, quantization, or runtime support. Pair it with [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] when the HTTP call succeeds but chat behavior is wrong.

## Outcome

After this lab you should be able to:

- state exactly which local base URL and route your client is using
- distinguish native runtime APIs from OpenAI-compatible compatibility routes
- prove one non-streaming chat request, one streaming chat request, and one harmless failure case
- record which OpenAI-style features are supported, ignored, translated, or unsupported by the local runtime
- decide whether a generic OpenAI client can safely point at the local server for your workload

## Mental Model

OpenAI-compatible does not mean "identical to OpenAI's hosted platform." It means the local server accepts enough of an OpenAI-style request and returns enough of an OpenAI-style response for a chosen client and workload.

The compatibility boundary is a contract between five things:

| Layer | Contract question | Evidence |
| --- | --- | --- |
| Base URL | Does the client point at the local `/v1` surface, not the native runtime route? | `base_url`, port, host binding, and route. |
| Model id | Does the requested `model` match the served model name? | `/v1/models`, runtime model list, or server config. |
| Request shape | Are `messages`, `temperature`, `max_tokens`, `stream`, tools, JSON mode, and stop settings accepted? | Saved request body and response or error body. |
| Response shape | Can the client extract content, finish reason, usage, tool calls, or structured output? | Parsed response fields plus raw excerpt if needed. |
| Streaming | Does the stream use server-sent events or another chunk shape the client understands? | First event, first content delta, final event, chunk count. |
| Error behavior | Do unsupported fields, bad model ids, wrong routes, and bad JSON fail in a diagnosable way? | HTTP status, error class, body excerpt, first fix. |
| Feature gap | Which OpenAI-style fields are ignored, translated, or absent? | Compatibility card and runtime docs. |

If any field above is unknown, treat the endpoint as an experiment. Do not reuse it for tools, RAG, private documents, or benchmark comparisons yet.

When the workload needs tools, the contract card is only the first gate. The tool loop still needs schema validation, policy checks, execution logging, and bounded retries in [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]].

## Runtime Contract Map

| Runtime | Native surface | OpenAI-compatible surface to test | Contract notes |
| --- | --- | --- | --- |
| Ollama | `http://localhost:11434/api` | `http://localhost:11434/v1/chat/completions`, `/v1/completions`, `/v1/responses` | Native API is useful for Ollama-specific timings. OpenAI-compatible routes support common chat/completion features, but context size is set through a `Modelfile`, not the OpenAI request. |
| LM Studio | LM Studio REST API under `/api/v1` | `http://localhost:1234/v1` by default | Good desktop API compatibility path. Its native `/api/v1/chat` and compatibility endpoints have different feature surfaces, so record which one the client uses. |
| llama.cpp `llama-server` | llama.cpp server routes and web UI | OpenAI-compatible chat completions, responses, embeddings, and related routes | Good for GGUF, CPU/GPU edge serving, schema-constrained JSON, monitoring, and low-level control. Verify the exact server binary and flags. |
| llama-cpp-python server | Python server wrapper | `python3 -m llama_cpp.server --model <model_path>` then chosen `/v1` endpoint | Useful when Python packaging is easier than building llama.cpp directly. Record `chat_format`, tokenizer, context, and model path. |
| vLLM | vLLM serving stack | OpenAI-compatible `/v1/completions`, `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, plus utility routes such as `/health` | Strong GPU/server fit. Chat completions require a text-generation model with a chat template; some request fields are ignored or unsupported. |
| Other compatible servers | Runtime-specific | Usually `/v1/chat/completions` | Do not assume support from the name. Run the same contract probes and record unsupported fields. |

## Compatibility Card

Copy this before wiring a client library to the endpoint.

| Field | Value |
| --- | --- |
| Workload |  |
| Runtime and version |  |
| Startup command or GUI setting |  |
| Host binding | loopback / LAN / remote |
| Base URL |  |
| Route | `/v1/chat/completions` / `/v1/responses` / `/v1/completions` / native |
| Served model id |  |
| Model artifact | Ollama tag / GGUF / HF directory / quantized checkpoint |
| Auth behavior | none / placeholder bearer / real token / reverse proxy |
| Non-streaming chat | pass / fail / not tested |
| Streaming chat | pass / fail / unsupported / not tested |
| Models route or model-list proof |  |
| Usage fields returned? | prompt tokens / output tokens / total tokens / none |
| Tool calls | pass / fail / unsupported / not needed |
| JSON or schema output | pass / fail / unsupported / not needed |
| Responses API | pass / fail / unsupported / not needed |
| Embeddings route | pass / fail / unsupported / not needed |
| Ignored or unsupported fields |  |
| Error behavior checked | wrong model / wrong route / bad JSON / unsupported field |
| Security boundary checked | loopback / auth / logs / private corpus |
| Client decision | compatible / partial / not compatible |

## Probe 1: Route And Model List

First prove that the client and server agree on base URL and model name.

```powershell
$BaseUrl = "http://localhost:1234/v1"

try {
  Invoke-RestMethod `
    -Uri "$BaseUrl/models" `
    -Method Get `
    -Headers @{ Authorization = "Bearer local" } `
    -TimeoutSec 30
}
catch {
  $_.Exception.Message
  if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode }
}
```

If `/v1/models` is absent but the chat route works, record the runtime-native model-list proof instead. The contract needs an exact served model id; it does not require every runtime to expose the same discovery route.

## Probe 2: Non-Streaming Chat

Use this as the baseline contract. Keep it boring and deterministic.

```powershell
$BaseUrl = "http://localhost:1234/v1"
$Model = "<served-model-id>"
$Body = @{
  model = $Model
  messages = @(
    @{ role = "system"; content = "Answer exactly as requested." }
    @{ role = "user"; content = "Reply with exactly: api contract ok" }
  )
  temperature = 0
  max_tokens = 32
  stream = $false
} | ConvertTo-Json -Depth 8

Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body `
  -TimeoutSec 120
```

Pass signal:

- HTTP success
- assistant content is extractable at the expected response path
- model id in the response is understandable, even if rewritten by the runtime
- finish reason or stop behavior is recorded
- usage fields are recorded if present, and explicitly marked absent if not

## Probe 3: Streaming Chat

Streaming compatibility fails more often than non-streaming compatibility because chunk shapes differ. Use the client you plan to use in the real workflow, then record the actual event shape.

| Check | Evidence |
| --- | --- |
| HTTP stream opens | First event timestamp. |
| User-visible token appears | First non-empty content delta timestamp. |
| Final event is detected | Final event text, done marker, or connection close behavior. |
| Partial JSON does not crash parser | Raw first two event excerpts saved locally if parser fails. |
| Usage accounting | Usage present in final chunk, separate event, absent, or runtime-specific. |
| Cancellation behavior | Ctrl+C/client abort leaves server healthy or produces a known error. |

If the real client does not need streaming, write "not required for workload" instead of forcing a streaming dependency.

## Probe 4: Feature Gap Test

Pick only the features your workload needs.

| Feature | Minimal test | Failure meaning |
| --- | --- | --- |
| Tool call | Send one no-op JSON-schema tool and inspect returned tool call shape. | Client cannot assume hosted-provider tool semantics. |
| JSON mode or schema | Ask for a strict object and validate it with a parser. | Prompt-only structure may not be enough; consider constrained decoding. |
| Responses API | Send a minimal `/v1/responses` request if the client uses that API. | Use chat completions or runtime-native route instead. |
| Embeddings | Send one short input to `/v1/embeddings` only if the served model is an embedding/pooling model. | Chat model and embedding model may need separate endpoints. |
| Logprobs | Request logprobs only when the runtime docs claim support. | Evaluation harness may need a different runtime or route. |
| Sampler fields | Send the temperature, top-p, top-k, min-p, seed, stop, and penalty fields the workload depends on. | A compatibility route may silently ignore local sampler controls. |
| Multimodal input | Send one tiny image/text request only when the model and runtime support vision. | Model family, template, and runtime feature must all align. |

Do not use a passing chat request as proof that tools, embeddings, JSON schema, images, or the Responses API work.

## Probe 5: Harmless Failure

Force one failure so the client harness can prove error logging before real work.

| Failure | How to trigger | Useful evidence |
| --- | --- | --- |
| Wrong model | Append `-missing` to the model id. | HTTP status, error body, first fix. |
| Wrong route | Use `/chat/completion` or omit `/v1`. | Confirms route diagnosis. |
| Bad JSON | Send malformed body from a disposable shell. | Confirms parser/server boundary. |
| Unsupported field | Send one feature you know the runtime does not support. | Documents compatibility gap. |
| Timeout | Set a very small timeout for a long prompt. | Confirms timeout classification. |

The failure row is part of the contract. A local server that only works on happy-path prompts is not ready for toolchains, RAG, or benchmark automation.

## Client Handoff

After the probes pass, hand these values to [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]:

| Harness field | Source in this lab |
| --- | --- |
| `runtime` | Compatibility card. |
| `base_url` | Route and model-list probe. |
| `route` | Chat, responses, completions, embeddings, or native route. |
| `model_id` | Served model id proof. |
| `stream` | Streaming probe result. |
| `sampling` | Non-streaming baseline request. |
| `error_contract` | Harmless failure row. |
| `feature_flags` | Tool/JSON/responses/embeddings decisions. |
| `security_boundary` | Loopback/auth/logging decision. |

If a generic client library requires a hosted-provider-only field, do not hide that mismatch with adapter code until the contract card records it.

## Completion Gate

This lab is complete when you have:

- [ ] a compatibility card for one local server
- [ ] exact base URL, route, and served model id
- [ ] one non-streaming chat response
- [ ] one streaming result or explicit "not required/unsupported" note
- [ ] one harmless failure row with HTTP status or error class
- [ ] a list of supported, ignored, and unsupported OpenAI-style fields needed by the workload
- [ ] a decision: compatible, partial compatibility with adapter, or not compatible
- [ ] a client harness config updated from this contract
- [ ] a handoff to [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] if tools or structured final answers are required

## References

Internal evidence:

- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]

Current external docs checked 2026-06-14:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [LM Studio REST API](https://lmstudio.ai/docs/developer/rest)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama-cpp-python OpenAI-compatible server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [vLLM online serving](https://docs.vllm.ai/en/stable/serving/online_serving/)
