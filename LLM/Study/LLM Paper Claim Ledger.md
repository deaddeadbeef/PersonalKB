---
tags: [study, llm, papers, research-literacy, claims, evidence, synthesis]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-15
---

# LLM Paper Claim Ledger

> **One-line summary** Academic LLM knowledge becomes durable when every important paper is reduced to a claim, evidence type, limitation, mechanism, and local deployment implication.

Use this with [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] and [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]]. The protocol tells you how to read one paper. The synthesis map tells the historical story. This ledger is the proof artifact: it records what each paper actually changed and what that claim does or does not justify for local inference, RAG, adaptation, or evaluation. Use [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] when a filled row needs a concrete local proof route.

## Ledger Rule

Do not count a paper as "read" until it has this row:

```text
paper -> claim -> evidence -> limitation -> mechanism -> local implication -> follow-up proof
```

If any field is blank, the paper is still a reading target, not usable knowledge.

## Claim Types

| Claim type | What to isolate | Common confounder |
|---|---|---|
| Architecture | Model component, shape, routing, or representation change. | Data, scale, or training recipe also changed. |
| Objective | Loss, target construction, preference objective, or supervision signal. | Evaluation benchmark may not match the objective. |
| Scaling | Parameter, data, compute, or emergent behavior relationship. | More compute may be doing the work. |
| Systems | Kernel, memory, parallelism, cache, or scheduler improvement. | Hardware assumptions may not transfer locally. |
| Alignment | Behavior shaped after pretraining. | Prompt format, data mixture, or judge bias may explain the result. |
| Adaptation | How a frozen or quantized model is changed cheaply. | Held-out regression and deployment loading may be missing. |
| Retrieval/tooling | External knowledge or action channel around the model. | Retrieval, tool policy, and generation are separate failure owners. |
| Evaluation | How behavior is measured. | Metric may miss robustness, safety, calibration, latency, or workload fit. |

## 20-Paper Claim Ledger

| Paper | Main claim to retain | Evidence type | Limitation to remember | Mechanism anchor | Local implication |
|---|---|---|---|---|---|
| Attention Is All You Need | Self-attention can replace recurrence/convolution for strong sequence modeling. | Machine translation quality and parallel training comparison. | Original evidence is seq2seq translation, not chat assistant behavior. | Scaled dot-product attention, multi-head projections, positional encoding. | Explains why local inference cost depends on attention, context length, prefill, and KV cache. |
| BERT | Bidirectional masked pretraining creates strong encoder representations. | GLUE, SQuAD, and transfer benchmarks. | Encoder-only MLM is not a generative chat model. | Masked language modeling, bidirectional encoder stack. | Use encoder models for embeddings/classification, not as local chat decoders. |
| GPT-1 | Generative pretraining plus task adaptation improves language understanding. | Downstream task transfer after decoder pretraining. | Requires task-specific adaptation and predates scale-based prompting. | Causal decoder pretraining plus supervised adaptation. | Connects decoder-only pretraining to later chat/local model families. |
| GPT-2 | Larger decoder LMs show zero-shot task transfer from language modeling. | Zero-shot benchmark behavior and qualitative examples. | Transfer is uneven and sensitive to data/task framing. | Web-scale causal LM and prompt-as-task framing. | Small local models may need examples, RAG, tools, or adaptation instead of pure zero-shot use. |
| GPT-3 | Scale enables few-shot in-context learning without weight updates. | Few-shot benchmark gains across tasks. | Closed model; gains mix scale, data, prompt budget, and evaluation design. | In-context examples condition next-token prediction. | Separate prompting from fine-tuning when testing local models. |
| Scaling Laws | Loss follows predictable trends with model size, data, and compute. | Empirical power-law fits. | Original compute-optimal balance underweighted data compared with later work. | Coupled parameter/data/compute planning. | Treat model size, token budget, and serving cost as linked choices. |
| Chinchilla | More training data per parameter can be compute-optimal. | Loss comparisons under fixed compute. | Training recipe result, not a direct serving benchmark. | Data/parameter trade-off under compute budget. | Smaller well-trained open models can be rational local candidates. |
| Megatron-LM | Tensor/model parallelism makes very large transformer training practical. | Scaling and throughput measurements. | Training infrastructure result, not a user-facing quality metric. | Tensor parallel layers and communication placement. | Explains why multi-GPU serving/training has communication and partition costs. |
| FlashAttention | IO-aware exact attention can be faster by reducing memory movement. | Kernel speed and memory measurements. | Benefit depends on hardware, sequence length, and kernel integration. | Tiled attention, SRAM/HBM traffic, online softmax. | Hardware kernels can change local context throughput without changing model quality. |
| LLaMA | Strong open foundation models can be trained efficiently enough for broad local use. | Benchmark comparisons across size ladder. | License, data, tokenizer, and chat tuning still matter. | Open-weight decoder, RoPE, SwiGLU, heavy token training. | Model provenance, artifact format, and local compatibility become practical gates. |
| T5 | Text-to-text framing unifies many supervised NLP tasks. | Transfer results across text tasks. | Encoder-decoder path differs from decoder-only chat/local serving. | Span corruption and text-to-text task format. | Know when seq2seq/encoder-decoder models are a better fit than chat decoders. |
| InstructGPT | SFT plus human preference optimization makes models more helpful and aligned. | Human preference comparisons. | Human preference is not truth; reward models and PPO add complexity. | Demonstrations, reward model, PPO, KL control. | Base, instruct, and chat variants should not be treated as interchangeable. |
| Constitutional AI | Principle-guided critique and revision can reduce human labeling load for harmlessness. | Preference/evaluation comparisons after AI feedback. | Depends on chosen principles and evaluator behavior. | Self-critique, revision, RLAIF. | Local safety behavior needs explicit policy and refusal tests, not trust in model branding. |
| DPO | Preference optimization can be framed directly without an explicit reward model/PPO loop. | Preference benchmark and simplification evidence. | Still depends on preference data quality and reference policy. | Direct preference loss over chosen/rejected pairs. | Adaptation decisions must identify whether preference data, not just SFT examples, is needed. |
| LoRA | Low-rank adapter updates can fine-tune efficiently while freezing base weights. | Adaptation quality with fewer trainable parameters. | Rank, target modules, and data quality control results. | `W = W0 + BA` low-rank update. | Local customization can stay reversible and small if adapter loading is supported. |
| QLoRA | Quantized base weights plus adapters enable memory-efficient fine-tuning. | Single-GPU fine-tuning and benchmark comparisons. | Training quantization, adapter quality, and deployment merge/load path must be checked. | NF4/double quantization, paged optimizers, LoRA adapters. | Memory savings do not remove held-out eval, privacy, or artifact custody requirements. |
| Chain-of-Thought | Prompted intermediate reasoning can improve multi-step task performance. | Reasoning benchmark gains with examples. | Reasoning traces may be unfaithful and add latency/tokens. | Few-shot reasoning demonstrations, self-consistency. | Local reasoning models need budget, parser, trace policy, latency, and quality tests. |
| RAG | Retrieval can add external knowledge and attribution to generation. | Knowledge-intensive task evidence. | Retrieval and generation failures are separable. | Retriever, top-k evidence, context assembly, generator. | Evaluate retrieval recall, citation support, and answer faithfulness before blaming the model. |
| ReAct | Interleaving reasoning and actions improves interactive problem solving. | Agent/task examples and tool-use evaluations. | Tool execution, safety, and observation reliability are outside the model. | Thought-action-observation loop. | Local tool loops require schema validation, policy gates, execution logs, and bounded retries. |
| HELM | Model evaluation must be multi-scenario and multi-metric. | Holistic benchmark framework across metrics. | Benchmark coverage is still not your private workload. | Scenario taxonomy, robustness, calibration, fairness, efficiency. | Local model choice needs quality, latency, memory, privacy, safety, and workload-specific gates. |

