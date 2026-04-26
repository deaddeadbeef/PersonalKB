---
tags: [spacex, chunk]
source: "[[raw-spacex-015]]"
confidence: high
supports:
  - "[[Autonomous Flight Termination System]]"
  - "[[Launch Cadence and Turnaround Records]]"
qna_seeds:
  - "Q: How does AFTS work? A: AFTS uses on-board GPS receivers and an IMU to continuously compute the vehicle's state vector, comparing it in real time against pre-loaded approved flight corridor boundaries. If the actual or predicted state exits the corridor, AFTS autonomously initiates termination with no ground command required."
---

# AFTS On-Board Autonomous Design

The Autonomous Flight Termination System (AFTS) replaces ground-commanded termination with on-board autonomous trajectory monitoring. It combines GPS receivers and an inertial measurement unit (IMU) to continuously compute the vehicle's state vector in real time, comparing it against pre-loaded approved flight corridor boundaries. If the actual or predicted vehicle state exits the approved corridor, AFTS autonomously initiates vehicle termination with no ground command required — eliminating the need for ground radar and range safety officers.
