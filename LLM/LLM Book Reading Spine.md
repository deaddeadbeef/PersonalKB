---
tags: [llm, index, book, reading-path, navigation]
up: "[[LLM/LLM]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Book Reading Spine

> **One-line summary** Read the LLM wiki like a book: a curated narrative path through the main articles first, then the labs, runners, evidence layers, and complete corpus index when you want proof or implementation detail.

This page is the reader-facing spine. [[LLM/LLM Corpus Index|LLM Corpus Index]] is the back-of-book index. [[LLM/Study/LLM Study Index|LLM Study Index]] is the workbook. The era folders are the chapters. The raw notes and chunks are the footnotes.

## How To Read This Wiki Like A Book

Read in passes:

1. **First pass: story.** Read the chapter openers and main articles below. Skip runners, raw notes, chunks, and most implementation proofs.
2. **Second pass: mechanism.** Re-read the same path with [[LLM/Study/LLM Math and Tensor Shape Primer]], [[LLM/Study/Attention Implementation Lab]], and [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] open beside you.
3. **Third pass: local practice.** Follow the local-hosting chapters from environment preflight through endpoint proof, benchmarking, quality, privacy, operations, and deployment decisions.
4. **Fourth pass: defense.** Use the paper reading, claim ledger, oral defense, and academic-to-local matrix notes to prove you can explain the literature and turn it into local inference decisions.

Do not try to read the whole corpus linearly. Runners are machines for producing evidence. Raw notes are source records. Chunks are footnotes. The book is the ordered path below.

## Prologue: What A Language Model Is

Start with the basic object: a model estimates text probability, turns symbols into vectors, trains against a prediction objective, and is judged by metrics that only partially predict usefulness.

- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]] — A language model learns to assign probabilities to token sequences, usually by predicting what token comes next.
- [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives|Language Modeling Objectives]] — Pretraining objectives teach models by turning raw text into prediction tasks that force them to learn structure, semantics, and usable world knowledge.
- [[LLM/Pre-2017 — Before Transformers/Perplexity and Intrinsic Metrics|Perplexity and Intrinsic Metrics]] — Perplexity measures how surprised a language model is by held-out text, while related intrinsic metrics like cross-entropy, bits-per-byte, and calibration reveal different aspects of predictive quality.
- [[LLM/Pre-2017 — Before Transformers/Tokenization|Tokenization]] — Tokenization turns raw text into model-readable token IDs, and the tokenizer design directly shapes efficiency, context usage, multilingual fairness, and downstream performance.
- [[LLM/Pre-2017 — Before Transformers/Embeddings and Representation Geometry|Embeddings and Representation Geometry]] — Dense token vectors and their high-dimensional geometry reveal how language models encode meaning, similarity, and knowledge.
- [[LLM/Pre-2017 — Before Transformers/Optimizers and Training Stability|Optimizers and Training Stability]] — Large language models train successfully only when optimization speed is paired with techniques that prevent numerical instability and catastrophic divergence.

Reader checkpoint: you should be able to explain tokens, embeddings, logits, loss, perplexity, and why probability is not the same thing as usefulness.

## Book I: Before Transformers

The pre-transformer world teaches the problem that transformers solved. Statistical models counted local patterns. Neural networks learned representations. RNNs gave sequence state but paid for it with serial computation and long-range weakness.

- [[LLM/Pre-2017 — Before Transformers/Pre-2017 — Before Transformers Overview|Pre-2017 — Before Transformers Overview]] — The foundations of modern language AI — from counting words to learning representations.
- [[LLM/Pre-2017 — Before Transformers/Pre-LLM Neural Network Foundations|Pre-LLM Neural Network Foundations]] — Pre-LLM neural networks contributed the training machinery, representation idea, sequence-state problem, and first attention mechanisms that transformers later scaled into general-purpose language models.
- [[LLM/Pre-2017 — Before Transformers/Pre-Transformer Foundations|Pre-Transformer Foundations]] — Before transformers, NLP advanced through n-grams, static embeddings, and recurrent models that each solved part of the language problem while exposing the limitations transformers later overcame.

Reader checkpoint: you should be able to say why embeddings, recurrence, gating, encoder-decoder models, and attention were necessary but not sufficient.

## Book II: Attention Becomes Architecture

The transformer turns attention from an encoder-decoder accessory into the main computational substrate. This is the architectural hinge of the whole corpus.

