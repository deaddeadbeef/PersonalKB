---
tags: [llm, fine-tuning]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Domain Adaptation

> **Domain adaptation specializes a general model for fields like medicine, law, code, or science by adding domain knowledge and domain-specific behavior.**

## 🎯 Intuition
**The Core Idea:** Domain adaptation makes a general language model better at a specific field by teaching it the field's knowledge, terminology, formats, and reasoning habits.
**Analogy:** Domain adaptation is like teaching a polyglot to speak doctor-speak, lawyer-speak, or programmer-speak fluently without forgetting ordinary language.
**Why It Matters:** General-purpose models are impressive but often lack depth in specialized domains. Domain adaptation bridges this gap by helping models use correct terminology and conventions, understand domain-specific context and nuance, and perform specialized reasoning such as legal analysis or medical diagnosis. But it also has clear limits: it does not add real-time knowledge, can introduce narrow-domain biases, may hallucinate domain-specific "facts," and can be expensive in compute and data curation.

---

## ⚙️ Core Mechanics
### How It Works
- **Domain Adaptation** is the process of specializing general-purpose language models for specific fields—legal, medical, code, scientific writing, finance, etc.
- The goal: improve performance on domain-specific tasks by incorporating specialized knowledge, terminology, and reasoning patterns.
- Two main strategies:
  1. **Continued pretraining** on domain-specific corpora (inject knowledge)
  2. **Domain-specific supervised fine-tuning** on task examples (align behavior)
- Often both are used sequentially: continued pretraining → SFT → (optionally) RLHF.

**Continued Pretraining:**
- Start with general base model (LLaMA, GPT, etc.)
- Continue causal language modeling on domain corpus
- Data: Millions–billions of tokens of domain text
- Examples: Medical journals, legal documents, GitHub code, ArXiv papers
- Updates all model weights with domain knowledge
- Risk: May degrade general capabilities ("catastrophic forgetting")

**Domain-Specific SFT:**
- Fine-tune on (instruction, output) pairs for domain tasks
- Examples: "Diagnose this case" → medical diagnosis, "Fix this bug" → code fix
- Smaller datasets than continued pretraining (1K–100K examples)
- Teaches task-specific formats and reasoning styles
- Often follows continued pretraining

**Code Models:**
- **CodeLlama (Meta 2023)**: LLaMA-2 → continued pretraining on 500B tokens of code → SFT on code instructions
- **DeepSeek-Coder (2023)**: 2T tokens code pretraining → fill-in-middle → instruction tuning
- **StarCoder**: Trained from scratch on The Stack (3T+ tokens, permissively licensed code)
- **Specialization**: Python-only models, repository-level context, test generation

**Medical Models:**
- **Med-PaLM (Singhal et al. 2022)**: FLAN-PaLM → SFT on medical QA → ensemble + CoT prompting
- **Med-PaLM 2 (2023)**: Scaled to 540B, expert-level performance on medical exams
- **BioGPT (Luo et al. 2022)**: GPT-2 architecture, pretrained exclusively on PubMed abstracts (15M)
- **Clinical BERT**: BERT → continued pretraining on clinical notes (privacy challenges)
- Challenge: Medical data is sensitive, high-quality labeled data is scarce

**Legal Models:**
- Continued pretraining on legal corpora (case law, statutes, contracts)
- Task-specific SFT: contract analysis, legal reasoning, citation generation
- Challenge: Legal reasoning requires precise logic + vast precedent knowledge

**Scientific Models:**
- **Galactica (Meta 2022)**: 120B model trained on scientific papers, references, formulas
- Strengths: Citation generation, LaTeX, chemical formulas
- Controversy: Generated plausible-looking but incorrect scientific claims → withdrawn
- Lesson: Domain adaptation ≠ factual reliability without grounding

