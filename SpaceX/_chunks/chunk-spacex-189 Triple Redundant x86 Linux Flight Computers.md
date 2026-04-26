---
tags: [spacex, chunk]
source: "[[raw-spacex-048]]"
confidence: high
supports:
  - "[[Avionics and Flight Software]]"
  - "[[Propulsive Landing Technology]]"
qna_seeds:
  - "Q: What flight computers does SpaceX use? A: Falcon 9 and Starship use triple-redundant x86 Linux flight computers where three identical units process sensor inputs independently and a majority-vote mechanism masks single-event upsets without radiation-hardened components."
---

# Triple Redundant x86 Linux Flight Computers

Falcon 9 and Starship use triple-redundant x86 flight computers running Linux, where three identical computers process sensor inputs independently and a voting system selects the majority output. If one computer produces a divergent output due to a radiation-induced bit flip or hardware fault, the other two outvote it. Using COTS x86 processors (rather than rad-hardened chips costing 10–100x more) gives SpaceX access to performance generations ahead of traditional space-qualified hardware.