- [[LLM/2017 — The Transformer/2017 — The Transformer Overview|2017 — The Transformer Overview]] — One paper changes everything. "Attention Is All You Need" (Vaswani et al., June 2017) replaces recurrence with parallelizable self-attention, enabling the scaling revolution that followed.
- [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]] — Attention lets each token directly compare itself with all other tokens and build a relevance-weighted representation of the whole sequence.
- [[LLM/2017 — The Transformer/Positional Encoding|Positional Encoding]] — Positional encoding injects sequence order into transformers so self-attention can tell not just which tokens exist, but where they occur.
- [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]] — The transformer replaced recurrence with attention-based blocks, creating a scalable architecture that underlies modern large language models.
- [[LLM/2017 — The Transformer/Encoder-Decoder Models|Encoder-Decoder Models]] — Encoder-decoder transformers read the full input with an encoder, then generate outputs step by step with a decoder that cross-attends back to the encoded representation.
- [[LLM/2017 — The Transformer/Transformer Breakthrough and Scaling Era|Transformer Breakthrough and Scaling Era]] — From 2017 to 2020, transformers and scaling laws turned language modeling from a benchmark-driven field into the foundation of the modern LLM era.

Reader checkpoint: you should be able to draw scaled dot-product attention, explain why position is external to attention, and explain why parallelism mattered.

## Book III: Pretraining Becomes The Product

The next step is not just a better model shape. It is a new workflow: pretrain broadly, adapt narrowly, and split the model family into encoder, decoder, and encoder-decoder use cases.

- [[LLM/2018–2019 — Pretrained Language Models/2018–2019 — Pretrained Language Models Overview|2018–2019 — Pretrained Language Models Overview]] — The pretrain-then-fine-tune paradigm emerges. The architecture splits into encoder-only vs decoder-only paths, establishing a divergence that defines the field to this day.
- [[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage|BERT and Encoder Lineage]] — BERT showed that a transformer encoder can understand text better by reading in both directions at once, then be adapted efficiently to many downstream tasks.
- [[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage|GPT and Decoder-Only Lineage]] — Decoder-only models learn by predicting the next token from all previous tokens, and scaling that simple objective unlocked broad capabilities from transfer learning to dialogue and multimodal reasoning.
- [[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models|Encoder-Only Models]] — Encoder-only models read an entire sequence at once and learn to understand masked pieces using both left and right context.
- [[LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models|Decoder-Only Models]] — A decoder-only transformer reads left-to-right under a causal mask, making next-token prediction and text generation the same basic operation.
- [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning|Supervised Fine-Tuning]] — Supervised fine-tuning adapts a pretrained language model by showing it labeled examples of the exact behavior you want. Analogy: Like teaching a know-it-all to follow instructions instead of just knowing a lot of facts.
- [[LLM/2018–2019 — Pretrained Language Models/Domain Adaptation|Domain Adaptation]] — Domain adaptation makes a general language model better at a specific field by teaching it the field's knowledge, terminology, formats, and reasoning habits.
- [[LLM/2018–2019 — Pretrained Language Models/Distillation and Model Compression|Distillation and Model Compression]] — A smaller student model can inherit much of a larger teacher model's capability by learning from its richer outputs instead of only from hard labels.
- [[LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication|Data Curation and Deduplication]] — Raw web data is full of noise and repetition, so model quality depends heavily on how well you clean, deduplicate, and mix the corpus before training.
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks|Knowledge and Reasoning Benchmarks]] — LLMs are commonly evaluated with standardized benchmark suites that test factual knowledge, commonsense reasoning, and mathematical problem-solving across many formats.

Reader checkpoint: you should be able to choose encoder-only, decoder-only, or encoder-decoder architectures from workload needs.

## Book IV: Scale Becomes A Method

Scaling changes the field from architecture invention to systems strategy. Data, compute, parameters, infrastructure, and adaptation methods become first-class levers.

