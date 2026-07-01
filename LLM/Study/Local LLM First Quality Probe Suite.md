---
tags: [study, llm, evaluation, local-llm, ollama, quality, inference, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Quality Probe Suite

> **One-line summary** After a local endpoint answers once, run this tiny private prompt suite to decide whether the response is only route proof or whether it has enough first quality evidence to enter the full harness.

Use this after [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] or [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]] has interpreted the first saved response. The debrief proves the local route answered and names the timing mechanism. This suite asks the next question: can the same local endpoint handle a few controlled quality probes without changing model, runtime, sampler, route, or evidence folder? Use [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]] when you want the same suite captured as Python request, response, output, score, CSV, Markdown, and JSONL artifacts.

Use [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] when one of these prompts should be rerun through a reusable OpenAI-compatible client instead of a native Ollama route. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] after this when a real workload, model selection, quantization decision, RAG assistant, or deployment choice needs a scored acceptance gate. This note is smaller: it is the first quality bridge between smoke output and a formal harness.

## What This Proves

| Result | Proves | Does not prove |
|---|---|---|
| All requests save request/response files | The local endpoint can run a fixed prompt suite. | The model is good for the target workload. |
| Arithmetic or known-answer prompt passes | The model can handle one locally checkable question. | Broad reasoning, factuality, or benchmark performance. |
| JSON prompt returns valid JSON | The route and prompt can support one structured-output constraint. | Tool calling, full schema reliability, or client compatibility. |
| Extraction prompt uses only supplied text | The model can ground an answer in provided context. | RAG retrieval quality or long-context behavior. |
| Missing-evidence prompt refuses or narrows | The model can avoid unsupported claims in one case. | Safety, policy, or jailbreak robustness. |
| Timing fields are attached | Quality rows can be read alongside latency evidence. | Scheduler, concurrency, or production throughput. |

Treat this suite as a first gate, not a leaderboard. It is useful because it is private, reproducible, and close to the local endpoint you actually run.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Runtime | Ollama native `/api/chat` / other |
| Base URL | `http://127.0.0.1:11434` |
| Model id |  |
| Model-pull evidence |  |
| First response debrief |  |
| Temperature | `0` |
| Output cap | `256` unless the prompt says otherwise |
| Route boundary | loopback / exposed / unclear |
| Scorer | human / script-assisted / LLM judge support |

Do not compare quality across runs unless these conditions are fixed or the changed condition is the experiment.

## Probe Set

These prompts are intentionally local and self-authored. They avoid copied public benchmark examples.

| Prompt id | Task class | User prompt | Expected first signal |
|---|---|---|---|
| K-01 | Known-answer arithmetic | `Compute 17 * 23 + 19. Return exactly: answer=<number>; reason=<one short sentence>.` | Contains `answer=410` and a short reason. |
| S-01 | Structured output | `A local model produced 128 output tokens in 4 seconds. Return JSON with keys "tokens", "seconds", "tokens_per_second", and "caveat".` | Valid JSON; `tokens_per_second` is `32`. |
| X-01 | Extraction from supplied text | `Text: "The local server is bound to 127.0.0.1, the selected model is qwen3.5:4b, and the run folder is D:\LLM-Runs\first." Extract server, model, and run_folder as a three-row markdown table. Do not add facts.` | Keeps only the three supplied facts. |
| G-01 | Grounded refusal | `Using only this text: "The model tag is qwen3.5:4b." What GPU is being used? If the answer is not present, say exactly: not enough evidence.` | Says `not enough evidence`. |
| C-01 | Constraint following | `Give two bullet points. Each bullet must have exactly five words. Topic: why route proof is not quality proof.` | Two bullets only; each bullet has five words. |

Replace `qwen3.5:4b` with the model id from the run only if the prompt needs to reflect the actual model tag. Keep the expected-answer logic stable.

## PowerShell Runner

Run this from a new PowerShell after the local endpoint is already running:

```powershell
$RunRoot = "<paste-run-folder-path>"
$Model = "<paste-model-tag>"
$BaseUrl = "http://127.0.0.1:11434"
$SuiteRoot = Join-Path $RunRoot "first-quality-probe-suite"
New-Item -ItemType Directory -Force -Path $SuiteRoot | Out-Null

$Cases = @(
  [pscustomobject]@{
    id = "K-01"
    task_class = "known-answer arithmetic"
    system = "Answer the user exactly. Keep reasoning to one short sentence."
    user = "Compute 17 * 23 + 19. Return exactly: answer=<number>; reason=<one short sentence>."
    expected = "answer=410"
    format = $null
  },
  [pscustomobject]@{
    id = "S-01"
    task_class = "structured output"
    system = "Return only valid JSON. Do not wrap it in markdown."
    user = "A local model produced 128 output tokens in 4 seconds. Return JSON with keys `"tokens`", `"seconds`", `"tokens_per_second`", and `"caveat`"."
    expected = "32"
    format = "json"
  },
  [pscustomobject]@{
    id = "X-01"
    task_class = "extraction"
    system = "Use only the provided text. Do not add facts."
    user = "Text: `"The local server is bound to 127.0.0.1, the selected model is qwen3.5:4b, and the run folder is D:\LLM-Runs\first.`" Extract server, model, and run_folder as a three-row markdown table. Do not add facts."
    expected = "127.0.0.1"
    format = $null
  },
  [pscustomobject]@{
    id = "G-01"
    task_class = "grounded refusal"
    system = "Use only the supplied text. If the answer is absent, follow the requested refusal string exactly."
    user = "Using only this text: `"The model tag is qwen3.5:4b.`" What GPU is being used? If the answer is not present, say exactly: not enough evidence."
    expected = "not enough evidence"
    format = $null
  },
  [pscustomobject]@{
    id = "C-01"
    task_class = "constraint following"
    system = "Follow the format constraints exactly."
    user = "Give two bullet points. Each bullet must have exactly five words. Topic: why route proof is not quality proof."
    expected = "-"
    format = $null
  }
)

$Rows = foreach ($Case in $Cases) {
  $Body = @{
    model = $Model
    stream = $false
    messages = @(
      @{ role = "system"; content = $Case.system },
      @{ role = "user"; content = $Case.user }
    )
    options = @{
      temperature = 0
      num_predict = 256
    }
  }
  if ($Case.format) {
    $Body.format = $Case.format
  }

  $RequestPath = Join-Path $SuiteRoot "$($Case.id)-request.json"
  $ResponsePath = Join-Path $SuiteRoot "$($Case.id)-response.json"
  $Body | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 -Path $RequestPath

  $Status = "ok"
  $ErrorText = $null
  try {
    $Response = Invoke-RestMethod -Method Post -Uri "$BaseUrl/api/chat" -ContentType "application/json" -Body (Get-Content -Raw $RequestPath)
    $Response | ConvertTo-Json -Depth 12 | Set-Content -Encoding utf8 -Path $ResponsePath
    $Text = if ($Response.message -and $Response.message.content) { $Response.message.content } else { "" }
  } catch {
    $Status = "error"
    $ErrorText = $_.Exception.Message
    $Response = $null
    $Text = ""
    [pscustomobject]@{ error = $ErrorText } | ConvertTo-Json -Depth 3 | Set-Content -Encoding utf8 -Path $ResponsePath
  }

  $JsonValid = $null
  if ($Case.format -eq "json" -and $Text) {
    try {
      $null = $Text | ConvertFrom-Json
      $JsonValid = $true
    } catch {
      $JsonValid = $false
    }
  }

  $ExpectedHit = if ($Case.expected) {
    $Text -match [regex]::Escape($Case.expected)
  } else {
    $null
  }

  [pscustomobject]@{
    run_id = Split-Path $RunRoot -Leaf
    prompt_id = $Case.id
    task_class = $Case.task_class
    model = $Model
    status = $Status
    response_path = $ResponsePath
    total_duration_ns = if ($Response) { $Response.total_duration } else { $null }
    prompt_eval_count = if ($Response) { $Response.prompt_eval_count } else { $null }
    eval_count = if ($Response) { $Response.eval_count } else { $null }
    done = if ($Response) { $Response.done } else { $null }
    done_reason = if ($Response) { $Response.done_reason } else { $null }
    expected_signal = $Case.expected
    expected_signal_seen = $ExpectedHit
    json_valid = $JsonValid
    human_score = ""
    decision = "unscored"
    error = $ErrorText
    response_excerpt = ($Text -replace "\s+", " ").Substring(0, [Math]::Min(180, ($Text -replace "\s+", " ").Length))
  }
}

