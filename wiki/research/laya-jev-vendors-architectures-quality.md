---
title: Do Laya and Jev share a vendor, architecture, and answer quality?
rkey: laya-jev-vendors-architectures-quality
date: 2026-09-23
brief: Different vendors and similar decision APIs; Jev's unpublished internals prevent an architecture match, while quality gaps vary by task.
turn_url: https://github.com/smith-wiki/wiki/issues/95
mode: QUESTION_ANSWER
---

## Answer

**Different vendors:** [ConvAI Innovations](../../entities/convai-innovations/) publishes [Laya](../../entities/laya/); [TypeSafe AI](../../entities/typesafe-ai/) makes [Jev](../../entities/jev/). Their own legal notices name distinct organizations, Convai Innovations Pvt. Ltd. and TypeSafe AI, Inc. They expose similar `choice`, `score`, and `noul` interfaces. ([Convai Innovations Pvt. Ltd., 2026](../../sources/convai-privacy-policy/); [TypeSafe AI, 2026](../../sources/typesafe-terms-of-use/); [Mukkunnoth, n.d.](../../sources/laya-research-announcement/); [Almeida, 2026](../../sources/typesafe-system-one-jev/))

**Same architecture? Unknown.** Laya documents ModernBERT/mmBERT encoders, a two-layer decision head, and option-marker scoring. TypeSafe describes Jev's decision contract and RLCD training goal but publishes neither model weights nor comparable architectural details. [API compatibility is not architectural identity](../../notes/a-shared-decision-api-does-not-reveal-a-shared-model/). ([ConvAI Innovations, n.d.](../../sources/laya-model-card/); [TypeSafe AI, n.d.](../../sources/typesafe-system-one-documentation/); [TypeSafe AI, n.d.](../../sources/typesafe-machine-learning-primer/))

**Answer quality depends on the task:** in the [paired comparison](../../notes/laya-and-jev-quality-varies-by-task/), Jev leads triage by 8.8 percentage points (88.8% vs 80.0%), moderation by 15.6, and ordinal SST-5 by 25.0; Laya leads AG News by 3.0 and MNLI by 11.7. With multilingual routing, Laya reaches 84% versus Jev's 100% on only 25 decisions. This benchmark covers 541 states/751 decisions. A second 500-example-per-dataset report finds Jev +38.2 points on 77-way Banking77 and Laya +6.3 on AG News, but publishes no raw predictions. Neither pins Laya weights or establishes a universal winner. ([instax-dutta, n.d.](../../sources/sysone-bench-repository/); [dhruvmehra, n.d.](../../sources/jevbench-repository/))