- [[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era Overview|2020–2021 — The Scaling Era Overview]] — GPT-3 proves that scale is a strategy. Few-shot learning, scaling laws, and parameter-efficient methods rewrite the rules.
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws]] — Scaling laws show that test loss improves in smooth, predictable ways as you increase parameters, data, and compute.
- [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs|Compute Data and Parameter Trade-offs]] — Pretraining is an allocation problem: with fixed compute, you must decide how much to spend on model size versus training tokens.
- [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism|Training Infrastructure and Parallelism]] — Training infrastructure scales frontier models by coordinating many GPUs so they act like one much larger training system.
- [[LLM/2020–2021 — The Scaling Era/Few-Shot Prompting|Few-Shot Prompting]] — A language model can infer a task pattern from a few in-prompt demonstrations and apply that pattern to a new input at inference time.
- [[LLM/2020–2021 — The Scaling Era/In-Context Learning Mechanisms|In-Context Learning Mechanisms]] — Large language models can learn how to do a task from prompt examples at inference time by using attention over the context window instead of gradient-based training updates.
- [[LLM/2020–2021 — The Scaling Era/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]] — Most task adaptation does not require changing every parameter in a large model—training a small, well-designed subset is often enough.
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]] — LoRA adapts a frozen model by learning low-rank weight updates, and QLoRA pushes that idea further by combining those adapters with 4-bit quantization of the base model.
- [[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models|Mixture-of-Experts Models]] — Instead of sending every token through the same feed-forward network, an MoE model routes each token to only the most relevant expert sub-networks.
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines and Context Assembly]] — Production RAG works best as a multi-stage pipeline—query transformation, retrieval, reranking, and context assembly—rather than a simple query → top-k → generate loop.
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage|Contamination and Data Leakage]] — Benchmark contamination occurs when evaluation examples appear in a model's training data, so the model may score well by memorization rather than genuine generalization.
- [[LLM/2020–2021 — The Scaling Era/Continual Fine-Tuning and Catastrophic Forgetting|Continual Fine-Tuning and Catastrophic Forgetting]] — In continual learning, fine-tuning on Task B can overwrite weights needed for Task A, causing the model to forget earlier capabilities.
- [[LLM/2020–2021 — The Scaling Era/Vision-Language Models|Vision-Language Models]] — A vision-language model gives a language model access to visual information so it can answer, describe, and reason about images.

Reader checkpoint: you should be able to explain why more parameters alone are not enough: data quality, compute allocation, evaluation contamination, and serving cost all matter.

## Book V: Alignment Turns Models Into Assistants

This is where a model that predicts text becomes an assistant that follows instructions, uses role conditioning, and is judged by human preference and safety behavior.

- [[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat Overview|2022 — Alignment and Chat Overview]] — Making LLMs helpful, harmless, and honest. RLHF, instruction tuning, and chain-of-thought transform raw language models into usable assistants — and ChatGPT changes the world.
- [[LLM/2022 — Alignment and Chat/Instruction Tuning|Instruction Tuning]] — Instruction tuning is supervised fine-tuning on many natural-language instruction tasks so a model learns to generalize instruction-following to new tasks.
- [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]] — RLHF aligns language models with human preferences by combining supervised fine-tuning, reward modeling, and reinforcement learning with a constraint against drifting too far from the base behavior.
- [[LLM/2022 — Alignment and Chat/Direct Preference Optimization|Direct Preference Optimization]] — DPO turns preference-based alignment into a direct supervised-style objective, removing the separate reward model and PPO loop used in RLHF.
- [[LLM/2022 — Alignment and Chat/Constitutional AI|Constitutional AI]] — Constitutional AI aligns models by having them critique and revise their own outputs using explicit natural-language principles instead of relying only on human feedback.
- [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning|System Prompts and Role Conditioning]] — System prompts steer model identity, behavior, and constraints at inference time, but they also create a critical security boundary vulnerable to prompt injection.
- [[LLM/2022 — Alignment and Chat/Chain-of-Thought Prompting|Chain-of-Thought Prompting]] — Chain-of-thought prompting improves reasoning performance by getting models to generate intermediate steps before the final answer.
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation and Preference Studies]] — Human evaluation is the gold standard for open-ended LLM quality, but it is costly, noisy, and shaped by systematic human biases.
- [[LLM/2022 — Alignment and Chat/Alignment Objectives and Failure Modes|Alignment Objectives and Failure Modes]] — Alignment is about getting AI systems to do what humans actually want rather than what we accidentally specify, while understanding the failure modes that emerge when proxy objectives are optimized too hard.
- [[LLM/2022 — Alignment and Chat/Red-Teaming and Safety Evaluations|Red-Teaming and Safety Evaluations]] — Red-teaming and safety evaluations stress-test language models with adversarial prompts and benchmarks to expose harmful capabilities and failure modes before deployment.
- [[LLM/2022 — Alignment and Chat/Mechanistic Interpretability|Mechanistic Interpretability]] — Mechanistic interpretability tries to reverse-engineer neural networks by identifying the features, circuits, and internal representations that produce model behavior.
- [[LLM/2022 — Alignment and Chat/Quantization|Quantization]] — Quantization compresses model weights and sometimes activations into lower-precision formats to cut memory use and inference cost while trying to preserve quality.

