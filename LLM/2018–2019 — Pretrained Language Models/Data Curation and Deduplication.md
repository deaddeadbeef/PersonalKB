---
tags: [llm, pretraining]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Data Curation and Deduplication

> **Modern pretraining corpora are built by turning noisy web crawls into cleaner, more useful datasets through filtering, deduplication, and source mixing.**

## 🎯 Intuition
**The Core Idea:** Raw web data is full of noise and repetition, so model quality depends heavily on how well you clean, deduplicate, and mix the corpus before training.
**Analogy:** Data curation is like panning for gold: most of the river is mud, gravel, and junk, and the real value comes from separating out the few useful pieces.
**Why It Matters:** Data curation and deduplication are critical preprocessing steps that transform raw web crawls into high-quality training corpora, with careful filtering and mixing determining model capabilities and biases. Two models with identical architecture and compute can perform very differently depending on data quality. The field increasingly treats **quality > quantity**, because better tokens teach more than larger amounts of mediocre text.

---

## ⚙️ Core Mechanics
### How It Works
- The standard pipeline is: **crawl → filter → deduplicate → mix**.
- Most pretraining datasets start with **Common Crawl**, a monthly snapshot of billions of web pages.
- However, raw Common Crawl is mostly garbage—spam, duplicate content, porn, low-quality text, non-English (if you want English), auto-generated SEO spam.
- Quality filtering removes the worst content using heuristics (length, perplexity, toxic language filters, HTML tag ratios) and classifier-based approaches (train a classifier on "good" vs "bad" examples).
- **Common Crawl**: Monthly web snapshots; ~250-400 TiB raw per month; serves as base for most datasets.
- **Quality filtering heuristics**: Min/max length, word count, mean word length, symbol-to-word ratio, profanity filters, language ID.
- **Classifier-based filtering**: Train fastText or transformer classifier on human-labeled examples; filter by probability threshold.
- **Exact deduplication** uses hash-based matching (SHA-256) to remove byte-identical documents.
- **Fuzzy deduplication** finds near-duplicates using MinHash LSH (locality-sensitive hashing): compute MinHash signatures, find documents with high Jaccard similarity, cluster and keep one representative.
- **Exact deduplication**: Compute SHA-256 hashes; remove duplicates within and across dumps.
- **MinHash deduplication**: Compute k-min-hash signatures (e.g., 128 hashes); use LSH to find Jaccard similarity > 0.8; cluster and deduplicate.
- This removes 30-50% of data in typical web corpora but dramatically improves quality and reduces memorization.
- After filtering and deduplication, you **mix** datasets.
- **Data mixing**: Combine sources (web, books, code, scientific papers) with proportions; upsample high-quality sources.
- The Pile mixed 22 sources (Common Crawl, books, GitHub, arXiv, StackExchange) with hand-tuned proportions.
- RedPajama reproduced LLaMA's data mix.
- FineWeb (HuggingFace, 2024) and DCLM (DataComp for Language Models) represent the new generation: massive scale (15T tokens), extensive filtering, quality-focused curation.
- **The Pile**: 22 datasets, 825 GiB, widely used for research (GPT-NeoX, Pythia).
- **RedPajama**: Open reproduction of LLaMA data; 1.2T tokens.
- **FineWeb & DCLM**: 15T+ tokens, advanced filtering, quality-first curation.

### Key Specifications

| Dataset | Size | Deduplication | Key Features |
|---------|------|---------------|--------------|
| Common Crawl (raw) | ~250 TiB/month | None | Unfiltered web; mostly garbage |
| C4 | 750 GB | Exact | Simple heuristics; widely used baseline |
| The Pile | 825 GB | Fuzzy | 22 diverse sources; research standard |
| RedPajama | 1.2T tokens | Fuzzy | LLaMA data reproduction |
| FineWeb | 15T tokens | Extensive fuzzy | Aggressive quality filtering; HuggingFace |
| DCLM | Variable | Extensive | DataComp approach; quality-focused |

### Key Facts
- Deduplication is crucial because the web contains massive redundancy: boilerplate, template text, duplicated articles, and scraped content.
- Aggressive deduplication and quality filtering yield better downstream performance with less data.
- Models trained on deduplicated data memorize less, generalize better, and are less likely to regurgitate copyrighted content verbatim.
- The data mixing proportions encode choices about what the model should know.
- Upsampling code improves reasoning and structured output, books improve coherence and long-form generation, and scientific papers improve technical reasoning.

---

## 🔬 Deep Dive
### Technical Details
Data quality is the most underappreciated driver of model performance. C4 (Colossal Clean Crawled Corpus) applied simple heuristics and achieved good results, but later work showed aggressive deduplication and quality filtering yield better downstream performance with less data.

The art is balancing diversity (broad knowledge) with quality (each token teaches something useful). The data mixing stage operationalizes this trade-off by choosing how much web text, books, code, and scientific writing the model sees. The shift toward quality-first datasets like FineWeb represents the field learning that scaling laws apply to *effective* data—10 high-quality tokens teach more than 100 low-quality ones.

After filtering and deduplication, the remaining corpus is not just smaller but structurally different: boilerplate-heavy pages disappear, near-duplicate clusters collapse, and dataset composition becomes a deliberate design decision rather than an accident of the crawl. FineWeb and DCLM exemplify this newer view of pretraining data as an engineered asset rather than a raw web dump.

### Limitations and Criticisms
- Heuristic and classifier-based filtering can remove low-quality text, but they can also discard valuable niche, multilingual, or stylistically unusual content.
- Deduplication improves quality and reduces memorization, but aggressive thresholds may collapse distinct documents that share substantial overlap.
- Data mixing is powerful, but it embeds subjective judgments about what a model should know and which domains deserve more weight.

### Impact and Legacy
This pipeline—crawl, filter, deduplicate, then mix—became the standard recipe for building serious pretraining corpora. The Pile, RedPajama, FineWeb, and DCLM illustrate the shift from raw scale toward deliberate curation. More broadly, this work established that model capability depends not just on architecture and compute, but on the quality and composition of the text itself.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is raw Common Crawl a poor training corpus without substantial filtering?
2. What problem does fuzzy deduplication solve that exact hash-based deduplication cannot?
3. Why can a smaller high-quality corpus outperform a much larger low-quality one?

### Core Problems
1. Compare exact deduplication with MinHash LSH deduplication: what kinds of redundancy does each catch, and what trade-offs do they impose?
2. Suppose you want a model that is stronger at coding and technical reasoning without losing broad world knowledge. How would you alter the data mix, and what capabilities would you expect to change?

### Challenge
1. Defend or critique the claim that scaling laws should be understood in terms of *effective data quality* rather than raw token count alone.

---

*See also:* [[2018–2019 — Pretrained Language Models Overview]], [[Language Model Fundamentals]], [[Scaling Laws]], [[Contamination and Data Leakage]], [[Compute Data and Parameter Trade-offs]], [[Open-Weight Model Ecosystem]], [[LLM/Sources/Sources Index]]

## Supporting Chunks / References
### Supporting Chunks
*(To be populated as chunks are created)*

### References
- [[LLM/Sources/Sources Index]]
