---
tags: [study, llm, inference, local-llm, windows, ollama, install, readiness, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM Windows Runtime Install Gate

> **One-line summary** Prove the Windows runtime install, PATH refresh, model-store inheritance, log locations, and loopback listener before the first model pull.

Use this after [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] and [[LLM/Study/Local LLM Model Store Bootstrap Runner|Local LLM Model Store Bootstrap Runner]], and before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]. The model-store snapshot says this machine is ready to create `D:\Models` and set `OLLAMA_MODELS`; the bootstrap runner proves the actual folder and user-env action; this install gate says how to prove the Ollama runtime itself is installed correctly before downloading model weights. Use [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] after install or existing-runtime discovery when you want the PATH, version, model-store env, loopback listener, `/api/version`, and `/api/tags` checks saved as repeatable JSON, Markdown, CSV, and JSONL evidence. After the first model pull, use [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] to capture a no-inference listener and model-list artifact before sending a smoke prompt.

This note is an execution gate, not proof that the runtime is installed now. Do not mark it complete until the evidence files exist in a dated run folder.

## Outcome

After this gate you should be able to:

- identify the installer path and source used for Ollama on Windows
- prove `OLLAMA_MODELS` was set before the runtime starts and before any model pull
- prove a new PowerShell sees the `ollama` command
- prove the local API listener is expected, loopback-only, and not a stale unrelated process
- know which no-inference health snapshot should be captured after the first model pull and before endpoint smoke
- know where to look for Windows logs, binaries, default model/config files, and temporary files
- decide whether to proceed to the first model pull or stop at install/PATH/service diagnosis

## Install Contract

Fill this card in the run folder before executing the installer.

| Field | Value |
|---|---|
| Run folder |  |
| Runtime | Ollama for Windows |
| Installer source | `https://ollama.com/download/windows` |
| Installer method | Windows installer / PowerShell installer / existing install |
| Intended install location | default user install / custom installer `/DIR=...` |
| Intended model store | `D:\Models\ollama` unless this snapshot is updated |
| `OLLAMA_MODELS` set before install? | yes / no / not needed / hold |
| First model pull allowed? | no, not until this gate passes |
| First model source after gate | [[LLM/Study/Local LLM First Model Candidate Ladder]] |
| Failure owner if blocked | install source / PATH / env inheritance / listener / logs |

## Step 0: Create Evidence Folder

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-ollama-install-gate")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
$RunRoot | Tee-Object -FilePath "$RunRoot\run-root.txt"
```

Save the gate card:

```powershell
@"
date=$(Get-Date -Format o)
gate=Local LLM Windows Runtime Install Gate
runtime=Ollama for Windows
installer_source=https://ollama.com/download/windows
model_store=D:\Models\ollama
first_model_pull_allowed=no
"@ | Set-Content "$RunRoot\install-gate-card.txt"
```

## Step 1: Set Storage Before Runtime Start

This step prevents the first model pull from landing in an unintended user-profile store. If you already ran [[LLM/Study/Local LLM Model Store Bootstrap Runner|Local LLM Model Store Bootstrap Runner]] with `--apply`, use this section as verification from a new PowerShell rather than repeating manual setup.

```powershell
$ModelRoot = "D:\Models\ollama"
$HfRoot = "D:\Models\hf"
$GgufRoot = "D:\Models\gguf"

New-Item -ItemType Directory -Force -Path $ModelRoot, $HfRoot, $GgufRoot | Out-Null

[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", $ModelRoot, "User")

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
  model_root_exists = Test-Path $ModelRoot
  hf_root_exists = Test-Path $HfRoot
  gguf_root_exists = Test-Path $GgufRoot
} | ConvertTo-Json |
  Tee-Object -FilePath "$RunRoot\storage-before-install.json"
```

After changing the user environment variable, start a new PowerShell before installing or launching Ollama. If the new shell does not see the variable, stop and fix the environment before installing.

```powershell
$RunRoot = "<paste-run-folder-path>"

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
} | ConvertTo-Json |
  Tee-Object -FilePath "$RunRoot\storage-new-shell-before-install.json"