**Decision Tree:**
1. **New factual knowledge needed?** → Continued pretraining or RAG
2. **Specific output format/style?** → SFT
3. **Dynamic/current information?** → RAG (domain adaptation can't help)
4. **Limited compute?** → RAG + prompting, or PEFT instead of full training

### Key Specifications

| Scenario | Continued Pretraining | Domain SFT | RAG | Prompting Only |
|----------|----------------------|------------|-----|----------------|
| **Need domain knowledge** | ✓ Essential | Helpful | ✓ Essential | May suffice if shallow |
| **Need domain task skills** | Helpful | ✓ Essential | Helpful | May suffice |
| **Have domain corpus** | ✓ Required | Not needed | ✓ Required | Optional |
| **Have labeled examples** | Not needed | ✓ Required | Helpful | Helpful |
| **Need up-to-date info** | No (static snapshot) | No (static) | ✓ Yes | Via retrieval |
| **Compute budget** | Very high | Medium | Low | Very low |

| Dimension | General Model + Prompting | Domain SFT Only | Continued Pretrain + SFT | RAG + Prompting |
|-----------|--------------------------|----------------|-------------------------|----------------|
| **Domain knowledge** | Shallow (pretrain only) | Shallow–medium | Deep | Deep (from retrieval) |
| **Task alignment** | Weak | Strong | Strong | Medium |
| **Data needs** | None | 1K–100K examples | Billions tokens + examples | External database |
| **Compute cost** | None | Medium | Very high | Low (inference) |
| **Freshness** | Static | Static | Static | Dynamic |
| **Best for** | Quick prototypes | Task-specific tools | Domain experts (offline) | Current info needs |

### Key Facts
- Continued pretraining injects domain knowledge; domain SFT aligns the model to domain-specific tasks and formats.
- Code, medical, legal, and scientific domains all need different mixtures of data, task supervision, and evaluation.
- Continued pretraining can deepen expertise but risks catastrophic forgetting.
- RAG is essential when the task depends on dynamic or current information.
- Galactica showed that domain adaptation alone does not guarantee factual reliability.

---

## 🔬 Deep Dive
### Technical Details
Domain adaptation usually proceeds in stages. Continued pretraining modifies the base model itself by exposing it to millions or billions of domain-specific tokens, thereby injecting terminology, genre conventions, and latent domain knowledge into the weights. Domain-specific SFT then sharpens behavior using instruction-output examples that teach task formats, style, and reasoning patterns. In many real systems the pipeline becomes continued pretraining → SFT → optionally RLHF.

The examples in code, medicine, law, and science show that "domain adaptation" is not one method but a family of specialization strategies. CodeLlama and DeepSeek-Coder emphasize large-scale code pretraining plus instruction tuning, while StarCoder was trained from scratch on a permissively licensed corpus. Medical systems such as Med-PaLM, Med-PaLM 2, BioGPT, and Clinical BERT demonstrate that domain specialization can come from SFT, continued pretraining, or both, but also that privacy and high-quality labels are major bottlenecks. Legal adaptation depends on absorbing precedent-heavy corpora and producing precise outputs. Scientific adaptation, as Galactica showed, can improve symbol-heavy tasks like citations and formulas while still failing badly on reliability.

The decision framework is therefore conditional. If you need new factual knowledge, continued pretraining or RAG may be appropriate. If you need a specific output format or style, SFT is central. If the knowledge must stay current, domain adaptation alone will not help and retrieval becomes necessary. If compute is limited, RAG plus prompting—or PEFT instead of full training—may dominate.

### Limitations and Criticisms
- Continued pretraining can degrade general capabilities through catastrophic forgetting.
- Domain adaptation does not solve freshness; real-time or changing knowledge still requires retrieval.
- Narrow domain data can inject bias, and even well-adapted models may hallucinate plausible but false domain-specific claims.

### Impact and Legacy
Domain adaptation turned general LLMs into more useful expert tools for code, medicine, law, and science. It clarified the division of labor between continued pretraining, SFT, and retrieval, and made domain-specific evaluation a first-class concern. It also taught the field that specialization improves terminology and task fit, but not necessarily truthfulness or up-to-date grounding.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between continued pretraining and domain-specific SFT?
2. Why might a medical model need both domain adaptation and retrieval?
3. What does Galactica teach about the limits of domain specialization?

### Core Problems
1. Given a new legal assistant project, decide when you would use continued pretraining, SFT, RAG, or prompting only, and justify the sequence.
2. Compare code, medical, legal, and scientific adaptation: which constraints are mainly about data availability, which are about reasoning, and which are about reliability?

### Challenge
1. Build an argument for when domain adaptation should be replaced by retrieval-based systems instead of additional training, especially in high-stakes domains.

---

*See also:* [[2018–2019 — Pretrained Language Models Overview]], Continued Pretraining vs Fine-Tuning, [[Continual Fine-Tuning and Catastrophic Forgetting|Catastrophic Forgetting]], Retrieval-Augmented Generation (RAG), Code Models and Code Understanding, Medical and Scientific LLMs, [[LLM/Sources/Sources Index|LLM Sources Index]]

## Supporting Chunks
### Supporting Chunks
- Continued Pretraining vs Fine-Tuning — When to use each
- [[Continual Fine-Tuning and Catastrophic Forgetting|Catastrophic Forgetting]] — Preserving general capabilities
- Retrieval-Augmented Generation (RAG) — Alternative to knowledge injection
- Code Models and Code Understanding — Deep dive into code domain
- Medical and Scientific LLMs — Healthcare/science domain specifics

## References
See [[LLM/Sources/Sources Index|LLM Sources Index]] for papers:
- Rozière et al. 2023: Code Llama
- Guo et al. 2024: DeepSeek-Coder
- Li et al. 2023: StarCoder
- Singhal et al. 2022: Med-PaLM
- Singhal et al. 2023: Med-PaLM 2
- Luo et al. 2022: BioGPT
- Taylor et al. 2022: Galactica
- Domain-specific benchmarks and evaluation frameworks
