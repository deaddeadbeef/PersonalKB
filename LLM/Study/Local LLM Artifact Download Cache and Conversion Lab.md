---
tags: [study, llm, inference, local-llm, artifact, cache, hugging-face, gguf, ollama, conversion]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Artifact Download Cache and Conversion Lab

> **One-line summary** A local model artifact is ready for serving only when the exact downloaded bytes, cache path, file list, verification result, conversion path, and cleanup plan are known.

Use this after [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] approves the source, license, gated-access state, and intended artifact. If the candidate needs machine-checkable source, license, access, pinning, and unsafe-file evidence, run [[LLM/Study/Local LLM Model Acquisition and License Gate Runner|Local LLM Model Acquisition and License Gate Runner]] before downloading. Use this before [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] when the next risk is "which files did I actually download, where did they go, and can my runtime load that artifact?" Use [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]] after file-list, `config.json`, tokenizer, GGUF metadata, or Ollama show capture when downstream checks need normalized model facts. Use [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]] after this lab when the saved rows need machine-checkable proof before compatibility, serving, benchmark, or deployment evidence depends on the artifact. If the risk is earlier - choosing the Windows model store or cache root before a large pull - start with [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]].

This lab is deliberately operational. The acquisition checklist decides whether the artifact is acceptable. This lab proves that the artifact was downloaded, inspected, verified, optionally converted, and handed to the runtime without losing provenance.

## What This Lab Decides

It answers eight questions:

1. Is this a cached Hugging Face snapshot, a local directory, a single GGUF file, an Ollama package, or a converted derivative?
2. Is the revision, tag, filename, or digest pinned enough for future benchmarks?
3. Did the download use the intended cache or local artifact directory?
4. Are the required config, tokenizer, template, and weight files present?
5. Are unsafe file types, `trust_remote_code`, or custom conversion scripts part of the path?
6. Is GGUF downloaded directly, imported into Ollama, or converted from Safetensors?
7. Is the converted artifact hashable, named, and reversible to its source?
8. Can unused cache entries or failed conversion outputs be cleaned up without deleting the accepted artifact?

Pass signal: a future run can identify exactly which local bytes became the served model, how they were produced, and how to remove or reacquire them.

## Artifact Storage Map

| Storage path | Good for | Evidence to record | Risk |
| --- | --- | --- | --- |
| Hugging Face hub cache | Version-aware reuse across Python, Transformers, vLLM, SGLang, and scripts. | `HF_HOME` or cache dir, snapshot path, revision, `hf cache ls`, `hf cache verify`. | Editing cached files can corrupt the shared cache. |
| `--local-dir` mirror | Human-visible copy for conversion, archiving, or offline transfer. | Local directory, `.cache/huggingface` metadata, file list, hash. | Easy to drift from the Hub cache or mix revisions. |
| Single GGUF file | llama.cpp, LM Studio, Ollama, edge/CPU workflow. | Source URL/repo, filename, quantization, GGUF metadata, hash. | Wrong quant, missing chat template, unclear conversion provenance. |
| Ollama model store | Convenient local model id for `ollama run` and UIs. | `Modelfile`, `ollama create` or `ollama run hf.co/...`, `ollama show`, tag, digest when visible. | Package can hide template, quantization, and source unless recorded. |
| Converted derivative | When no suitable GGUF exists or you converted a fine-tune. | Source revision, converter repo commit, command, output path, output hash. | Conversion can change metadata, template behavior, and quality. |

Do not treat these as interchangeable. A model can be acceptable in one storage form and still fail compatibility in another.

## Lab 0: Freeze The Artifact Contract

Copy this before the download or conversion.

| Field | Value |
| --- | --- |
| Workload |  |
| Approved source/provenance card |  |
| Acquisition/license gate output |  |
| Candidate model repo or URL |  |
| License/gate status |  |
| Desired artifact form | HF snapshot / Safetensors / GGUF / Ollama package / adapter / converted derivative |
| Desired revision, tag, or filename |  |
| Runtime target | Ollama / LM Studio / llama.cpp / vLLM / SGLang / Transformers / other |
| Storage boundary | HF cache / local artifact dir / external drive / runtime store |
| Disk budget |  |
| Unsafe file policy | avoid pickle / review custom code / sandbox conversion / other |
| Cleanup plan if rejected |  |

Pass signal: the download command can be checked against this card before it moves large files.

## Lab 1: Dry-Run And Download With A Pinned Boundary

Use the current `hf` CLI for Hugging Face Hub downloads. Start with a dry run when the repository is large.

```powershell
hf download <org-or-user>/<repo> --revision <commit-or-tag> --dry-run
```

For a full Hugging Face-style model snapshot:

```powershell
$env:HF_HOME = "D:\Models\hf"
hf download <org-or-user>/<repo> --revision <commit-or-tag> --cache-dir "D:\Models\hf\hub"
```

For a controlled local mirror, such as a conversion input directory:

```powershell
hf download <org-or-user>/<repo> --revision <commit-or-tag> --local-dir "D:\Models\source\<model-name>"
```

For a subset, restrict the file set explicitly:

```powershell
hf download <org-or-user>/<repo> `
  --revision <commit-or-tag> `
  --include "config.json" `
  --include "tokenizer.*" `
  --include "*.safetensors" `
  --exclude "*.bin" `
  --dry-run
```

Record the final path printed by the CLI. A path under the Hugging Face cache is a shared cache pointer; do not edit files in place. Copy to a working directory before conversion or manual experiments.

## Lab 2: Inspect And Verify The Download

Fill this after the download.

| Evidence | Command or source | Result |
| --- | --- | --- |
| Cache root | `$env:HF_HOME`, `hf cache ls`, or chosen `--cache-dir` |  |
| Snapshot/local path | Last line of `hf download` output |  |
| Revision | Commit hash, tag, or branch ref |  |
| Required files present | `Get-ChildItem -Recurse <path>` |  |
| File size total | `Get-ChildItem -Recurse <path> | Measure-Object Length -Sum` |  |
| Hash or checksum | `Get-FileHash <file>` or `hf cache verify` |  |
| Unsafe files | file list includes `.bin`, `.pt`, `.pth`, custom code, or unknown scripts |  |
| Tokenizer/template files | `tokenizer.json`, `tokenizer_config.json`, `chat_template`, GGUF metadata, or runtime info |  |

Useful cache commands:

```powershell
hf cache ls
hf cache ls --revisions
hf cache verify <repo-id> --revision <commit-or-tag>
hf cache rm model/<repo-id> --dry-run
hf cache prune --dry-run
```

Use `--cache-dir <path>` on cache commands when the model was downloaded outside the default cache.

## Lab 3: Prefer Existing GGUF Before Converting

If the target runtime is llama.cpp, LM Studio, or Ollama, first check whether a GGUF artifact already exists.

| Choice | Use when | Evidence |
| --- | --- | --- |
| Download existing GGUF | Trusted repo has the right model, quantization, and metadata. | GGUF repo, filename, quant type, file size, hash, Hub GGUF viewer metadata. |
| Ollama `hf.co` shortcut | Exploratory run from a Hugging Face GGUF repo is enough. | Exact `hf.co/<repo>:<quant-or-filename>` string and `ollama show` output. |
| Local Ollama import | You need controlled local file provenance. | GGUF path, Modelfile, `ollama create`, `ollama show`, smoke response. |
| Convert from Safetensors | No suitable GGUF exists or you own the fine-tuned source. | Source snapshot, converter commit, command, output hash, compatibility test. |

For a controlled Ollama import from one local GGUF file:

```text
FROM D:\Models\gguf\<model-file>.gguf
PARAMETER num_ctx 4096
```

Then:

```powershell
ollama create <local-model-name> -f .\Modelfile
ollama show <local-model-name>
ollama run <local-model-name> "Reply with exactly: local artifact ok"
```

For an exploratory Hugging Face GGUF run in Ollama:

```powershell
ollama run hf.co/<username-or-org>/<gguf-repo>:<quantization-or-filename>
```

Treat the shortcut as a quick experiment unless you also record the repo, chosen quantization/file, resulting runtime model id, and `ollama show` evidence.

## Lab 4: Convert Only With Provenance

Conversion is a derived artifact, not a neutral copy. Use it only when the compatibility matrix says the source architecture and target runtime support the conversion.

| Conversion field | Value |
| --- | --- |
| Source snapshot/local dir |  |
| Source revision |  |
| Source file types | Safetensors / PyTorch / adapter / other |
| Converter tool | llama.cpp `convert_hf_to_gguf.py` / `convert_lora_to_gguf.py` / other |
| Converter repo and commit |  |
| Converter requirements/version |  |
| Command |  |
| Output file |  |
| Output hash |  |
| Metadata check | tokenizer, context, template, architecture |
| Next compatibility test |  |

Example conversion shape:

```powershell
python .\convert_hf_to_gguf.py "D:\Models\source\<model-name>" --outfile "D:\Models\gguf\<model-name>.f16.gguf"
Get-FileHash "D:\Models\gguf\<model-name>.f16.gguf"
```

If you quantize after conversion, record that as a separate decision in [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]]. Do not let "converted successfully" become "quality accepted."

## Lab 5: Handoff To Compatibility And Serving

The artifact handoff is complete only after these links exist:

| Handoff | Required evidence |
| --- | --- |
| Acquisition | Source, license, gate, intended use, unsafe-file decision. |
| Acquisition/license gate | Runner output proving pass/hold/fail for requested use, access, pinned artifact, unsafe files, and source artifacts. |
| Artifact lab | Download path, revision, cache/local dir, file list, verification, conversion/import evidence. |
| Model metadata | Config, tokenizer, Ollama show, or file-inventory facts are normalized by [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]]. |
| Compatibility | Runtime supports architecture, file format, quantization, tokenizer, template, route, workload. |
| Sizing | Weights, context, KV-cache, runtime overhead, and disk headroom fit the machine. |
| Serving | Runtime-visible model id returns a smoke response on the intended endpoint. |
| Benchmark | Model/runtime/quantization/hardware/context/TTFT/tokens/sec/memory row exists. |

Do not debug answer quality until the artifact handoff is known. A bad answer from the wrong file, wrong quantization, wrong template, or stale cache is not model evaluation.

## Failure Triage

| Symptom | Likely artifact layer | First check |
| --- | --- | --- |
| C drive fills during download | Default Hugging Face cache location. | Set `HF_HOME` or `--cache-dir`; inspect `hf cache ls`; clean with dry-run first. |
| Downloaded more files than expected | Whole repo or missing include/exclude filters. | Repeat with `hf download --dry-run` and explicit patterns. |
| Reproducing benchmark pulls different files | Floating `main` or tag drift. | Pin commit hash or exact filename and record revision. |
| Runtime loads an older model | Stale runtime store or cached package. | List runtime models, cache snapshots, and local directories. |
| GGUF runs but chat format is wrong | Missing or wrong chat template metadata. | Check GGUF metadata and run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |
| Conversion fails | Unsupported architecture, missing tokenizer/config, wrong converter version. | Inspect `config.json`, converter registry/support, and llama.cpp commit. |
| Converted GGUF loads but quality drops | Conversion or quantization changed behavior. | Compare source/HF baseline if possible and run quantization/quality gates. |
| Cache cleanup deletes needed artifact | Confused cache vs local mirror vs runtime store. | Mark accepted artifact path before `hf cache rm`, `hf cache prune`, or `ollama rm`. |

## Decision Card

| Field | Decision |
| --- | --- |
| Accepted artifact |  |
| Artifact form | HF snapshot / local dir / GGUF / Ollama package / converted derivative |
| Source revision or file |  |
| Local path or runtime id |  |
| Verification evidence | hash / `hf cache verify` / runtime digest / partial |
| Conversion or import evidence | none / Modelfile / converter command / output hash |
| Unsafe-file decision |  |
| Cache cleanup action | keep / prune dry-run / remove rejected / hold |
| Compatibility next step |  |
| Serving next step |  |
| Reject reason if any |  |

## Completion Gate

This lab is complete when you have:

- [ ] source/provenance card linked
- [ ] acquisition/license gate output linked when source, license, gated access, pinning, or unsafe-file posture must be audited before download
- [ ] dry-run or file-size decision recorded before large download
- [ ] exact revision/tag/file recorded
- [ ] cache or local directory recorded
- [ ] required files and unsafe file types inspected
- [ ] model metadata card produced when config, tokenizer, Ollama show, context, quantization, or architecture fields feed later runners
- [ ] hash, `hf cache verify`, runtime digest, or partial-verification note recorded
- [ ] GGUF/import/conversion path chosen with evidence
- [ ] derived artifact hash recorded if converted
- [ ] artifact custody audit output linked when the artifact supports compatibility, serving, benchmark, or deployment evidence
- [ ] cleanup or rollback command identified but not run blindly
- [ ] handoff to [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Runtime and Model Compatibility Matrix]]
- [ ] handoff to [[LLM/Study/Local LLM Serving Runbook|Serving Runbook]] only after compatibility is plausible

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]

Current external docs checked 2026-06-15:

- [Hugging Face Hub download guide](https://huggingface.co/docs/huggingface_hub/en/guides/download)
- [Hugging Face Hub cache guide](https://huggingface.co/docs/huggingface_hub/en/guides/manage-cache)
- [Hugging Face CLI guide](https://huggingface.co/docs/huggingface_hub/en/guides/cli)
- [Hugging Face GGUF on the Hub](https://huggingface.co/docs/hub/en/gguf)
- [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index)
- [Hugging Face llama.cpp integration](https://huggingface.co/docs/transformers/en/community_integrations/llama_cpp)
- [Ollama importing a model](https://docs.ollama.com/import)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [Use Ollama with any GGUF model on Hugging Face Hub](https://huggingface.co/docs/hub/ollama)
