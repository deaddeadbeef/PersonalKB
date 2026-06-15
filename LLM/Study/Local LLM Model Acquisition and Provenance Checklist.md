---
tags: [study, llm, inference, local-llm, model-acquisition, provenance, security]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-14
---

# Local LLM Model Acquisition and Provenance Checklist

> **One-line summary** A local model is not ready to download just because it fits memory; it needs a documented source, license, exact revision, artifact format, safety posture, cache path, and workload boundary.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] proves disk, runtime boundary, and hardware, and before [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] turns the candidate into a memory plan. Use [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] when the open question is where Windows should store model bytes before the first pull. Use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] after this checklist when the next step is a pinned Hugging Face download, cache inspection, GGUF/Ollama import, or conversion. Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] after the artifact lab to confirm the exact local bytes can load in the chosen runtime.

This note answers "am I allowed and prepared to acquire this exact model artifact?" The sizing and serving notes answer "will it fit?" and "can I call it?"

## Outcome

After this checklist you should be able to:

- read a model card for intended use, limitations, license, datasets, evaluation, and architecture clues
- distinguish a model family from a specific artifact, revision, quantization, and runtime package
- decide whether gated access, license terms, or private-data boundaries block a download
- prefer safe tensor formats when possible and treat pickle-style files as executable-code risk
- record the exact local cache path, file size, digest, and runtime-visible model id
- preserve enough provenance for a future benchmark, quality gate, or deployment review

## Acquisition Decision Flow

Do not start with `pull` or `download`. Start with this sequence:

1. Name the workload and data boundary.
2. Choose a candidate model family and size from [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Model and Hardware Sizing Guide]].
3. Read the model card or runtime model page.
4. Check license, intended use, limitations, and gated-access requirements.
5. Choose one artifact format: Ollama tag, GGUF, Hugging Face/Safetensors, GPTQ/AWQ, adapter, or other.
6. Pin the exact revision, tag, file, or digest when the workflow needs reproducibility.
7. Check unsafe artifact risk: pickle, `trust_remote_code`, unknown scripts, or unreviewed conversion steps.
8. Download into a known cache or model directory with enough disk headroom; for Windows first-run storage, complete [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] first.
9. Use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] to record the download command, cache/local path, file list, hash or verification result, import/conversion command, and cleanup plan.
10. Record file size, cache path, checksum/digest if available, and runtime-visible id.
11. Only then move to the compatibility matrix and serving runbook.

Pass signal: a future run can identify which bytes were served and why the artifact was acceptable for the workload.

## Model Card Read

| Model-card field | What to decide | Evidence to record |
| --- | --- | --- |
| Model family and architecture | Is this a decoder-only chat/instruct/code/base/embedding model? | Repo id, architecture, parameter size. |
| Intended use | Does the author claim this model fits the workload? | Chat, code, RAG, extraction, multilingual, tool, or embedding use. |
| Limitations and risks | What failures are known before testing? | Bias, hallucination, language coverage, tool/schema limits, safety caveats. |
| Training or fine-tuning data | Is there a data boundary concern or contamination risk? | Dataset summary, unknown data note, or no disclosure. |
| Evaluation results | Are scores relevant to your prompt suite? | Benchmarks plus why they do or do not match the workload. |
| License | Is local, commercial, redistribution, or derivative use allowed? | License name and any extra terms. |
| Files and formats | Which artifact will you actually download? | `safetensors`, GGUF, Ollama tag, GPTQ/AWQ, adapter, or pickle-style weights. |
| Revision or tag | Which version is being tested? | Commit hash, tag, release, Ollama tag, or file digest. |

If the model card is vague, the model can still be used for learning, but it should not become a deployment choice without a stronger quality, license, and safety record.

## Artifact Risk Map

| Artifact | Acquisition rule | Risk to record |
| --- | --- | --- |
| Ollama tag | Pull by exact tag when possible, then inspect `ollama show` or `/api/show`. | Tag may hide exact template, license, quantization, and blob digest unless recorded. |
| GGUF file | Record source repo, filename, quantization, file size, and checksum if available. | A GGUF file can have wrong quantization, missing template metadata, or unclear conversion provenance. |
| Hugging Face Safetensors | Prefer when runtime supports it; record repo, revision, config, tokenizer, and shard list. | The weights alone are insufficient without config and tokenizer. |
| PyTorch `.bin`, `.pt`, `.pth`, pickle | Avoid unless trusted and necessary. Treat deserialization as code execution risk. | Pickle-family formats can execute code during load; scanner results are supporting evidence, not a guarantee. |
| GPTQ/AWQ/FP8 checkpoint | Confirm runtime and hardware support before download. | Quantized checkpoints are kernel/runtime dependent and not interchangeable with GGUF. |
| Adapter or LoRA | Record exact base model and adapter revision. | Adapter cannot be evaluated or served without the matching base model and tokenizer. |
| Converted model | Record original source, conversion command, converter version, and output hash. | Conversion can change metadata, template behavior, and quantization quality. |

## Safe Download Patterns

Use the tool that matches the source. Do not mix model registries and local paths without recording the handoff.

| Source | Pattern | Evidence |
| --- | --- | --- |
| Ollama library | `ollama pull <model>:<tag>` | `ollama list`, `ollama show --modelfile <model>`, `/api/show` details, cache path if needed. |
| Hugging Face Hub CLI | `hf download <repo-id> --revision <rev>` | Repo id, revision, local directory, downloaded filenames. |
| Hugging Face Python | `snapshot_download(repo_id=..., revision=...)` | Script, revision, cache path, allow/ignore file patterns. |
| Manual GGUF download | Download one named `.gguf` file from the intended repo. | URL, filename, size, checksum/digest if available. |
| Internal artifact | Copy from internal registry or signed storage. | Source path, owner, approval, hash, retention boundary. |