Reader checkpoint: you should be able to separate base-model capability, instruction following, preference alignment, safety evaluation, and deployment constraint.

## Book VI: Open Models, Retrieval, And Tools

The field becomes practical and modular: open weights, vector databases, RAG, reranking, structured output, function calling, and tool loops turn language models into systems.

- [[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents Overview|2023 — Open Models and Agents Overview]] — LLMs break out of the chatbox. Open-weight models democratize access, RAG becomes production infrastructure, and agents begin using tools autonomously.
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem|Open-Weight Model Ecosystem]] — The open-weight model ecosystem turned frontier language models from tightly controlled APIs into broadly accessible infrastructure that organizations and individuals could run, adapt, and study themselves.
- [[LLM/2023 — Open Models and Agents/Frontier Labs and Open vs Closed Models|Frontier Labs and Open vs Closed Models]] — A small set of frontier labs are racing with different business, safety, and openness strategies to define the future of AI.
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases|Embeddings and Vector Databases]] — Embeddings turn meaning into vectors, and vector databases make those vectors searchable at scale.
- [[LLM/2023 — Open Models and Agents/Chunking Strategies|Chunking Strategies]] — Chunking decides how documents are split for retrieval, and that choice strongly shapes RAG quality.
- [[LLM/2023 — Open Models and Agents/Hybrid Search|Hybrid Search]] — Hybrid search improves retrieval by combining semantic vector search with exact lexical matching.
- [[LLM/2023 — Open Models and Agents/Reranking|Reranking]] — Reranking improves RAG quality by taking a fast first-pass retrieval result set and rescoring it with a stronger relevance model before sending context to the LLM.
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]] — RAG evaluation works only when you separately measure retrieval quality and answer quality, then diagnose which stage failed when the system gets something wrong.
- [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]] — Function calling lets an LLM request structured tool use instead of only generating free-form text.
- [[LLM/2023 — Open Models and Agents/Tool-Augmented Prompting|Tool-Augmented Prompting]] — Tool-augmented prompting lets language models call external tools and incorporate their results, turning static text generation into grounded, actionable problem solving.
- [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops|Tool Selection and Execution Loops]] — Tool selection and execution loops define how an agent chooses tools, sequences actions, handles errors, and decides when to stop.
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]] — Structured output makes LLMs produce machine-usable responses by constraining generation to valid formats or schemas instead of relying on free-form text.
- [[LLM/2023 — Open Models and Agents/Planning and Task Decomposition|Planning and Task Decomposition]] — Planning lets an agent turn a complex goal into a sequence of manageable actions, with different strategies trading off adaptability, coherence, and cost.
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]] — LLM-as-Judge uses strong models to score other models quickly, cheaply, and at scale—but with important biases.
- [[LLM/2023 — Open Models and Agents/Multimodal Tokenization and Fusion|Multimodal Tokenization and Fusion]] — Multimodal systems must first turn images, audio, and video into tokens, then decide how those tokens interact with text.

Reader checkpoint: you should be able to design a RAG/tool system without confusing retrieval quality, generation quality, citation quality, and tool safety.

## Book VII: Frontier Systems And Efficiency

Now the bottleneck is not only intelligence. It is serving. Context windows, KV cache, batching, speculative decoding, long-context attention, and multimodal input shape what you can host and what it costs.