```

Pass signal: the new shell sees `OLLAMA_MODELS=D:\Models\ollama`.

## Step 2: Capture Pre-Install State

```powershell
$RunRoot = "<paste-run-folder-path>"

"installer_source=https://ollama.com/download/windows" |
  Tee-Object -FilePath "$RunRoot\installer-source.txt"

$OllamaCommand = Get-Command ollama -ErrorAction SilentlyContinue
if ($OllamaCommand) {
  $OllamaCommand |
    Select-Object Source, Version |
    Format-List
} else {
  "ollama not found"
} | Tee-Object -FilePath "$RunRoot\ollama-command-before-install.txt"

Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners-before-install.txt"
```

If `ollama` is already available, switch this run to the existing-install path and capture version/listener proof before deciding whether any installer is needed.

## Step 3: Choose Installer Path

Use one path only.

| Path | Use when | Evidence |
|---|---|---|
| Windows installer | You want the normal Windows app, tray/background behavior, and user PATH setup. | Installer source URL, install time, `ollama --version` from a new shell. |
| PowerShell installer | You want the official one-line PowerShell path from the download page. | Command string, source URL, output saved in the run folder. |
| Existing install | `ollama` already exists and version/listener proof is enough. | Existing binary path, version, model list, listener proof. |

PowerShell installer command from the official download page:

```powershell
"installer_command=irm https://ollama.com/install.ps1 | iex" |
  Tee-Object -FilePath "$RunRoot\installer-choice.txt"

irm https://ollama.com/install.ps1 | iex |
  Tee-Object -FilePath "$RunRoot\installer-output.txt"
```

If you use the Windows installer executable instead, save a note like this:

```powershell
@"
installer_method=Windows installer
installer_source=https://ollama.com/download/windows
install_location=default user install or custom /DIR path
"@ | Set-Content "$RunRoot\installer-choice.txt"
```

Official Windows docs say the default install does not require Administrator and installs in the home directory by default; they also document a `/DIR=...` flag for a custom install location. Do not use a custom install path unless you also record why it is needed.

## Step 4: Verify From A New PowerShell

Close and reopen PowerShell after installation. Then run:

```powershell
$RunRoot = "<paste-run-folder-path>"

[pscustomobject]@{
  OLLAMA_MODELS_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  OLLAMA_MODELS_process = $env:OLLAMA_MODELS
} | ConvertTo-Json |
  Tee-Object -FilePath "$RunRoot\storage-new-shell-after-install.json"

$OllamaCommand = Get-Command ollama -ErrorAction SilentlyContinue
if ($OllamaCommand) {
  $OllamaCommand |
    Select-Object Source, Version |
    Format-List
} else {
  "ollama not found"
} | Tee-Object -FilePath "$RunRoot\ollama-command-after-install.txt"

ollama --version |
  Tee-Object -FilePath "$RunRoot\ollama-version-after-install.txt"

ollama ls |
  Tee-Object -FilePath "$RunRoot\ollama-list-after-install.txt"
```

Pass signal: `ollama` resolves from the new shell, version output exists, model list output exists, and `OLLAMA_MODELS` still points at the intended model store.

Hold signal: `ollama` works only in the old shell, `OLLAMA_MODELS` is missing, or `ollama ls` errors. The failed layer is install/PATH/env inheritance, not model quality.

## Step 5: Listener And Log Proof

Ollama for Windows normally runs in the background and serves the API on `http://localhost:11434`. Prove whether that is true on this machine.

```powershell
$RunRoot = "<paste-run-folder-path>"

Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object { $_.LocalPort -in 11434,1234,8000,8001,8080,30000 } |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Format-Table |
  Tee-Object -FilePath "$RunRoot\listeners-after-install.txt"

@(
  "$env:LOCALAPPDATA\Ollama",
  "$env:LOCALAPPDATA\Programs\Ollama",
  "$HOME\.ollama",
  "$env:TEMP"
) | ForEach-Object {
  [pscustomobject]@{ path = $_; exists = Test-Path $_ }
} | Format-Table |
  Tee-Object -FilePath "$RunRoot\ollama-windows-paths.txt"
```

