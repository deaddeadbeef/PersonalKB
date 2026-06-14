---
tags: [study, llm, inference, local-llm, security, privacy, runbook]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Security and Privacy Runbook

> **One-line summary** Local inference reduces provider exposure, but it still creates an application server that can leak prompts, documents, logs, tool outputs, and model access if endpoint, storage, and trust boundaries are weak.

Use this with [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] before moving beyond a one-person loopback experiment. The serving runbook proves the model can answer; this runbook proves the local setup has a defensible privacy and exposure boundary. Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] before loading weights from a registry, gated model, converted artifact, or unknown local file. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to record auth behavior, base URL, route, feature gaps, and harmless failure behavior before connecting generic clients. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] before executing any model-requested tool call. Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] for the host, port, listener, runtime-boundary, and logging evidence behind this checklist. Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] when the security boundary should decide whether the workload belongs on local CPU/GPU, self-hosted infrastructure, a hosted API, hybrid RAG, or batch inference.

## Security Model

Local does not automatically mean private. A local model avoids sending prompts to an external model provider, but the local stack still has surfaces:

| Surface | What can leak or break |
|---|---|
| Model endpoint | Anyone who can reach the port may be able to send prompts, read outputs, or exhaust resources. |
| Web UI | Browser sessions, saved chats, uploaded files, provider settings, and admin panels may expose data. |
| Logs | Prompts, retrieved passages, tool results, generated answers, headers, and stack traces can persist. |
| RAG corpus | Indexed private documents may be retrievable through indirect prompts or weak citation boundaries. |
| Tool calls | A model can request actions that read files, call APIs, or mutate state if the runtime allows it. |
| Tunnels and LAN binding | A loopback toy server becomes a network service once bound to LAN, VPN, reverse proxy, or tunnel. |

The safe default is single-user, loopback-only, no public tunnel, minimal logs, no write-capable tools, and no sensitive corpus until the boundary is explicit.

## Exposure Levels

| Level | Access | Requirements before using |
|---|---|---|
| 0. Offline CLI | No listening network port | Model file provenance, local prompt/output handling, no secrets in prompts. |
| 1. Loopback API | `127.0.0.1` / `localhost` only | Confirm bind address, use non-sensitive test prompts, log minimally. |
| 2. Local desktop UI | Browser UI on same machine | Check saved-chat storage, uploads, provider settings, and local account boundary. |
| 3. LAN or VPN service | Other devices can reach it | Authentication, firewall allowlist, log policy, resource limits, and user separation. |
| 4. Internet/tunnel/reverse proxy | External clients can reach it | Do not use for experiments unless you have explicit auth, TLS, abuse controls, monitoring, and a reason to accept the risk. |

Do not skip levels. A setup that is acceptable at Level 1 is not automatically acceptable at Level 3.

## Pre-Run Checklist

Before starting a local server:

- [ ] Workload is named: personal chat, coding helper, RAG assistant, extraction API, agent, or benchmark.
- [ ] Model source, license, exact revision, and unsafe artifact risk are recorded.
- [ ] Data sensitivity is named: public, personal, private, regulated, secret, or mixed.
- [ ] Endpoint bind address is planned: loopback by default.
- [ ] Port is known and not shared with another service.
- [ ] Authentication decision is explicit: none only for loopback experiments.
- [ ] Log policy is explicit: what is logged, where, how long, and whether prompts/documents are included.
- [ ] RAG corpus boundary is explicit before documents are indexed.
- [ ] Tool permissions are read-only unless there is a separate approval boundary.
- [ ] Model output is treated as untrusted until validated by [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

## Endpoint Boundary Checks

Run these checks for a local API proof:

| Check | Evidence to save |
|---|---|
| Server listens only where intended | Bind address and port from server command, UI setting, or process list. |
| Loopback request succeeds | Smoke-test response from `localhost` or `127.0.0.1`. |
| Non-loopback access is intentionally blocked or authenticated | Firewall, proxy, or auth setting. |
| API key or bearer token is not a real secret reused elsewhere | Local placeholder or separate scoped token. |
| CORS or browser access is not broader than needed | UI/proxy setting if a browser app calls the endpoint. |
| Resource exhaustion is considered | Concurrency, max tokens, context length, and model size limits. |

Useful Windows inspection command:

```powershell
Get-NetTCPConnection -State Listen |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,30000 } |
  Select-Object LocalAddress,LocalPort,OwningProcess
```

Pass signal: you can explain who can reach the model server and why.

## Prompt, Log, And Storage Map

Create this map before using private data:

| Data class | Example | Stored where | Retention | Redaction needed? |
|---|---|---|---|---|
| Prompt text | User request, system prompt |  |  |  |
| Retrieved passages | RAG chunks, citations |  |  |  |
| Generated output | Chat answer, JSON result |  |  |  |
| Tool results | File contents, API responses |  |  |  |
| Uploaded files | PDFs, notes, exports |  |  |  |
| Server logs | Requests, errors, timings |  |  |  |
| Evaluation records | Prompt suite, scores, examples |  |  |  |

If a prompt is too sensitive to appear in a plain-text log, it is too sensitive to use until the logging path is understood.

## RAG Privacy Checks

Pair this section with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]].

