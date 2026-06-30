---
tags: [llm, prompting]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Chain-of-Thought Prompting

> **One-line summary** Chain-of-thought prompting improves reasoning performance by getting models to generate intermediate steps before the final answer.

## 🎯 Intuition
**The Core Idea:** Chain-of-thought (CoT) prompting (Wei et al., 2022) elicits intermediate reasoning steps from language models before producing final answers. By including demonstrations that show step-by-step reasoning, or by using zero-shot prompts like "Let's think step by step," CoT dramatically improves performance on tasks requiring multi-step inference, arithmetic, and logical reasoning.

The technique works by encouraging the model to "show its work," externalizing an internal reasoning process into tokens. This not only improves accuracy but also provides interpretable traces of how the model arrived at answers, though faithfulness of these explanations remains debated.

**Analogy:** CoT is like showing your work on a math exam — writing out each step helps you avoid jumps, makes errors easier to catch, and lets someone else inspect how you got the answer.

**Why It Matters:** CoT prompting revealed that language models contain latent reasoning capabilities that can be unlocked through appropriate prompting strategies. It showed that forcing models to produce intermediate tokens improves not just accuracy but also interpretability and debuggability of model outputs.

The technique is particularly critical for complex reasoning tasks where direct question-answering fails. It bridges the gap between models that memorize patterns and models that perform genuine multi-step reasoning, though debates continue about the nature of this "reasoning."

---

## ⚙️ Core Mechanics
### How It Works
- **Zero-shot CoT**: append "Let's think step by step" or similar phrase to trigger reasoning without examples
- **Few-shot CoT**: provide demonstrations with explicit reasoning chains between input and output
- **Self-consistency**: generate multiple reasoning paths with sampling, select most common answer
- **Tree-of-thought**: search over possible reasoning branches, backtrack and explore alternatives
- **Program-of-thought**: generate Python/code to solve problem, execute for answer
- **Automatic CoT**: use clustering and diversity to select demonstrations automatically
- **Faithfulness concerns**: CoT explanations may be post-hoc rationalizations rather than true reasoning traces

### Key Specifications
- **Zero-shot trigger example**: "Let's think step by step"
- **Primary use case**: tasks requiring multi-step inference, arithmetic, and logical reasoning
- **Major extensions**: self-consistency, tree-of-thought, and program-of-thought

### Key Facts
- CoT works by externalizing intermediate computation into tokens.
- Few-shot CoT and zero-shot CoT use different prompting strategies to elicit reasoning.
- Sampling multiple reasoning paths can outperform a single greedy decode.
- Better-looking reasoning traces are not necessarily faithful accounts of how the model actually reasoned.

### Common Distinctions

| Comparison | Chain-of-Thought | Alternative |
|------------|------------------|-------------|
| **vs Direct prompting** | Includes intermediate steps | Input → output directly |
| **vs Scratchpad** | Reasoning in natural language | Symbolic/numerical workspace |
| **Zero-shot vs Few-shot CoT** | Uses trigger phrase only | Requires reasoning demonstrations |
| **Self-consistency vs greedy** | Samples multiple paths, votes | Single greedy decode |
| **CoT vs ToT** | Linear reasoning chain | Tree search over branches |
| **CoT vs PoT** | Natural language reasoning | Code generation + execution |
| **Faithful vs plausible** | Reflects actual reasoning process | Post-hoc rationalization |

---

## 🔬 Deep Dive
### Technical Details
Extensions like self-consistency (sample multiple reasoning paths and take majority vote), tree-of-thought (explore reasoning branches), and program-of-thought (generate executable code) build on CoT's core insight that intermediate computation tokens improve final outputs.

Zero-shot CoT shows that some reasoning ability can be triggered with surprisingly small prompt changes, while few-shot CoT uses demonstrations to anchor the pattern more explicitly. Self-consistency shifts the method from a single trajectory to a distribution over possible trajectories, and tree-of-thought generalizes linear chains into explicit branching search.

### Limitations and Criticisms
- CoT explanations may be post-hoc rationalizations rather than true reasoning traces.
- Interpretability improves only if the emitted reasoning is faithful enough to trust.
- The observed performance gains do not settle the debate over whether models are "really" reasoning or just producing better structured outputs.

### Impact and Legacy
CoT changed prompting practice across the field by showing that latent reasoning capabilities could be unlocked without changing model weights. It also became the conceptual basis for later methods that treat reasoning as search, sampling, or tool-augmented computation rather than a single left-to-right answer string.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is chain-of-thought prompting trying to elicit from a language model?
2. Why can adding intermediate reasoning steps improve final-answer accuracy?
3. What is the difference between zero-shot CoT and few-shot CoT?

### Core Problems
1. Explain why self-consistency can outperform greedy decoding for reasoning tasks.
2. Compare chain-of-thought, tree-of-thought, and program-of-thought as three ways of structuring intermediate computation.

### Challenge
1. Design a benchmark or experiment that could help distinguish faithful reasoning traces from plausible but post-hoc rationalizations.

## See Also

- [[LLM/Agents and Tool Use/Planning and Task Decomposition|Planning]] — CoT as a form of reasoning that enables planning
- [[LLM/Evaluation and Benchmarks/Knowledge and Reasoning Benchmarks|Reasoning Benchmarks]] — GSM8K and MATH showcase CoT effectiveness

## Supporting Chunks

- [[Few-Shot Prompting]]
- Self-Consistency Decoding
- Tree-of-Thought Reasoning
- Program-of-Thought
- Reasoning Faithfulness
- Zero-Shot Prompting

## References

→ [[LLM/Sources/Sources Index|LLM Sources Index]]
- Wei et al. (2022) - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Kojima et al. (2022) - "Large Language Models are Zero-Shot Reasoners"
- Wang et al. (2022) - "Self-Consistency Improves Chain of Thought Reasoning"
- Yao et al. (2023) - "Tree of Thoughts"
- Chen et al. (2022) - "Program of Thoughts"
- Turpin et al. (2023) - "Language Models Don't Always Say What They Think"