## Paper Row Template

Copy this when reading a paper outside the fast path.

| Field | Value |
|---|---|
| Paper |  |
| Claim type | architecture / objective / scaling / systems / alignment / adaptation / retrieval-tools / evaluation |
| Main claim |  |
| Evidence type | benchmark / ablation / scaling curve / human preference / systems measurement / case study |
| Strongest baseline |  |
| Main mechanism |  |
| Key limitation |  |
| Confounder to control | data / compute / prompt / model size / evaluator / hardware / context / runtime |
| Local implication | hosting / inference cost / RAG / tools / fine-tuning / quality evaluation / deployment |
| Follow-up vault route |  |
| Open question |  |

## Synthesis Checks

Use these to prove that the papers are connected:

| If you claim | You must connect |
|---|---|
| Attention changed the field. | Transformer mechanism -> scaling-friendly training -> prefill/KV-cache cost. |
| Scaling changed behavior. | GPT-2/GPT-3 -> Scaling Laws/Chinchilla -> local model-size economics. |
| Open weights matter. | LLaMA -> provenance, license, artifact, runtime compatibility, benchmark rows. |
| Alignment made assistants useful. | InstructGPT/DPO/Constitutional AI -> chat templates, refusal tests, quality harness. |
| Adaptation is cheap now. | LoRA/QLoRA -> adapter data, held-out eval, deployment loading, rollback. |
| RAG/tools change capability. | RAG/ReAct -> retrieval/tool evidence, context budget, safety boundary. |
| Evaluation is not a leaderboard. | HELM -> metric interpretation, local quality, latency, memory, privacy, deployment. |

## Completion Gate

The paper-claim ledger is useful when:

- [ ] every fast-path paper has claim, evidence, limitation, mechanism, and local implication fields
- [ ] at least five papers are connected to a local hosting or inference consequence
- [ ] at least three papers are connected to evaluation or safety consequences
- [ ] at least one paper-to-local proof route is generated for the current capstone claim set
- [ ] every new paper outside the fast path receives a row before it changes a wiki note
- [ ] the capstone workbook links this ledger or a filled copy of it as academic proof

## References

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