Before building the index, write down which fields from the harness artifacts may be logged or shown in citations: raw paths, source titles, chunk text, source ids, digests, retrieval scores, and generated answers. Private file paths and sensitive note titles may need redacted citation labels.

| Risk | Guardrail |
|---|---|
| Private corpus indexed without a versioned boundary | Record corpus version, source folder, and inclusion rules before embedding. |
| Retrieved private passages shown to the wrong user | Keep single-user scope or add access control before multi-user use. |
| Prompt injection inside documents overrides instructions | Treat retrieved text as untrusted evidence, not instructions. |
| Citation output exposes paths or secret filenames | Choose citation style deliberately and redact sensitive paths. |
| Evaluation logs contain private source text | Store only minimal excerpts or synthetic test cases when possible. |
| Stale index answers from removed documents | Rebuild or delete index when corpus membership changes. |

The key idea from [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning|System Prompts and Role Conditioning]] is that trusted instructions and untrusted text share the same context window. Retrieved documents should not be allowed to redefine the assistant's policy, tools, or output boundary.

## Tool And Agent Boundary

If the local model can call tools, use the boundary from [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]] and prove it with [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]]: the model requests actions; the runtime decides whether to execute them.

| Tool class | Default policy |
|---|---|
| Pure read-only lookup | Allow only scoped paths or datasets. |
| File read | Restrict to an allowlisted folder; log path, not full content. |
| File write | Require explicit approval or sandbox output path. |
| Shell command | Avoid for local assistant experiments; require a separate approval boundary. |
| Network/API call | Allowlist destination and method; never let the model choose credentials. |
| Browser or UI control | Treat as high risk; separate observation from action. |

Never treat a model-generated tool call as permission. Validate schema, check policy, execute with least privilege, and record the decision.

Tool-call logs should record tool name, argument validity, policy decision, execution status, and a short redacted result summary. Avoid logging full file contents, credentials, private documents, or raw network responses unless the data boundary explicitly allows it.

## Incident Triage

| Symptom | First action |
|---|---|
| Endpoint reachable from another device unexpectedly | Stop server, bind to loopback, inspect firewall/proxy settings. |
| Logs contain private prompts or documents | Stop run, move or delete logs according to policy, reduce logging, rerun with test data. |
| RAG answer cites private path or secret name | Change citation style, redact metadata, rebuild index if needed. |
| Model follows instructions from retrieved document | Strengthen context delimiter and policy, then add an injection test to the quality harness. |
| Tool call tries to read or write outside scope | Block execution, tighten allowlist, add regression test. |
| Server is slow or unresponsive under load | Reduce context/max tokens/concurrency before exposing to more users. |

## Go / No-Go Gate

Move from loopback experiment to shared service only when all are true:

- [ ] Endpoint access is intentional and documented.
- [ ] Authentication or network allowlisting exists for non-loopback access.
- [ ] Prompt, output, upload, and log storage locations are known.
- [ ] RAG corpus access is scoped and versioned.
- [ ] Tool permissions are least-privilege and validated outside the model.
- [ ] Prompt injection and private-data leakage tests are included in the evaluation harness.
- [ ] Resource limits prevent accidental runaway generation or denial of service.
- [ ] Deployment path is justified against privacy, quality, latency, cost, and operations evidence.
- [ ] Rollback plan is clear: stop command, service location, log location, and index location.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning]]
- [[LLM/2023 — Open Models and Agents/Function Calling]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[chunk-llm-119 PagedAttention Copy-on-Write Sharing]]
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]]