- [[LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency Overview|2024–2025 — Frontier and Efficiency Overview]] — Pushing the frontier on two axes — maximum capability (multimodal, agents, million-token context) and maximum efficiency (serving, inference, architecture alternatives).
- [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]] — Efficient attention methods make long-context transformers practical by reducing the memory and IO costs that make naive $O(n²)$ attention infeasible at large sequence lengths.
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] — The KV cache speeds autoregressive inference by storing prior attention keys and values so each new token can reuse past computation instead of recomputing it.
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]] — Continuous batching keeps GPU decode batches full by swapping finished requests out and new requests in at each iteration instead of waiting for the longest request to finish.
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]] — LLM serving is a constant balancing act between serving more work per second and keeping each user’s wait time low enough to feel responsive.
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding|Speculative Decoding]] — Speculative decoding speeds up autoregressive generation by letting a small model draft several tokens ahead and a larger model verify them in parallel without changing the final output distribution.
- [[LLM/2024–2025 — Frontier and Efficiency/State Space Models and Mamba|State Space Models and Mamba]] — State space models replace quadratic attention with linear-time sequence processing by evolving a latent state, and Mamba makes that state selective enough to compete on language tasks.
- [[LLM/2024–2025 — Frontier and Efficiency/Memory and State Management|Memory and State Management]] — Memory systems let stateless LLMs act as if they remember past turns by deciding what to keep in context, what to summarize, and what to store and retrieve externally.
- [[LLM/2024–2025 — Frontier and Efficiency/Code Generation Agents|Code Generation Agents]] — Code generation agents turn LLMs from autocomplete systems into autonomous write-test-debug loops that can navigate codebases, execute code, and iterate toward working patches.
- [[LLM/2024–2025 — Frontier and Efficiency/Code and Agentic Benchmarks|Code and Agentic Benchmarks]] — Code and agentic benchmarks test whether models can generate correct code and complete multi-step tasks in interactive environments, with execution-based evaluation providing unusually objective ground truth.
- [[LLM/2024–2025 — Frontier and Efficiency/Multi-Agent Systems|Multi-Agent Systems]] — Multi-agent systems improve capability and reliability on complex tasks by dividing work across specialized agents that coordinate through messages, delegation, or critique.
- [[LLM/2024–2025 — Frontier and Efficiency/OCR Documents and UI Understanding|OCR Documents and UI Understanding]] — Document and UI understanding teach multimodal models to read dense visual structure, preserve layout meaning, and interpret interfaces well enough to extract information or act on screens.
- [[LLM/2024–2025 — Frontier and Efficiency/Speech-Language Models|Speech-Language Models]] — Speech-language models connect spoken audio with language reasoning, moving from cascaded speech pipelines toward systems that natively understand and generate voice.
- [[LLM/2024–2025 — Frontier and Efficiency/Video Understanding Models|Video Understanding Models]] — Video understanding extends image understanding into time, forcing models to reason about motion, causality, and long temporal structure under severe token and compute constraints.
- [[LLM/2024–2025 — Frontier and Efficiency/Multimodal Evaluation and Safety|Multimodal Evaluation and Safety]] — Multimodal evaluation asks whether a model truly reasons across images and text, while multimodal safety asks whether those same cross-modal abilities create new failure and attack surfaces.

Reader checkpoint: you should be able to explain why a local model can be "small enough to load" but still fail latency, context, memory, or quality requirements.

## Book VIII: Reasoning And Agents

The latest era adds test-time compute, reasoning distillation, GUI control, coding agents, prompt caching, and common tool protocols. Read this last so the claims sit on top of the full stack rather than floating as product hype.

- [[LLM/2026 — Reasoning and Agents/2026 — Reasoning and Agents Overview|2026 — Reasoning and Agents Overview]] — The biggest paradigm shift since scaling laws: rather than making models bigger, make them think longer at inference time.
- [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute|Reasoning Models and Test-Time Compute]] — Reasoning models allocate additional compute at inference time to solve harder problems, representing a new scaling axis orthogonal to parameter count.
- [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning|DeepSeek R1 and Open Reasoning]] — DeepSeek R1 demonstrated that reasoning capabilities can be developed through reinforcement learning alone and released as open weights, making advanced reasoning accessible to the broader community.
- [[LLM/2026 — Reasoning and Agents/Reasoning Distillation|Reasoning Distillation]] — Training smaller models on the reasoning traces of larger models, enabling compact architectures to exhibit reasoning capabilities that were previously exclusive to frontier-scale systems.
- [[LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure|Prompt Caching and Inference Infrastructure]] — Prompt caching stores processed prefixes to avoid recomputation on repeated prompts, reducing latency and cost for agentic and conversational workloads by 50–90%.
- [[LLM/2026 — Reasoning and Agents/Model Context Protocol|Model Context Protocol]] — MCP is an open standard for connecting LLMs to external tools, data sources, and services through a uniform client-server interface, replacing ad-hoc tool integration approaches.
- [[LLM/2026 — Reasoning and Agents/Agentic Coding Systems|Agentic Coding Systems]] — LLM-based coding agents that autonomously navigate codebases, write code, run tests, and submit pull requests — transforming software development from pair programming to delegation.
- [[LLM/2026 — Reasoning and Agents/Computer Use and GUI Agents|Computer Use and GUI Agents]] — LLMs that interact with graphical user interfaces by perceiving screenshots and executing mouse/keyboard actions, enabling automation of arbitrary software workflows.
- [[LLM/2026 — Reasoning and Agents/Frontier Models 2025-2026|Frontier Models 2025-2026]] — A survey of the latest generation of frontier language models, characterised by improved reasoning, native multimodality, and dramatically expanded context windows.

