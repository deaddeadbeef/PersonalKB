---
tags: [study, llm, inference, local-llm, tools, function-calling, structured-output, agents, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local LLM Tool Calling and Structured Output Lab

> **One-line summary** A local tool-using LLM is reliable only when tool schemas, model output, runtime parsing, policy checks, execution, tool-result injection, retries, and evaluation are all explicit.

Use this after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]], [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]], and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]. The API contract proves the route can carry tool or schema fields. The decoding lab explains constrained generation. The context lab makes tool schemas and tool results part of the token budget. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] when the same boundary should be saved as JSON, CSV, Markdown, and JSONL evidence.

Use this before building an agent loop, file assistant, API wrapper, database helper, or local RAG assistant that can call tools. Pair it with [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before any tool reads files, writes files, calls a network API, runs code, or touches private data.

## Outcome

After this lab you should be able to:

- distinguish structured output, function calling, tool execution, and agent loops
- define a small tool with JSON Schema and strict validation rules
- prove whether a local runtime supports `tools`, `tool_choice`, structured output, JSON mode, or best-effort parsing
- execute a single harmless local tool call and feed the result back to the model
- add a bounded multi-turn tool loop with stop, retry, timeout, and approval rules
- evaluate wrong-tool, bad-argument, unsafe-action, malformed-output, and stale-result failures

## Mental Model

Tool calling is not the model doing the work. The model emits a structured request. Your application validates the request, checks policy, executes the tool if allowed, and returns the result as a new message or observation.

The safe loop is:

```text
user task
  -> model chooses text or tool call
  -> runtime parses tool name and arguments
  -> schema validation
  -> policy/permission check
  -> tool execution
  -> tool result injected back into conversation
  -> model produces final answer or another tool call
```

The academic anchor is [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]]. The systems anchor is [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops|Tool Selection and Execution Loops]]. The reliability anchor is [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]].

## Structured Output Versus Tool Calling

| Pattern | Use when | Pass signal |
|---|---|---|
| Prompt-only JSON | A quick exploratory script can tolerate parse failures and retries. | Output usually parses, but failures are expected and logged. |
| Structured response format | The final answer must match a schema and no external action is needed. | Parser accepts the result on first pass or the runtime guarantees schema adherence. |
| Function/tool calling | The model needs external data or an action from your application. | Tool name and arguments validate, policy approves, execution succeeds, and the final answer uses the result. |
| Agent loop | The task may need multiple observations and actions. | Loop stops under explicit completion, max-iteration, timeout, or human-approval rules. |

Do not use tool calling just to get JSON if no tool will execute. Use structured output for final typed answers. Use tool calling when the model must ask the application for data or action.

## Runtime Support Map

| Runtime or API surface | Tool/schema path | What to verify |
|---|---|---|
| Ollama native chat | `tools` in `/api/chat`, tool result returned as a tool-role message | Model supports tool use, tool calls parse, tool result injection works, multi-turn loop stops. |
| OpenAI-compatible local routes | `tools`, `tool_choice`, response format, or runtime-specific extras | Compatibility route may support chat but not the tool semantics your client expects. |
| vLLM | Named and required function calling use structured-output backends; auto tool choice needs parser flags | `tool_choice`, selected parser, strict mode, first-call schema/FSM latency, and schema adherence. |
| llama.cpp server | OpenAI-compatible routes plus schema-constrained JSON and tool-use support | Exact server build, chat template/tool parser, response shape, and schema constraint behavior. |
| llama-cpp-python | `response_format` for JSON/schema and high-level function/tool calling formats | `chat_format`, JSON schema mode, tool-call response shape, and local model compatibility. |
| Hosted OpenAI-style APIs | Function tools and structured outputs are separate interface choices | Use as a reference contract, but do not assume local servers match every hosted field. |

Pass signal: your [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|API contract card]] says which tool/schema fields are supported, ignored, translated, or unsupported.

## Lab 1: Tool Contract Card

Choose one harmless read-only tool. Start with arithmetic or lookup over a tiny local dictionary before using files or networks.

| Field | Value |
|---|---|
| Tool name |  |
| Purpose |  |
| Read/write/network/shell class | read-only / write / network / shell |
| Allowed input schema |  |
| Disallowed inputs |  |
| Runtime route | native / `/v1/chat/completions` / `/v1/responses` / other |
| `tool_choice` mode | none / auto / required / named |
| Validation library or parser |  |
| Policy check |  |
| Timeout and retry limit |  |
| Tool result format |  |
| Log fields |  |

Starter schema rules:

- Give the tool one clear responsibility.
- Use specific names and descriptions.
- Prefer enums or bounded strings over free-form strings.
- Require every needed field.
- For strict local/hosted compatibility, test `additionalProperties: false` where supported.
- Treat optional fields as a real schema decision, not a vague prompt instruction.

## Lab 2: Structured Output Baseline

Before executing a tool, prove the model/runtime can produce a typed final answer.

| Test | Expected schema | Runtime support | Parse result | Decision |
|---|---|---|---|---|
| Prompt-only JSON |  |  | pass / fail |  |
| Structured response format or JSON schema |  |  | pass / fail / unsupported |  |
| Malformed-output recovery |  |  | retry / fail closed |  |

Pass signal: you can separate "the model cannot produce valid structure" from "tool execution failed."

