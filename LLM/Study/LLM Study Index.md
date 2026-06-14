---
tags: [study, llm]
up: "[[LLM/LLM]]"
---

# LLM Study Index

Study and review materials for the LLM knowledge base.

## Review Drills

- [[LLM/Study/Foundations and Architecture - Review Drill|Foundations & Architecture]]
- [[LLM/Study/Pretraining and Scaling - Review Drill|Pretraining & Scaling]]
- [[LLM/Study/Alignment and Safety - Review Drill|Alignment & Safety]]
- [[LLM/Study/Inference and Efficiency - Review Drill|Inference & Efficiency]]
- [[LLM/Study/RAG and Prompting - Review Drill|RAG & Prompting]]
- [[LLM/Study/Agents and Evaluation - Review Drill|Agents & Evaluation]]

## Quick References

- [[LLM/Study/LLM Architecture Cheatsheet|LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]]
- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]

## Hands-On Labs

- [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] — implement scaled dot-product attention, causal masking, multi-head reshaping, and tensor-shape checks
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] — train a toy causal LM to connect tokens, logits, cross-entropy loss, gradients, validation loss, and generation
- [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] — trace raw data through pretraining, SFT, preference optimization, adaptation, evaluation, and deployment gates
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] — run a local model, call a local API, choose a runtime, and benchmark inference
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] — record model card, license, gated access, exact revision, artifact safety, local path, and digest before serving
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] — match model artifact, quantization, tokenizer, chat template, runtime, route, and workload before serving
- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] — prove hardware, runtime boundary, storage, ports, and endpoint safety before serving a model
- [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] — map local inference failures to environment, sizing, server, route, client, prompt, quality, RAG, or security layers
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] — prove base URL, model id, routes, streaming, errors, and feature gaps before pointing generic clients at a local server
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] — check endpoint exposure, logs, RAG corpus boundaries, prompt injection, and tool permissions
- [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] — trace one request through tokens, prefill, decode, sampling, stopping, streaming, and measurement
- [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] — tune temperature, top-p, top-k, min-p, penalties, seeds, stops, and structured-output controls with reproducible local experiments
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] — build a reusable client wrapper that logs request settings, latency, streaming, errors, and benchmark rows
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] — verify tokenizer, special-token, chat-template, role-boundary, and stop-condition compatibility
- [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] — build a local document-grounded assistant with retrieval, citations, and failure diagnosis
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] — decide when to prompt, use RAG, fine-tune, train adapters, optimize preferences, or distill

## Suggested 20-Paper Fast Path

For a rapid orientation to the LLM field, read these papers in order. Use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] to turn each paper into a claim, mechanism, evidence, limitation, and deployment implication.

1. Attention Is All You Need (Vaswani et al. 2017)
2. BERT (Devlin et al. 2018)
3. GPT-1 (Radford et al. 2018)
4. GPT-2 (Radford et al. 2019)
5. GPT-3 (Brown et al. 2020)
6. Scaling Laws (Kaplan et al. 2020)
7. Chinchilla (Hoffmann et al. 2022)
8. Megatron-LM (Shoeybi et al. 2019)
9. FlashAttention (Dao et al. 2022)
10. LLaMA (Touvron et al. 2023)
11. T5 (Raffel et al. 2019)
12. InstructGPT (Ouyang et al. 2022)
13. Constitutional AI (Bai et al. 2022)
14. DPO (Rafailov et al. 2023)
15. LoRA (Hu et al. 2021)
16. QLoRA (Dettmers et al. 2023)
17. Chain-of-Thought (Wei et al. 2022)
18. RAG (Lewis et al. 2020)
19. ReAct (Yao et al. 2022)
20. HELM (Liang et al. 2022)
