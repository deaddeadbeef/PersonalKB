---
type: home
tags: [moc, playbook, vault-home]
---
# PersonalKB — Vault Playbook

> **Authoritative location:** `D:\Vaults\PersonalKB`
> The old OneDrive copy is backup only — do not treat it as the active vault.

This is a personal knowledge base built in Obsidian. It is designed to be **human-readable first, structured enough for automation, and progressively enhanced** — no plugins required to browse or edit, but everything is schema-ready for Dataview, RAG, or semantic search later.

---

## How This Vault Works

Every topic follows a **four-layer pipeline**:

| Layer | Folder | Purpose |
|-------|--------|---------|
| **Raw** | `_raw/` | Human-readable source captures with structured frontmatter |
| **Chunk** | `_chunks/` | Atomic claims / evidence extracted from raw notes |
| **Wiki** | domain folders | Polished analysis notes that synthesise chunks |
| **Query** | `_queries/` | Search aids, QnA notes, Dataview-ready queries |

**Design principles (keep these stable):**
- Every content note has YAML frontmatter with `up:` parent link and `tags:`.
- Cross-link aggressively so the graph view is immediately useful.
- `## References` footer on every wiki note pointing to `[[Sources Index]]`.
- Confidence taxonomy: *verified · plausible · fictional · policy · uncertain*.
- No full copyrighted text in the vault — summaries, metadata, and short fair-use quotes only.

---

## Starting a New Topic

1. **Create the topic folder** at vault root — e.g. `NewTopic/`.
2. **Add a MOC note** — `NewTopic/NewTopic.md` — and link it back here under *Active Projects*.
3. **Create subfolders**: `_raw/`, `_chunks/`, `_queries/`, `_templates/`, `Sources/`, and any domain folders you need.
4. **Copy templates** from an existing project's `_templates/` into yours. Adapt more than just `up:` links and tags — review section headings (e.g. "Why It Matters to …") and replace any hardcoded project paths in query Dataview/search blocks with your topic root.
5. **Stage legal source files outside the vault** in `D:\Sources\<Topic>\` (keeps copyrighted material out of sync/version control).
6. **Capture your first source** → use your adapted `[[Raw Material Template]]`.
7. **Extract chunks** → one note per atomic claim using `[[Chunk Template]]`.
8. **Build wiki notes** in domain folders, synthesising chunks and adding analysis.
9. **Add queries** using `[[Query Template]]` for structured Q&A.
10. **Create a Sources Index** — `NewTopic/Sources/Sources Index.md` — for citation metadata (each topic keeps its own).
11. **Link the new MOC** back to this Welcome note so it shows in *Active Projects* below.

> For book-length ingestion, see `[[Novel Ingestion Guide]]` — it covers chapter-level extraction, fair-use quoting, and the staging convention.

---

## Folder & File Conventions

| Convention | Detail |
|------------|--------|
| `_raw/`, `_chunks/`, `_queries/` | Prefixed with `_` so they sort to the top |
| `_templates/` | Project-scoped; copy into each new topic and adapt headings, paths, `up:` links, and tags |
| Domain folders | Free-form names (`Astrophage/`, `Propulsion/`, etc.) |
| `up:` frontmatter | Every child note links to its parent MOC |
| Tags | Lowercase, topic-namespaced (e.g. `phm/astrophage`) |
| Confidence values | Inline in frontmatter: `confidence: verified` |
| Sources | `D:\Sources\<Topic>\` for full files; each topic keeps its own `TopicName/Sources/Sources Index.md` for citation metadata |

---

## Active Projects

| Project | Status | Description |
|---------|--------|-------------|
| 🚀 **[[Project Hail Mary]]** | Mature | Science, fiction & adaptation analysis of Andy Weir's novel — the reference implementation of this vault's workflow |
| 📊 [[Science Accuracy Scorecard]] | Complete | Grounded / extrapolated / impossible ratings for every major science claim |
| 📚 **[[CS Algorithms]]** | Active | Source notes, 60 chunk notes, 36 canonical wiki pages, 9 study notes, hub-based navigation — built from Cormen's *Algorithms Unlocked* |
| 🖥️ **[[CS Operating Systems]]** | Active | 42 canonical wiki pages, learning-path navigation, 6 study notes — built from Tanenbaum's *Modern Operating Systems* |
| 🤖 **[[LLM/LLM\|Large Language Models]]** | Active | Full-stack LLM knowledge base — transformers, pretraining, alignment, inference, RAG, agents, evaluation, multimodal — 13 hubs, 88 wiki pages, 120-paper source catalog |
| 🚀 **[[SpaceX/SpaceX\|SpaceX]]** | Active | Complete SpaceX knowledge base — origins, Falcon, engines, reusability, Dragon, Starship, Starlink, facilities, technology, business, Mars — 12 hubs, 72 wiki pages |
| 🏗️ **[[CS Data Structures/CS Data Structures\|CS Data Structures]]** | Active | Data structures knowledge base — arrays, linked lists, trees, heaps, hash tables, graphs, tries, advanced — 8 hubs, 45 wiki pages |
| 🎮 **[[NES Emulation]]** | Active | NES hardware theory and OxideNES emulator deep dive — CPU, PPU, APU, mappers, rendering pipeline — 50 wiki pages, 30 raw, 120 chunks |
| 💻 **[[Programming Languages]]** | Active | Design philosophies across 16 languages — type systems, memory, concurrency, paradigms — 78 wiki pages, 50 raw, 200 chunks |
| 🇯🇵 **[[Japanese]]** | Active | Japanese language learning wiki — writing systems, grammar (N5–N3), vocabulary, listening, speaking, culture, keigo — 5-phase learning path, 75 wiki pages, 40 raw, 150 chunks |
| 🍱 **[[Recipes]]** | Active | High-protein portable meal wiki — burritos, crunchwraps, rice bowls, bentos, subs, stir-fries — 12 recipes, weekly meal plans with consolidated shopping lists |

---

## Templates

| Template | Use it for |
|----------|------------|
| [[Raw Material Template]] | Capturing a new source with structured frontmatter |
| [[Chunk Template]] | Extracting a single atomic claim from a raw note |
| [[Query Template]] | Writing a structured Q&A search note |
| [[Chapter Summary Template]] | Summarising a novel chapter (fair-use compliant) |

Templates live inside each project's `_templates/` folder. To start a new topic, copy the set and adjust `up:` links, tags, section headings, and any hardcoded paths (see the *Starting a New Topic* checklist above).

---

## Query System

See **[[QnA System Roadmap]]** for the phased plan.

- **Now:** manual Obsidian search + structured query notes in each topic's `_queries/`. **No community plugins required** — `Ctrl+Shift+F` search works immediately with the path/tag conventions above.
- **Next:** Dataview live tables (schema is already compatible; install when you want live dashboards).
- **Later:** semantic search / Smart Connections / local RAG.

---

> **First time here?** Open [[Project Hail Mary]] — it's the fully worked example of every convention above. For language learning, start with [[Japanese]] — it has a guided 5-phase learning path.


