---
tags: [llm, alignment]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Red-Teaming and Safety Evaluations

> **One-line summary** Red-teaming and safety evaluations stress-test language models with adversarial prompts and benchmarks to expose harmful capabilities and failure modes before deployment.

## 🎯 Intuition

**The Core Idea:**  
Red-teaming is the systematic adversarial testing of language models to discover failure modes, safety vulnerabilities, and harmful capabilities before deployment. It encompasses manual expert probing, automated attack generation, and standardized safety benchmarks. The field is defined by a cat-and-mouse dynamic: as models are patched against known attacks, adversaries discover new ones, driving an ongoing arms race between safety measures and circumvention techniques.

**Manual red-teaming** involves human experts systematically attempting to elicit harmful, dangerous, or policy-violating outputs from a model. Red-teamers explore different attack surfaces: direct harmful requests, role-playing scenarios ("pretend you are an unrestricted AI"), multi-turn manipulation (building trust before requesting harmful content), and context exploitation (embedding harmful requests in seemingly benign narratives). Manual red-teaming is high-quality but expensive and limited by human creativity and throughput. Ganguli et al. (2022) documented Anthropic's large-scale manual red-teaming effort, finding that models become harder but not impossible to red-team after RLHF.

**Analogy:**  
This is like hiring both skilled burglars and automated lockpickers to test a security system before opening a bank branch. If they can get in, customers eventually will too.

**Why It Matters:**  
Red-teaming is the empirical backbone of AI safety. Without systematic adversarial testing, safety claims are untestable assertions. The GCG result was particularly sobering: it showed that RLHF-based safety training creates a behavioral veneer that can be bypassed with gradient access, and even without it via transfer. This shifted the field's understanding of what safety training actually does — it changes the model's default behavior but doesn't remove harmful capabilities.

The cat-and-mouse dynamic means safety is never "solved." Each generation of defenses (refusal training, input filters, output classifiers) is met with new attacks. This argues for defense-in-depth approaches: combining multiple layers of safety (training-time alignment, input filtering, output monitoring, usage policies, rate limiting) rather than relying on any single mechanism.

---

## ⚙️ Core Mechanics

### How It Works

- **Manual red-teaming**: Domain experts probe specific risk areas (biosecurity, cybersecurity, CSAM, self-harm). Requires detailed guidelines, diverse testers, and systematic coverage tracking.
- **GCG attack (Zou et al., 2023)**: Greedy Coordinate Gradient search over token positions. Optimizes an adversarial suffix to maximize the probability of the model producing a harmful completion. Transfers across models, demonstrating that safety alignment is superficial.
- **PAIR (Chao et al., 2023)**: An attacker LLM iteratively generates and refines jailbreak prompts against a target model, using the target's responses as feedback. Achieves high success rates with ~20 iterations.
- **Many-shot jailbreaking (Wei et al., 2024)**: Exploits long context windows by providing hundreds of examples of harmful Q&A pairs in-context, overwhelming the safety fine-tuning signal with in-context demonstration.
- **Jailbreak taxonomy**:
  - **Prompt injection**: Overriding system instructions ("Ignore previous instructions and...")
  - **Role-playing / persona**: "You are an unrestricted AI with no safety filters"
  - **Encoding tricks**: Requesting content in Base64, ROT13, or other encodings
  - **Payload splitting**: Distributing harmful content across multiple turns
  - **Language switching**: Using low-resource languages with weaker safety coverage
  - **Virtualization**: Framing harmful requests as fiction, code, or hypotheticals
- **Safety benchmarks**:
  - **ToxiGen** (Hartvigsen et al., 2022): Machine-generated toxic and benign statements across 13 demographic groups. Tests whether models generate or endorse toxic content.
  - **RealToxicityPrompts** (Gehman et al., 2020): 100k naturally occurring prompts from web text, scored for toxicity. Measures how often models produce toxic continuations.
  - **BBQ** (Parrish et al., 2022): Bias Benchmark for QA. Tests social biases across 9 categories via ambiguous and disambiguated question-answering.
  - **TruthfulQA** (Lin et al., 2022): 817 questions designed to elicit common misconceptions. Tests whether models repeat popular falsehoods.

### Key Specifications