When using Hugging Face, prefer a pinned revision for reproducible benchmarks. When using Ollama, record the tag plus `ollama show` evidence because the runtime package may include template, parameters, and license details behind the tag.

## Security And Trust Checks

| Check | Pass signal | If missing |
| --- | --- | --- |
| Trusted source | Known organization, signed or reviewed release, or internal artifact owner. | Restrict to learning sandbox or choose another source. |
| License understood | License and extra terms are named in the run record. | Do not use for commercial/shared/service deployment. |
| Gated access handled | Access was granted to the actual user/account and terms are recorded. | Do not mirror or share the artifact. |
| Safe file format preferred | `safetensors`, GGUF, or runtime package is available. | Treat pickle-like files as high risk. |
| Scanner status checked when visible | Malware/pickle scan does not show unsafe files. | Do not load until reviewed or replaced. |
| `trust_remote_code` avoided | Runtime does not need unreviewed repo code to load. | Review code in an isolated environment before use. |
| Cache path known | You know where the runtime stored the bytes. | Find cache before serving or benchmarking. |
| Digest/hash recorded | File hash, blob digest, or exact revision identifies the artifact. | Mark reproducibility as partial. |
| No private prompt/data in model store | Download cache contains model artifacts only. | Separate private corpora, adapters, and logs. |

The security posture is not "Hugging Face says it is safe." Scanner badges and official hosting reduce some risks, but local loading is still your boundary decision.

## Provenance Card

Copy this before the first serve attempt.

| Field | Value |
| --- | --- |
| Workload |  |
| Data sensitivity | public / personal / private / regulated / secret / mixed |
| Candidate model |  |
| Model family / size |  |
| Source registry or URL |  |
| Model card reviewed | yes / no / not available |
| Intended use matches workload | yes / partial / no |
| License and extra terms |  |
| Gated access | none / accepted / pending / denied |
| Artifact chosen | Ollama tag / GGUF / Safetensors / GPTQ / AWQ / adapter / other |
| Exact revision, tag, or filename |  |
| Download command or method |  |
| Local cache or model path |  |
| File size or shard list |  |
| Hash, digest, or revision proof |  |
| Unsafe file types present | none / pickle / custom code / unknown |
| `trust_remote_code` needed | no / yes / unknown |
| Runtime-visible model id |  |
| Allowed next step | sizing / compatibility / serve / reject / hold |
| Reason for hold or reject |  |

## Lab: Acquire One Candidate Cleanly

Choose one small instruct model for a local first run. Then fill the card above.

| Step | Evidence |
| --- | --- |
| Read model card | Intended use, limits, license, evaluation summary. |
| Pick artifact | Why Ollama tag, GGUF, or Safetensors fits the runtime. |
| Pin version | Revision, tag, filename, or digest. |
| Download | Command used and final local path. |
| Inspect | File list, size, template/license fields if runtime exposes them. |
| Safety check | Unsafe formats, scanner status if visible, `trust_remote_code` decision. |
| Artifact handoff | Link to [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Artifact Download Cache and Conversion Lab]] for cache, hash, GGUF/import, or conversion evidence. |
| Handoff | Link to compatibility card and serving runbook row. |

Pass signal: the model can be rejected before serving if provenance, license, or artifact safety is weak.

## Failure Triage

| Symptom | Likely acquisition layer | First check |
| --- | --- | --- |
| Download blocked | Gated access or auth | Confirm accepted terms and account/token scope. |
| Model id resolves to unexpected files | Wrong repo, branch, or tag | Pin revision and inspect file list. |
| Runtime pulls a different quantization than expected | Hidden runtime package metadata | Inspect runtime model details and Modelfile. |
| File is too large after download starts | Wrong precision or all-shard clone | Download only the intended file or choose smaller format. |
| License is unclear | Model card incomplete | Treat as learning-only or choose a clearer artifact. |
| Loading requires `trust_remote_code` | Custom architecture or repo code | Review code in isolation or choose supported architecture. |
| Security scan warns or is missing | Artifact trust weak | Hold until reviewed or use safer artifact. |
| Benchmark cannot be reproduced later | Revision/digest missing | Reacquire with pinned revision and record hash. |

## Completion Gate

This checklist is complete when you have:

- [ ] model card or source page reviewed
- [ ] license and intended-use boundary recorded
- [ ] gated-access decision recorded
- [ ] exact artifact format, revision/tag/file, and local path recorded
- [ ] safe-format or unsafe-format decision recorded
- [ ] hash, digest, or exact revision proof recorded, or reproducibility marked partial
- [ ] runtime-visible model id recorded
- [ ] artifact download/cache/conversion evidence linked when the model was downloaded, imported, mirrored, or converted locally
- [ ] handoff to [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Runtime and Model Compatibility Matrix]]
- [ ] handoff to [[LLM/Study/Local LLM Serving Runbook|Serving Runbook]] only if the acquisition card says proceed

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]
- [[LLM/2022 — Alignment and Chat/Quantization]]

Current external docs checked 2026-06-14:

- [Hugging Face model cards](https://huggingface.co/docs/hub/en/model-cards)
- [Hugging Face downloading models](https://huggingface.co/docs/hub/en/models-downloading)
- [Hugging Face gated models](https://huggingface.co/docs/hub/en/models-gated)
- [Hugging Face Hub security](https://huggingface.co/docs/hub/security)
- [Hugging Face malware scanning](https://huggingface.co/docs/hub/en/security-malware)
- [Hugging Face pickle scanning](https://huggingface.co/docs/hub/en/security-pickle)
- [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [Ollama API show and pull endpoints](https://github.com/ollama/ollama/blob/main/docs/api.md)