Reader checkpoint: you should be able to separate model reasoning, tool execution, agent orchestration, context protocol, and serving infrastructure.

## Book IX: The Local LLM Practicum

This is the practical book inside the book. It turns the academic spine into a local system you can run, measure, debug, and either accept or reject.

### First Endpoint

- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] — Local inference starts with proving the machine, runtime path, storage, accelerator, and network boundary before diagnosing model quality.
- [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] — This is the machine-specific readiness card for the first local LLM run: as of 2026-06-15T11:10:33+08:00, the workstation has an NVIDIA RTX 3080 Ti with 12 GB VRAM, no local LLM runtime installed, no endpoint listening.
- [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] — For this Windows workstation, the first local LLM model should prove the runtime and loopback routes cheaply before testing stronger, larger, or more specialized candidates.
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]] — Decide where model weights, runtime stores, artifact caches, conversion outputs, and evidence logs live before the first large local LLM download.
- [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] — Prove the Windows runtime install, PATH refresh, model-store inheritance, log locations, and loopback listener before the first model pull.
- [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] — Before the first inference call, freeze the selected Ollama tag, prove where the bytes will land, pull only one small baseline model, capture model metadata.
- [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] — Before treating a local LLM server as ready for inference, capture one no-inference health snapshot.
- [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] — This is the fill-in execution sheet for the first local LLM endpoint: install or open the runtime, pull one small model, prove the native and OpenAI-compatible loopback routes, save the evidence files.
- [[LLM/Study/Local LLM First Inference Proof - 2026-06-16|Local LLM First Inference Proof - 2026-06-16]] — This workstation now has a working local Ollama endpoint on loopback: model store, runtime install, model pull, runtime health, native response, OpenAI-compatible response, first response debrief, endpoint audit.

### Client, Timing, And Benchmarking

- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] — A local server is "OpenAI-compatible" only after you prove the base URL, model id, route, request fields, response shape, streaming behavior, errors, and unsupported features that your client actually depends on.
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] — A local model run is reproducible only when the client captures request settings, timing, response text, errors, and benchmark fields in the same shape every time.
- [[LLM/Study/Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16|Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16]] — The local Ollama OpenAI-compatible route now has saved client and streaming timing evidence.
- [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16|Local LLM First Benchmark Row Proof - 2026-06-16]] — The first-smoke OpenAI-compatible client/streaming evidence now has a normalized benchmark row and a passing benchmark evidence audit, scoped only to first-run interpretation rather than model comparison.
- [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] — Local inference metrics are useful only when each number is tied to a phase, claim, confounder, and next controlled action.
- [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] — A local LLM run only proves competence when the model, runtime, hardware, prompts, latency, memory, and quality notes are recorded well enough to reproduce the result.

### Quality, Safety, And Operations

- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16|Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]] — The first Ollama endpoint evidence now audits cleanly, but the first quality probe is a real hold.
- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]] — The first focused remediation pass did not clear the quality hold: output-cap changes and stricter prompts did not fix K-01, and C-01 only passed when the exact target bullet template was supplied.
- [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]] — The held K-01 arithmetic probe is remediated when qwen3.5:2b-q4_K_M routes through a native Ollama calculator tool loop.
- [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]] — The held C-01 strict-format probe is remediated only when the model emits validated structured IDs and the application renders the two five-word bullets; free-text and loose structured attempts still failed.
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] — Local inference reduces provider exposure, but it still creates an application server that can leak prompts, documents, logs, tool outputs, and model access if endpoint, storage, and trust boundaries are weak.
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16|Local LLM Security and Privacy Proof - 2026-06-16]] — The first Ollama endpoint passed a no-generation security/privacy check for one-person loopback use.
- [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] — A local LLM server is operable only when every quality or performance claim is backed by request logs, timing metrics, resource pressure, error evidence, and an explicit next action.
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] — A local LLM server is maintainable only when startup mode, pinned runtime and model versions, cache paths, health checks, backups, upgrade steps, rollback steps.

