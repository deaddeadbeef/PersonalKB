---
tags: [llm, era-hub]
up: "[[LLM]]"
---

# 2023 — Open Models and Agents

LLMs break out of the chatbox. Open-weight models democratize access, RAG becomes production infrastructure, and agents begin using tools autonomously. The field fragments from a two-player race (OpenAI vs Google) into a broad ecosystem where startups, open-source communities, and research labs all contribute frontier-competitive models and tooling.

## The Open-Weight Revolution

Meta's LLaMA (Touvron et al., February 2023) released 7B–65B parameter models that matched proprietary performance at comparable scale. LLaMA 2 (July 2023) added RLHF-aligned chat variants with a permissive license. This catalyzed an explosion of open-weight development: Mistral 7B (September 2023) matched LLaMA 2 13B, Mixtral 8x7B brought MoE to open models, and community fine-tunes (Vicuna, WizardLM, OpenHermes) proliferated on Hugging Face. Open weights shifted the balance of power from API providers to the broader developer community. See [[Open-Weight Model Ecosystem]].

## Open vs Closed: The Debate

The open-vs-closed debate intensified throughout 2023. Advocates of open release argued for reproducibility, safety research access, and democratization. Opponents cited dual-use risks and the difficulty of preventing misuse once weights are public. Meta, Mistral, and others chose permissive open-weight licenses, while OpenAI, Anthropic, and Google kept frontier model weights proprietary but offered API access. The debate shaped policy discussions globally, with the EU AI Act and US Executive Order on AI both grappling with these questions. See [[Frontier Labs and Open vs Closed Models]].

## RAG Goes Production

Retrieval-Augmented Generation matured from a research technique into production infrastructure. The standard pipeline crystallized: chunk documents, embed with models like `text-embedding-ada-002` or open alternatives (E5, BGE), store in vector databases (Pinecone, Weaviate, Qdrant, pgvector), retrieve at query time, and inject context into the prompt. Chunking strategy — fixed-size, semantic, recursive, parent-child — became a critical design choice affecting retrieval quality. See [[Chunking Strategies]], [[Embeddings and Vector Databases]], and [[Retrieval Pipelines and Context Assembly]].

## Evaluating RAG

As RAG systems proliferated, evaluation became critical. Hybrid search (combining dense vector retrieval with sparse BM25/keyword matching) consistently outperformed either approach alone. Reranking with cross-encoders (Cohere Rerank, BGE-reranker) improved precision by re-scoring retrieved chunks. Frameworks like RAGAS and TruLens emerged to evaluate faithfulness, relevance, and context utilization. Common failure modes — retrieval misses, context poisoning, lost-in-the-middle effects — were systematically catalogued. See [[Hybrid Search]], [[Reranking]], and [[RAG Evaluation and Failure Modes]].

## Agents and Tool Use

LLMs gained the ability to call external tools through structured function calling. OpenAI's function calling API (June 2023) formalized the pattern: the model outputs a JSON-structured tool invocation, the runtime executes it, and the result is fed back. Frameworks like LangChain, LlamaIndex, and AutoGPT built orchestration layers around this capability. The ReAct pattern (Yao et al.) interleaved reasoning and action steps, enabling models to dynamically decide when and which tools to use. See [[Function Calling]] and [[Tool Selection and Execution Loops]].

## Planning and Decomposition

Complex tasks require breaking problems into subtasks. Tree-of-Thought (Yao et al., May 2023) extended chain-of-thought by exploring multiple reasoning branches. Plan-and-solve prompting generated explicit plans before execution. Task decomposition became essential for agent architectures, where a planner module breaks a high-level goal into a sequence of tool calls. The reliability of LLM-generated plans — and the failure modes when plans go wrong — emerged as a key research challenge. See [[Planning and Task Decomposition]].

## Structured Output

Production applications required models to output valid JSON, XML, or domain-specific formats. Constrained decoding techniques (guided generation, grammar-based sampling) ensured structural validity by restricting the token sampling space at each step. OpenAI's JSON mode, Outlines (for open-source models), and LMQL provided different approaches. Structured output became essential infrastructure for tool calling, data extraction, and API integrations. See [[Structured Output and Constrained Generation]] and [[Tool-Augmented Prompting]].

## LLM-as-Judge

Using LLMs to evaluate other LLMs became a scalable alternative to expensive human evaluation. GPT-4 as a judge showed high agreement with human raters on open-ended generation quality. Chatbot Arena (Zheng et al.) combined human pairwise comparisons with Elo ratings to create dynamic leaderboards. Systematic studies of judge biases (position bias, verbosity bias, self-preference) informed calibration strategies. LLM-as-judge evaluation became standard for model development iteration. See [[LLM-as-Judge]].

## Multimodal Architecture Design

GPT-4V (September 2023) and LLaVA (Liu et al.) demonstrated that vision encoders could be integrated with language model decoders through projection layers or cross-attention, enabling models to reason over images and text jointly. Multimodal tokenization — converting images, audio, and video into token sequences compatible with transformer processing — became an active research area with approaches ranging from discrete visual tokens (VQ-VAE) to continuous feature injection. See [[Multimodal Tokenization and Fusion]].

## Pages in This Era

- [[Function Calling]]
- [[Tool Selection and Execution Loops]]
- [[Planning and Task Decomposition]]
- [[Chunking Strategies]]
- [[Embeddings and Vector Databases]]
- [[Hybrid Search]]
- [[Reranking]]
- [[RAG Evaluation and Failure Modes]]
- [[Frontier Labs and Open vs Closed Models]]
- [[Open-Weight Model Ecosystem]]
- [[Tool-Augmented Prompting]]
- [[Structured Output and Constrained Generation]]
- [[LLM-as-Judge]]
- [[Multimodal Tokenization and Fusion]]

## Related Eras

← Previous: [[2022 — Alignment and Chat Overview|2022 — Alignment and Chat]]
→ Next: [[2024–2025 — Frontier and Efficiency Overview|2024–2025 — Frontier and Efficiency]]
