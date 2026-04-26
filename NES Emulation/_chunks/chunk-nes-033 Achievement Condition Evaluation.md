---
tags: [chunk, nes-emulation, achievement]
source: "[[raw-nes-009]]"
up: "[[Achievement System]]"
---

# Chunk NES 033 — Achievement Condition Evaluation

Achievements are defined in JSON with conditions using disjunctive normal form: AND logic within condition groups, OR between groups. Each condition specifies a CPU memory address, comparison operator (eq, neq, gt, lt, gte, lte), target value, and value type (current, previous, or delta). The evaluator runs once per frame, reading addresses through the bus for mapper-correct values. Delta conditions detect changes like score increased rather than score equals X. A per-achievement state machine tracks inactive to active to triggered transitions. Once triggered, achievements never re-fire and persist to disk independently of save states.