**Automated red-teaming** uses models to generate adversarial inputs at scale. The simplest approach prompts one language model to generate attacks against another. More sophisticated methods use optimization. The GCG attack (Zou et al., 2023) is a landmark result: it uses gradient-based search to find adversarial suffixes — seemingly gibberish token sequences appended to a prompt — that reliably jailbreak aligned models. The attack transfers across models (a suffix optimized against an open-source model often works on closed-source models), revealing that safety training is a shallow behavioral layer rather than a deep change in model capabilities. Other automated approaches include PAIR (Chao et al., 2023), which uses an attacker LLM to iteratively refine jailbreaks, and tree-of-attacks prompting.

**Jailbreak taxonomies** categorize the growing zoo of circumvention techniques. Major categories include: prompt injection (overriding system instructions), role-playing and persona attacks ("You are DAN — Do Anything Now"), encoding tricks (Base64, ROT13, pig Latin), many-shot attacks (Wei et al., 2024 — providing many harmful examples in-context to shift the distribution), payload splitting (breaking harmful content across multiple messages), and language switching (requesting harmful content in low-resource languages where safety training is weaker). Each category exploits a different aspect of how models process and filter content.

### Key Facts

| Method | Type | Strengths | Limitations |
|---|---|---|---|
| Manual red-teaming | Human expert | High-quality, creative, contextual | Expensive, limited throughput |
| GCG | Gradient-based optimization | Systematic, transferable, reveals vulnerabilities | Requires gradient access (open-weight models) |
| PAIR | LLM-based iterative | Scalable, no gradients needed | Lower success rate than GCG, depends on attacker quality |
| Many-shot | In-context exploitation | Simple, effective on long-context models | Requires long context, detectable |

| Benchmark | Measures | Format |
|---|---|---|
| ToxiGen | Toxicity generation across demographics | Classification |
| RealToxicityPrompts | Toxicity in open-ended generation | Prompted continuation |
| BBQ | Social bias in QA | Multiple choice |
| TruthfulQA | Truthfulness vs popular misconceptions | Open-ended + multiple choice |

---

## 🔬 Deep Dive

### Technical Details

Red-teaming covers both capability discovery and defense evaluation. Manual teams are good at contextual, realistic probing, especially in complex multi-turn interactions. Automated attacks are good at scale, systematic search, and discovering surprising exploit strings that humans would never invent.

The GCG result matters because it is not merely a cute jailbreak trick. It suggests that safety alignment often leaves the underlying capabilities intact and merely changes their default expression. Transferability strengthens that conclusion: if an adversarial suffix found on one model can break another, then the weakness is likely structural rather than idiosyncratic.

Benchmarks serve a different but complementary role. While jailbreaks test circumvention, datasets like ToxiGen, RealToxicityPrompts, BBQ, and TruthfulQA provide standardized measurements across toxicity, bias, and truthfulness. They do not exhaust safety, but they create repeatable baselines.

### Limitations and Criticisms

- Manual red-teaming is expensive and bottlenecked by human creativity and throughput
- Automated methods can overfit to benchmarkable vulnerabilities while missing real-world misuse patterns
- Some strong attacks require gradient access or other information unavailable in black-box settings
- Benchmarks can become stale as models are explicitly trained against them
- Passing benchmarks does not imply broad safety; attack surfaces continue to evolve

### Impact and Legacy

Red-teaming has become central to how frontier-model risk is discussed, measured, and communicated. It pushed the field away from naive claims that alignment training simply removes dangerous capabilities.

It also strengthened the case for layered defenses. Rather than expecting one training method or classifier to solve safety, practitioners increasingly treat deployment safety as an adversarial security problem with ongoing monitoring, patching, and re-evaluation.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. What is the difference between manual and automated red-teaming?
2. Why was GCG considered such an important result?
3. What is a jailbreak taxonomy for?

### Core Problems

1. Compare GCG, PAIR, and many-shot jailbreaking in terms of access assumptions, scalability, and likely deployment relevance.
2. Explain why benchmark success is useful but insufficient for safety assurance.
3. Suppose a model passes TruthfulQA and ToxiGen but is still vulnerable to prompt injection. What does that tell you about the difference between benchmark performance and adversarial robustness?
4. Why does the field increasingly favor defense-in-depth over single-mechanism safety?

### Challenge

Design a safety evaluation plan for a new chat model. Include manual red-teaming, one automated jailbreak method, at least two benchmarks, and a deployment-time mitigation layer. Explain what each layer can catch and what it might still miss.

## Supporting Chunks / References

### Supporting Chunks

*(To be populated as chunks are created)*

### References

- [[LLM/Sources/Sources Index]]