$Rows | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 -Path (Join-Path $SuiteRoot "quality-probe-results.json")
$Rows | ConvertTo-Csv -NoTypeInformation | Set-Content -Encoding utf8 -Path (Join-Path $SuiteRoot "quality-probe-results.csv")
$Cases | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 -Path (Join-Path $SuiteRoot "quality-probe-cases.json")
```

Pass signal: the suite folder contains request files, response files, `quality-probe-results.json`, `quality-probe-results.csv`, and `quality-probe-cases.json`. If using [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]], also preserve its results Markdown and `quality-probe-runs.jsonl` file.

## Scoring Row

Fill one row per prompt after reading the saved response:

| Run id | Prompt id | Task class | Output path | Fact | Instr | Format | Ground | Complete | Safe | Latency acceptable | Decision | Failure owner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | K-01 | known-answer arithmetic |  | 0/1/2 | 0/1/2 | 0/1/2 | n/a | 0/1/2 | 0/1/2 | yes/no | Pass/Hold/Fail | model / prompt / sampler / route |
|  | S-01 | structured output |  | n/a | 0/1/2 | 0/1/2 | n/a | 0/1/2 | 0/1/2 | yes/no | Pass/Hold/Fail | model / prompt / JSON mode / route |
|  | X-01 | extraction |  | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | yes/no | Pass/Hold/Fail | context / prompt / model |
|  | G-01 | grounded refusal |  | 0/1/2 | 0/1/2 | n/a | 0/1/2 | 0/1/2 | 0/1/2 | yes/no | Pass/Hold/Fail | grounding / refusal / prompt |
|  | C-01 | constraint following |  | n/a | 0/1/2 | 0/1/2 | n/a | 0/1/2 | 0/1/2 | yes/no | Pass/Hold/Fail | instruction / sampler / model |

Use the same 0/1/2 meaning as [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]:

- `0` means wrong, unusable, or unsupported
- `1` means partly usable with repair
- `2` means acceptable on first use

## Pass / Hold / Fail

| Decision | Use when | Next route |
|---|---|---|
| Pass | Every request saved, no route errors, K-01 is correct, S-01 is valid JSON, X-01 does not invent facts, G-01 refuses missing evidence, and C-01 mostly obeys constraints. | Copy the scoring rows into [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] and continue to workload prompts. |
| Hold | The route works, but one probe needs a prompt, sampler, JSON-mode, or format rerun. | Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] or [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] before blaming the model. |
| Fail | The endpoint errors, returns empty text, misses the arithmetic answer, invents unsupported context, or cannot produce usable structured output. | Route to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] or pick a different model/runtime after evidence is saved. |

A pass here is still not a deployment decision. It only means the first endpoint deserves a broader workload-specific quality harness.

## Academic Interpretation

| Probe | Academic concept | Applied implication |
|---|---|---|
| K-01 | Accuracy and basic reasoning are task-level metrics, not training loss. | One correct answer supports only a narrow local quality claim. |
| S-01 | Constrained generation and schema validity are separate from semantic correctness. | JSON mode can help parsing, but it does not make the answer true. |
| X-01 | Context use must be separated from parametric memory. | A local assistant needs evidence that answers came from the supplied context. |
| G-01 | Calibration and abstention matter when evidence is missing. | Local RAG must refuse unsupported answers instead of guessing. |
| C-01 | Instruction following is an observable behavior, not an internal guarantee. | A model that cannot follow simple constraints needs prompt, sampler, template, or model changes before real workload use. |

This mirrors the evaluation discipline behind [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]]: quality, latency, calibration, robustness, and efficiency are different evidence types. Do not collapse them into one score.

## Completion Gate

This probe suite is complete only when:

- [ ] the model id matches the model-pull evidence
- [ ] first response debrief link is recorded
- [ ] fixed conditions are written before the run
- [ ] all request and response files are saved
- [ ] `quality-probe-results.json` and `.csv` exist
- [ ] each prompt has a human score or explicit unscored reason
- [ ] pass/hold/fail decision names the failure owner
- [ ] no smoke response is promoted to workload quality without the full harness

## References

Internal routes:

- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [OpenAI evals guide](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI evals repository](https://github.com/openai/evals)
- [HELM paper](https://arxiv.org/abs/2211.09110)
