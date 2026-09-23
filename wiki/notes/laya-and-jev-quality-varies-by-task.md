---
title: Laya and Jev quality varies by task
summary: A paired-input evaluation finds Jev ahead on several sampled tasks and Laya ahead on two, with routing changing the multilingual result.
---

The independent [sysone-bench](../../sources/sysone-bench-repository/) harness evaluated [Laya](../../entities/laya/) and [Jev](../../entities/jev/) on shared states and questions. Its captured routed-Laya comparison contains 541 states yielding 751 scored decisions in nine suites. Jev is versioned `jev-1.13.0`; the Laya checkpoint and package revision were not pinned. Reported accuracy varies more by task than a single overall ranking would reveal. The percentage-point gap below is Jev minus Laya, so a negative value favors Laya. ([instax-dutta, n.d.](../../sources/sysone-bench-repository/))

| Suite | Decisions | Routed Laya | Jev | Gap, pp |
| --- | ---: | ---: | ---: | ---: |
| Triage (curated) | 160 | 80.0% | 88.8% | +8.8 |
| Guardrails (curated) | 60 | 88.3% | 96.7% | +8.3 |
| Moderation (curated) | 90 | 83.3% | 98.9% | +15.6 |
| AG News | 100 | 94.0% | 91.0% | -3.0 |
| Emotion | 100 | 54.0% | 55.0% | +1.0 |
| Banking77, 12 options | 96 | 80.2% | 90.6% | +10.4 |
| MNLI | 60 | 98.3% | 86.7% | -11.7 |
| SST-5 ordinal score | 60 | 36.7% | 61.7% | +25.0 |
| Multilingual intent, five languages | 25 | 84.0% | 100.0% | +16.0 |

The untuned English Laya checkpoint scored only 36% on that last suite; routing raised it to 84%. This is a small 25-decision sample, not evidence that Jev is perfect across languages. The paired Banking77 subset uses only **12** options and still favors Jev by 10.4 points; an unrelated vendor comparison against 72/77 options cannot explain away that measured gap. The SST-5 harness counts an ordinal prediction as correct within 0.5 of its integer label. Curated questions include multiple correlated decisions per state, so raw decision counts overstate independent sample sizes. ([instax-dutta, n.d.](../../sources/sysone-bench-repository/); [ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/))

A second independent [jevbench report](../../sources/jevbench-repository/) sampled 500 public examples per dataset with shared label descriptions. It reports Laya/Jev accuracy of 90.6%/84.3% on AG News (Laya +6.3 points), 38.2%/76.4% on **77-way** Banking77 (Jev +38.2), and 92.0%/95.4% on SST-2 (Jev +3.4). The default Jev AG News run has 0.4% errors, and reported accuracy excludes errors; its separate 85.8% "new descriptions" rerun is not a matched Laya prompt. The published report lacks raw paired predictions and immutable Laya weights, so these aggregate gaps cannot establish deployment performance or paired uncertainty. ([dhruvmehra, n.d.](../../sources/jevbench-repository/))

**Inference:** Jev is stronger on several sampled routing, moderation, multi-choice and ordinal questions; Laya is stronger on sampled AG News and MNLI. There is no credible universal percentage advantage. Neither answer correctness nor [calibration](../calibration-depends-on-task-and-checkpoint/) transfers automatically to a new domain, and local M2 CPU versus hosted Jev latency is not a controlled architecture comparison. ([instax-dutta, n.d.](../../sources/sysone-bench-repository/); [dhruvmehra, n.d.](../../sources/jevbench-repository/))