If the listener is missing but `ollama --version` works, open Ollama from the Start menu or run the app path documented by the Windows troubleshooting note, then rerun the listener check. If a listener appears on `0.0.0.0` or another non-loopback address, stop and use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before any model pull.

Useful Windows evidence paths:

| Path | Use |
|---|---|
| `%LOCALAPPDATA%\Ollama` | App/server/upgrade logs. |
| `%LOCALAPPDATA%\Programs\Ollama` | Installed binaries; the installer adds this to user PATH. |
| `%HOMEPATH%\.ollama` | Default models and configuration when `OLLAMA_MODELS` is not changed. |
| `%TEMP%` | Temporary `ollama*` executable directories. |

## Pass, Hold, Fail

| Decision | Required evidence | Next action |
|---|---|---|
| Pass | `storage-new-shell-after-install.json`, `ollama-command-after-install.txt`, `ollama-version-after-install.txt`, `ollama-list-after-install.txt`, and `listeners-after-install.txt` exist. | Continue to model pull in [[LLM/Study/Local LLM First Endpoint Run Sheet|First Endpoint Run Sheet]]. |
| Hold | Installer ran, but PATH, env, model list, or listener proof is missing or inconsistent. | Diagnose install/PATH/listener before pulling a model. |
| Fail | Installer source is unclear, install errors, or logs show startup failure. | Save logs and route to [[LLM/Study/Local LLM Troubleshooting Decision Tree|Troubleshooting Decision Tree]]. |

Do not run `ollama pull` while this gate is hold or fail.

When the manual evidence exists, run [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] to turn the same state into a machine-checkable pass/hold/fail artifact before [[LLM/Study/Local LLM First Model Source Recheck Runner|Local LLM First Model Source Recheck Runner]] and [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]].

## Copyable Handoff Card

Paste this into the first endpoint run folder when the gate passes.

```text
install_gate=Local LLM Windows Runtime Install Gate
runtime=Ollama for Windows
installer_source=https://ollama.com/download/windows
installer_method=
ollama_command_path=
ollama_version=
OLLAMA_MODELS=
listener_after_install=
logs_path=%LOCALAPPDATA%\Ollama
binary_path=%LOCALAPPDATA%\Programs\Ollama
model_config_path=%HOMEPATH%\.ollama or OLLAMA_MODELS path
decision=pass / hold / fail
next_step=first model pull from Local LLM First Model Candidate Ladder
```

## Rollback Before First Pull

Before any model is downloaded, rollback is mostly runtime cleanup:

- uninstall Ollama from Windows Settings if the installer path is wrong
- remove or correct `OLLAMA_MODELS` only if no model pull has used it yet
- keep the run folder because the failed install evidence is useful
- do not delete `D:\Models` blindly if another tool has started using it

Official Windows docs note that the uninstaller exists under Windows Settings and that a changed `OLLAMA_MODELS` location is not removed by the installer. Treat model directories as owned data, not throwaway application files.

## Completion Gate

This install gate is complete when:

- [ ] dated run folder exists
- [ ] storage decision is captured before install
- [ ] new shell sees `OLLAMA_MODELS`
- [ ] installer source and method are recorded
- [ ] `ollama` command path is captured after install
- [ ] `ollama --version` output is captured
- [ ] `ollama ls` output is captured
- [ ] listener proof is captured after install
- [ ] Windows log/binary/model paths are recorded
- [ ] pass/hold/fail decision is copied into the first endpoint run sheet
- [ ] optional runner output from [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] is linked when you need machine-checkable install readiness
- [ ] no model pull occurred before this gate passed

## References

Internal:

- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Store Bootstrap Runner]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Runner]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]

External/current docs checked 2026-06-16:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download page](https://ollama.com/download/windows)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama troubleshooting documentation](https://docs.ollama.com/troubleshooting)
- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama list local models API](https://docs.ollama.com/api/tags)
- [Ollama get version API](https://docs.ollama.com/api-reference/get-version)