## Lab 3: Single Tool Call

Run one deterministic request where the correct behavior is to call exactly one harmless tool.

| Step | Evidence |
|---|---|
| Request includes the tool definition | Saved redacted request body or config. |
| Model emits a tool call | Tool name and argument object. |
| Arguments validate | Schema validator result. |
| Policy approves execution | Allow/deny decision and reason. |
| Tool executes | Result value or controlled error. |
| Tool result is injected back | Tool-role or runtime-specific result message. |
| Final answer uses the result | Answer text and support check. |

Use temperature `0` or the lowest supported deterministic setting for the first proof. Raise sampling only after the integration passes.

## Lab 4: Wrong Tool And Bad Argument Tests

Force failures before relying on the loop.

| Failure | How to trigger | Expected behavior |
|---|---|---|
| Unknown tool name | Remove a tool or ask for an unavailable action | Runtime refuses or asks clarification; no execution. |
| Missing required argument | Use an ambiguous user request | Validator blocks execution and returns repairable error. |
| Invalid enum/path/id | Ask for a disallowed value | Policy denies before tool runs. |
| Tool timeout | Use a controlled slow mock | Loop records timeout and stops or retries once. |
| Tool error | Mock an exception | Error result is fed back without crashing the harness. |
| Unsafe action | Ask to write/delete/call network without permission | Approval boundary blocks execution. |

Pass signal: every failure becomes a structured row, not a silent model hallucination or uncontrolled action.

## Lab 5: Bounded Multi-Turn Tool Loop

Build the smallest loop that can call a tool, observe the result, and decide whether to stop.

| Loop control | Setting |
|---|---|
| Maximum iterations |  |
| Maximum parallel calls |  |
| Per-tool timeout |  |
| Retry limit |  |
| Approval-required tool classes |  |
| Stop condition | final answer / no tool call / max iterations / error limit / user interrupt |
| Tool result truncation policy |  |
| Log destination |  |

Completion logic matters more than clever prompting. A tool loop without max iterations, timeouts, and denial behavior is not safe enough for local private use.

## Lab 6: Tool Evaluation Row

Add one tool-specific prompt to [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

| Run id | Model/runtime | Prompt id | Tool expected? | Tool selected | Args valid? | Policy result | Execution result | Final answer supported? | Decision |
|---|---|---|---|---|---|---|---|---|---|
|  |  | T-01 | Yes/No |  | Yes/No | allow/deny | pass/fail | Yes/No | Pass/Hold/Fail |

Score the tool loop separately from the final prose. A fluent final answer fails if it used the wrong tool, ignored the tool result, or bypassed policy.

## Failure Triage

| Symptom | Likely layer | First fix |
|---|---|---|
| Tool call appears as prose | Runtime route, chat template, or model lacks tool parser | Recheck API contract and chat template. |
| Arguments are invalid JSON | Structured-output enforcement missing or prompt too loose | Use schema/grammar support or lower sampling. |
| Correct JSON, wrong tool | Tool descriptions overlap or tool list is too broad | Rename tools, sharpen descriptions, reduce visible tool set. |
| Correct tool, unsafe arguments | Policy boundary missing | Validate and deny before execution. |
| Tool result ignored | Result injection format or context budget issue | Inspect tool-role message and context budget. |
| Loop never stops | Missing iteration/error stop rule | Add max iterations and explicit done criteria. |
| First tool call is slow | Schema/FSM compilation or runtime overhead | Warm up schema path and record first-call latency separately. |
| Local server supports chat but not tools | Compatibility gap | Use native route, another runtime, prompt-only fallback, or no-tool decision. |

## Benchmark Add-On

Add these fields to [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] when the workload uses tools:

| Field | Why |
|---|---|
| Tool schema version | Makes argument behavior reproducible. |
| Tool-choice mode | Explains auto, forced, required, or disabled behavior. |
| Tool parser / structured-output backend | Explains local runtime compatibility and latency. |
| Tool-call count | Normalizes latency across single-turn and agent loops. |
| Validation result | Separates model output errors from tool execution errors. |
| Policy decision | Proves unsafe actions were not executed by model fiat. |
| Tool execution latency | Separates model latency from external work. |
| Tool result token count | Explains context growth after observations. |

## Completion Gate

This lab is complete when you have:

- [ ] one tool contract card for a harmless read-only tool
- [ ] one structured-output baseline before tool execution
- [ ] one single-tool call with validated arguments and injected result
- [ ] one wrong-tool or bad-argument failure row
- [ ] one unsafe-action denial row if any tool can read files, write files, call network, or run commands
- [ ] optional runner output from [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] when the proof needs repeatable artifacts
- [ ] one bounded multi-turn loop with max iterations, timeout, retry, and stop rules
- [ ] one quality-harness tool row with pass/hold/fail decision
- [ ] one benchmark row updated with tool-call fields
- [ ] one security/logging decision for tool inputs, outputs, and traces

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/2023 — Open Models and Agents/Function Calling]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops]]
- [[LLM/Study/Agents and Evaluation - Review Drill]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]

Current external docs checked 2026-06-15:

- [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [OpenAI structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling)
- [vLLM tool calling](https://docs.vllm.ai/en/latest/features/tool_calling/)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama-cpp-python structured output and function calling](https://llama-cpp-python.readthedocs.io/en/latest/)
