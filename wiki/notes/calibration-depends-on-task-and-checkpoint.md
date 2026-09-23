---
title: Calibration depends on the task and checkpoint
summary: Proper scoring objectives and valid probabilities do not guarantee reliable confidence after domain or model changes.
---

A decision model's probability may look precise and still be unreliable for a different task, language, option count, or model version. Calibration is empirical: among decisions assigned probability $p$, roughly $p$ should be correct in the relevant deployment population. A proper-scoring-rule training objective rewards truthful forecasts in expectation under its training distribution; it does not prove that every deployed checkpoint is calibrated on every new workload. This is separate from [schema validity](../schema-validity-does-not-imply-semantic-correctness/). ([ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/); [Almeida, 2026](../../sources/typesafe-system-one-jev/))

## Consequence for Laya and Jev

[Laya](../../entities/laya/)'s vendor benchmark reports an English base-checkpoint expected calibration error of 0.466 as shipped, falling to 0.081 after fitting a temperature on held-out examples; its multilingual checkpoint likewise drops from 0.314 to 0.106. The vendor also warns that one 51-language sweep's confidence values predate a later temperature clamp. A separate paired-input [benchmark](../../sources/sysone-bench-repository/) finds both Laya and [Jev](../../entities/jev/) inaccurate on Emotion while recording model- and suite-specific calibration differences. Cross-study ECE values from different tasks or post-processing stages do not rank intrinsic calibration. ([ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/); [instax-dutta, n.d.](../../sources/sysone-bench-repository/))

**Inference:** Evaluate accuracy and calibration on labeled target-domain examples for the chosen checkpoint and version, then set escalation thresholds from observed outcomes. A high model confidence is not an uncertainty detector for an unsupported script: Laya's English checkpoint reported 0.952 mean confidence with zero accuracy on Khmer in its vendor sweep. ([ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/))
