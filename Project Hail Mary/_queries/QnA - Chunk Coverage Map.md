---
tags:
  - phm
  - query
up: "[[QnA System Roadmap]]"
---
# QnA — Chunk Coverage Map

## Purpose

See which wiki notes have supporting chunks and which are still unsupported. Identifies gaps in the evidence base.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual approach below.

**Chunks grouped by the wiki notes they support:**
```dataview
TABLE rows.claim AS "Supporting Claims", rows.confidence AS "Confidence"
FROM "Project Hail Mary/_chunks"
FLATTEN supports AS supported_note
GROUP BY supported_note
```

## Manual Search Fallback

**Check a specific wiki note's coverage:**

1. Open the wiki note (e.g., [[The Hail Mary Drive]]).
2. Scroll to the `## Supporting Chunks` section — linked chunks are listed there.
3. Alternatively, use backlinks: open the backlinks pane and look for chunk notes linking to the wiki note.

**Find all wiki notes mentioned in chunk `supports` fields:**
```
path:"Project Hail Mary/_chunks" supports
```

## Current Coverage

As of this session:

| Wiki Note | Chunk Count |
|---|---|
| [[Rocky and the Eridians]] | 25 |
| [[Taumoeba and the Biological Solution]] | 18 |
| [[Xenolinguistics and First Contact]] | 13 |
| [[Ryland Grace]] | 13 |
| [[Rocky]] | 14 |
| [[Resolution and Aftermath]] | 14 |
| [[Astrophage Life Cycle and Migration]] | 10 |
| [[Arc - Grace and Rocky]] | 10 |
| [[Eridian Civilization Profile]] | 10 |
| [[Hail Mary Ship Design and Systems]] | 11 |
| [[The Hail Mary Drive]] | 10 |
| [[Xenonite - Eridian Structural Material]] | 8 |
| [[Astrophage Biology]] | 8 |
| [[Arc - Xenolinguistics Progression]] | 8 |
| [[Eva Stratt and the Ethics of Existential Response]] | 8 |
| [[Arc - Astrophage Crisis Escalation]] | 9 |
| [[Eridian Sensory Biology]] | 7 |
| [[Alternative Biochemistry]] | 7 |
| [[The Hail Mary Crew - Yao and Ilyukhina]] | 5 |
| [[Science Accuracy Scorecard]] | 5 |
| [[Arc - Taumoeba Discovery]] | 5 |
| [[The Adrian Ecology]] | 7 |
| [[Stellar Dimming and the Petrova Line]] | 4 |
| [[The Eridian Vessel]] | 4 |
| [[Artificial Gravity and Induced Torpor]] | 3 |
| [[Relativistic Travel and Time Dilation]] | 3 |
| [[Solar Variability and Historical Precedents]] | 2 |
| [[Tau Ceti and 40 Eridani]] | 2 |
| [[Earth Energy Budget Under Threat]] | 2 |
| [[Weir's Hard SF Method]] | 2 |
| [[Themes and Motifs]] | 2 |
| [[Astrophage Energy Physics]] | 1 |

**Not yet covered by chunks:** [[Novel vs Film Adaptation]].

## Notes

- This coverage map should be updated as new chunks are added. With Dataview, it auto-updates; without it, maintain manually.
- As of the Phase 11 breadth pass, 4 of 9 new notes have Supporting Chunks sections. New notes that reuse existing chunks (no new extraction) are included in the map below.