### Selection, Deployment, And Extension

- [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] — Choose a local LLM by workload contract, evidence, and hardware fit: define the job, pick the smallest plausible candidate, prove compatibility, run a quality gate, and keep only measured winners.
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] — Model choice is a memory, latency, quality, and workload decision: estimate weights, add KV-cache headroom, choose a runtime, then prove the result with benchmarks.
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] — A local LLM works only when the model architecture, file format, quantization, tokenizer, chat template, runtime, API route, and workload contract all match.
- [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]] — A local LLM endpoint is a stack of contracts: hardware, OS boundary, package environment, model bytes, numeric format, tokenizer/template, runtime loader, scheduler/cache, API route, client/UI, workload.
- [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] — The right deployment path is the one whose quality, latency, privacy, cost, reliability, and operational burden fit the workload after measurement.
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] — Local LLM work is the practical bridge between model theory and real systems: choose weights, choose a runtime, expose an API, measure latency/quality, and iterate.
- [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] — This is the ordered practice path for turning local LLM knowledge into proof: first endpoint, reproducible request, controlled runtime, measured quality, RAG/tool extension, and maintained service.
- [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] — A local RAG assistant proves that you can connect retrieval theory to a running local model.

Reader checkpoint: you should be able to host a local endpoint, call it through an OpenAI-compatible client, measure latency and tokens, evaluate quality, keep it private, and decide whether it is good enough for a specific workload.

## Book X: Defense, Papers, And Mastery

The final book is not more reading. It is proving that you can explain the field without hand-waving and connect papers to local decisions.

- [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] — Reading LLM papers well means extracting the problem, method, evidence, limitations, and deployment implication, then placing the paper inside the field map instead of memorizing isolated claims.
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]] — The 20-paper fast path is one causal story: attention made scalable sequence modeling possible, pretraining made general representations useful, scaling made prompting work, systems made training and inference practical.
- [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]] — Academic LLM knowledge becomes durable when every important paper is reduced to a claim, evidence type, limitation, mechanism, and local deployment implication.
- [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]] — Academic LLM mastery is defensible only when each core paper has a claim, evidence type, limitation, mechanism, source proof, local implication, and follow-up proof route.
- [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] — Academic LLM mastery counts only when paper claims can be answered from memory and connected to mechanism, evidence, limitation, local implication, and next proof route.
- [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] — Use this after LLM Paper Claim Ledger and LLM Paper Claim Audit Runner when a paper row has a claim, evidence type, limitation, mechanism, source proof, and local implication, but the next local proof is still vague.
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]] — LLM mastery is defensible when each academic claim can predict or explain a local inference artifact, metric, failure owner, and next decision.
- [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] — Mastery means you can explain the field, read the core papers, implement the core mechanisms, evaluate model behavior, and operate a local model with measured trade-offs.
- [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] — You know LLMs when you can explain the field, derive the core mechanisms, read papers skeptically, operate a local model, diagnose failures, and defend adaptation and deployment decisions without guessing.
- [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] — Mastery becomes credible only when the conceptual, mechanism-to-inference, implementation, local inference, RAG, evaluation, adaptation, and deployment artifacts are linked in one evidence ledger.
- [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]] — The LLM capstone is a small local assistant that you can explain academically, run through a local endpoint, evaluate against a workload, secure on loopback, and operate with evidence.

Reader checkpoint: you should be able to defend a paper claim, name the evidence, state the limitation, predict the local implication, and route the next proof artifact.

## Appendices

Use these when the book path is not enough:

- [[LLM/LLM Corpus Index|LLM Corpus Index]] — complete all-links map.
- [[LLM/Sources/Sources Index|Sources Index]] — source bibliography.
- [[LLM/Study/LLM Study Index|LLM Study Index]] — all study notes, labs, runners, and drills.
- [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] — recall prompts after reading.
- [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]] — daily next action and evidence routing.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Corpus Index]]
- [[LLM/Study/LLM Study Index]]
